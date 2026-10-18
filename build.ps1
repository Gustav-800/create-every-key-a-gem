param(
    [Parameter(Mandatory = $true)][string]$MinecraftDir,
    [string]$JavaHome = "$env:APPDATA\.minecraft\runtime\java-runtime-delta"
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$buildDir = Join-Path $root 'build'
$classesDir = Join-Path $buildDir 'classes'
$libsDir = Join-Path $buildDir 'libs'
$jarName = 'create-every-key-a-gem-1.0.0.jar'
$jarPath = Join-Path $libsDir $jarName

$javac = Join-Path $JavaHome 'bin\javac.exe'
$jarTool = Join-Path $JavaHome 'bin\jar.exe'
if (-not (Test-Path $javac)) { throw "javac not found: $javac" }

$libraryRoot = Join-Path $MinecraftDir 'libraries'
$srgJar = Get-ChildItem (Join-Path $libraryRoot 'net\minecraft\client') -Recurse -Filter 'client-1.21.1-*-srg.jar' |
    Select-Object -First 1
if (-not $srgJar) { throw "Minecraft 1.21.1 client jar not found under $libraryRoot" }

$classpath = @(
    $srgJar.FullName,
    (Join-Path $libraryRoot 'net\neoforged\neoforge\21.1.262\neoforge-21.1.262-universal.jar'),
    (Join-Path $libraryRoot 'net\neoforged\fancymodloader\loader\4.0.45\loader-4.0.45.jar'),
    (Join-Path $libraryRoot 'net\neoforged\mergetool\2.0.3\mergetool-2.0.3-api.jar'),
    (Join-Path $libraryRoot 'net\fabricmc\sponge-mixin\0.16.4+mixin.0.8.7\sponge-mixin-0.16.4+mixin.0.8.7.jar'),
    (Join-Path $libraryRoot 'org\slf4j\slf4j-api\2.0.9\slf4j-api-2.0.9.jar')
)
$missing = $classpath | Where-Object { -not (Test-Path $_) }
if ($missing) { throw "Missing required jars: $($missing -join '; ')" }

if (Test-Path $classesDir) { Remove-Item $classesDir -Recurse -Force }
New-Item -ItemType Directory -Force -Path $classesDir | Out-Null
New-Item -ItemType Directory -Force -Path $libsDir | Out-Null

$sources = Get-ChildItem (Join-Path $root 'src\main\java') -Recurse -Filter *.java | ForEach-Object FullName
$cpString = $classpath -join ';'
Write-Host "Compiling $($sources.Count) source file(s)..."
& $javac -encoding UTF-8 -source 21 -target 21 -proc:none -classpath $cpString -d $classesDir $sources
if ($LASTEXITCODE -ne 0) { throw "javac failed with exit code $LASTEXITCODE" }

Copy-Item (Join-Path $root 'src\main\resources\*') $classesDir -Recurse -Force

$manifest = Join-Path $buildDir 'MANIFEST.MF'
@(
    'Manifest-Version: 1.0',
    'Implementation-Title: Create: Every Key a Gem',
    'Implementation-Version: 1.0.0'
) | Set-Content -Path $manifest -Encoding ASCII

if (Test-Path $jarPath) { Remove-Item $jarPath -Force }
& $jarTool --create --file $jarPath --manifest $manifest -C $classesDir .
if ($LASTEXITCODE -ne 0) { throw "jar failed with exit code $LASTEXITCODE" }

$distDir = Join-Path $root 'dist'
New-Item -ItemType Directory -Force -Path $distDir | Out-Null
Copy-Item $jarPath (Join-Path $distDir $jarName) -Force

$hash = (Get-FileHash $jarPath -Algorithm SHA256).Hash
Write-Host "Built: $jarPath"
Write-Host "Size:  $((Get-Item $jarPath).Length) bytes"
Write-Host "SHA256: $hash"

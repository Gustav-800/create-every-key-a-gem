# 发布操作手册 / Publishing guide

这份手册按顺序覆盖：GitHub 开源 → GitHub Release → Modrinth → MC百科。
每一步都给出需要填写的材料和可直接复制的文案。

建议顺序：**先 GitHub（源码 + Release）→ 再用 GitHub 登录 Modrinth 发布 → 最后创建 MC百科条目并回填前两者的链接。**

> 当前发布信息：
>
> - GitHub 用户名：`Gustav-800`
> - 署名：`Gustav-800`
> - 版权年份：`2026`
>
> 如果之后要换署名，改 `LICENSE`、`src/main/resources/META-INF/neoforge.mods.toml`、`README.md`。

---

## 0. 发布前检查

- [ ] 在真实整合包里重启游戏，确认模组能加载。
- [ ] 激活打字机，按一个会打开其他模组界面的绑定键，确认不再弹出界面。
- [ ] 按 `Esc` 能退出打字机；`F2` / `F11` 正常。
- [ ] 运行 `.\gradlew build` 或 `build.ps1`，确认 jar 生成。
- [ ] 记录 jar 的 SHA-256，发布时可选附上。
- [ ] 截图：打字机激活、按键编辑界面、模组列表（见第 5 节）。

当前版本：`1.0.0`  
jar：`build/libs/create-every-key-a-gem-1.0.0.jar`

---

## 1. GitHub 开源

### 1.1 注册

1. 打开 <https://github.com/signup>。
2. 填写邮箱、密码、用户名（用户名会进入仓库 URL，建议用英文/数字）。
3. 完成邮箱验证。
4. 建议开启两步验证（Settings → Password and authentication）。

### 1.2 创建仓库

1. 打开 <https://github.com/new>。
2. **Repository name**：`create-every-key-a-gem`
3. **Description**：
   ```
   Client-side keyguard for the Create: Aeronautics wireless typewriter. | 机械动力：字字珠玑
   ```
4. 选择 **Public**。
5. **不要**勾选 “Add a README file”“Add .gitignore”“Choose a license”——项目里已经有这些文件。
6. 点击 **Create repository**。

### 1.3 上传代码

本地仓库**已经初始化并完成首次提交**（`Create: Every Key a Gem 1.0.0`），
`origin` 已指向 `https://github.com/Gustav-800/create-every-key-a-gem.git`。

你只需要在 GitHub 创建好空仓库后，在项目目录打开 PowerShell：

```powershell
cd "C:\Users\Administrator\Documents\deepseek-harness\default-workspace\create-every-key-a-gem"
git push -u origin main
```

如果仓库名不是 `create-every-key-a-gem`，先改远程地址：

```powershell
git remote set-url origin https://github.com/Gustav-800/你的仓库名.git
```

如果 push 时要求密码：GitHub 不接受账户密码，使用 **Personal Access Token**（Settings → Developer settings → Personal access tokens → Fine-grained tokens，给 repo 读写权限），或使用 GitHub Desktop 登录后发布。

### 1.4 仓库设置

进入仓库 → 右侧 **About** 齿轮：

- **Description**：
  ```
  Client-side keyguard for the Create: Aeronautics wireless typewriter. | 机械动力：字字珠玑
  ```
- **Website**：发布 Modrinth 后填 `https://modrinth.com/mod/create-every-key-a-gem`
- **Topics**：
  ```
  minecraft
  minecraft-mod
  neoforge
  create
  create-aeronautics
  typewriter
  keybind
  redstone
  client-side
  ```

Settings → General：

- 确认 **Issues** 开启。
- Discussions 可选。
- 不需要 Wiki / Projects。
- **Social preview**：上传 `assets/github-social.png`（1280×640），发链接时预览图会好看很多。

### 1.5 创建 Release

1. 仓库右侧 **Releases** → **Draft a new release**。
2. **Choose a tag**：输入 `v1.0.0` → “Create new tag on publish”。
3. **Release title**：`Create: Every Key a Gem 1.0.0`
4. **Describe this release**：复制 `docs/metadata.md` 里的 “GitHub Release 文案”。
5. 上传 jar：`build/libs/create-every-key-a-gem-1.0.0.jar`
6. 勾选 **Set as the latest release**。
7. 点击 **Publish release**。

发布后把 release 链接补到 README 和百科。

---

## 2. Modrinth 发布

### 2.1 注册

1. 打开 <https://modrinth.com>。
2. 点击右上角 **Sign in**，推荐用 **GitHub** 登录（后续仓库/Issues 链接也方便）。
3. 在 Settings 里补邮箱并验证。

### 2.2 创建项目

1. 登录后点击右上角头像 → **Projects** → **Create a project**。
   - 或直接打开 <https://modrinth.com/dashboard/projects>。
2. **Project type**：`Mod`
3. 填写：

| 字段 | 值 |
| --- | --- |
| Name | `Create: Every Key a Gem` |
| Slug | `create-every-key-a-gem` |
| Summary | `Keeps the Create: Aeronautics wireless typewriter in control of your keyboard: while it is active, mapped shortcut keys no longer trigger other mods. Client-side, no config.` |
| Categories | `Utility`、`Technology` |
| Environment | **Client only** |
| License | `MIT` |
| Source | `https://github.com/Gustav-800/create-every-key-a-gem` |
| Issues | `https://github.com/Gustav-800/create-every-key-a-gem/issues` |

4. **Description**：把 `docs/modrinth-description.md` 的全文粘贴进去。
5. **Icon**：上传 `src/main/resources/icon.png`（512×512，PNG，<256KB）。
6. **Gallery**：先保存草稿，等截图准备好再上传（见第 5 节）。
7. 保存草稿，不要急着提交。

### 2.3 上传版本

在项目页点击 **Create a version**（或 Versions → Create version）：

| 字段 | 值 |
| --- | --- |
| Version number | `1.0.0` |
| Version title | `1.0.0 — Initial release` |
| Release channel | `Release` |
| Loaders | `NeoForge` |
| Game versions | `1.21.1` |
| File | `create-every-key-a-gem-1.0.0.jar` |
| Changelog | 复制 `CHANGELOG.md` 的 1.0.0 段 |

**Dependencies**：

- `Create` → Required
- `Create: Aeronautics` → Required
- 不需要把 Sable 单独列为必需；它由 Create: Aeronautics 带入。

**Version 环境**：Client only（与项目设置一致）。

上传后确认：
- jar 内 `META-INF/neoforge.mods.toml` 的版本是 `1.0.0`；
- 文件名与版本号一致；
- 游戏版本只勾 `1.21.1`，加载器只勾 `NeoForge`。

### 2.4 提交审核

1. 回到项目页，确认所有必填项完整。
2. 点击 **Submit for review**。
3. 在 <https://modrinth.com/dashboard/projects> 查看状态。
4. 审核通过后，项目页 URL 为：
   ```
   https://modrinth.com/mod/create-every-key-a-gem
   ```
5. 把这个 URL 填到 GitHub 仓库的 Website、README、MC百科相关链接。

> 审核可能会问：模组是否包含他人的代码、是否重复上传、jar 是否与源码一致。本项目是 MIT 开源的原创 Mixin 实现，不打包 Simulated/Create 的代码，正常说明即可。

---

## 3. MC百科发布

### 3.1 注册

1. 打开 <https://www.mcmod.cn/>。
2. 注册账号并验证邮箱；完善个人资料。
3. 新用户默认是“百科用户”，编辑需要审核；不影响创建条目。
4. 如果要长期维护，可之后在百科论坛“申请相关”版块申请编辑员，或加官方 QQ 群咨询。

### 3.2 先搜索，避免重复条目

在百科搜索：
- `字字珠玑`
- `Every Key a Gem`
- `Create: Aeronautics`（确认父模组条目名）

如果已有条目，直接编辑；没有则创建。

### 3.3 添加模组

1. 打开 <https://www.mcmod.cn/class/add>（或首页右侧“添加模组”）。
2. 按下表填写：

| 字段 | 值 |
| --- | --- |
| MOD名称 | `机械动力：字字珠玑` |
| MOD原名 | `Create: Every Key a Gem` |
| 简写名称 | 留空（没有通用缩写，不要硬编） |
| 所属分类 | `辅助` |
| 支持MC版本 | `1.21.1` |
| 模组关系 | 前置：`Create`（百科 2021）、`Create: Aeronautics`（百科 26350） |
| 模组元素 | `辅助`、`红石`（以百科下拉选项为准） |
| 模式 | `SSP/SMP` |
| 官方状态 | `维护中` |
| 作者/团队 | `Gustav-800` |
| 相关链接 | GitHub、Modrinth（发布后补） |
| 开源协议 | `MIT` |

3. **封面**：百科封面建议 240×150。直接用 `assets/mcmod-cover.png`，或在游戏里截一张 16:10 的图。
   - 上传方法：编辑器图片按钮 → 本地上传 → 插入后点击图片 → 远程图片 → 复制地址 → 填到“封面”。
4. **模组标签**：`打字机`、`快捷键`、`客户端`、`红石`、`航空学`、`机械动力`。
5. **正文**：把 `docs/mcmod-body.md` 全文粘贴进编辑器。
   - 如果编辑器是富文本，按标题/列表手动排版；也可以在个人设置里切换为 Markdown 编辑器。
6. 点击 **提交修改**，等待审核。

### 3.4 审核通过后

- 在“下载地址”/“相关链接”中补充：
  - Modrinth：`https://modrinth.com/mod/create-every-key-a-gem`
  - GitHub Releases：`https://github.com/Gustav-800/create-every-key-a-gem/releases`
- 在“日志”页添加 1.0.0 更新日志（复制 `CHANGELOG.md`）。
- 如果条目被合并/重命名，按审核意见修改，不要重复创建。

> 百科对“模组关系”的定义：前置 = 必须安装才能启动；拓展 = 向本模组追加内容；联动 = 双方可独立存在、互相有少量互动。本项目应把 Create / Create: Aeronautics 填为前置。

---

## 4. 三处互相链接

发布后统一补链：

| 位置 | 填什么 |
| --- | --- |
| GitHub About → Website | Modrinth 项目 URL |
| GitHub README 顶部 | Modrinth、MC百科链接 |
| Modrinth Description 顶部 | GitHub、MC百科链接 |
| Modrinth Source / Issues | GitHub 仓库 / Issues |
| MC百科“相关链接” | GitHub、Modrinth |
| MC百科正文开头 | “源码 / 下载见 GitHub、Modrinth” |

---

## 5. 截图与封面

### 5.1 需要拍的图

1. **打字机激活**：站在打字机前，屏幕上有按键提示/HUD，最好能看到打字机模型。
2. **按键编辑界面**：潜行右击打字机打开的 GUI，展示已绑定的按键。
3. **模组列表**：NeoForge 的 Mods 界面，能看到 `Create: Every Key a Gem`。
4. 可选：其他模组界面没有弹出的对比图（用文字说明即可，很难用截图证明“没发生”）。

拍摄建议：
- 1920×1080，窗口模式，UI 缩放 2。
- 关闭光影，使用原版/清爽材质，保证文字可读。
- 用 `F2` 截图，文件在 `screenshots/`。
- 第一张作为 Modrinth featured image；选最能说明“打字机 + 按键”的图。

### 5.2 Modrinth Gallery

- 上传 2–4 张，第一张设为 featured。
- 每张图配一句说明：
  - “Typewriter active — every key belongs to the typewriter.”
  - “Bind keys in the typewriter GUI.”
  - “The addon appears in the mod list as Create: Every Key a Gem.”

### 5.3 MC百科封面

- 240×150，建议用打字机截图裁切，不要直接用方形图标拉伸。
- 如果暂时没有截图，可用 `assets/mcmod-cover.png`（如已生成）占位，之后再换。

---

## 6. 常见问题与注意事项

**Q：GitHub 上要不要提交 `build/`、`dist/`、`run/`？**  
A：不要。`.gitignore` 已忽略；jar 通过 GitHub Release 附件分发。

**Q：Modrinth 提示 “No matching versions” 或依赖找不到？**  
A：确认游戏版本只选 1.21.1、加载器只选 NeoForge；依赖项目要选对 slug（`create`、`create-aeronautics`）。

**Q：MC百科说“编辑需要审核”要等多久？**  
A：新用户/新条目通常需要审核；在个人中心或条目历史里看状态。急的话去百科论坛“申请相关”版块或官方群问。

**Q：可以同时发 CurseForge 吗？**  
A：可以，但本次只准备了 Modrinth 和 MC百科。CurseForge 需要另外填项目、上传文件、等待审核。

**Q：jar 里的作者名/版本号怎么改？**  
A：改 `src/main/resources/META-INF/neoforge.mods.toml` 的 `authors` / `version`，重新构建。`LICENSE` 的版权行也要同步。

**Q：需要给 Modrinth 提供源码压缩包吗？**  
A：不需要。填 Source 链接即可；审核可能核对 GitHub 代码与 jar 是否一致。

---

## 7. 发布后

- 在 GitHub Release、Modrinth、MC百科三处确认下载链接可用。
- 发一个简短的发布动态（B站/动态/群），附一张打字机截图和一句话：
  > 打字机终于不会打着打着弹出别的模组界面了。
- 收集反馈：如果某个模组仍然串键，记录“模组名 + 按键 + 是否使用 GLFW 原始轮询”，再判断是否需要扩展兼容层。

---

## 8. 材料索引

| 文件 | 用途 |
| --- | --- |
| `docs/metadata.md` | 所有短字段、名称、依赖、Release 文案 |
| `docs/modrinth-description.md` | Modrinth 项目正文（英文 + 中文） |
| `docs/mcmod-body.md` | MC百科正文 |
| `CHANGELOG.md` | 版本日志 |
| `README.md` | GitHub 首页 |
| `LICENSE` | MIT 许可证 |
| `src/main/resources/icon.png` | 项目图标 / 百科封面素材 |

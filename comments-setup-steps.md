# 完成评论功能配置步骤

## 1. 访问 Giscus 配置页面
https://giscus.app/zh-CN

## 2. 配置参数
- Repository: TsanChingKim/blog
- Category: General (或 Discussions)
- Mapping: Pathname
- Theme: 根据您的网站主题选择
- Language: zh-CN

## 3. 获取配置参数
复制生成的配置代码中的以下参数：
- data-repo-id="R_kgDOKxxxxxxxxx"
- data-category-id="DIC_kwDOKxxxxxxxxx"

## 4. 更新 config/_default/params.toml
取消注释并填入实际值：
```toml
giscusRepo = "TsanChingKim/blog"
giscusRepoId = "R_kgDOKxxxxxxxxx"  # 从giscus.app获取
giscusCategory = "General"
giscusCategoryId = "DIC_kwDOKxxxxxxxxx"  # 从giscus.app获取
```

## 5. 确保GitHub仓库启用了Discussions
- 进入 TsanChingKim/blog 仓库
- Settings → Features → Discussions
- 启用 Discussions 功能

## 6. 部署和测试
- 提交所有更改
- 推送到GitHub
- 访问网站查看文章底部是否显示评论框

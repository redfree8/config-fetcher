[![Stars](https://img.shields.io/github/stars/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/stargazers)
[![Forks](https://img.shields.io/github/forks/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/network/members)
[![Issues](https://img.shields.io/github/issues/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/issues)
[![License](https://img.shields.io/github/license/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/blob/main/LICENSE)
[![Activity](https://img.shields.io/github/last-commit/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/commits)

# 多协议代理配置获取器

[**🇺🇸English**](README.md) | [**![Lang_farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png)فارسی**](README_FA.md) | [**🇨🇳中文**](README_CN.md) | [**🇷🇺Русский**](README_RU.md)

该项目可以自动从公共 Telegram 频道、SSCONF 链接和其他包含配置数据的 URL 获取并更新各种代理配置。它支持多种代理协议，包括 WireGuard、Hysteria2、VLESS、VMess、Shadowsocks、TUIC 和 Trojan。

## 快速访问配置

您可以通过以下 URL 直接访问最新配置：
```
https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt
```
该项目具有高级代理配置管理功能。获取的配置会自动转换为 Sing-box 格式并存储在单独的 JSON 文件中。对于每个服务器，系统使用 get location 方法识别其地理位置，并自动将相应的国旗表情符号和国家名称添加到其标签中。这些功能使代理管理和使用变得更加用户友好和高效。

Sing-box 订阅链接：
```
https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/singbox_configs.json
```

## 频道和 URL 性能

以下是配置源（Telegram 频道和其他 URL）的实时性能统计。该图表每小时自动更新。

### 快速概览
<div align="center">
  <a href="assets/channel_stats_chart.svg">
    <img src="assets/channel_stats_chart.svg" alt="源性能统计" width="800">
  </a>
</div>

### 详细报告
📊 [查看完整交互式仪表盘](https://htmlpreview.github.io/?https://github.com/4n0nymou3/multi-proxy-config-fetcher/blob/main/assets/performance_report.html)

> **Fork 仓库的重要说明**：  
如果您 fork 此仓库，请确保将上述链接中的 `USERNAME` 替换为您的 GitHub 用户名。这确保链接指向您自己的交互式仪表盘而不是原始项目的仪表盘。操作步骤：
1. 在您 fork 的仓库中编辑 `README.md` 文件。
2. 找到以下行：
   ```markdown
   📊 [查看完整交互式仪表盘](https://htmlpreview.github.io/?https://github.com/USERNAME/multi-proxy-config-fetcher/blob/main/assets/performance_report.html)
   ```
3. 将 `USERNAME` 替换为您的 GitHub 用户名。
4. 提交更改。

每个源基于四个关键指标进行评分：
- **可靠性得分（35%）**：获取和更新配置的成功率。
- **配置质量（25%）**：有效配置与总获取配置的比率。
- **配置唯一性（25%）**：贡献的唯一配置百分比。
- **响应时间（15%）**：服务器响应时间和可用性。

总分实时计算并每小时更新。得分低于 30% 的源将自动禁用。

> **注意**：列出的源是示例。您可以在 `src/config.py` 中轻松修改源列表以使用您首选的 Telegram 频道、SSCONF 链接或其他 URL。上述性能指标基于对每个源在提供有效配置方面的可靠性的实时监控。

## 特性

- 支持多种代理协议：
  - WireGuard
  - Hysteria2
  - VLESS
  - VMess
  - Shadowsocks (SS)
  - Trojan
  - TUIC
- 从以下来源获取配置：
  - 公共 Telegram 频道
  - SSCONF 格式链接
  - 托管配置文件的 URL
- 智能处理 base64 编码配置（保留原始格式）
- 协议特定的验证和校验
- 每小时自动更新配置
- 验证配置年龄（排除超过 90 天的配置）
- 删除重复项
- 实时源性能监控
- 自动源健康管理
- 动态协议分布平衡

## 设置

1. Fork 此仓库。
2. 编辑 `src/config.py` 并将您的 Telegram 频道、SSCONF 链接或其他 URL 添加到 `SOURCE_URLS` 列表。
3. 在您 fork 的仓库中启用 GitHub Actions。
4. 配置将每小时自动更新在 `configs/proxy_configs.txt` 中。

## 手动设置

```bash
# 克隆仓库
git clone https://github.com/4n0nymou3/multi-proxy-config-fetcher.git
cd multi-proxy-config-fetcher

# 安装依赖
pip install -r requirements.txt

# 手动运行
python src/fetch_configs.py
```

## 配置

编辑 `src/config.py` 以修改：
- 源列表（Telegram 频道、SSCONF 链接或 URL）
- 每个协议的最小/最大配置数
- 协议比率和平衡
- 最大配置年龄
- 输出文件位置
- 支持的协议
- 请求头和超时

## Fork 仓库注意事项

如果您 fork 此仓库，需要手动启用 GitHub Actions：
1. 转到您 fork 的仓库中的 `Settings > Actions`。
2. 选择 **Allow all actions and reusable workflows**。
3. 保存设置。

## 项目结构

```
├── src/
│   ├── config.py              # 项目配置
│   ├── config_validator.py    # 配置验证和校验
│   └── fetch_configs.py       # 主获取器实现
├── configs/
│   ├── proxy_configs.txt      # 输出配置
│   └── channel_stats.json     # 源性能统计
└── .github/
    └── workflows/
        └── update-configs.yml # GitHub Actions 工作流
```

## 源统计

项目在 `configs/channel_stats.json` 中跟踪每个源的综合性能指标：
- 整体性能得分（0-100%）
- 获取配置的成功率
- 有效配置与总配置比率
- 唯一配置贡献
- 响应时间和可靠性
- 源健康状态

## 免责声明

本项目仅供教育和信息目的。开发者对本项目的任何滥用或其后果不承担责任。使用本软件时，请确保遵守所有相关法律法规。

## 关于开发者

由 **4n0nymou3** 开发。  
欲了解更多信息或联系开发者，请访问其 [X (Twitter) 个人资料](https://x.com/4n0nymou3)。
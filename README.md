[![Stars](https://img.shields.io/github/stars/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/stargazers)
[![Forks](https://img.shields.io/github/forks/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/network/members)
[![Issues](https://img.shields.io/github/issues/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/issues)
[![License](https://img.shields.io/github/license/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/blob/main/LICENSE)
[![Activity](https://img.shields.io/github/last-commit/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/commits)

# Multi Proxy Config Fetcher

[**🇺🇸English**](README.md) | [**![Lang_farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png)فارسی**](README_FA.md) | [**🇨🇳中文**](README_CN.md) | [**🇷🇺Русский**](README_RU.md)

This project automatically fetches and updates various proxy configurations from public Telegram channels, SSCONF links and other URLs containing configuration data. It supports multiple proxy protocols including WireGuard, Hysteria2, VLESS, VMess, Shadowsocks, TUIC, and Trojan.

## Quick Access to Configs

You can directly access the latest configurations through this URL:
```
https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt
```
This project features advanced capabilities for proxy configuration management. The retrieved configurations are automatically converted to Sing-box format and stored in a separate JSON file. For each server, its geographical location is identified using the get location method, and the corresponding flag emoji and country name are automatically added to its tag. These features make proxy management and usage significantly more user-friendly and efficient.

Sing-box subscription link:
```
https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/singbox_configs.json
```

## Channel and URL Performance

Below is the real-time performance statistics of the configured sources (Telegram channels and other URLs). This chart is automatically updated every hour.

### Quick Overview
<div align="center">
  <a href="assets/channel_stats_chart.svg">
    <img src="assets/channel_stats_chart.svg" alt="Source Performance Statistics" width="800">
  </a>
</div>

### Detailed Report
📊 [View Full Interactive Dashboard](https://htmlpreview.github.io/?https://github.com/4n0nymou3/multi-proxy-config-fetcher/blob/main/assets/performance_report.html)

> **Important for Forked Repositories**:  
If you fork this repository, make sure to replace `USERNAME` in the above link with your GitHub username. This ensures that the link directs to your own interactive dashboard instead of the original project's dashboard. To do this:
1. Edit the `README.md` file in your forked repository.
2. Locate the following line:
   ```markdown
   📊 [View Full Interactive Dashboard](https://htmlpreview.github.io/?https://github.com/USERNAME/multi-proxy-config-fetcher/blob/main/assets/performance_report.html)
   ```
3. Replace `USERNAME` with your GitHub username.
4. Commit the changes.

Each source is scored based on four key metrics:
- **Reliability Score (35%)**: Success rate in fetching and updating configurations.
- **Config Quality (25%)**: Ratio of valid configs to total fetched configurations.
- **Config Uniqueness (25%)**: Percentage of unique configs contributed.
- **Response Time (15%)**: Server response time and availability.

The overall score is calculated in real-time and updated hourly. Sources scoring below 30% are automatically disabled.

> **Note**: The sources listed are examples. You can easily modify the source list in `src/config.py` to use your preferred Telegram channels, SSCONF links or other URLs. The performance metrics shown above are based on real-time monitoring of each source's reliability in providing valid configurations.

## Features

- Supports multiple proxy protocols:
  - WireGuard
  - Hysteria2
  - VLESS
  - VMess
  - Shadowsocks (SS)
  - Trojan
  - TUIC
- Fetches configs from:
  - Public Telegram channels
  - SSCONF format links
  - URLs hosting configuration files
- Smart handling of base64-encoded configs (preserves original format)
- Protocol-specific validation and verification
- Automatically updates configs every hour
- Validates config age (excludes configs older than 90 days)
- Removes duplicates
- Real-time source performance monitoring
- Automatic source health management
- Dynamic protocol distribution balancing

## Setup

1. Fork this repository.
2. Edit `src/config.py` and add your Telegram channels, SSCONF links or other URLs to the `SOURCE_URLS` list.
3. Enable GitHub Actions in your forked repository.
4. The configs will be automatically updated every hour in `configs/proxy_configs.txt`.

## Manual Setup

```bash
# Clone the repository
git clone https://github.com/4n0nymou3/multi-proxy-config-fetcher.git
cd multi-proxy-config-fetcher

# Install dependencies
pip install -r requirements.txt

# Run manually
python src/fetch_configs.py
```

## Configuration

Edit `src/config.py` to modify:
- Source list (Telegram channels, SSCONF links or URLs)
- Minimum/maximum configs per protocol
- Protocol ratios and balancing
- Maximum config age
- Output file location
- Supported protocols
- Request headers and timeouts

## Note for Forked Repositories

If you fork this repository, you need to manually enable GitHub Actions:
1. Go to `Settings > Actions` in your forked repository.
2. Select **Allow all actions and reusable workflows**.
3. Save the settings.

## Project Structure

```
├── src/
│   ├── config.py              # Project configuration
│   ├── config_validator.py    # Config validation and verification
│   └── fetch_configs.py       # Main fetcher implementation
├── configs/
│   ├── proxy_configs.txt      # Output configs
│   └── channel_stats.json     # Source performance stats
└── .github/
    └── workflows/
        └── update-configs.yml # GitHub Actions workflow
```

## Source Statistics

The project tracks comprehensive performance metrics of each source in `configs/channel_stats.json`:
- Overall performance score (0-100%)
- Success rate in fetching configurations
- Valid vs total configs ratio
- Unique config contribution
- Response time and reliability
- Source health status

## Disclaimer

This project is provided for educational and informational purposes only. The developer is not responsible for any misuse of this project or its outcomes. Please ensure compliance with all relevant laws and regulations when using this software.

## About the Developer

Developed by **4n0nymou3**.  
For more information or to contact the developer, visit their [X (Twitter) profile](https://x.com/4n0nymou3).
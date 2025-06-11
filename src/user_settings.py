# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt",
    "https://t.me/s/v2rayfree",
    "https://t.me/s/FreeV2rays",
    "https://t.me/s/v2ray_free_conf",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/IP_CF_Config",
    "https://t.me/s/prrofile_purple",
    "https://t.me/s/meli_proxyy",
    "https://t.me/s/DirectVPN",
    "https://t.me/s/VmessProtocol",
    "https://t.me/s/vpnfail_vless",
    "https://t.me/s/DailyV2RY",
    "https://t.me/s/shadowproxy66",
    "https://t.me/s/moftconfig",
    "https://t.me/s/ConfigsHUB2",
    "https://t.me/s/ArV2ray",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = False

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 100

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": True,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 7
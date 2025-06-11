import json
import base64
import uuid
import time
import socket
import requests
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse, parse_qs

class ConfigToSingbox:
    def __init__(self):
        self.output_file = 'configs/singbox_configs.json'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def get_location_from_ip_api(self, ip: str) -> Tuple[str, str]:
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}', headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success' and data.get('countryCode'):
                    return data['countryCode'].lower(), data['country']
        except Exception:
            pass
        return '', ''

    def get_location_from_ipapi_co(self, ip: str) -> Tuple[str, str]:
        try:
            response = requests.get(f'https://ipapi.co/{ip}/json/', headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('country_code') and data.get('country_name'):
                    return data['country_code'].lower(), data['country_name']
        except Exception:
            pass
        return '', ''

    def get_location_from_ipwhois(self, ip: str) -> Tuple[str, str]:
        try:
            response = requests.get(f'https://ipwhois.app/json/{ip}', headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('country_code') and data.get('country'):
                    return data['country_code'].lower(), data['country']
        except Exception:
            pass
        return '', ''

    def get_location_from_ipdata(self, ip: str) -> Tuple[str, str]:
        try:
            response = requests.get(f'https://api.ipdata.co/{ip}?api-key=test', headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('country_code') and data.get('country_name'):
                    return data['country_code'].lower(), data['country_name']
        except Exception:
            pass
        return '', ''

    def get_location_from_abstractapi(self, ip: str) -> Tuple[str, str]:
        try:
            response = requests.get(f'https://ipgeolocation.abstractapi.com/v1/?api_key=test&ip_address={ip}', 
                                  headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('country_code') and data.get('country'):
                    return data['country_code'].lower(), data['country']
        except Exception:
            pass
        return '', ''

    def get_location(self, address: str) -> tuple:
        try:
            ip = socket.gethostbyname(address)
            apis = [
                self.get_location_from_ip_api,
                self.get_location_from_ipapi_co,
                self.get_location_from_ipwhois,
                self.get_location_from_ipdata,
                self.get_location_from_abstractapi
            ]
            
            for api_func in apis:
                country_code, country = api_func(ip)
                if country_code and country and len(country_code) == 2:
                    flag = ''.join(chr(ord('🇦') + ord(c.upper()) - ord('A')) for c in country_code)
                    time.sleep(1)
                    return flag, country
                time.sleep(1)
                
        except Exception:
            pass
            
        return "🏳️", "Unknown"

    def decode_vmess(self, config: str) -> Optional[Dict]:
        try:
            encoded = config.replace('vmess://', '')
            decoded = base64.b64decode(encoded).decode('utf-8')
            return json.loads(decoded)
        except Exception:
            return None

    def parse_vless(self, config: str) -> Optional[Dict]:
        try:
            url = urlparse(config)
            if url.scheme.lower() != 'vless' or not url.hostname:
                return None
            netloc = url.netloc.split('@')[-1]
            address, port = netloc.split(':') if ':' in netloc else (netloc, '443')
            params = parse_qs(url.query)
            return {
                'uuid': url.username,
                'address': address,
                'port': int(port),
                'flow': params.get('flow', [''])[0],
                'sni': params.get('sni', [address])[0],
                'type': params.get('type', ['tcp'])[0],
                'path': params.get('path', [''])[0],
                'host': params.get('host', [''])[0]
            }
        except Exception:
            return None

    def parse_trojan(self, config: str) -> Optional[Dict]:
        try:
            url = urlparse(config)
            if url.scheme.lower() != 'trojan' or not url.hostname:
                return None
            port = url.port or 443
            params = parse_qs(url.query)
            return {
                'password': url.username,
                'address': url.hostname,
                'port': port,
                'sni': params.get('sni', [url.hostname])[0],
                'alpn': params.get('alpn', [''])[0],
                'type': params.get('type', ['tcp'])[0],
                'path': params.get('path', [''])[0]
            }
        except Exception:
            return None

    def parse_hysteria2(self, config: str) -> Optional[Dict]:
        try:
            url = urlparse(config)
            if url.scheme.lower() not in ['hysteria2', 'hy2'] or not url.hostname or not url.port:
                return None
            query = dict(pair.split('=') for pair in url.query.split('&')) if url.query else {}
            return {
                'address': url.hostname,
                'port': url.port,
                'password': url.username or query.get('password', ''),
                'sni': query.get('sni', url.hostname)
            }
        except Exception:
            return None

    def parse_shadowsocks(self, config: str) -> Optional[Dict]:
        try:
            parts = config.replace('ss://', '').split('@')
            if len(parts) != 2:
                return None
            method_pass = base64.b64decode(parts[0]).decode('utf-8')
            method, password = method_pass.split(':')
            server_parts = parts[1].split('#')[0]
            host, port = server_parts.split(':')
            return {
                'method': method,
                'password': password,
                'address': host,
                'port': int(port)
            }
        except Exception:
            return None

    def convert_to_singbox(self, config: str) -> Optional[Dict]:
        try:
            config_lower = config.lower()
            if config_lower.startswith('vmess://'):
                vmess_data = self.decode_vmess(config)
                if not vmess_data or not vmess_data.get('add') or not vmess_data.get('port') or not vmess_data.get('id'):
                    return None
                transport = {}
                if vmess_data.get('net') in ['ws', 'h2']:
                    if vmess_data.get('path', ''):
                        transport["path"] = vmess_data.get('path')
                    if vmess_data.get('host', ''):
                        transport["headers"] = {"Host": vmess_data.get('host')}
                    transport["type"] = vmess_data.get('net', 'tcp')
                flag, country = self.get_location(vmess_data['add'])
                return {
                    "type": "vmess",
                    "tag": f"{flag} vmess-{str(uuid.uuid4())[:8]} ({country})",
                    "server": vmess_data['add'],
                    "server_port": int(vmess_data['port']),
                    "uuid": vmess_data['id'],
                    "security": vmess_data.get('scy', 'auto'),
                    "alter_id": int(vmess_data.get('aid', 0)),
                    "transport": transport,
                    "tls": {
                        "enabled": vmess_data.get('tls') == 'tls',
                        "insecure": True,
                        "server_name": vmess_data.get('sni', vmess_data['add'])
                    }
                }
            elif config_lower.startswith('vless://'):
                vless_data = self.parse_vless(config)
                if not vless_data:
                    return None
                transport = {}
                if vless_data['type'] == 'ws':
                    if vless_data.get('path', ''):
                        transport["path"] = vless_data.get('path')
                    if vless_data.get('host', ''):
                        transport["headers"] = {"Host": vless_data.get('host')}
                    transport["type"] = "ws"
                flag, country = self.get_location(vless_data['address'])
                return {
                    "type": "vless",
                    "tag": f"{flag} vless-{str(uuid.uuid4())[:8]} ({country})",
                    "server": vless_data['address'],
                    "server_port": vless_data['port'],
                    "uuid": vless_data['uuid'],
                    "flow": vless_data['flow'],
                    "tls": {
                        "enabled": True,
                        "server_name": vless_data['sni'],
                        "insecure": True
                    },
                    "transport": transport
                }
            elif config_lower.startswith('trojan://'):
                trojan_data = self.parse_trojan(config)
                if not trojan_data:
                    return None
                transport = {}
                if trojan_data['type'] != 'tcp' and trojan_data.get('path', ''):
                    transport["path"] = trojan_data.get('path')
                    transport["type"] = trojan_data['type']
                flag, country = self.get_location(trojan_data['address'])
                return {
                    "type": "trojan",
                    "tag": f"{flag} trojan-{str(uuid.uuid4())[:8]} ({country})",
                    "server": trojan_data['address'],
                    "server_port": trojan_data['port'],
                    "password": trojan_data['password'],
                    "tls": {
                        "enabled": True,
                        "server_name": trojan_data['sni'],
                        "alpn": trojan_data['alpn'].split(',') if trojan_data['alpn'] else [],
                        "insecure": True
                    },
                    "transport": transport
                }
            elif config_lower.startswith('hysteria2://') or config_lower.startswith('hy2://'):
                hy2_data = self.parse_hysteria2(config)
                if not hy2_data or not hy2_data.get('address') or not hy2_data.get('port'):
                    return None
                flag, country = self.get_location(hy2_data['address'])
                return {
                    "type": "hysteria2",
                    "tag": f"{flag} hysteria2-{str(uuid.uuid4())[:8]} ({country})",
                    "server": hy2_data['address'],
                    "server_port": hy2_data['port'],
                    "password": hy2_data['password'],
                    "tls": {
                        "enabled": True,
                        "insecure": True,
                        "server_name": hy2_data['sni']
                    }
                }
            elif config_lower.startswith('ss://'):
                ss_data = self.parse_shadowsocks(config)
                if not ss_data or not ss_data.get('address') or not ss_data.get('port'):
                    return None
                flag, country = self.get_location(ss_data['address'])
                return {
                    "type": "shadowsocks",
                    "tag": f"{flag} ss-{str(uuid.uuid4())[:8]} ({country})",
                    "server": ss_data['address'],
                    "server_port": ss_data['port'],
                    "method": ss_data['method'],
                    "password": ss_data['password']
                }
            return None
        except Exception:
            return None

    def process_configs(self):
        try:
            with open('configs/proxy_configs.txt', 'r') as f:
                configs = f.read().strip().split('\n')
            outbounds = []
            valid_tags = []
            for config in configs:
                config = config.strip()
                if not config or config.startswith('//'):
                    continue
                converted = self.convert_to_singbox(config)
                if converted:
                    outbounds.append(converted)
                    valid_tags.append(converted['tag'])
            if not outbounds:
                return
            dns_config = {
                "dns": {
                    "final": "local-dns",
                    "rules": [
                        {"clash_mode": "Global", "server": "proxy-dns", "source_ip_cidr": ["172.19.0.0/30"]},
                        {"server": "proxy-dns", "source_ip_cidr": ["172.19.0.0/30"]},
                        {"clash_mode": "Direct", "server": "direct-dns"}
                    ],
                    "servers": [
                        {"address": "tls://208.67.222.123", "address_resolver": "local-dns", "detour": "proxy", "tag": "proxy-dns"},
                        {"address": "local", "detour": "direct", "tag": "local-dns"},
                        {"address": "rcode://success", "tag": "block"},
                        {"address": "local", "detour": "direct", "tag": "direct-dns"}
                    ],
                    "strategy": "prefer_ipv4"
                }
            }
            inbounds_config = [
                {"address": ["172.19.0.1/30", "fdfe:dcba:9876::1/126"], "auto_route": True, "endpoint_independent_nat": False, "mtu": 9000, "platform": {"http_proxy": {"enabled": True, "server": "127.0.0.1", "server_port": 2080}}, "sniff": True, "stack": "system", "strict_route": False, "type": "tun"},
                {"listen": "127.0.0.1", "listen_port": 2080, "sniff": True, "type": "mixed", "users": []}
            ]
            outbounds_config = [
                {"tag": "proxy", "type": "selector", "outbounds": ["auto"] + valid_tags + ["direct"]},
                {"tag": "auto", "type": "urltest", "outbounds": valid_tags, "url": "http://www.gstatic.com/generate_204", "interval": "10m", "tolerance": 50},
                {"tag": "direct", "type": "direct"}
            ] + outbounds
            route_config = {
                "auto_detect_interface": True,
                "final": "proxy",
                "rules": [
                    {"clash_mode": "Direct", "outbound": "direct"},
                    {"clash_mode": "Global", "outbound": "proxy"},
                    {"protocol": "dns", "action": "hijack-dns"}
                ]
            }
            singbox_config = {**dns_config, "inbounds": inbounds_config, "outbounds": outbounds_config, "route": route_config}
            with open(self.output_file, 'w') as f:
                json.dump(singbox_config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error processing configs: {str(e)}")

def main():
    converter = ConfigToSingbox()
    converter.process_configs()

if __name__ == '__main__':
    main()
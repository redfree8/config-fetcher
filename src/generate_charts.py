import json
import os
from datetime import datetime

def generate_basic_svg(stats_data):
    width = 800
    height = len(stats_data['channels']) * 50 + 100
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
    <svg width="{width}" height="{height}" version="1.1" xmlns="http://www.w3.org/2000/svg">
    <style>
        .row {{ font: 14px Arial; fill: #64748b; }}
        .score {{ font: bold 14px Arial; fill: #64748b; }}
    </style>
    <text x="400" y="40" text-anchor="middle" font-size="20px" font-weight="bold" fill="#64748b">Channel Performance Overview</text>'''
    
    for idx, channel in enumerate(stats_data['channels']):
        y = 80 + (idx * 50)
        name = channel['url'].split('/')[-1]
        score = channel['metrics']['overall_score']
        success = (channel['metrics']['success_count'] / 
                  max(1, channel['metrics']['success_count'] + channel['metrics']['fail_count'])) * 100
        
        svg += f'<rect x="150" y="{y}" width="500" height="30" fill="#eee" rx="5"/>'
        
        width = min(500, 5 * score)
        color = '#22c55e' if score >= 70 else '#eab308' if score >= 50 else '#ef4444'
        svg += f'<rect x="150" y="{y}" width="{width}" height="30" fill="{color}" rx="5"/>'
        
        svg += f'''
        <text x="140" y="{y+20}" text-anchor="end" class="row">{name}</text>
        <text x="660" y="{y+20}" text-anchor="start" class="score">{score:.1f}% (S:{success:.0f}%)</text>'''
    
    svg += '</svg>'
    return svg

def generate_html_report(stats_data):
    html = f'''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Channel Performance Report</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gradient-to-br from-gray-50 to-gray-100 min-h-screen">
        <div class="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8">
            <header class="bg-white rounded-lg shadow-lg p-6 mb-8">
                <h1 class="text-3xl font-bold text-gray-900 text-center">Proxy Channel Performance Dashboard</h1>
                <p class="text-center text-gray-600 mt-2">Last Updated: {stats_data['timestamp']}</p>
                <div class="mt-6 bg-blue-50 rounded-lg p-4 flex flex-col items-center justify-center">
                    <h2 class="text-lg font-semibold text-blue-800">Developer Information</h2>
                    <div class="flex items-center space-x-6 mt-2">
                        <a href="https://github.com/4n0nymou3" target="_blank" class="flex items-center text-gray-700 hover:text-blue-600">
                            <svg class="w-5 h-5 mr-2" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
                            </svg>
                            GitHub Profile
                        </a>
                        <a href="https://github.com/4n0nymou3/multi-proxy-config-fetcher" target="_blank" class="flex items-center text-gray-700 hover:text-blue-600">
                            <svg class="w-5 h-5 mr-2" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
                            </svg>
                            Project Repository
                        </a>
                        <a href="https://x.com/4n0nymou3" target="_blank" class="flex items-center text-gray-700 hover:text-blue-600">
                            <svg class="w-5 h-5 mr-2" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                            </svg>
                            X (Twitter)
                        </a>
                    </div>
                </div>
            </header>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">Active Channels</h3>
                    <div class="text-3xl font-bold text-blue-600">
                        {sum(1 for c in stats_data['channels'] if c['enabled'])}
                        <span class="text-sm font-normal text-gray-500">/ {len(stats_data['channels'])}</span>
                    </div>
                </div>

                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">Total Valid Configs</h3>
                    <div class="text-3xl font-bold text-green-600">
                        {sum(c['metrics']['valid_configs'] for c in stats_data['channels'])}
                    </div>
                </div>

                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">Average Success Rate</h3>
                    <div class="text-3xl font-bold text-yellow-600">
                        {sum((c['metrics']['success_count']/(max(1, c['metrics']['success_count'] + c['metrics']['fail_count'])))*100 for c in stats_data['channels'])/len(stats_data['channels']):.1f}%
                    </div>
                </div>

                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">Average Response Time</h3>
                    <div class="text-3xl font-bold text-purple-600">
                        {sum(c['metrics']['avg_response_time'] for c in stats_data['channels'])/len(stats_data['channels']):.2f}s
                    </div>
                </div>
            </div>

            <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
                <h3 class="text-xl font-semibold text-gray-800 mb-6">Detailed Channel Statistics</h3>
                <div class="overflow-x-auto">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Channel</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Score</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Success Rate</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Response Time</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Valid/Total</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Last Success</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">'''

    for channel in sorted(stats_data['channels'], key=lambda x: x['metrics']['overall_score'], reverse=True):
        success_rate = (channel['metrics']['success_count'] / 
                       max(1, channel['metrics']['success_count'] + channel['metrics']['fail_count'])) * 100
        
        status_color = 'green' if channel['enabled'] else 'red'
        score_color = 'green' if channel['metrics']['overall_score'] >= 70 else 'yellow' if channel['metrics']['overall_score'] >= 50 else 'red'
        
        html += f'''
                            <tr>
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                                    {channel['url'].split('/')[-1]}
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-{status_color}-100 text-{status_color}-800">
                                        {'Active' if channel['enabled'] else 'Inactive'}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-{score_color}-100 text-{score_color}-800">
                                        {channel['metrics']['overall_score']:.1f}%
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {success_rate:.1f}%
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {channel['metrics']['avg_response_time']:.2f}s
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {channel['metrics']['valid_configs']}/{channel['metrics']['total_configs']}
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {channel['metrics']['last_success']}
                                </td>
                            </tr>'''

    html += '''
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>'''
    
    return html

def main():
    try:
        with open('configs/channel_stats.json', 'r') as f:
            stats_data = json.load(f)
        
        os.makedirs('assets', exist_ok=True)
        
        svg_content = generate_basic_svg(stats_data)
        with open('assets/channel_stats_chart.svg', 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        html_content = generate_html_report(stats_data)
        with open('assets/performance_report.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("Successfully generated chart and report!")
        
    except Exception as e:
        print(f"Error generating outputs: {str(e)}")

if __name__ == '__main__':
    main()
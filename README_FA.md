[![Stars](https://img.shields.io/github/stars/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/stargazers)
[![Forks](https://img.shields.io/github/forks/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/network/members)
[![Issues](https://img.shields.io/github/issues/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/issues)
[![License](https://img.shields.io/github/license/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/blob/main/LICENSE)
[![Activity](https://img.shields.io/github/last-commit/4n0nymou3/multi-proxy-config-fetcher?style=flat-square)](https://github.com/4n0nymou3/multi-proxy-config-fetcher/commits)

<div dir="rtl">

# دریافت‌کننده پیکربندی‌های پراکسی

[**🇺🇸English**](README.md) | [**فارسی![Lang_farsi](https://user-images.githubusercontent.com/125398461/234186932-52f1fa82-52c6-417f-8b37-08fe9250a55f.png)**](README_FA.md) | [**🇨🇳中文**](README_CN.md) | [**🇷🇺Русский**](README_RU.md)

این پروژه به‌طور خودکار پیکربندی‌های مختلف پراکسی را از کانال‌های عمومی تلگرام، لینک‌های SSCONF و سایر URL‌های حاوی داده‌های پیکربندی دریافت و به‌روزرسانی می‌کند. این پروژه از پروتکل‌های متعدد پراکسی از جمله WireGuard، Hysteria2، VLESS، VMess، Shadowsocks، TUIC و Trojan پشتیبانی می‌کند.

## دسترسی سریع به پیکربندی‌ها

شما می‌توانید مستقیماً از طریق این URL به آخرین پیکربندی‌ها دسترسی پیدا کنید:
```
https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt
```
این پروژه دارای قابلیت‌های پیشرفته‌ای برای مدیریت کانفیگ‌های پروکسی است. کانفیگ‌های دریافت شده به صورت خودکار به فرمت Sing-box تبدیل می‌شوند و در یک فایل JSON جداگانه ذخیره می‌شوند. برای هر سرور، موقعیت جغرافیایی آن با استفاده از متد get location شناسایی شده و به صورت خودکار ایموجی پرچم و نام کشور مربوطه به تگ آن اضافه می‌شود. این ویژگی‌ها باعث می‌شود مدیریت و استفاده از پروکسی‌ها برای کاربران بسیار ساده‌تر شود.

لینک اشتراک Sing-box:
```
https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/refs/heads/main/configs/singbox_configs.json
```

## عملکرد کانال‌ها و URL‌ها

در زیر، آمار عملکرد بلادرنگ منابع پیکربندی شده (کانال‌های تلگرام و سایر URL‌ها) را مشاهده می‌کنید. این نمودار هر ساعت به‌طور خودکار به‌روزرسانی می‌شود.

### نمای کلی
<div align="center">
  <a href="assets/channel_stats_chart.svg">
    <img src="assets/channel_stats_chart.svg" alt="آمار عملکرد منابع" width="800">
  </a>
</div>

### گزارش تفصیلی
📊 [مشاهده داشبورد تعاملی کامل](https://htmlpreview.github.io/?https://github.com/4n0nymou3/multi-proxy-config-fetcher/blob/main/assets/performance_report.html)

> **نکته مهم برای مخازن فورک شده**:  
اگر این مخزن را فورک می‌کنید، حتماً `USERNAME` را در لینک بالا با نام کاربری گیت‌هاب خود جایگزین کنید. این کار اطمینان می‌دهد که لینک به داشبورد تعاملی مخزن شما به جای داشبورد پروژه اصلی هدایت می‌شود. برای این کار:
1. فایل `README.md` را در مخزن فورک شده خود ویرایش کنید.
2. این خط را پیدا کنید:
   ```markdown
   📊 [مشاهده داشبورد تعاملی کامل](https://htmlpreview.github.io/?https://github.com/USERNAME/multi-proxy-config-fetcher/blob/main/assets/performance_report.html)
   ```
3. `USERNAME` را با نام کاربری گیت‌هاب خود جایگزین کنید.
4. تغییرات را ثبت کنید.

هر منبع بر اساس چهار معیار کلیدی امتیازدهی می‌شود:
- **امتیاز قابلیت اطمینان (۳۵٪)**: نرخ موفقیت در دریافت و به‌روزرسانی پیکربندی‌ها.
- **کیفیت پیکربندی (۲۵٪)**: نسبت پیکربندی‌های معتبر به کل پیکربندی‌های دریافت شده.
- **یکتایی پیکربندی (۲۵٪)**: درصد پیکربندی‌های منحصر به فرد ارائه شده.
- **زمان پاسخ (۱۵٪)**: زمان پاسخ سرور و دسترس‌پذیری.

امتیاز کلی به صورت بلادرنگ محاسبه و هر ساعت به‌روز می‌شود. منابعی که امتیاز زیر ۳۰٪ کسب کنند به طور خودکار غیرفعال می‌شوند.

> **نکته**: منابع فهرست شده نمونه هستند. شما می‌توانید به راحتی فهرست منابع را در `src/config.py` برای استفاده از کانال‌های تلگرام، لینک‌های SSCONF یا URL‌های مورد نظر خود تغییر دهید. معیارهای عملکرد نشان داده شده بر اساس نظارت بلادرنگ بر قابلیت اطمینان هر منبع در ارائه پیکربندی‌های معتبر است.

## ویژگی‌ها

- پشتیبانی از پروتکل‌های متعدد پراکسی:
  - WireGuard
  - Hysteria2
  - VLESS
  - VMess
  - Shadowsocks (SS)
  - Trojan
  - TUIC
- دریافت پیکربندی‌ها از:
  - کانال‌های عمومی تلگرام
  - لینک‌های فرمت SSCONF
  - URL‌های میزبان فایل‌های پیکربندی
- مدیریت هوشمند پیکربندی‌های کدگذاری شده با base64 (حفظ فرمت اصلی)
- اعتبارسنجی و تأیید مختص پروتکل
- به‌روزرسانی خودکار پیکربندی‌ها هر ساعت
- اعتبارسنجی سن پیکربندی (حذف پیکربندی‌های قدیمی‌تر از ۹۰ روز)
- حذف موارد تکراری
- نظارت بلادرنگ بر عملکرد منابع
- مدیریت خودکار سلامت منابع
- متعادل‌سازی پویای توزیع پروتکل‌ها

## راه‌اندازی

1. این مخزن را فورک کنید.
2. فایل `src/config.py` را ویرایش کنید و کانال‌های تلگرام، لینک‌های SSCONF یا URL‌های خود را به لیست `SOURCE_URLS` اضافه کنید.
3. GitHub Actions را در مخزن فورک شده خود فعال کنید.
4. پیکربندی‌ها هر ساعت به طور خودکار در `configs/proxy_configs.txt` به‌روزرسانی می‌شوند.

## راه‌اندازی دستی

```bash
# کلون کردن مخزن
git clone https://github.com/4n0nymou3/multi-proxy-config-fetcher.git
cd multi-proxy-config-fetcher

# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای دستی
python src/fetch_configs.py
```

## پیکربندی

برای تغییر موارد زیر، فایل `src/config.py` را ویرایش کنید:
- لیست منابع (کانال‌های تلگرام، لینک‌های SSCONF یا URL‌ها)
- حداقل/حداکثر پیکربندی برای هر پروتکل
- نسبت‌ها و متعادل‌سازی پروتکل‌ها
- حداکثر سن پیکربندی
- محل فایل خروجی
- پروتکل‌های پشتیبانی شده
- هدرهای درخواست و مهلت‌های زمانی

## نکته برای مخازن فورک شده

اگر این مخزن را فورک می‌کنید، باید به صورت دستی GitHub Actions را فعال کنید:
1. به `Settings > Actions` در مخزن فورک شده خود بروید.
2. گزینه **Allow all actions and reusable workflows** را انتخاب کنید.
3. تنظیمات را ذخیره کنید.

## ساختار پروژه

```
├── src/
│   ├── config.py              # پیکربندی پروژه
│   ├── config_validator.py    # اعتبارسنجی و تأیید پیکربندی
│   └── fetch_configs.py       # پیاده‌سازی اصلی دریافت‌کننده
├── configs/
│   ├── proxy_configs.txt      # پیکربندی‌های خروجی
│   └── channel_stats.json     # آمار عملکرد منابع
└── .github/
    └── workflows/
        └── update-configs.yml # گردش کار GitHub Actions
```

## آمار منابع

پروژه معیارهای عملکرد جامع هر منبع را در `configs/channel_stats.json` پیگیری می‌کند:
- امتیاز کلی عملکرد (۰-۱۰۰٪)
- نرخ موفقیت در دریافت پیکربندی‌ها
- نسبت پیکربندی‌های معتبر به کل
- مشارکت پیکربندی‌های منحصر به فرد
- زمان پاسخ و قابلیت اطمینان
- وضعیت سلامت منبع

## سلب مسئولیت

این پروژه صرفاً برای اهداف آموزشی و اطلاع‌رسانی ارائه شده است. توسعه‌دهنده مسئولیتی در قبال سوء استفاده از این پروژه یا پیامدهای آن ندارد. لطفاً هنگام استفاده از این نرم‌افزار، از رعایت تمام قوانین و مقررات مربوطه اطمینان حاصل کنید.

## درباره توسعه‌دهنده

توسعه یافته توسط **4n0nymou3**.  
برای اطلاعات بیشتر یا تماس با توسعه‌دهنده، از [پروفایل X (توییتر)](https://x.com/4n0nymou3) دیدن کنید.

</div>
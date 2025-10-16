
# Tron Wallet Address Generator from Seed Phrase

این کد **فایل متنی شما که حاوی کلمات ریکاوری (seed phrase)** را دریافت می‌کند و **آدرس‌های شبکه ترون** مربوطه را تولید کرده و در یک فایل متنی ذخیره می‌کند.

---

## 📄 فایل‌های مورد نیاز

- **seed.txt**  
  این فایل باید حاوی کلمات ریکاوری شما باشد. می‌توانید سید خود را جایگزین کنید یا آدرس seed خود را در آن قرار دهید.

- **result.txt**  
  پس از اجرای برنامه، سیدها و آدرس‌های مربوطه در این فایل ذخیره می‌شوند.

---

## ⚡ ویژگی‌ها

- **تولید سریع آدرس ترون از seed phrase**  
- **پردازش موازی (Multi Processing)**: سرعت بررسی چندین برابر حالت عادی است
- پشتیبانی از کتابخانه‌های: `tropy`, `multiprocessing`

---

## 🚀 نحوه اجرای برنامه

### نصب کتابخانه‌ها
```bash
pip install tropy
```

### 🖥️ Installation Method on Linux:

### 🚧 آموزش نصب روی لینوکس :
### 🚦 برای اجرای بروی گوشی موبایل می توانید از pydroid3 یا Termux استفاده کنید 
```bash 
git clone https://github.com/blackBat7/Seed_phrase_to_trc20Address
```
```bash
cd Seed_phrase_to_trc20Address
```
```bash
python SeedToTrxAddress.py
```

# 📷 Telegram Channel Image Extractor

This tool allows you to **extract and download all images from a public or private Telegram channel** using Python and the [Telethon](https://github.com/LonamiWebs/Telethon) library.

---

## 🧩 Features

- Extracts **photos/images** from any Telegram **channel or group** you have access to.
- Automatically saves images in a local folder.
- Works with **public** and **private** channels (if you're a member).
- Simple and lightweight script.

---

## 🚀 Requirements

- Python 3.6+
- Telegram API credentials (Get from [my.telegram.org](https://my.telegram.org))
- Telethon Python package

---

## 🔧 Setup Instructions

### 1. **Install Python dependencies**

```bash
pip install telethon
```

## 2. Get Telegram API Credentials

- Go to [https://my.telegram.org](https://my.telegram.org)
- Log in with your Telegram number
- Click on **API Development Tools**
- Note down your:
  - **API ID**
  - **API Hash**


### 3. **Run The Script**

```bash
python image_extractor.py
```

---

## 🗂️ Output

- All images are saved to a local folder named `downloaded_images/`
- Files are named using the message ID for uniqueness



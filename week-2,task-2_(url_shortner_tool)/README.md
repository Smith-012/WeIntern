# Tiny URL CLI Project

## 📌 Project Overview
This is a **Tiny URL (URL Shortener) CLI application** built using **Python**.  
It allows users to shorten long URLs, store them persistently, and retrieve the original URLs using generated slugs.

---

## 🚀 Features
- Shorten long URLs into unique slugs
- Retrieve original URLs using slugs
- Persistent storage using a JSON file
- Input validation for URLs
- Simple Command Line Interface (CLI)
- Duplicate URL prevention

---

## 🛠️ Technologies Used
- Python 3
- UUID
- Hashlib
- JSON (file-based storage)

---

## 📂 Project Structure
```
.
├── url_short.py        # Application code
├── urls.json           # Stored URL data (auto-generated)
└── README.md           # Project documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone or download the project
```bash
git clone <repository-url>
cd tiny-url-cli
```

### 2️⃣ Run the program
```bash
python url_short.py
```

---

## 📋 How It Works

### Menu Options
```
1. Shorten URL
2. Retrieve URL
3. Exit
```

### Shorten URL
- Enter a valid URL (must start with http:// or https://)
- A unique slug is generated and saved in `urls.json`

### Retrieve URL
- Enter the previously generated slug, which you can find from previously generated file `urls.json`
- The original URL is displayed and you can open that url directly from terminal

---

## 💾 Data Persistence
All shortened URLs are stored in a `urls.json` file.  
Even after closing and reopening the program, previously generated slugs remain accessible.

---

## 🧪 Example Stored Data
```json
{
  "a3f9c1": "https://google.com",
  "7b2e4d": "https://github.com"
}
```

---

## Sample Execution (CLI Output)

Below is an example of how the URL Shortener CLI application works during runtime:
```bash
PS C:\Users\Hp\Downloads\url_shortner> python url_short.py

1. Shorten URL
2. Retrieve URL
3. Exit
Choose option: 2
Enter slug: cb0a96
Original URL: https://chatgpt.com/c/6956aaf6-29d4-8322-8f52-13c1f44a1104

1. Shorten URL
2. Retrieve URL
3. Exit
Choose option:
```

---

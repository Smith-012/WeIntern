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
├── main.py        # Application code
├── urls.json      # Stored URL data (auto-generated)
└── README.md      # Project documentation
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
python main.py
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
- Enter the previously generated slug
- The original URL is displayed

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

## ✅ Assignment Compliance
✔ CLI-based application  
✔ URL shortening and retrieval  
✔ Input validation  
✔ Persistent storage  
✔ Uses UUID and hashing  

---

## 📄 License
This project is created for educational purposes.

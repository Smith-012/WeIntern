# Text Analyzer Desktop Application

## 📌 Project Overview
This is a **Python desktop GUI application** built using **Tkinter**.
The application analyzes user-provided text and displays useful statistics in a clean interface with **Dark Mode support**.

---

## 🛠️ Technologies Used
- **Python 3**
- **Tkinter** (for GUI – comes with Python)
- **NLTK** (for stopword filtering)

---

## ✨ Features
- Text input using GUI
- Word count
- Average sentence length
- Top 5 most frequent words
- Stopword removal using NLTK
- Dark Mode toggle
- Export results to `.txt` file

---

## 📁 Project Structure
```
text_analyzer_tool/
├── app.py
├── text_analysis.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python
Make sure **Python 3+** is installed on your system.

### 2️⃣ Install Dependencies
Use the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3️⃣ Download NLTK Stopwords (One-Time Setup)
```bash
python -m nltk.downloader stopwords
```

---

## ▶️ How to Run the Application
```bash
python app.py
```

A window titled **Text Analyzer Tool** will open.

---

## 🧪 Example for Testing

### Sample Input
```
Artificial Intelligence is transforming the world.
Artificial Intelligence helps people solve complex problems.
The world is changing rapidly because of artificial intelligence.
```

### Expected Output
```
Word Count: 12
Average Sentence Length: 4

Top 5 Words:
artificial : 3
intelligence : 3
world : 2
transforming : 1
helps : 1
```

---

## 📁 Export Feature
- Click **Export to TXT**
- Save dialog opens with default name:
  ```
  txtextract.txt
  ```
- Choose any location to save the file

---

## 📄 requirements.txt
The project requires only one external dependency:
```
nltk
```

Tkinter and other modules are part of standard Python.

---
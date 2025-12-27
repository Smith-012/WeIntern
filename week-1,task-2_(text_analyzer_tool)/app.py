import sys
sys.dont_write_bytecode = True

import tkinter as tk
from tkinter import messagebox, filedialog
from text_analysis import analyze_text

class TextAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Analyzer Tool")
        self.root.geometry("650x520")
        self.dark_mode = False
        self.light_theme = {
            "bg": "#f5f5f5",
            "fg": "#000000",
            "card": "#ffffff",
        }
        self.dark_theme = {
            "bg": "#1e293b",
            "fg": "#ffffff",
            "card": "#334155",
        }
        self.theme = self.light_theme
        self.root.configure(bg=self.theme["bg"])
        header = tk.Frame(root, bg=self.theme["bg"])
        header.pack(fill="x", pady=8)
        self.title_label = tk.Label(
            header,
            text="📝 Text Analyzer",
            font=("Arial", 16, "bold"),
            bg=self.theme["bg"],
            fg=self.theme["fg"]
        )
        self.title_label.pack(side="left", padx=15)
        self.theme_btn = tk.Button(
            header,
            text="🌙 Dark Mode",
            command=self.toggle_theme
        )
        self.theme_btn.pack(side="right", padx=15)
        self.text_area = tk.Text(
            root,
            height=10,
            font=("Arial", 12),
            bg=self.theme["card"],
            fg=self.theme["fg"],
            wrap="word"
        )
        self.text_area.pack(padx=15, pady=10, fill="both")
        btn_frame = tk.Frame(root, bg=self.theme["bg"])
        btn_frame.pack(pady=5)
        tk.Button(
            btn_frame,
            text="Analyze Text",
            width=15,
            command=self.analyze
        ).pack(side="left", padx=5)
        tk.Button(
            btn_frame,
            text="Export to TXT",
            width=15,
            command=self.export
        ).pack(side="left", padx=5)
        self.result_label = tk.Label(
            root,
            text="",
            justify="left",
            font=("Arial", 11),
            bg=self.theme["bg"],
            fg=self.theme["fg"]
        )
        self.result_label.pack(padx=15, pady=10, anchor="w")
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.theme = self.dark_theme if self.dark_mode else self.light_theme
        self.root.configure(bg=self.theme["bg"])
        self.title_label.configure(bg=self.theme["bg"], fg=self.theme["fg"])
        self.result_label.configure(bg=self.theme["bg"], fg=self.theme["fg"])
        self.text_area.configure(bg=self.theme["card"], fg=self.theme["fg"])
        self.theme_btn.configure(
            text="☀ Light Mode" if self.dark_mode else "🌙 Dark Mode"
        )
    def analyze(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text.")
            return
        self.word_count, self.avg_len, self.top_words = analyze_text(text)
        result = (
            f"Word Count: {self.word_count}\n"
            f"Average Sentence Length: {self.avg_len}\n\n"
            "Top 5 Words:\n"
        )
        for word, count in self.top_words:
            result += f"• {word}: {count}\n"
        self.result_label.config(text=result)
    def export(self):
        if not self.result_label.cget("text"):
            messagebox.showerror("Error", "Analyze text first.")
            return
        file_path = filedialog.asksaveasfilename(
            initialfile="txtextract.txt",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.result_label.cget("text"))

            messagebox.showinfo("Success", "File exported successfully.")
if __name__ == "__main__":
    root = tk.Tk()
    TextAnalyzerApp(root)
    root.mainloop()

import os
from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import ttk

class TxtScannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TXT File Scanner")
        self.geometry("700x500")

        self.order_var = tk.StringVar(value="ascending")

        order_frame = ttk.Frame(self)
        order_frame.pack(pady=10)
        ttk.Radiobutton(order_frame, text="Ascending", variable=self.order_var,
                        value="ascending").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(order_frame, text="Descending", variable=self.order_var,
                        value="descending").pack(side=tk.LEFT, padx=5)

        self.scan_button = ttk.Button(self, text="Scan", command=self.scan)
        self.scan_button.pack(pady=5)

        self.listbox = tk.Listbox(self, width=100)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def scan(self):
        self.listbox.delete(0, tk.END)
        home = Path.home()
        search_dirs = [home / "Documents", home / "Desktop", home / "Downloads"]
        results = []
        for directory in search_dirs:
            if directory.exists():
                for root, _, files in os.walk(directory):
                    for name in files:
                        if name.lower().endswith('.txt'):
                            path = Path(root) / name
                            try:
                                mtime = path.stat().st_mtime
                            except OSError:
                                continue
                            results.append((mtime, str(path)))
        reverse = self.order_var.get() == "descending"
        results.sort(key=lambda x: x[0], reverse=reverse)
        for mtime, path in results:
            dt = datetime.fromtimestamp(mtime)
            self.listbox.insert(tk.END, f"{dt:%Y-%m-%d %H:%M:%S} - {path}")

def main():
    app = TxtScannerApp()
    app.mainloop()

if __name__ == "__main__":
    main()

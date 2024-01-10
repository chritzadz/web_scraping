import tkinter as tk
import threading
import os, sys

from request_data_scraping import launchBrowserWOS

def resource_path(relative_path):
     try:
          base_path = sys._MEIPASS
     except Exception:
          base_path = os.path.join(base_path, relative_path)

class WebScrapingApp:
     def __init__(self, root):
          self.root = root
          self.root.title("Web Scraping")

          self.width = 400
          self.height = 300
          self.root.geometry(f"{self.width}x{self.height}")

          self.input_label = tk.Label(self.root, text="Web Scraping")
          self.input_label.pack()

          self.search_label = tk.Label(self.root, text="Search query")
          self.search_label.pack()

          self.input_entry = tk.Entry(self.root, width=50)
          self.input_entry.pack()

          self.save_button = tk.Button(self.root, text="Run", command=self.run_scraping)
          self.save_button.pack()

          self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_scraping)
          self.stop_button.pack()

     def run_scraping(self):
          search_query = self.input_entry.get()
          scraping_thread = threading.Thread(target=self.launch_scraping, args=(search_query,))
          scraping_thread.start()

     def launch_scraping(self, search_query):
          launchBrowserWOS(search_query)

     def stop_scraping(self):
          pass

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScrapingApp(root)
    root.mainloop()

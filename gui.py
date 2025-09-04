# gui.py
import tkinter as tk
from tkinter import ttk
from recommender import recommend_path
from utils import open_url

def run_app():
    def show_recommendations():
        goal = career_choice.get()
        steps = recommend_path(goal)

        result_box.config(state=tk.NORMAL)
        result_box.delete("1.0", tk.END)

        if not steps:
            result_box.insert(tk.END, "❌ Goal not found. Please select a valid goal.\n")
            result_box.config(state=tk.DISABLED)
            return

        for title, link in steps:
            start = result_box.index(tk.INSERT)
            result_box.insert(tk.END, f"{title}: {link}\n\n")
            end = result_box.index(tk.INSERT)
            result_box.tag_add(link, start, end)
            result_box.tag_config(link, foreground="blue", underline=True)
            result_box.tag_bind(link, "<Button-1>", lambda e, url=link: open_url(e, url))

        result_box.config(state=tk.DISABLED)

    # GUI Setup
    window = tk.Tk()
    window.title("Career Path Recommender")
    window.geometry("800x550")

    tk.Label(window, text="🎯 Select Your Career Goal:", font=("Arial", 14)).pack(pady=10)

    career_options = ["Data Science", "Web Development", "Java Developer", "Cybersecurity", "SSC CGL", "Banking"]

    career_choice = ttk.Combobox(window, values=career_options, font=("Arial", 12), state="readonly")
    career_choice.pack(pady=5)

    result_box = tk.Text(window, height=20, width=90, font=("Arial", 10), wrap=tk.WORD)
    result_box.pack(pady=10)
    result_box.config(state=tk.DISABLED)

    tk.Button(window, text="Show Learning Path", command=show_recommendations,
              font=("Arial", 12), bg="lightgreen").pack(pady=5)

    window.mainloop()

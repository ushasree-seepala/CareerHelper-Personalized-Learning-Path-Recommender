import tkinter as tk
from tkinter import ttk
import webbrowser


# Function to return recommended links
def recommend_path(goal):
    goal = goal.lower()
    if goal == "data science":
        return [("📺 Python Full Course (2025)",
                 "https://www.youtube.com/watch?v=K5KVEU3aaeQ"),
                ("📺 NumPy & Pandas Tutorial",
                 "https://www.youtube.com/watch?v=FniLzpaSFGk"),
                ("📺 Data Analysis Project Demo",
                 "https://www.youtube.com/watch?v=r67SfaiYaDI"),
                ("📝 Practice",
                 "https://www.kaggle.com/learn/intro-to-machine-learning")]
    elif goal == "web development":
        return [("📺 HTML & CSS Crash Course",
                 "https://www.youtube.com/watch?v=UB1O30fR-EE"),
                ("📺 Flask Web App Tutorial",
                 "https://www.youtube.com/watch?v=Z1RJmh_OqeA"),
                ("📺 Deploy Flask App",
                 "https://www.youtube.com/watch?v=BegXzZQ03D0"),
                ("📝 Practice", "https://www.frontendmentor.io/")]
    elif goal == "java developer":
        return [
            ("📺 Java Full Course",
             "https://www.youtube.com/watch?v=zBaFu3XEeTk"),
            ("📺 Core Java & OOP",
             "https://www.youtube.com/watch?v=ntLJmHOJ0ME"),
            ("📺 Spring Boot Guide",
             "https://www.youtube.com/watch?v=35EQXmHKZYs"),
            ("📝 Practice",
             "https://www.hackerrank.com/domains/tutorials/10-days-of-java")
        ]
    elif goal == "cybersecurity":
        return [("📺 Intro to Cybersecurity",
                 "https://www.youtube.com/watch?v=inWWhr5tnEA"),
                ("📺 Ethical Hacking Course",
                 "https://www.youtube.com/watch?v=3Kq1MIfTWCE"),
                ("📺 Network Security Basics",
                 "https://www.youtube.com/watch?v=YqUcT-BFUM0"),
                ("📝 Practice", "https://www.tryhackme.com/")]
    elif goal == "ssc cgl":
        return [
            ("📺 SSC CGL Maths (Akshay Sir)",
             "https://www.youtube.com/watch?v=sBOA3DjqslY"),
            ("📺 SSC CGL Number System",
             "https://www.youtube.com/watch?v=Rw_22AhxumM"),
            ("📺 SSC Maths Revision",
             "https://www.youtube.com/watch?v=_Z7NbJ1rtrI"),
            ("📝 Practice",
             "https://ssc.digialm.com/EForms/configuredHtml/2207/76167/login.html"
             )
        ]
    elif goal == "banking":
        return [("📺 Bank Exam Quant Basics",
                 "https://www.youtube.com/watch?v=nobGZzdkQNs"),
                ("📺 Banking Quant Tricks",
                 "https://www.youtube.com/watch?v=epDDJEhlVik"),
                ("📺 Bank Strategy 2025",
                 "https://www.youtube.com/watch?v=DzaSWaiz5ic"),
                ("📝 Practice", "https://www.practiceMock.com/")]
    else:
        return []


# Function to open URL
def open_url(event, url):
    webbrowser.open_new(url)


# Function to display results
def show_recommendations():
    goal = career_choice.get()
    steps = recommend_path(goal)

    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)

    if not steps:
        result_box.insert(tk.END,
                          "❌ Goal not found. Please select a valid goal.\n")
        result_box.config(state=tk.DISABLED)
        return

    for title, link in steps:
        start = result_box.index(tk.INSERT)
        result_box.insert(tk.END, f"{title}: {link}\n\n")
        end = result_box.index(tk.INSERT)
        result_box.tag_add(link, start, end)
        result_box.tag_config(link, foreground="blue", underline=True)
        result_box.tag_bind(link,
                            "<Button-1>",
                            lambda e, url=link: open_url(e, url))

    result_box.config(state=tk.DISABLED)


# GUI Setup
window = tk.Tk()
window.title("Career Path Recommender")
window.geometry("800x550")

tk.Label(window, text="🎯 Select Your Career Goal:",
         font=("Arial", 14)).pack(pady=10)

career_options = [
    "Data Science", "Web Development", "Java Developer", "Cybersecurity",
    "SSC CGL", "Banking"
]

career_choice = ttk.Combobox(window,
                             values=career_options,
                             font=("Arial", 12),
                             state="readonly")
career_choice.pack(pady=5)

result_box = tk.Text(window,
                     height=20,
                     width=90,
                     font=("Arial", 10),
                     wrap=tk.WORD)
result_box.pack(pady=10)
result_box.config(state=tk.DISABLED)

tk.Button(window,
          text="Show Learning Path",
          command=show_recommendations,
          font=("Arial", 12),
          bg="lightgreen").pack(pady=5)

window.mainloop()

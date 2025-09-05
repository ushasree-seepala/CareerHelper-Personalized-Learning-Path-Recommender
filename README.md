CareerHelper – Personalized Learning Path Recommender 🎯
A Python-based career guidance tool that recommends personalized learning paths for various IT and government job roles.
It provides YouTube tutorial links and official practice question resources, helping students and job seekers prepare effectively.

🚀 Features
- Career Role Selection – Choose from multiple IT and government job options.
- Personalized Learning Paths – Get structured step-by-step learning guidance.
- Free Resources – Includes YouTube tutorials and official practice sites.
- Beginner Friendly – Simple GUI (Tkinter desktop interface).

🖥️ Tech Stack
- Programming Language: Python 
- GUI Framework: Tkinter
- Widget Styling: ttk (Themed Tkinter Widgets)
- Web Integration: webbrowser module (to open links in default browser)
- Data Handling: Hardcoded role-based learning paths in Python lists/tuples
- Version Control: Git & GitHub

📂 Project Structure
CareerHelper-Personalized-Learning-Path-Recommender/
│── main.py              # Entry point (run this file, from main1.py)
│── backup/
│    └── main_old.py     # Old version of main.py kept as backup
│── src/
│    ├── gui.py          # GUI setup and event handling
│    ├── recommender.py  # Role-based recommendations
│    └── utils.py        # Helper functions (e.g., open_url)
│── README.md            # Documentation
│── .replit              # (Optional) Replit run configuration
│── .gitignore           # Git ignore rules
│── pyproject.toml       # (Optional) Dependency file
│── uv.lock              # (Optional) Dependency lock file

🛠 How to Run
Clone the repository:

git clone https://github.com/ushasree-seepala/CareerHelper-Personalized-Learning-Path-Recommender.git
cd CareerHelper-Personalized-Learning-Path-Recommender

Run the program:

python main.py

A Tkinter window will open where you can select your career path and view recommended resources.

👩‍💻 Author
Usha Sree Seepala

- LinkedIn: Usha Sree Seepala
- GitHub: ushasree-seepala

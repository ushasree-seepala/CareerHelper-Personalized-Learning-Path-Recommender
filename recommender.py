# recommender.py

def recommend_path(goal):
    goal = goal.lower()
    if goal == "data science":
        return [("📺 Python Full Course (2025)", "https://www.youtube.com/watch?v=K5KVEU3aaeQ"),
                ("📺 NumPy & Pandas Tutorial", "https://www.youtube.com/watch?v=FniLzpaSFGk"),
                ("📺 Data Analysis Project Demo", "https://www.youtube.com/watch?v=r67SfaiYaDI"),
                ("📝 Practice", "https://www.kaggle.com/learn/intro-to-machine-learning")]
    elif goal == "web development":
        return [("📺 HTML & CSS Crash Course", "https://www.youtube.com/watch?v=UB1O30fR-EE"),
                ("📺 Flask Web App Tutorial", "https://www.youtube.com/watch?v=Z1RJmh_OqeA"),
                ("📺 Deploy Flask App", "https://www.youtube.com/watch?v=BegXzZQ03D0"),
                ("📝 Practice", "https://www.frontendmentor.io/")]
    elif goal == "java developer":
        return [("📺 Java Full Course", "https://www.youtube.com/watch?v=zBaFu3XEeTk"),
                ("📺 Core Java & OOP", "https://www.youtube.com/watch?v=ntLJmHOJ0ME"),
                ("📺 Spring Boot Guide", "https://www.youtube.com/watch?v=35EQXmHKZYs"),
                ("📝 Practice", "https://www.hackerrank.com/domains/tutorials/10-days-of-java")]
    elif goal == "cybersecurity":
        return [("📺 Intro to Cybersecurity", "https://www.youtube.com/watch?v=inWWhr5tnEA"),
                ("📺 Ethical Hacking Course", "https://www.youtube.com/watch?v=3Kq1MIfTWCE"),
                ("📺 Network Security Basics", "https://www.youtube.com/watch?v=YqUcT-BFUM0"),
                ("📝 Practice", "https://www.tryhackme.com/")]
    elif goal == "ssc cgl":
        return [("📺 SSC CGL Maths (Akshay Sir)", "https://www.youtube.com/watch?v=sBOA3DjqslY"),
                ("📺 SSC CGL Number System", "https://www.youtube.com/watch?v=Rw_22AhxumM"),
                ("📺 SSC Maths Revision", "https://www.youtube.com/watch?v=_Z7NbJ1rtrI"),
                ("📝 Practice", "https://ssc.digialm.com/EForms/configuredHtml/2207/76167/login.html")]
    elif goal == "banking":
        return [("📺 Bank Exam Quant Basics", "https://www.youtube.com/watch?v=nobGZzdkQNs"),
                ("📺 Banking Quant Tricks", "https://www.youtube.com/watch?v=epDDJEhlVik"),
                ("📺 Bank Strategy 2025", "https://www.youtube.com/watch?v=DzaSWaiz5ic"),
                ("📝 Practice", "https://www.practiceMock.com/")]
    else:
        return []

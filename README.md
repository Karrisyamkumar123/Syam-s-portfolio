# 🌐 Syam's Portfolio Website

A personal portfolio website built with **Flask**, **HTML/CSS**, and **Bootstrap**. Features include:
- Snowflake animation
- Responsive layout with carousel
- Contact form
- Resume download
- Sections for education, skills, and contact info

---

## 🚀 Features

- ✅ Flask backend with GET & POST request handling
- 🎨 Bootstrap 5 for responsive UI
- ❄️ Animated snowflake effect using pure CSS and JavaScript
- 📤 Contact form (data prints to terminal)
- 📄 Resume download link

---

## 📁 Project Structure
/SyamPortfolio/
│
├── static/
│ ├── images/
│ │ └── ksk_logo.png
│ │ └── face_pic.jpg
│ └── files/
│ └── syam_cv.pdf
│
├── templates/
│ └── index.html
│
├── app.py
└── README.md


---

## 🛠️ How to Run the Project

### 📌 Prerequisites

- Python 3.x
- Flask installed

### ✅ Setup Instructions

1. **Clone the repository** (or download the files):

   ```bash
   git clone <your_repo_link>
   cd SyamPortfolio

Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Flask:
pip install flask

Run the app:
python app.py

Visit in your browser:
http://127.0.0.1:5000/

Contact Form Behavior
When you fill out the contact form and click "Send", it prints the submitted data in the terminal running Flask:

Message received:
Name: John Doe
Subject: Internship
Email: john@example.com
Message: I am interested in your profile.

Resume Download
The "Download CV" button allows users to download your CV (syam_cv.pdf) placed in static/files/.





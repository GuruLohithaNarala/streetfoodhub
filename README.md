
🍜 Street Food Supply Web App
A Flask-powered platform that connects street food vendors with raw material suppliers. Built as part of the Tutedude’s Web Development Hackathon 1.0 – Solving for Street Food.



💡 Features
👤 User Registration/Login for vendors and suppliers

🗺️ Google Maps Integration to locate vendors

💬 Message Board & Chat between users

📦 Order Notifications for suppliers

📝 Testimonials from happy users

🧾 Vendor and Supplier Dashboards

🛠️ Tech Stack
Frontend: HTML5, CSS3, Jinja2 (Flask templates)

Backend: Python, Flask

Database: SQLite

Hosting: Render

Version Control: Git + GitHub

🗂️ Project Structure

/street-food-supply-app/
│
├── app.py                 # Main Flask app
├── render.yaml            # Render deployment config
├── requirements.txt       # Python dependencies
├── users.db               # SQLite DB (dev mode only)
│
├── /templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── chat.html
│   ├── supplier_dashboard.html
│   └── vendor_dashboard.html
│
└── /static/
    └── style.css
🧪 Running Locally
Clone the repository:


git clone https://github.com/YourUsername/street-food-supply-app.git
cd street-food-supply-app
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py


🧑‍💻 Authors

Narala Guru Lohitha


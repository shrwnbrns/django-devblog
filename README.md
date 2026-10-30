# 🚀 DevBlog Platform

A full-stack community blog application built with **Django (MTV Architecture)** and styled with **Bootstrap 5**. This project serves as a robust foundation for learning production-grade backend development, database management, and user authentication workflows.

---

## 🛠️ Tech Stack
* **Backend:** Python, Django (MTV - Model, Template, View)
* **Frontend:** HTML5, Bootstrap 5 (CDN)
* **Database:** SQLite (Development)
* **Authentication:** Django Built-in Auth System (`UserCreationForm`, `AuthenticationForm`)

---

## ✨ Features
* **User Authentication:** Secure sign-up, login, logout, and session management.
* **Frontend Post Creation:** Authenticated users can publish posts directly via a clean UI form.
* **Dynamic Feed:** Displays all published posts sorted by recency with author details and timestamps.
* **Responsive Design:** Built with Bootstrap 5 cards, containers, and a dark navigation bar.

---

## ⚙️ Getting Started & Installation

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/django-devblog.git](https://github.com/YOUR_USERNAME/django-devblog.git)
cd django-devblog


2. Create and Activate a Virtual Environment
python -m venv venv
# On Windows:
source venv/Scripts/activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install django

4. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser(Optional for Admin access)
python manage.py createsuperuser

6. Run the Development Server
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/



===============================================================

📌 Roadmap / Upcoming Features
- [ ] Post Detail Pages (/post/<int:pk>/)

- [ ] Comment Section (One-to-Many Model Relationships)

- [ ] Author Post Management (Edit/Delete permissions)
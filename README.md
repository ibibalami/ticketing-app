# 🎟️ Ticketing App

The **Ticketing App** is a **Django-based web application** designed to **streamline ticket management** within an organization. It enables efficient tracking, handling, and resolution of tickets, ensuring smooth workflow and communication.

---

## ✨ Features

✔️ **User-Friendly Interface** 🎨 – Clean and intuitive UI for seamless navigation.

✔️ **Ticket Creation** 📝 – Easily create new tickets using a simple form.

✔️ **Ticket Management** 🔧 – Admins can view, filter, and manage ticket lifecycles.

✔️ **Real-Time Notifications** 🔔 – Stay updated with new ticket alerts.

✔️ **Email Notifications** 📧 – Automatic email updates for ticket status changes.

✔️ **Responsive Design** 📱 – Works smoothly across various devices.

✔️ **Ticket Printing** 🖨️ – Tickets can be printed for offline reference.

✔️ **Status Tracking** ✅ – Each ticket shows whether it is treated, pending, or resolved.


---

## 🛠️ Technologies Used

- **🐍 Django** – A high-level Python framework for web development.
- **🗄️ SQLite** – Lightweight database for development and testing.
- **🎨 HTML/CSS** – Provides structure and styling for the frontend.
- **🖥️ JavaScript/jQuery** – Enhances frontend interactivity.
- **📱 Bootstrap** – Ensures a mobile-friendly design.
- **📨 SMTP** – Sends email notifications.
- **🔗 Git & GitHub** – Version control and repository management.

---
## 📂 File Structure

```db.sqlite3
manage.py
ticketing_project/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
tickets/
    __init__.py
    admin.py
    apps.py
    forms.py
    migrations/
        __init__.py
        0001_initial.py
        0002_ticket_status.py
        0003_alter_ticket_status_notification.py
    models.py
    static/
        tickets/
    templates/
        tickets/
            base.html
            home.html
            notification_center.html
            temp.html
            ticket_form.html
            ticket_list.html
            ticket_success.html
    tests.py
    utils.py
    views.py
workers.json
```
---

## 🚀 How to Run

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/ticketing-app.git
   cd ticketing-app
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
4. **Run the server**
   ```sh
   python manage.py runserver
   ```
5. **Access the app** in your browser at `http://127.0.0.1:8000/`.
---

## 📌 Internal Use Only

🚨 **This repository is private and intended for work-related purposes only.** Do not share, clone, or distribute the code externally.

---

## 📜 License

This project is for internal use only and is not licensed for public distribution.

---

🔐 **Access Restricted: Authorized Users Only**


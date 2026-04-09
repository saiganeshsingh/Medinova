# Medinova - Healthcare Management System 🏥

Medinova is a robust, full-stack hospital management web application designed to bridge the gap between healthcare providers and patients. Built using the **Django** framework, it provides a seamless experience for booking appointments, exploring medical services, and finding specialist doctors.

## ✨ Key Features

- **📅 Online Appointment Booking**: Patients can schedule appointments by selecting departments, doctors, dates, and times. Data is securely stored in the database.
- **👨‍⚕️ Doctor Directory**: Comprehensive listings of medical professionals with their specializations, descriptions, and social profiles.
- **🔍 Advanced Search**: Find doctors and services filtered by departments or specific keywords.
- **📩 Contact & Support**: Integrated contact system for patient inquiries and feedback.
- **📰 Medical Blog**: A dedicated section for health-related news, tips, and hospital updates.
- **📱 Fully Responsive**: Optimized for all devices—desktops, tablets, and smartphones.
- **🛡️ Admin Dashboard**: Secure management of appointments, contact messages, and doctor profiles.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS), Bootstrap
- **Database**: SQLite3 (Development) / PostgreSQL (Optional for Production)
- **Styling**: Medinova Premium Template (HTML Codex)

## 🚀 Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/saiganeshsingh/Medinova.git
cd Medinova
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows
\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```

Now, open your browser and visit `http://127.0.0.1:8000/`.

## 📸 Screenshots
*(Tip: Add your project screenshots in an `img/` folder and link them here)*

| Home Page | Appointment Form |
|---|---|
| ![Home](https://via.placeholder.com/400x200?text=Home+Page) | ![Appointment](https://via.placeholder.com/400x200?text=Appointment+Form) |

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is based on the **MEDINOVA** template by [HTML Codex](https://htmlcodex.com). Please refer to their license for template usage policies.

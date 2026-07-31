# 📧 Email Automation System

A web-based Email Automation System built with Django that enables users to import recipient data, create reusable email templates, send personalized bulk emails, schedule email campaigns, and monitor delivery through a dashboard.

---

## 📌 Project Overview

The Email Automation System simplifies bulk email communication by automating recipient management, template creation, email delivery, scheduling, and tracking.

The system supports importing recipient data from CSV and Excel files, dynamically maps different column names, sends personalized emails using placeholders, schedules campaigns for future delivery, and provides a dashboard to monitor email activity.

---

## ✨ Features

### 📥 Recipient Management
- Import recipients from CSV files
- Import recipients from Excel files
- Dynamic column mapping
- Email validation
- Duplicate prevention
- View all recipients
- Delete recipients

---

### 📝 Email Template Management
- Create templates
- Edit templates
- Delete templates
- Preview templates

---

### 📨 Email Campaign
- Personalized bulk email sending
- Gmail SMTP integration
- Placeholder replacement
- Send to all imported recipients

---

### ⏰ Campaign Scheduling
- Schedule campaigns
- Automatic email delivery using APScheduler
- Campaign status tracking

---

### 📊 Dashboard
- Total Recipients
- Total Templates
- Scheduled Campaigns
- Successfully Sent Emails
- Failed Emails
- Recent Email Logs

---

### 📋 Email Logs
- Delivery status
- Recipient email
- Template used
- Timestamp
- Error message (if any)

---

## 🏗️ Project Architecture

```
Email Automation System

│
├── Dashboard
│
├── Data Engine
│      ├── CSV Import
│      ├── Excel Import
│      ├── Column Mapper
│      └── Recipient Management
│
├── Mailer
│      ├── Template Engine
│      ├── SMTP Service
│      ├── Placeholder Engine
│      └── Campaign Service
│
└── Automation
       ├── APScheduler
       └── Scheduled Campaigns
```

---

## 🛠️ Technology Stack

|    Category    |  Technology   |
|----------------|---------------|
|     Backend    |   Django 6    |
|    Language    |  Python 3.13  |
|    Database    |    SQLite     |
|  Email Service |   Gmail SMTP  |
|    Scheduler   |  APScheduler  |
| Data Processing|     Pandas    |
|  Excel Support |    OpenPyXL   |
|    Frontend    |    HTML,CSS   |
| Version Control| Git & GitHub  |

---

## 📂 Project Structure

```
apps/
│
├── automation/
├── dashboard/
├── data_engine/
└── mailer/

config/
manage.py
requirements.txt
README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Nithiyasree19/email-automation-system.git

cd email-automation-system
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
EMAIL_USE_TLS=True
```

---

### Apply Migrations

```bash
python manage.py migrate
```

---

### Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

## 🚀 Usage

1. Import recipients from CSV or Excel.
2. Create an email template.
3. Preview the template.
4. Send emails immediately or schedule them.
5. Monitor campaign status from the dashboard.
6. View email logs.

---

## 📸 Screenshots

Add screenshots here after capturing them.

- Dashboard
- Recipient Import
- Recipient List
- Template List
- Template Preview
- Send Email
- Scheduled Campaign
- Email Logs

---

## 📈 Future Enhancements

- User authentication
- Multiple SMTP providers
- Email attachments
- Rich text editor
- Campaign analytics
- Retry failed emails
- REST API support
- Docker deployment

---

## 👨‍💻 Team

- Project Lead  - Nithiyasree M (System Architect & Email Engine Developer)
- Team Member 2 - Harini (Data Engineer)
- Team Member 3 - Nithyasri D (Automation Engineer)
- Team Member 4 - Asma Fathima (Dashboard & QA Engineer)

---


This project was developed for academic purposes.
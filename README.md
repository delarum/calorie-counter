# CalTrack — Daily Calorie Counter

A clean, responsive calorie tracking web app built with Django and Tailwind CSS. Track your daily food intake, monitor your calorie goal, and reset your log at any time.

## Features

- **Add food items** with name and calorie count
- **View your daily log** with a running total
- **Remove individual items** from the log
- **Progress bar** showing calories vs. your 2,000 kcal daily goal
- **Reset the day** with a single click
- Fully responsive — works on mobile and desktop

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.x, Django 3.x |
| Database | PostgreSQL |
| Frontend | HTML5, Tailwind CSS (CDN) |
| Deployment | Render |
| Static files | WhiteNoise |

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/calorie-tracker.git
cd calorie-tracker
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://USER:PASSWORD@localhost/calorie_tracker
ALLOWED_HOSTS=localhost 127.0.0.1
```

### 5. Create the PostgreSQL database

```bash
createdb calorie_tracker
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. (Optional) Create a superuser for the admin panel

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## Deployment to Render

### Automatic (Blueprint)

1. Fork this repository to your GitHub account.
2. Go to [render.com](https://render.com) and click **New → Blueprint**.
3. Connect your GitHub repo — Render will read `render.yaml` and create the web service + PostgreSQL database automatically.
4. Set the `SECRET_KEY` environment variable if not auto-generated.
5. Deploy — Render runs migrations and `collectstatic` automatically.

### Manual

1. Create a **PostgreSQL** database on Render. Copy the *Internal Database URL*.
2. Create a **Web Service** with:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command:** `gunicorn myproject.wsgi:application`
3. Add environment variables:
   - `SECRET_KEY` — a long random string
   - `DEBUG` — `False`
   - `DATABASE_URL` — the Internal Database URL from step 1
   - `ALLOWED_HOSTS` — `.onrender.com`

### Live URL

> 🔗 **https://calorie-counter-0edr.onrender.com** 

---

## Project Structure

```
calorie-tracker/
├── myproject/           # Django project config
│   ├── settings.py      # Settings with env variable support
│   ├── urls.py          # Root URL routing
│   └── wsgi.py
├── myapp/               # calorie_tracker application
│   ├── models.py        # DailyLog + FoodItem models
│   ├── views.py         # index, delete, reset views
│   ├── forms.py         # FoodItemForm with validation
│   ├── urls.py          # App URL patterns
│   ├── admin.py         # Admin registrations
│   └── templates/
│       └── myapp/
│           ├── base.html    # Base template with nav & toasts
│           └── index.html   # Main tracker page
├── requirements.txt
├── render.yaml          # Render deployment blueprint
├── manage.py
└── .env
```

---

## Security Notes

- `SECRET_KEY` is loaded from environment variables — never hard-coded
- `DEBUG=False` in production
- CSRF protection enabled on all POST forms
- `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`, and HSTS enabled in production
- `.env` is gitignored — secrets never committed

---

## License

MIT


## known bugs
None
 ## Support nad Contact information
 **email:** delarum7@gmail.com
 **Phone number:** 0792651083
# DoClinic

Django project for a medical clinic website with:
- Appointment booking + admin management
- Case studies editable in admin (with image upload)
- Specialists editable in admin
- Clinic address + Google Maps embed editable in admin
- SMS logging with a development console backend

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py load_initial_data
python manage.py runserver
```

Open:
- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Admin access

The admin panel is only available when the Django backend is running (local dev or a deployed server like Render).

Create an admin user:

```bash
python manage.py createsuperuser
```

Then log in at:
- `http://127.0.0.1:8000/admin/`

## Demo data

This repo ships demo content as fixtures (not a database file). Load it with:

```bash
python manage.py load_initial_data
```

## Environment

Create a `.env` file (or set env vars) based on `.env.example`.

Required for production:
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS=your-domain.com`

## Notes

Local database (`db.sqlite3`) and uploads (`media/`) are intentionally not committed to Git.

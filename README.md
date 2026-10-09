# Vehicle Maintenance Log API

A Python Flask API for recording vehicle maintenance services. It uses SQLAlchemy for storage, bcrypt for authentication support, and Flask-JWT-Extended to protect maintenance log operations.

## Features

- Authentication routes under `/auth`.
- Create, list, update, and delete maintenance records.
- Records are associated with the authenticated user.
- File logging to `logs/app.log`.

## Run locally

Requires Python 3 and pip. From the repository root:

```sh
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

The development server normally runs at `http://127.0.0.1:5000`. Tables are created when the app starts.

## Configuration

`config.py` reads `DATABASE_URI`, `SECRET_KEY`, and `JWT_SECRET_KEY` from the process environment. The database defaults to SQLite at `sqlite:///autocare.db`. Set your own local secret values before using authentication. `app.py` does not explicitly load a `.env` file; export the variables in your shell if overriding the defaults.

## Maintenance endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| POST | `/logs/` | Create a maintenance record |
| GET | `/logs/` | List the current user's records |
| PUT | `/logs/<log_id>` | Update an owned record |
| DELETE | `/logs/<log_id>` | Delete an owned record |

Protected requests require `Authorization: Bearer <access_token>`. Record fields include `service_type` and `description`. See `controllers/auth_controller.py` for the registration/login request format.

## Structure

- `app.py`: application startup, extensions, and blueprints.
- `config.py`: environment and database configuration.
- `controllers/`: authentication and maintenance routes.
- `models/`: database models.
- `services/`: authentication helpers.
- `requirements.txt`: dependencies.

This is a learning project. The startup command enables Flask debug mode for local development.

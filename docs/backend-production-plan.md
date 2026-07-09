# BhramGuard Backend Production Plan

## Direction

BhramGuard backend will be developed as a production FastAPI service backed by PostgreSQL hosted on Neon.

The backend should own:

- user registration and authentication
- protected phishing/social-engineering scans
- scan history
- feedback for model improvement
- risk-engine integration
- stable API contracts for the dashboard and browser extension

## Stack

- Python
- FastAPI
- PostgreSQL on Neon
- SQLAlchemy ORM
- Alembic migrations
- Pydantic settings and schemas
- JWT authentication
- bcrypt password hashing
- pytest for backend tests

## Important Migration Rule

Migration files will be created manually by the project owner.

The codebase may include SQLAlchemy models, metadata, and Alembic-ready structure, but Codex should not auto-generate migration revisions unless explicitly asked.

## Target Directory Layout

```text
backend/
  app/
    main.py
    core/
      config.py
      security.py
      logging.py
    db/
      base.py
      session.py
    models/
      user.py
      scan.py
      feedback.py
    schemas/
      auth.py
      user.py
      scan.py
      feedback.py
    api/
      v1/
        deps.py
        routes/
          auth.py
          scan.py
          history.py
          feedback.py
    services/
      auth_service.py
      scan_service.py
      history_service.py
      feedback_service.py
    risk_engine/
      predict.py
      risk_score.py
      features/
    public/
      index.html
      styles.css
      script.js
```

## Database

Production database: Neon PostgreSQL.

Required environment variables:

```text
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST/DB?sslmode=require
JWT_SECRET_KEY=replace-with-strong-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
ENVIRONMENT=development
```

## Tables

### users

Stores account identity and authentication data.

- id
- email
- hashed_password
- is_active
- created_at
- updated_at

### scans

Stores each authenticated scan and the model output.

- id
- user_id
- input_text
- input_url
- input_web
- risk_score
- risk_level
- model_results
- created_at

### feedback

Stores user correction/feedback on scan results.

- id
- scan_id
- user_id
- feedback_type
- note
- created_at

## API Plan

### Auth

```text
POST /api/v1/auth/register
POST /api/v1/auth/login
GET  /api/v1/auth/me
```

### Scan

```text
POST /api/v1/scan
```

This endpoint should eventually require JWT auth, run the risk engine, save scan history, and return the scan result.

### History

```text
GET    /api/v1/scans
GET    /api/v1/scans/{scan_id}
DELETE /api/v1/scans/{scan_id}
```

### Feedback

```text
POST /api/v1/scans/{scan_id}/feedback
GET  /api/v1/feedback
```

## Build Order

1. Core config and settings.
2. Neon/PostgreSQL database session.
3. SQLAlchemy table models.
4. Pydantic schemas.
5. Auth service and routes.
6. Protected scan route and scan persistence.
7. Scan history routes.
8. Feedback routes.
9. Public tester UI updates for auth and history.
10. Tests.

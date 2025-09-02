# Deployment Options

## Docker

1. Build image:
   ```bash
   docker build -t flashcard-app .
   ```
2. Run container:
   ```bash
   docker run -p 5000:5000 --env DATABASE_URL="mysql+mysqlconnector://user:password@host/dbname" flashcard-app
   ```

## Heroku

1. Add `Procfile`:
   ```
   web: flask run --host=0.0.0.0
   ```
2. Set buildpack to Python.
3. Add MySQL add-on (ClearDB or JawsDB).
4. Set `DATABASE_URL` in Heroku config.

## Other Cloud Platforms

- **Fly.io:** Use Dockerfile and `flyctl` for deployment.
- **Azure App Service:** Use Python runtime, set env vars, and configure MySQL.
- **Vercel/Netlify:** For frontend only, deploy static files.

## Production Notes

- Set `HUGGINGFACE_API_KEY` in environment.
- Use proper DB credentials.
- Consider HTTPS and security best practices.
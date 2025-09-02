# Web App Project

This project is a simple web application with the following structure:

- **backend/**: Python Flask API server.
- **frontend/**: Static files for the frontend (HTML, CSS, JS).
- **db/**: SQL scripts for MySQL database setup.

## Tech Stack

- **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
- **Frontend:** HTML5, CSS3, JavaScript (vanilla)
- **Database:** MySQL

---

## Setup Instructions

### 1. MySQL Database

1. Install MySQL server if not already installed.
2. Create the database and table:
    ```bash
    cd db
    mysql -u <your_mysql_user> -p < setup.sql
    ```
3. (Optional) Insert sample data:
    ```bash
    cd ../backend
    python sample_data.py
    ```
4. Update the backend configuration if needed (in `app.py` or via `DATABASE_URL` environment variable):
    ```
    mysql+mysqlconnector://<user>:<password>@localhost/webapp_db
    ```

---

### 2. Hugging Face API Key (Optional, for advanced question generation)

- Register at [Hugging Face](https://huggingface.co/) and create an API token:  
  https://huggingface.co/settings/tokens

- Set the API key in your environment:
    ```bash
    export HUGGINGFACE_API_KEY=your_token_here
    ```

- The backend will use this key when generating flashcards with the Hugging Face API.

---

### 3. Backend (Flask API)

1. Install Python dependencies:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```
2. Start Flask API:
    ```bash
    python app.py
    ```
    By default, runs at `http://localhost:5000`.

---

### 4. Frontend

1. Open `frontend/index.html` in your browser.
2. Enter your study notes, generate flashcards, save, and retrieve as needed.

**Note:** For full API access, ensure the backend server is running and accessible from your browser.

---

## Screenshots & Demo

### Main UI

![Screenshot: Main Flashcard Generator UI](screenshots/flashcard_ui.png)

### Flashcard Flip Animation

![Demo GIF: Flip Animation](screenshots/flashcard_flip.gif)

> Place your images or GIFs in the `/screenshots` folder.  
> Example tools for creating GIFs: [ScreenToGif](https://www.screentogif.com/) or [LiceCap](https://www.cockos.com/licecap/).

---

## Troubleshooting

- **CORS Issues:** You may need to enable CORS in Flask for local development.
- **Database Connection Errors:** Verify MySQL is running and credentials are correct.
- **API Key Errors:** If using Hugging Face, ensure the API key is set.

---

## Deployment

See [`DEPLOYMENT.md`](DEPLOYMENT.md) for Docker, Heroku, and other deployment options.

---

Feel free to extend this project!
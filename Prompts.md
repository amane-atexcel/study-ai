Hackathon prompts for Github Copilot



I want to work in vibe coding for the following project: "1. "AI Study Buddy" - Flashcard GeneratorTech Stack:Fronted: HTML5(cards) + CSS(animation) + JS(flip cards)Backend:Python (Flask) + MySQL (store flashcards)AI: **Hugging Face Question-Answering API How it works: 1. User pastes study notes (HTML textarea -> python) 2. Python sends text to Hugging Face: *"Generate 5 quiz questions"* 3. JS creates interactive flashcards (save to MySQL for reuse) " Give me step by step prompts to use copilot from coding to implementation of web app



After giving the above prompt to copilot it gave me 8 steps prompt to build backend, database, and frontend. Below are the step by step prompt for Copilot.

## Step 1: Project Setup

Create a new web app project with the following structure:

- `/backend` for the Flask Python API
- `/frontend` for the HTML, CSS, and JS files
- `/db` for scripts to set up a MySQL database

Add a README.md at the root to describe the project and tech stack.

Step 2: Initialize Backend (Flask + MySQL)
------------------------------------------

Inside `/backend`, scaffold a Flask app with endpoints for:

- `/generate_flashcards` (POST): accepts study notes and returns generated questions
- `/save_flashcards` (POST): saves flashcards to MySQL
- `/get_flashcards` (GET): retrieves saved flashcards for a user/session

Include SQLAlchemy or mysql-connector for MySQL integration.
Step 3: Integrate Hugging Face API
----------------------------------

In the Flask backend, add a function to call Hugging Face’s Question-Answering API.

- It should take a block of study notes and return 5 quiz questions.
- Use the requests library to call Hugging Face’s API.
- Document the API key usage and error handling.
  
  

Step 4: Set Up MySQL DB
-----------------------

Write a MySQL schema for a `flashcards` table with columns:

- id (PK)
- question
- answer
- created_at
- user_id/session_id

Add DB setup scripts in `/db`.
Step 5: Build Frontend - HTML, CSS, JS
--------------------------------------

In `/frontend`, create:

- An index.html page with:
  
  - A textarea for user notes
  - A "Generate Flashcards" button
  - A container for flashcards

- Style flashcards with CSS for animation (flip effect).

- JS to:
  
  - Send notes to backend via fetch/AJAX
  - Render flashcards with flip animations
  - Save/retrieve flashcards from backend
    
    

Step 6: Connecting Frontend & Backend
-------------------------------------

Write JavaScript code to:

- POST notes to `/generate_flashcards` and render returned flashcards
- POST flashcards to `/save_flashcards`
- GET flashcards from `/get_flashcards` on page load

### Copilot said: Absolutely! Here’s a step-by-step guide to using

Absolutely! Here’s a step-by-step guide to using GitHub Copilot (and Copilot Chat) for developing your “AI Study Buddy” flashcard generator web app, from coding to implementation. This guide assumes you’re working in VS Code or GitHub Codespaces, but you can adapt it for other environments.

* * *

Step 1: Project Setup
---------------------

**Prompt for Copilot:**

Code
    Create a new web app project with the following structure:
    - `/backend` for the Flask Python API
    - `/frontend` for the HTML, CSS, and JS files
    - `/db` for scripts to set up a MySQL database
    Add a README.md at the root to describe the project and tech stack.

* * *

Step 2: Initialize Backend (Flask + MySQL)
------------------------------------------

**Prompt for Copilot:**

Code
    Inside `/backend`, scaffold a Flask app with endpoints for:
    - `/generate_flashcards` (POST): accepts study notes and returns generated questions
    - `/save_flashcards` (POST): saves flashcards to MySQL
    - `/get_flashcards` (GET): retrieves saved flashcards for a user/session
    Include SQLAlchemy or mysql-connector for MySQL integration.

* * *

Step 3: Integrate Hugging Face API
----------------------------------

**Prompt for Copilot:**

Code
    In the Flask backend, add a function to call Hugging Face’s Question-Answering API.
    - It should take a block of study notes and return 5 quiz questions.
    - Use the requests library to call Hugging Face’s API.
    - Document the API key usage and error handling.

* * *

Step 4: Set Up MySQL DB
-----------------------

**Prompt for Copilot:**

Code
    Write a MySQL schema for a `flashcards` table with columns:
    - id (PK)
    - question
    - answer
    - created_at
    - user_id/session_id
    Add DB setup scripts in `/db`.

* * *

Step 5: Build Frontend - HTML, CSS, JS
--------------------------------------

**Prompt for Copilot:**

Code
    In `/frontend`, create:
    - An index.html page with:
      - A textarea for user notes
      - A "Generate Flashcards" button
      - A container for flashcards
    - Style flashcards with CSS for animation (flip effect).

    - JS to:
      - Send notes to backend via fetch/AJAX
      - Render flashcards with flip animations
      - Save/retrieve flashcards from backend

* * *

Step 6: Connecting Frontend & Backend
-------------------------------------

**Prompt for Copilot:**

Code
    Write JavaScript code to:
    - POST notes to `/generate_flashcards` and render returned flashcards
    - POST flashcards to `/save_flashcards`
    - GET flashcards from `/get_flashcards` on page load

* * *

Step 7: Testing & Deployment
----------------------------

Add sample data and unit tests for the Flask backend (pytest).
Add browser-based tests or usage instructions for frontend.
Suggest deployment options (Dockerfile, Heroku, etc.).



Step 8: Documentation
---------------------

Update README.md with setup steps:

- How to start backend and frontend
- How to configure Hugging Face API key
- How to set up MySQL

Include screenshots or demo GIFs.

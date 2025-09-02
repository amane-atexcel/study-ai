# Database Setup

This folder contains scripts for setting up the MySQL database for the web app.

## Files

- `schema.sql`: Defines the schema for the `flashcards` table and creates the database.
- `setup.sql`: Helper script to source the schema in MySQL.

## Setup Instructions

1. Ensure MySQL server is running.
2. Run the setup script from the `/db` directory:
   ```bash
   mysql -u <your_mysql_user> -p < setup.sql
   ```
   This will create the database (`webapp_db`) and the `flashcards` table.

## Table: flashcards

| Column       | Type         | Description                        |
| ------------ | ------------ | ---------------------------------- |
| id           | INT, PK      | Flashcard ID (primary key)         |
| question     | TEXT         | Flashcard question                 |
| answer       | TEXT         | Flashcard answer                   |
| created_at   | DATETIME     | Timestamp when created             |
| user_id      | VARCHAR(64)  | Associated user ID (nullable)      |
| session_id   | VARCHAR(64)  | Associated session ID (nullable)   |
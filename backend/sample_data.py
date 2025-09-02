# Script to insert sample flashcards for testing
from app import db, Flashcard

def insert_sample_flashcards():
    samples = [
        Flashcard(user_id="demo-user", question="What is the capital of France?", answer="Paris"),
        Flashcard(user_id="demo-user", question="What is 2+2?", answer="4"),
        Flashcard(user_id="demo-user", question="Who wrote Hamlet?", answer="William Shakespeare"),
        Flashcard(user_id="demo-user", question="What is the boiling point of water?", answer="100°C"),
        Flashcard(user_id="demo-user", question="What is the chemical symbol for gold?", answer="Au"),
    ]
    db.session.bulk_save_objects(samples)
    db.session.commit()
    print("Inserted sample flashcards.")

if __name__ == "__main__":
    insert_sample_flashcards()
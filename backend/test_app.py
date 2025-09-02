import pytest
from app import app, db, Flashcard

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Add sample flashcard
            f = Flashcard(user_id="test-user", question="Test Q?", answer="Test A")
            db.session.add(f)
            db.session.commit()
        yield client

def test_generate_flashcards(client):
    resp = client.post("/generate_flashcards", json={"notes": "Fact 1\nFact 2"})
    assert resp.status_code == 200
    j = resp.get_json()
    assert "flashcards" in j
    assert len(j["flashcards"]) == 2

def test_save_flashcards(client):
    flashcards = [{"question": "Q1", "answer": "A1"}, {"question": "Q2", "answer": "A2"}]
    resp = client.post("/save_flashcards", json={"user_id": "test-user", "flashcards": flashcards})
    assert resp.status_code == 201
    j = resp.get_json()
    assert j["message"] == "Flashcards saved successfully"

def test_get_flashcards(client):
    resp = client.get("/get_flashcards?user_id=test-user")
    assert resp.status_code == 200
    j = resp.get_json()
    assert "flashcards" in j
    assert any(fc["question"] == "Test Q?" for fc in j["flashcards"])
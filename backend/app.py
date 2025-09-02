from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import requests
import os

app = Flask(__name__)

# Configure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'mysql+mysqlconnector://user:password@localhost/webapp_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Flashcard model
class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "question": self.question,
            "answer": self.answer,
            "created_at": self.created_at.isoformat()
        }

# --------------------------
# Hugging Face QA Integration
# --------------------------
def generate_flashcards_via_huggingface(study_notes, num_questions=5):
    """
    Calls Hugging Face's Question-Answering API to generate quiz questions from study notes.
    
    Requires the environment variable HUGGINGFACE_API_KEY to be set.

    Args:
        study_notes (str): The block of study notes.
        num_questions (int): Number of quiz questions to generate (default 5).

    Returns:
        list: List of dicts [{question: ..., answer: ...}, ...]
    """
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        raise EnvironmentError("HUGGINGFACE_API_KEY environment variable not set.")

    # Example uses Hugging Face's Inference API for text2text-generation.
    endpoint = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "inputs": study_notes,
        "parameters": {"num_return_sequences": num_questions}
    }
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        out = response.json()
        # The output format may vary by model. This example assumes each result is in 'generated_text'.
        questions = []
        for item in out:
            q_text = item.get('generated_text', '').strip()
            if q_text:
                questions.append({"question": q_text, "answer": ""})  # Answer empty unless model provides it
        return questions[:num_questions]
    except requests.exceptions.RequestException as e:
        # Log and raise error
        print(f"Hugging Face API error: {e}")
        raise RuntimeError("Failed to generate questions using Hugging Face API.")

@app.route("/generate_flashcards", methods=["POST"])
def generate_flashcards():
    data = request.json
    study_notes = data.get("notes", "")
    method = data.get("method", "local")  # "local" or "huggingface"
    if not study_notes.strip():
        return jsonify({"error": "No study notes provided."}), 400

    # Choose generation method
    if method == "huggingface":
        try:
            questions = generate_flashcards_via_huggingface(study_notes, num_questions=5)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        # Placeholder: Simple local Q/A generation from notes
        questions = [
            {
                "question": f"What is a key point from: {note[:40]}?",
                "answer": note
            }
            for note in study_notes.split("\n") if note.strip()
        ][:5]

    return jsonify({"flashcards": questions})

@app.route("/save_flashcards", methods=["POST"])
def save_flashcards():
    data = request.json
    user_id = data.get("user_id")
    flashcards = data.get("flashcards", [])
    if not user_id or not flashcards:
        return jsonify({"error": "Missing user_id or flashcards"}), 400

    for fc in flashcards:
        question = fc.get("question")
        answer = fc.get("answer")
        if question and answer:
            card = Flashcard(user_id=user_id, question=question, answer=answer)
            db.session.add(card)
    db.session.commit()
    return jsonify({"message": "Flashcards saved successfully"}), 201

@app.route("/get_flashcards", methods=["GET"])
def get_flashcards():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    cards = Flashcard.query.filter_by(user_id=user_id).order_by(Flashcard.created_at.desc()).all()
    return jsonify({
        "flashcards": [card.to_dict() for card in cards]
    })

if __name__ == "__main__":
    app.run(debug=True)
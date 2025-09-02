const API_BASE = "http://localhost:5000";
const userId = "demo-user"; // Replace with a real user/session management if needed

const notesTextarea = document.getElementById('notes');
const generateBtn = document.getElementById('generate-btn');
const saveBtn = document.getElementById('save-btn');
const flashcardsContainer = document.getElementById('flashcards-container');

let currentFlashcards = [];

/**
 * Render flashcards with flip animation.
 * @param {Array} flashcards - Array of {question, answer}
 */
function renderFlashcards(flashcards) {
    flashcardsContainer.innerHTML = "";
    flashcards.forEach(card => {
        const cardEl = document.createElement('div');
        cardEl.className = 'flashcard';
        cardEl.innerHTML = `
            <div class="flashcard-inner">
                <div class="flashcard-front">${card.question || "No question"}</div>
                <div class="flashcard-back">${card.answer || "No answer yet"}</div>
            </div>
        `;
        cardEl.addEventListener('click', () => {
            cardEl.classList.toggle('flipped');
        });
        flashcardsContainer.appendChild(cardEl);
    });
}

/**
 * POST notes to backend and render returned flashcards.
 */
generateBtn.onclick = async function() {
    const notes = notesTextarea.value.trim();
    if (!notes) {
        alert("Please enter your study notes.");
        return;
    }
    generateBtn.disabled = true;
    generateBtn.textContent = "Generating...";
    try {
        const resp = await fetch(`${API_BASE}/generate_flashcards`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ notes })
        });
        const data = await resp.json();
        if (data.flashcards) {
            currentFlashcards = data.flashcards;
            renderFlashcards(currentFlashcards);
        } else {
            alert(data.error || "No flashcards generated.");
        }
    } catch (err) {
        alert("Error generating flashcards.");
        console.error(err);
    }
    generateBtn.disabled = false;
    generateBtn.textContent = "Generate Flashcards";
};

/**
 * POST flashcards to backend for saving.
 */
saveBtn.onclick = async function() {
    if (!currentFlashcards.length) {
        alert("No flashcards to save.");
        return;
    }
    saveBtn.disabled = true;
    saveBtn.textContent = "Saving...";
    try {
        const resp = await fetch(`${API_BASE}/save_flashcards`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: userId, flashcards: currentFlashcards })
        });
        const data = await resp.json();
        if (resp.ok) {
            alert("Flashcards saved!");
        } else {
            alert(data.error || "Failed to save flashcards.");
        }
    } catch (err) {
        alert("Error saving flashcards.");
        console.error(err);
    }
    saveBtn.disabled = false;
    saveBtn.textContent = "Save Flashcards";
};

/**
 * GET flashcards from backend on page load.
 */
async function loadFlashcards() {
    try {
        const resp = await fetch(`${API_BASE}/get_flashcards?user_id=${encodeURIComponent(userId)}`);
        const data = await resp.json();
        if (data.flashcards) {
            currentFlashcards = data.flashcards;
            renderFlashcards(currentFlashcards);
        }
    } catch (err) {
        console.error("Error loading flashcards:", err);
    }
}

window.addEventListener("DOMContentLoaded", loadFlashcards);
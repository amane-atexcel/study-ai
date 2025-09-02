# Frontend Usage & Testing

## Manual Browser Usage

1. Start the backend Flask API (`python app.py`).
2. Open `index.html` in your browser.
3. Paste notes, click "Generate Flashcards" to create cards.
4. Click "Save Flashcards" to store them.
5. "Retrieve My Flashcards" loads your saved cards.

## Browser-based Testing

You can simulate usage by:
- Entering dummy notes and verifying generated cards appear.
- Flipping cards by clicking to see answers.
- Save and retrieve actions should persist flashcards (if backend DB is running).

### Automated Browser Testing

For automated browser tests, consider [Cypress](https://www.cypress.io/) or [Selenium](https://www.selenium.dev/).
Example Cypress test:

```javascript
describe('Flashcard Generator', () => {
  it('generates and flips flashcards', () => {
    cy.visit('frontend/index.html')
    cy.get('#notes').type('Fact 1\nFact 2')
    cy.get('#generate-btn').click()
    cy.get('.flashcard').should('have.length', 2)
    cy.get('.flashcard').first().click().should('have.class', 'flipped')
  })
})
```

## Troubleshooting

- If flashcards do not appear, check backend connectivity and browser console for errors.
# Hugging Face Question Generation Integration

The backend uses Hugging Face's Inference API to generate quiz questions from study notes.

## API Key

- You must set the environment variable `HUGGINGFACE_API_KEY` with your Hugging Face token.
- Get an API key from [Hugging Face Settings](https://huggingface.co/settings/tokens).

Example for Linux/macOS:
```bash
export HUGGINGFACE_API_KEY=youwill_get_startwit_hf
```

## Error Handling

- If the API key is missing or invalid, the backend will respond with an error.
- Network or API errors are caught and logged; the API will return a 500 status with an error message.

## Usage

Send a POST to `/generate_flashcards` with:
```json
{
  "notes": "Your study notes...",
  "method": "huggingface"
}
```
The backend will return 5 generated quiz questions.

---
For local/offline generation, omit `"method"` or set `"method": "local"`.
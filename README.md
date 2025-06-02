# Mac Calculator Backend

A FastAPI-based backend service for the Mac-style Calculator application, powered by Google's Gemini AI for mathematical expression recognition.

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
```

3. Start the server:
```bash
uvicorn main:app --reload
```

## Project Structure

```
calc-be/
├── apps/
│   └── calculator/
│       ├── route.py    # Calculator API endpoints
│       └── utils.py    # Utility functions
├── constants.py        # Global constants
├── main.py            # FastAPI application setup
├── requirements.txt    # Python dependencies
└── schema.py          # Pydantic models
```

## API Endpoints

### POST /calculate
Processes mathematical expressions from drawn images.

Request body:
```json
{
  "image_data": "base64_encoded_image"
}
```

Response:
```json
{
  "result": "calculation_result",
  "expression": "detected_expression"
}
```

## Dependencies

- FastAPI - Web framework
- uvicorn - ASGI server
- google-generativeai - Google's Gemini AI SDK
- python-dotenv - Environment variable management
- Pillow - Image processing

## Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Document functions and endpoints

### Best Practices
- Implement proper error handling
- Use async/await for I/O operations
- Keep the codebase modular
- Write clear documentation

## Error Handling

The API implements proper error handling for:
- Invalid image data
- AI service errors
- Mathematical expression parsing errors

## Configuration

Configuration is managed through environment variables and the `constants.py` file.

### Environment Variables
- `GEMINI_API_KEY` - Google Gemini API key

### Constants
- `SERVER_URL` - Server URL
- `PORT` - Server port
- `ENV` - Environment (development/production)

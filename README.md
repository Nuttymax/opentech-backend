# OpenTech AI Solutions - Backend API

FastAPI backend for OpenTech AI Solutions chatbot services.

## Deployment on Railway

This backend is deployed on Railway and connects to the B12 website.

### Environment Variables Required:
- `OPENAI_API_KEY`: Your OpenAI API key
- `PORT`: 8000 (Railway sets this automatically)

## Endpoints

- `GET /`: API status check
- `GET /health`: Health check endpoint
- `POST /chat`: Chatbot conversation endpoint

## Local Development

```bash
pip install -r requirements.txt
python main.py

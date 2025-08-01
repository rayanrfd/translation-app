# Translate App

A FastAPI-based web application for translating English text to Darija (Moroccan Arabic) using fine-tuned machine learning models.

## 🌟 Features

- **English to Darija Translation**: Powered by a fine-tuned Marian model
- **Web Interface**: Clean, responsive HTML/CSS/JavaScript frontend
- **JSON API**: FastAPI backend with automatic API documentation
- **Real-time Translation**: Instant translation results
- **Modern Architecture**: Built with FastAPI, Pydantic, and Transformers

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rayanrfd/translation-app
   cd gg-translate
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   uv run uvicorn app.main:app --reload
   ```

4. **Open your browser**
   Navigate to `http://localhost:8000` to access the web interface.

## 📖 Usage

### Web Interface

1. Open the application in your browser
2. Enter English text in the text area
3. Click "Translate" to get the Darija translation
4. View the result below the form

### API Usage

The application provides a RESTful API for programmatic access:

#### Translate Text

**Endpoint:** `POST /translate/`

**Request Body:**
```json
{
  "text": "Hello, how are you?"
}
```

**Response:**
```json
{
  "text": "ahlo, achno kif?"
}
```

**Example with curl:**
```bash
curl -X POST "http://localhost:8000/translate/" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, how are you?"}'
```

## 🏗️ Project Structure

```
gg-translate/
├── app/
│   ├── ai/
│   │   └── translate.py          # Translation model loading
│   ├── model/
│   │   └── translation.py        # Pydantic models
│   ├── routes/
│   │   └── translate.py          # API routes
│   ├── config.py                 # Configuration
│   ├── main.py                   # FastAPI application
│   └── router.py                 # Router configuration
├── static/
│   ├── script.js                 # Frontend JavaScript
│   └── styles.css                # Frontend styles
├── templates/
│   └── index.html                # Web interface template
├── pyproject.toml                # Project dependencies
├── uv.lock                       # Lock file
└── README.md                     # This file
```

## 🔧 Configuration

The application uses the following configuration:

- **Translation Model**: `rayanrfd/marian-finetuned-english-darija`
- **Framework**: FastAPI with Uvicorn server
- **Frontend**: HTML/CSS/JavaScript with Jinja2 templates

## 🛠️ Development

### Running in Development Mode

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### API Documentation

When running the application, you can access:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

### Dependencies

Key dependencies include:
- `fastapi`: Web framework
- `pydantic`: Data validation
- `transformers`: Hugging Face transformers library
- `sentencepiece`: Text tokenization
- `uvicorn`: ASGI server
- `python-dotenv`: Environment variable management

## 🐳 Docker

A Dockerfile is included for containerized deployment:

```bash
docker build -t gg-translate .
docker run -p 8000:8000 gg-translate
```

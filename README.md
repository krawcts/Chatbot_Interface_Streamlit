# Chatbot Interface with Streamlit

This is an interface project for an AI agent using Streamlit.

## Usage

### Recommended: Using Docker

The recommended way to run this application is using Docker:

```bash
# Build the Docker image
docker build -t chatbot-interface .

# Run the container
docker run -p 8501:8501 chatbot-interface
```

Then access the application at http://localhost:8501 in your browser.

### Docker Implementation Details

The Docker setup:
- Uses Python 3.11 slim image
- Runs the application on port 8501
- Uses a non-root user for security
- Requires a `requirements.txt` file (to be created)

## Alternative: Local Installation with Poetry

If you prefer a local installation, this project uses Poetry for dependency management:

1. Install dependencies:

```bash
poetry install
```

2. Run the Streamlit application:

```bash
poetry run streamlit run app/streamlit_app.py
```

Note: The Docker setup is the recommended and most reliable way to run this application.

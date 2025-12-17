# Website Snarky Summarizer

A Python project that scrapes website content and generates snarky, humorous summaries using an LLM (via Ollama).

## Features

- **Web Scraping**: Extracts and cleans website content using BeautifulSoup
- **AI Summarization**: Uses Ollama/Llama 3.2 model to generate snarky summaries
- **Content Cleaning**: Removes unnecessary elements like scripts, styles, images, and inputs
- **Configurable**: Easy to modify system prompts for different summarization styles

## Requirements

- Python 3.8+
- Ollama running locally (http://localhost:11434)
- Dependencies listed in `pyproject.toml`

## Installation

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd test
```

2. **Install dependencies using uv**:
```bash
uv sync
```

Or with pip:
```bash
pip install -r requirements.txt
```

3. **Ensure Ollama is running**:
```bash
ollama serve
ollama pull llama3.2
```

## Usage

Run the Jupyter notebook:
```bash
jupyter notebook test1.ipynb
```

Or use the module directly:
```python
from scrapper import get_page_content
from notebook import call_model

url = "https://example.com"
content = get_page_content(url)
system_prompt = "You are a snarky assistant..."
call_model(system_prompt, content)
```

## Project Structure

```
.
├── scrapper.py          # Web scraping functionality
├── test1.ipynb          # Main notebook with examples
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Locked dependencies
├── .python-version      # Python version specification
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Dependencies

- `beautifulsoup4` - HTML parsing and content extraction
- `requests` - HTTP requests for fetching web pages
- `openai` - Ollama API client (uses OpenAI-compatible interface)

## Configuration

The LLM model and parameters can be configured in `call_model()` function:
- `MODEL`: Currently set to 'llama3.2'
- `base_url`: Ollama server URL (default: http://localhost:11434/v1)
- System and user prompts can be customized for different styles

## Notes

- Website content is limited to 2000 characters
- The scraper removes navigation elements (scripts, styles, images)
- Requires Ollama running locally for LLM functionality

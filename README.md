# Chatbot - LangGraph Conversational Agent

A simple conversational agent built with LangGraph and LangChain, powered by Anthropic's Claude model.

## Description

This project implements a basic chatbot using LangGraph's state management and graph-based conversation flow. The agent maintains conversation history and responds to user messages using Claude 3.5 Sonnet.

## Prerequisites

- Python 3.11 or higher
- Anthropic API key

## Setup Instructions

### 1. Create Virtual Environment

#### For macOS/Linux:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

#### For Windows:
```cmd
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Command Prompt)
.venv\Scripts\activate

# OR for PowerShell
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
# Install the package and all dependencies
pip install -e .

# Or install from requirements.txt if available
pip install -r requirements.txt

# Note: You may also need to install python-dotenv if not included
pip install python-dotenv
```

### 3. Environment Configuration

Create a `.env` file in the project root directory and add your API keys:

```env
# Required: Anthropic API Key for Claude access
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional: LangSmith API Key for tracing and debugging
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=your_project_name
```

### 4. Get Your API Keys

#### Anthropic API Key (Required):
1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add it to your `.env` file

#### LangSmith API Key (Optional - for debugging):
1. Go to [LangSmith](https://smith.langchain.com/)
2. Sign up or log in
3. Generate an API key
4. Add it to your `.env` file

## Running the Application

### Using LangGraph CLI (Development):
```bash
# Start the development server
langgraph dev
```

### Using Python directly:
```bash
# Run the graph script
python les-01/graph.py
```

## Project Structure

```
.
├── README.md
├── setup.py
├── requirements.txt
├── langgraph.json
├── .env                 # Your environment variables (create this)
├── .venv/              # Virtual environment (created by you)
└── les-01/
    └── graph.py        # Main chatbot implementation
```

## Dependencies

The main dependencies include:
- `langgraph` - State graph framework
- `langchain` - LLM framework
- `langchain-anthropic` - Anthropic integration
- `langgraph-cli` - Development tools
- `python-dotenv` - Environment variable management

See `setup.py` for the complete list of dependencies.

## Troubleshooting

### Common Issues:

1. **"langgraph command not found"**: Make sure you've activated your virtual environment and installed the dependencies.

2. **API Key Errors**: Ensure your `.env` file is in the project root and contains the correct `ANTHROPIC_API_KEY`.

3. **Import Errors**: Make sure all dependencies are installed by running `pip install -e .`.

### Deactivating Virtual Environment

When you're done working:
```bash
deactivate
```

## License

This project is for educational purposes.

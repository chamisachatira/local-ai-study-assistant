\# Local AI Study Assistant 🎓🤖



An intelligent, privacy-focused Retrieval-Augmented Generation (RAG) study assistant built with Python, Flask, and Ollama (`llama3.2`). This project includes a universal RESTful API with CORS support, allowing seamless integration into external websites (PHP, HTML, JS) and mobile applications.



\---



\## ✨ Features

\- \*\*Local RAG Pipeline\*\*: Queries custom documents and study materials locally using Ollama.

\- \*\*Universal JSON API\*\*: Exposes `/api/chat` and `/api/health` endpoints for external integration.

\- \*\*CORS Enabled\*\*: Built-in cross-origin support for web frontends.

\- \*\*One-Click Startup\*\*: Automated Windows setup and launch script (`run.bat`).



\---



\## 🚀 Quick Start (For Local Use)



\### Prerequisites

\- Python 3.10+ installed

\- \[Ollama](https://ollama.com/) installed and running locally with the `llama3.2` model (`ollama pull llama3.2`)



\### Launching the Assistant

Simply double-click \*\*`run.bat`\*\* in the root directory. 

The script will automatically:

1\. Create a virtual environment (`venv`).

2\. Install all required dependencies from `requirements.txt`.

3\. Launch the Flask server at `http://127.0.0.1:5000`.



\---



\## 🔌 API \& External App Integration



To connect this assistant to an external website (such as a PHP college portal) or mobile application, refer to the detailed guide in \[INTEGRATION\_GUIDE.md](./INTEGRATION\_GUIDE.md).



\### API Endpoints

\- \*\*GET `/api/health`\*\*: Health check to verify server status.

\- \*\*POST `/api/chat`\*\*: Accepts JSON payloads `{"message": "Your query"}` and returns the AI's response.



\---



\## 🛠️ Built With

\- \*\*Backend\*\*: Python, Flask, Flask-CORS

\- \*\*AI Model\*\*: Ollama (`llama3.2`)

\- \*\*Version Control\*\*: Git \& GitHub


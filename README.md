# Deva AI Personal Assistant 🧠🎤

**Voice-controlled desktop AI assistant** with hotword detection, system automation, facial recognition, and conversational AI.

[![GitHub Repo stars](https://img.shields.io/github/stars/sharad5506/Deva?style=social)](https://github.com/sharad5506/Deva)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/sharad5506/Deva)](LICENSE)

## 🚀 Features

- **Hotword Detection** - "Hey Deva" wake word (Picovoice Porcupine)
- **Voice Commands** - Speech-to-text with real-time processing
- **System Automation** - Open apps, control Notepad, Win+Y shortcuts
- **Conversational AI** - OpenAI GPT / Google Gemini integration
- **Facial Recognition** - Face authentication system
- **Web Dashboard** - Modern HTML/CSS/JS interface via Eel
- **Local Database** - SQLite for contacts & custom commands
- **Text-to-Speech** - Voice responses

## 🎯 Demo

User: "Hey Deva, open Notepad"
Deva: [Win+R → notepad → Enter]
Deva: "Notepad opened successfully!"


## 🛠️ Tech Stack

Backend: Python 3.8+ | Eel | pvporcupine | SpeechRecognition | pyttsx3
Frontend: HTML5 | CSS3 | JavaScript | Responsive Web UI
AI: OpenAI GPT | Google Gemini
Database: SQLite3
Automation: PyAutoGUI | Pyperclip
Auth: OpenCV Facial Recognition


## 📦 Quick Start

1. **Clone & Install**
```bash
git clone https://github.com/sharad5506/Deva.git
cd Deva
pip install -r requirements.txt

2. **Api**
ASSISTANT_NAME = "Hey Deva"
OPENAI_API_KEY=your_new_openai_key_here
add the engine/config.py
# Add your API keys to .env

3. **Run command**
```bash
python main.py

Say "Hey Deva" to activate!

🔑 Environment Variables
OPENAI_API_KEY=sk-your-key-here
GOOGLE_API_KEY=your-google-key
PICOVOICE_ACCESS_KEY=your-picovoice-key
GOOGLE_CSE_ID=your-cse-id

🎮 Voice Commands
| Command                 | Action             |
| ----------------------- | ------------------ |
| "Hey Deva open Notepad" | Opens Notepad      |
| "Hey Deva play music"   | Opens music player |
| "Hey Deva time"         | Current time       |
| "Hey Deva who are you"  | Assistant info     |

🔧 Development
# Install dev dependencies
pip install -r requirements.txt

# Run in dev mode
python run.py

# Hotword detection only
python engine/hotword.py

🚀 Deployment
# Install dev dependencies
pip install -r requirements.txt

# Run in dev mode
python run.py

# Hotword detection only
python engine/hotword.py

🚀 Deployment
Windows Desktop App:

pip install pyinstaller
pyinstaller --onefile --windowed main.py

⚠️ Security Notes
✅ API keys use .env (gitignored)

✅ Push protection enabled

✅ No secrets in commit history

✅ Local SQLite database

📈 Project Status
| Phase         | Status         | Duration |
| ------------- | -------------- | -------- |
| Requirements  | ✅ Complete     | 7 days   |
| System Design | ✅ Complete     | 5 days   |
| Development   | ✅ Complete     | 20 days  |
| Testing       | 🔄 In Progress | 10 days  |

🙏 Acknowledgments
Picovoice Porcupine - Hotword detection

OpenAI - GPT models

Eel - Python-Web bridge

SpeechRecognition - Voice input


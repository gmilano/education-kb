<div align="center">

```
███████╗████████╗██╗   ██╗██████╗ ██╗   ██╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚██╗ ██╔╝
███████╗   ██║   ██║   ██║██║  ██║ ╚████╔╝ 
╚════██║   ██║   ██║   ██║██║  ██║  ╚██╔╝  
███████║   ██║   ╚██████╔╝██████╔╝   ██║   
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝    ╚═╝   
        A S S I S T A N T   🎓            
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=22D3EE&center=true&vCenter=true&width=700&lines=lines=AI+Developer+Portfolio.;Projects+%7C+Skills+%7C+Contact.;Built+by+Shalini🚀" alt="Typing SVG" />

<br/>

[![Live Demo](https://img.shields.io/badge/🎓_LIVE_DEMO-Try_it_Now_→-22d3ee?style=for-the-badge&labelColor=0a1628)](https://ai-study-assistant-fqe5mljcptjn7uvjzeeuap.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-Powered-F55036?style=for-the-badge)](https://groq.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)

<br/>

> *"What if you had a personal tutor who knew every subject, never got tired, and adapted to how YOU learn?"*
> **Meet your AI Study Assistant.**

</div>

---

## 📖 What Is This?

A **full-stack AI-powered study companion** built for students, self-learners, and curious minds. It doesn't just answer questions — it adapts to your level, summarizes your PDFs, stores your learning history, and exports your notes.

Think ChatGPT — but laser-focused on helping you actually learn and retain knowledge.

---

## ✨ Everything It Can Do

<table>
<tr>
<td width="50%">

**🔐 Authentication System**
Full login & signup with SQLite. Session persistence so you never lose your progress. Optional "Remember Me" support.

</td>
<td width="50%">

**💬 Chat-Based Learning**
Ask anything, get intelligent answers in a clean ChatGPT-style interface. Subject-aware responses that adapt to context.

</td>
</tr>
<tr>
<td width="50%">

**📄 PDF Summarization**
Upload any study material. AI extracts the text, understands it, and gives you a clean, concise summary.

</td>
<td width="50%">

**📥 Download Notes as PDF**
Every AI response can be exported as a formatted PDF — ready to print, share, or revise from.

</td>
</tr>
<tr>
<td width="50%">

**📜 Chat History**
Every question and answer is saved. Review your learning journey, revisit past explanations, or clear and start fresh.

</td>
<td width="50%">

**🌙 Dark Mode**
Toggle between light and dark themes. Study comfortably at 2am without burning your eyes.

</td>
</tr>
</table>

---

## 🧠 3 Study Modes — One Assistant

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   📘  BEGINNER MODE                                             │
│       Simple language · Analogies · Step-by-step breakdown      │
│       "Explain it like I'm hearing this for the first time"     │
│                                                                 │
│   📗  NORMAL MODE                                               │
│       Detailed explanations · Examples · Full context           │
│       "Give me a thorough, complete understanding"              │
│                                                                 │
│   📕  EXAM REVISION MODE                                        │
│       Bullet points · Key facts · Quick recall format           │
│       "I have 2 hours before my exam, let's go"                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🤖 Subject-Aware AI

The assistant doesn't give generic answers — it adapts its *style* to the subject:

| Subject | How It Responds |
|---------|----------------|
| ➕ Math | Step-by-step solving with working shown |
| 💻 Programming | Code examples + line-by-line explanation |
| 🔬 Science | Real-world analogies + visual descriptions |
| 📚 General | Structured explanation with examples |

---

## 🏗️ How It Works

```
  User logs in / signs up
          │
          ▼
  ┌───────────────────┐       ┌─────────────────────┐
  │  Ask a question   │  OR   │   Upload a PDF       │
  └────────┬──────────┘       └──────────┬──────────┘
           │                             │
           ▼                             ▼
  ┌────────────────────────────────────────────────┐
  │               prompts.py                       │
  │  Subject + Mode → Crafted System Prompt        │
  └─────────────────────┬──────────────────────────┘
                        │
                        ▼
  ┌────────────────────────────────────────────────┐
  │            Groq API ⚡ (LLM)                   │
  │         Fast inference, smart output           │
  └─────────────────────┬──────────────────────────┘
                        │
          ┌─────────────┼──────────────┐
          ▼             ▼              ▼
    Chat display   Save to DB    Export as PDF
                  (SQLite)      (ReportLab)
```

---

## 🗄️ Database Schema

```sql
-- Users table
CREATE TABLE users (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    username  TEXT UNIQUE NOT NULL,
    password  TEXT NOT NULL
);

-- Chat history table
CREATE TABLE history (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    username  TEXT,
    question  TEXT,
    answer    TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📂 Project Structure

```
ai-study-assistant/
│
├── 📄 app.py               ← main streamlit app + UI + routing
├── 📄 db.py                ← all SQLite database functions
├── 📄 prompts.py           ← subject + mode based prompt builder
│
├── 📄 study.db             ← SQLite database (auto-created)
├── 📄 notes.pdf            ← latest exported notes
├── 📄 session.txt          ← login session persistence
│
├── 📄 requirements.txt     ← all dependencies
└── 📄 .env                 ← GROQ_API_KEY (never push this!)
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/SHALINISAURAV/ai-study-assistant.git
cd ai-study-assistant

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate       # Mac/Linux
# venv\Scripts\activate        # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
echo "GROQ_API_KEY=your_api_key_here" > .env

# 5. Launch 🚀
streamlit run app.py
```

> 🔑 Get your **free** Groq API key → [console.groq.com](https://console.groq.com)

---

## 🔐 Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here
```

For Streamlit Cloud → **Settings → Secrets** mein add karo.

---

## 📦 Requirements

```
streamlit
groq
python-dotenv
PyPDF2
reportlab
pillow
requests
```

---

## 🗺️ Roadmap

- [x] 🔐 Login & Signup with SQLite
- [x] 💬 Chat-based AI tutor
- [x] 🧠 3 adaptive study modes
- [x] 📄 PDF upload & summarization
- [x] 📥 Download notes as PDF
- [x] 📜 Chat history storage
- [x] 🌙 Dark mode toggle
- [x] ⚡ Groq LLM integration

---

## 👩‍💻 Author

<div align="center">

**Shalini Saurav**

*AI Engineer · Data Scientist · Builder*

Building tools that make learning faster, smarter, and more accessible.

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/YOUR_USERNAME)

</div>

---

<div align="center">

### ⭐ If this made studying easier for you — star it!

[![Try Live Demo](https://img.shields.io/badge/🎓_Live_Demo-ai--study--assistant.streamlit.app-22d3ee?style=for-the-badge)](https://ai-study-assistant-fqe5mljcptjn7uvjzeeuap.streamlit.app)

<br/>

*"The smartest thing you can do is make learning easier for yourself."*

</div>

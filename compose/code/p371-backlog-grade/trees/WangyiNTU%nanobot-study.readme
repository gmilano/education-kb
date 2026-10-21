<div align="center">
  <pre>
                _           _           _ 
 _ __   __ _ _ __   ___ | |__   ___ | |_ 
| '_ \ / _` | '_ \ / _ \| '_ \ / _ \| __|
| | | | (_| | | | | (_) | |_) | (_) | |_ 
|_| |_|\__,_|_| |_|\___/|_.__/ \___/ \__|
  </pre>
  <h1>nanobot: 3-day Study Repository</h1>
  <p>
    <a href="./README_cn.md" style="font-size: 1.2em; border: 2px solid #007bff; border-radius: 5px; padding: 5px 10px; text-decoration: none; color: #007bff;">🇨🇳 中文文档 (Chinese)</a>
  </p>
  <p>
    <a href="https://pypi.org/project/nanobot-ai/"><img src="https://img.shields.io/pypi/v/nanobot-ai" alt="PyPI"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue" alt="Python">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
    <a href="https://discord.gg/MnCvHqpUGB"><img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  </p>
</div>

🐈 **nanobot** is an **ultra-lightweight** personal AI assistant designed to be **learned, dissected, and mastered**.

Unlike bloated frameworks that hide their logic, `nanobot` delivers core agent functionality in just **~3,500 lines of code**. It's the perfect "textbook" implementation of a modern LLM agent.

## 💡 Basic Idea

An **AI Agent** is not just a chatbot. It is a system that can:
1.  **Perceive**: Read files, search the web, see the terminal output.
2.  **Think**: Use an LLM (Large Language Model) to reason about what to do next.
3.  **Act**: Execute tools (Shell, File I/O, API calls) to affect the environment.
4.  **Loop**: Observe the result of its action and decide the next step.

`nanobot` implements this **Perceive-Think-Act-Loop** in its purest form in `agent/loop.py`. By studying this repository, you aren't just learning a tool; you are learning the fundamental anatomy of Agentic AI.

> [!TIP]
> **Using an AI Coding Assistant? (Cursor, Claude Code, GitHub Copilot)**
> 
> You can turn your AI assistant into a **Personal Nanobot Tutor**!
> 1.  Open `AI_COPILOT.md`.
> 2.  Copy its content or ask your AI to "Read AI_COPILOT.md and act as my tutor".
> 3.  The AI will now guide you through the 3-Day Plan using the Socratic method, helping you understand the code instead of just writing it for you.

---

## 📅 3-Day Mastery Plan

Follow this guided path to go from "User" to "AI Engineer" in just one weekend (2-3 hours/day).

### Day 1: The Soul (Architecture)
**Objective**: Understand how an LLM becomes an Agent.
1.  **Read (`30 min`)**:
    -   `agent/loop.py`: This is the heart. Read how `_process_message` handles the `LLM -> Tool -> LLM` cycle.
    -   `config/`: See how we manage prompts and model settings.
2.  **Action (`1 hour`)**:
    -   Run `nanobot onboard` to initialize.
    -   Chat: `nanobot agent -m "Calculate 128 * 455"`.
    -   **Trace**: Open `~/.nanobot/workspace` and find the log file. Follow the execution path you just read in `loop.py`.
3.  **Challenge (`1 hour`)**:
    -   Modify `agent/prompts.py` (or equivalent) to give the bot a "Pirate" personality.
    -   Restart and verify: `nanobot agent -m "Who are you?"`.

### Day 2: The Hands (Skills & Tools)
**Objective**: Teach the AI to interact with the real world.
1.  **Read (`30 min`)**:
    -   `agent/tools/`: Look at `web.py` to see how we define tools.
    -   `skills/`: Understand how to bundle tools into skills.
2.  **Action (`1 hour`)**:
    -   Create a simple python script `my_tool.py` that prints "Hello from tool!".
    -   Register it in the agent configuration.
3.  **Challenge (`1.5 hours`)**:
    -   Build a **"Daily Briefing" Skill**:
        -   Write a tool that fetches top Hacker News headlines (use an API or scraping).
        -   Combine it with the existing `weather` tool.
        -   Ask nanobot: "Give me my daily briefing."

### Day 3: The Body (Deployment & Channels)
**Objective**: Run your agent 24/7.
1.  **Read (`30 min`)**:
    -   `channels/`: How we bridge to Telegram/WhatsApp.
    -   `cron/`: How the agent wakes itself up.
2.  **Action (`1 hour`)**:
    -   Set up a mock Telegram bot (or real one via `@BotFather`).
    -   Configure `cron` to run your "Daily Briefing" skill every morning at 8:00 AM.
3.  **Challenge (`1.5 hours`)**:
    -   **Dockerize**: Build the container using the provided `Dockerfile`.
    -   Run it independently of your terminal.
    -   Chat with it via Telegram while it runs in Docker.

---

## 📦 Setup for Study

This repository contains the **Study Plan** and **Tutor Instructions**. To follow the plan, you need the actual `nanobot` source code.

**1. Clone the Repository (Recursive)**

This command downloads both the study guide AND the `nanobot` source code at once.

```bash
git clone --recursive https://github.com/YOUR_USERNAME/nanobot-study.git
cd nanobot-study
```

**2. Install Dependencies**

```bash
pip install -e nanobot/
```

**3. Start Learning**

Return to this `README` (or `AI_COPILOT.md`) and begin your [3-Day Mastery Plan](#-3-day-mastery-plan) tasks. Note that the source code is now in the `nanobot/` subdirectory.

### 🤖 How to Learn with an AI Tutor

If you are using **Cursor**, **Claude Code**, or **GitHub Copilot**, paste the content of `AI_COPILOT.md` into your chat. The AI will then act as a **Socratic Tutor**.

**Example Interaction:**

> **You**: "How does the agent decide which tool to use?"
>
> **Standard AI**: "It uses the `_process_message` function in `loop.py`. Here is the code..." (Gives you the answer, you learn nothing)
>
> **Nanobot Tutor (Socratic)**: "That's the core of the agent! Open `nanobot/agent/loop.py` and look at the `_process_message` method. Can you spot where we call `self.llm.chat`? What argument are we passing to it that contains the tool definitions?"

**Your Goal**: Don't just copy code. Answer the Tutor's questions to build your mental model of the system.

## 🚀 Quick Start

1.  **Initialize**: `nanobot onboard`
2.  **Configure**: Edit `~/.nanobot/config.json` with your API keys (OpenRouter/OpenAI/Anthropic).
3.  **Chat**: `nanobot agent -m "Hello World"`

## 🏗️ Architecture Reference

<p align="center">
  <img src="nanobot_arch.png" alt="nanobot architecture" width="800">
</p>

*   **bridge/**: Connectivity to external worlds (Telegram, etc).
*   **agent/**: The cognitive core.
*   **memory/**: Long-term storage (your `workspace/`).

## 🔗 Related Projects

*   [**HKUDS/nanobot**](https://github.com/HKUDS/nanobot) - The original lightweight agent framework this study guide is based on.
*   [**OpenClaw**](https://github.com/openclaw/openclaw) - A powerful autonomous agent framework for complex tasks.

## 📚 References

*   [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - Generally considered the seminal paper for modern Agents.
*   [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT) - An early popular implementation of autonomous agents.
*   [LangChain](https://github.com/langchain-ai/langchain) - A framework for developing applications powered by language models.

## 🤝 Contribute

We love PRs! If you finish your "Day 3 Challenge" and make a cool skill, make a PR to add it to the `skills/` directory.

---

<p align="center">
  <sub>Special thanks to the original <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a> repository for the excellent base implementation.</sub><br>
  <sub>nanobot is for educational, research, and technical exchange purposes only</sub>
</p>

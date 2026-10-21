# 🧠 Interleaved Learning MCP Server

A Model Context Protocol (MCP) server implementing cognitive science-backed interleaved learning techniques for optimal knowledge retention.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/sheikhcoders/interleaved-learning-mcp)

## 🚀 Live Server

**MCP Endpoint:** `https://interleaved-learning-mcp.vercel.app/api/mcp`

### LLMs.txt Support

- [`/llms.txt`](https://interleaved-learning-mcp.vercel.app/llms.txt) - Quick reference for LLMs
- [`/llms-full.txt`](https://interleaved-learning-mcp.vercel.app/llms-full.txt) - Complete documentation for LLMs

---

## 📚 Documentation

### What is Interleaved Learning?

Interleaved learning is a cognitive strategy backed by decades of research that involves mixing different topics during study sessions instead of focusing on one topic at a time (blocked practice).

#### Research-Backed Benefits

| Benefit | Improvement |
|---------|-------------|
| Long-term retention | Up to 43% better |
| Concept discrimination | Significantly improved |
| Knowledge transfer | Enhanced application |
| Problem-solving | More flexible approaches |

> "Interleaving is one of the most powerful learning strategies available, yet remains underutilized." — Rohrer & Taylor, 2007

---

## 🛠️ Available Tools

### 1. `create_study_plan`
Generate interleaved study schedules with 5 research-backed patterns.

```json
{
  "subjects": ["Mathematics", "Physics", "Chemistry"],
  "totalMinutes": 90,
  "pattern": "ABCABC"
}
```

**Patterns Available:**
- `ABAB` - Simple alternation (beginner)
- `ABCABC` - Triple rotation (intermediate)
- `ABACBC` - Spaced mixing (intermediate)
- `Random` - Maximum interleaving (advanced)
- `Blocked-to-Interleaved` - Gradual transition (beginner)

### 2. `generate_interleaved_quiz`
Create mixed-topic quizzes that strengthen discrimination learning.

### 3. `create_flashcard_deck`
Build multi-topic flashcard decks for interleaved review.

### 4. `get_shuffled_flashcards`
Retrieve flashcards in shuffled order across topics.

### 5. `log_study_session`
Track study sessions with duration and quiz scores.

### 6. `get_learning_progress`
View statistics and personalized recommendations.

### 7. `get_interleaving_patterns`
Learn about different interleaving strategies and their use cases.

---

## 🔌 Quick Start

### Connect with Cursor

Add to `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "interleaved-learning": {
      "url": "https://interleaved-learning-mcp.vercel.app/api/mcp"
    }
  }
}
```

### Connect with Claude Desktop

Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "interleaved-learning": {
      "transport": {
        "type": "streamable-http",
        "url": "https://interleaved-learning-mcp.vercel.app/api/mcp"
      }
    }
  }
}
```

---

## 🧪 Local Development

```bash
# Clone the repository
git clone https://github.com/sheikhcoders/interleaved-learning-mcp.git
cd interleaved-learning-mcp

# Install dependencies
npm install

# Run development server
npm run dev

# Test with MCP Inspector
npx @modelcontextprotocol/inspector@latest http://localhost:3000 undefined
```

Connect to `http://localhost:3000/api/mcp` using Streamable HTTP transport.

---

## 📦 Tech Stack

- **Framework:** Next.js 15
- **MCP Adapter:** mcp-handler (Vercel)
- **Protocol:** @modelcontextprotocol/sdk
- **Language:** TypeScript
- **Validation:** Zod
- **Deployment:** Vercel

---

## 📖 Learning Resources

- [Interleaving: A Research-Based Strategy](https://www.learningscientists.org/interleaving)
- [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- [Vercel MCP Deployment Guide](https://vercel.com/docs/mcp)
- [llms.txt Standard](https://llmstxt.org/)

---

## 👨‍💻 Author

**Likhon Sheikh**  
[@sheikhcoders](https://github.com/sheikhcoders)

---

## 📄 License

MIT License © 2024 Likhon Sheikh

---

<p align="center">
  <sub>Built with ❤️ for better learning outcomes</sub>
</p>

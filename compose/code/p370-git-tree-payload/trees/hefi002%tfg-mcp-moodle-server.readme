# Moodle MCP Server

A Model Context Protocol (MCP) server that connects AI agents with Moodle's API, enabling intelligent automation and integration with Learning Management Systems.

## Security Notice

This project was developed as a Final Degree Project with a focus on functionality and proof of concept. While fully operational, it has not undergone a comprehensive security audit. For production environments, please consider:

- Implementing proper authentication and authorization mechanisms
- Conducting a security review before deployment
- Following your organization's security policies and best practices
- Using appropriate rate limiting and access controls

Feel free to fork this project and adapt it to your security requirements.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Your Moodle Token](#getting-your-moodle-token)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [How It's Made](#how-its-made)
- [Lessons Learned](#lessons-learned)
- [Contributing](#contributing)
- [License](#license)

## Overview

This MCP server acts as a bridge between AI agents and Moodle, allowing intelligent systems to interact with Moodle's functionality through a standardized protocol. The server implements selected Moodle API endpoints as MCP tools, enabling AI agents to manage courses, users, enrollments, grades, and access course content.

## Features

- Plug-and-play integration with any Moodle instance
- Secure authentication using Moodle tokens
- Comprehensive API coverage for common Moodle operations
- Simple configuration via interactive setup script
- Well-tested with comprehensive test suite
- Detailed documentation and examples

## Prerequisites

- Python 3.11 or higher
- A Moodle instance you can access (version 5.1+ recommended)
- Access to Moodle tokens with appropriate permissions (more on this below)

For development and testing:
- Docker & Docker Compose (recommended for local Moodle instance)

## Installation

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hefi002/tfg-mcp-moodle-server.git
   cd tfg-mcp-moodle-server
   ```

2. **Create a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development dependencies (for testing):**
   ```bash
   pip install -r requirements-dev.txt
   ```

5. **Run the interactive setup:**
   ```bash
   python setup.py
   ```

   The setup script will guide you through configuring your Moodle URL, authentication token, and logging preferences.

6. **Verify the installation:**
   ```bash
   pytest
   ```

   > **Note:** You need to install `requirements-dev.txt` to run pytest (step 4).

### Manual Setup

If you prefer to configure manually:

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your configuration:**
   ```bash
   MOODLE_URL=https://your-moodle-instance.com
   MOODLE_TOKEN=your_authentication_token_here
   LOG_LEVEL=INFO
   DEBUG=false
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development dependencies (for testing):**
   ```bash
   pip install -r requirements-dev.txt
   ```

## Getting Your Moodle Token

### For Administrators: Creating Tokens

1. **Navigate to token management:**
   - Log in to Moodle as administrator
   - Go to: `Site administration` → `Server` → `Web services` → `Manage tokens`

2. **Create a new token:**
   - Select the user for whom you're creating the token
   - Choose the web service (Something like `MCP API service`, ask your Moodle admin in case of doubt)
   - Optionally set expiration date and IP restrictions
   - Click "Save changes"
   - Copy the generated token immediately

3. **Configure permissions:**
   - Tokens inherit permissions from the user's role
   - Default roles include: Administrator, Manager, Teacher, Student, etc.
   - For fine-grained control, create custom roles with specific capabilities

### For Teachers and Students: Obtaining a Token

1. **Check if self-service tokens are enabled:**
   - Log in to your Moodle account
   - Go to: `Preferences` → `Security` → `Security keys`
   - If available, you can generate your own token here
   - If an existing token is shown for this webservice but you don't know it, choose Reset to generate a new one

2. **If self-service is not available:**
   - Contact your Moodle site administrator
   - Request a token with appropriate permissions for your use case
   - The administrator can create the token following the steps above

### Advanced: Custom Roles and Permissions

For organizations requiring specific permission sets, Moodle offers granular permission control at system, category, course, and activity levels. You can create custom roles tailored to your needs:

1. Go to: `Site administration` → `Users` → `Permissions` → `Define roles`
2. Add a new role or duplicate an existing one
3. Configure specific capabilities for the role
4. Ensure the role has `webservice/rest:use` capability for API access

**Additional Resources:**
- [Moodle Roles and Permissions Documentation](https://docs.moodle.org/501/en/Roles_and_permissions)
- [Web Services Documentation](https://docs.moodle.org/501/en/Web_services)
- [Web Services Security](https://docs.moodle.org/501/en/Web_services_security)

## Configuration

### Environment Variables

The server uses the following environment variables (configured in `.env`):

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MOODLE_URL` | Your Moodle instance URL | - | Yes |
| `MOODLE_TOKEN` | Authentication token from Moodle | - | Yes |
| `LOG_LEVEL` | Logging verbosity (DEBUG, INFO, WARNING, ERROR) | INFO | No |
| `DEBUG` | Enable debug mode (true/false) | false | No |

### Security Best Practices

- Never commit your `.env` file to version control
- Keep your tokens secure and rotate them regularly
- Use HTTPS for production Moodle instances
- Apply IP restrictions when possible for tokens
- Set expiration dates for tokens in production

## Usage

### Starting the Server

1. **Activate your virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```
   
2. **Run the server:**
   ```bash
   python -m src
   ```
   
   Or alternatively:
   ```bash
   python -m src.mcp.server
   ```

3. **To close the server once you are done:**
    - Press `CTRL + C` in the terminal
    - Then exit your virtual environment:
    ```bash
    deactivate
    ```

### Connecting with Claude Desktop

Claude Desktop is used as example, each AI has its methods of adding an MCP tool.
To add the server to your Claude Desktop configuration:
- Open Claude Desktop and go to `Settings`.
- Navigate to the `Developer` section, then choose `Edit config`.
- Edit the file claude_desktop_config.json to add the following MCP server configuration:

**Windows:**
```json
{
  "mcpServers": {
    "moodle-api": {
      "command": "C:\\path\\to\\tfg-mcp-moodle-server\\venv\\Scripts\\python.exe",
      "args": ["-m", "src.mcp.server"],
      "cwd": "C:\\path\\to\\tfg-mcp-moodle-server", 
       "env": {
        "PYTHONPATH": "C:\\path\\to\\tfg-mcp-moodle-server"
      }
    }
  }
}
```

**Linux/macOS:**
```json
{
  "mcpServers": {
    "moodle-api": {
      "command": "/path/to/tfg-mcp-moodle-server/venv/bin/python",
      "args": ["-m", "src.mcp.server"],
      "cwd": "/path/to/tfg-mcp-moodle-server",
       "env": {
        "PYTHONPATH": "/path/to/tfg-mcp-moodle-server"
      }
    }
  }
}
```

- Replace `/path/to/tfg-mcp-moodle-server` with the actual path where you cloned the project.
- Once added, restart Claude Desktop to apply the changes.

### Example Usage

Once connected, you can use natural language to interact with Moodle:

```
"Show me all courses in my Moodle instance"
"Get the enrolled users in course ID 5"
"What's the completion status for user 10 in course 3?"
"List all assignments in course 'Introduction to Python'"
```

## 📖 Documentation

Full documentation is available by serving the documentation on your computer:

```bash
  # Install documentation dependencies
  pip install mkdocs mkdocs-material mkdocstrings[python]
  
  # Serve documentation locally
  mkdocs serve
```
  Then open http://127.0.0.1:8000 in your browser.

Documentation covers:
- [Installation & Usage Guide](docs/usage.md)
- [Architecture Overview](docs/architecture.md)
- [API Reference](docs/api.md)
- [Testing Guide](docs/testing.md)

## Testing

### Run All Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=src --cov-report=html
```

View coverage report:
```bash
# Windows
start htmlcov/index.html

# Linux/Mac
open htmlcov/index.html
```

## Project Structure

```
tfg-mcp-moodle-server/
├── src/
│   └── mcp/              # MCP Protocol implementation
│       └── utils/        # Utility functions
├── tests/                # Test suite
├── docs/                 # Additional documentation
├── dev-environment/      # Docker setup for local Moodle
├── setup.py              # Interactive setup script
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
├── .env.example          # Example environment file
└── README.md             # This file
```

## How It's Made

**Tech Stack:** Python, MCP (Model Context Protocol), Moodle REST API, Docker, Pytest

This project implements the Model Context Protocol to create a standardized interface between AI agents and Moodle. The server acts as a stateless proxy, forwarding requests to Moodle's REST API without data manipulation, ensuring security, simplicity, and data freshness.

### Architecture

**MCP Protocol Integration**
- Each Moodle API endpoint is exposed as an MCP tool with proper type definitions and validation
- Implements the MCP specification, using Anthropic's FastMCP framework, version 1.0.0
- Supports tools/list, tools/call, and comprehensive error handling

**Moodle API Client**
- Built using Python's `requests` library with robust error handling
- Implements authentication via Moodle tokens with secure credential management
- Extensible design - adding new endpoints requires minimal code changes

**Configuration Management**
- Interactive `setup.py` script for non-technical users
- Environment-based configuration following 12-factor app methodology
- Secure password input using `getpass` to prevent token exposure

**Development Environment**
- Containerized Moodle instance using Docker Compose for local testing
- Pre-configured with test data and sensible defaults
- Convenience scripts for easy environment management

**Testing & Quality**
- Comprehensive unit tests using Pytest
- Test coverage reporting with `pytest-cov`
- Type hints throughout the codebase for better IDE support and error detection

### Key Design Decisions

**Why MCP?**
The Model Context Protocol provides a standardized way for AI agents to interact with external services. By implementing MCP, this server works with any MCP-compatible AI agent, ensuring interoperability and future-proofing.

**Why a Proxy Approach?**
Instead of transforming or caching data, the server acts as a direct proxy to Moodle's API. This ensures data freshness, security (no sensitive data stored), simplicity (easier to maintain), reliability (fewer failure points), and most of all the highest level of control for the end user.

**Why Python?**
Python offers an excellent ecosystem for API clients and testing, strong typing support via type hints, easy integration with AI/ML workflows, and wide adoption in the education technology space. It is my primary programming language, allowing for rapid development and iteration.

## Lessons Learned

This project taught me how to effectively implement the Model Context Protocol, design secure API clients, and manage AI agents' tools. I gained experience in building robust, testable codebases and learned the importance of clear documentation for open-source projects. Additionally, I deepened my understanding of Moodle's architecture and web services. Furthermore, I learned that not everything will go as planned initially, and being adaptable is key for a successful project.

## Contributing

Contributions are closed for now. You may create your own fork.

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built as part of a Final Degree Project (TFG)
- Uses the [Model Context Protocol](https://modelcontextprotocol.io/) by Anthropic
- Integrates with [Moodle](https://moodle.org/) Learning Management System

## Support

For issues, or questions:
- [Report a bug](https://github.com/Hefi002/tfg-mcp-moodle-server/issues)
- [Request a feature](https://github.com/Hefi002/tfg-mcp-moodle-server/issues)
- [Read the docs](https://github.com/Hefi002/tfg-mcp-moodle-server/tree/main/docs)

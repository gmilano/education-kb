# ♿ AI Accessibility Checker
A smart Python CLI tool to scan your project’s frontend code for WCAG compliance issues using OpenAI AI analysis.

## Features
- Supports WCAG Levels: A, AA, AAA
- Supports WCAG Versions: 2.0, 2.1, 2.2
- Skips unnecessary folders & files (node_modules, .git, __pycache__, etc.)
- AI-powered suggestions for each detected issue
- Output in table, list or pdf format
- Works as standalone CLI or pre-commit hook

## Detects accessibility problems like:
- ✅ Missing alt attributes
- 🎨 Low contrast text
- ⌨️ Keyboard navigation issues
- 📜 Improper semantic markup
- 🖼️ ARIA misusage
- 🧠 AI-powered suggestions to fix detected issues

## How It Works

- Reads files and adds line numbers
- Sends file contents to OpenAI with WCAG context
- AI detects violations and returns JSON
- Script formats and displays results

## ⚠️ Data Privacy & Compliance Notice

This tool sends code snippets from your project to the OpenAI API for analysis.
Before using it, you are responsible for ensuring your project and organization allow sharing code with third-party services.
**DO NOT USE** this tool on proprietary or confidential code unless you have permission.

## Prerequisites
Before using this tool, make sure you have the following installed:
1. **Python 3.9+**
    
    Mac: 

    Python 3 is usually preinstalled. Check with:

    ```bash
    python3 --version
    ```

    If missing, install via Python.org or Homebrew:

    ```bash
    brew install python
    ```

    Windows:

    Download from Python.org
    When installing, make sure to check the box "Add Python to PATH".
    Verify:

    ```bash
    python3 --version
    ```

    Linux:

    ```bash
    sudo apt update && sudo apt install python3 python3-pip -y
    ```

2. **Pip (Python package manager)**

   ```bash
    pip --version
    ```

    If missing:
    ```bash
    python3 -m ensurepip --upgrade
    ```

3. **Virtual Environment (recommended)**

    This avoids dependency conflicts.

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    ```

## Installation

1️⃣ Clone / Copy this script into your project

```bash
git clone https://github.com/kiran-kadam911/ai-accessibility-checker.git
cd ai-accessibility-checker
```

2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

📄 requirements.txt

```bash
python-dotenv
tabulate
openai>=1.0.0
reportlab
```

## Usage

### Standalone CLI

#### Setup OpenAI API Key
You can get your key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys). (for AI suggestions - Use Paid API plan)

To use AI-powered features, you need to provide your OpenAI API key.
    
    bash -c 'read -p "Enter your OpenAI API Key: " key && echo "OPENAI_API_KEY=$key" > .env'

This will generate a .env file in your project root like:

    OPENAI_API_KEY=sk-xxxxxxx

Once API key set then,

**Run**

```bash
python ai_accessibility_checker.py
```

You will be prompted to:

```bash
👋 Welcome to AI Accessibility Checker

🧩 Which WCAG accessibility level do you want to check? (A / AA / AAA):
📘 Which WCAG version do you want to check? (2.0 / 2.1 / 2.2): 
📊 How would you like results? (table / list / pdf): 
📂 Enter the directory path to scan the files (leave blank for current directory): 
```

**Example Output (Table)**
| #  | Issue Title           | Type      | Severity | Line(s)      | Description | Suggestion |
|----|-----------------------|-----------|----------|--------------|-------------|------------|
| 1  | Low contrast for text | Contrast  | High     | 25, 29, 231, 233 | Text has low contrast due to faint opacity, making it hard for visually impaired users. | Increase opacity to ≥0.5 to meet contrast ratio requirements. |

**Example Output (List)**

**Missing Alt Text on Image** [Alt Text] _(Severity: High)_
   - **Lines:** 15  
   - **Description:** `<img>` lacks `alt` attribute for screen readers.  
   - **Suggestion:** Add descriptive `alt` text to all `<img>` elements.

**Example Output (PDF)**
![PDF Output Example](images/pdf_report.png)

#### checker.config.json

The checker.config.json file allows you to customize how the AI Accessibility Checker scans your project.

**Configuration options:**
- **SUPPORTED_EXTENSIONS** – List of file types the checker will scan (e.g., .html, .twig, .css, .jsx).
- **EXCLUDED_DIRS** – Directories to skip during scanning (e.g., node_modules, build, .git).
- **EXCLUDED_PATTERNS** – File name patterns to ignore (e.g., Storybook files like .stories.jsx).
- **MODEL** – Defines which AI model to use for accessibility analysis.

This configuration helps tailor the scan to your project’s structure, ensuring that only relevant files are checked while ignoring unnecessary or temporary files.

### Usage as a GitHub Action
You can use this tool directly in your GitHub workflows without needing to install anything locally.

#### Save API Key as a GitHub Secret
- Go to your repository → Settings → Secrets and variables → Actions → New repository secret.
- Name it: OPENAI_API_KEY
- Paste your actual key as the value.

```bash
name: AI Accessibility Checker

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  run-checker:
    runs-on: ubuntu-latest
    steps:
      # Step 1: Checkout repository
      - name: Checkout code
        uses: actions/checkout@v4

      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt || pip install openai python-dotenv tabulate

      # Step 4: Set environment variables
      - name: Set environment variables
        run: |
          echo "OPENAI_API_KEY=${{ secrets.OPENAI_API_KEY }}" >> $GITHUB_ENV
          echo "AI_CHECKER_ACKNOWLEDGED=true" >> $GITHUB_ENV

      # Step 5: Run Accessibility Checker
      - name: Run AI Accessibility Checker
        run: python ai_accessibility_checker.py --level A --version 2.0 --format table --dir ./themes/custom/my_theme
```
## Demo
[Demo Video](https://www.linkedin.com/posts/kiran-kadam-96041b63_a11y-accessibility-wcag-activity-7404507268437692416-Asx7?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA1pAJgBv0ZOhUrgPQBBHvmEJ2Y0bAET9p0)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

# a11y-mcp-server

MCP server for accessibility auditing, WCAG criteria lookup, and remediation guidance. Kept public as working evidence of standing up an MCP server end to end: five working tools plus a deployment runbook. The skills-based successor for day-to-day accessibility work is [claude-a11y-skills](https://github.com/shawnmcb/claude-a11y-skills).

## Features

- **a11y_lookup_wcag**: Look up WCAG 2.2 criteria by number, keyword, or level
- **a11y_check_pattern**: Analyze HTML snippets for common accessibility issues
- **a11y_suggest_fix**: Get remediation patterns with before/after code examples
- **a11y_document_component**: Generate accessibility docs for 18+ UI component types
- **a11y_audit_summary**: Generate professional audit reports from issues list

## Local Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Run locally
npm start

# Server runs on http://localhost:8080
# Health check: http://localhost:8080/health
# MCP endpoint: http://localhost:8080/mcp
```

## NFSN Deployment

### Prerequisites for my own path; YMMV:

1. NFSN account with funds (~$10 initial deposit)
2. SSH access configured

### Setup Steps

#### 1. Create NFSN Site

1. Log into NFSN Members Interface
2. Sites → Create a New Site
3. Site type: **Custom** (required for Node.js daemon)
4. Note your site hostname (e.g., `yoursite.nfshost.com`)

#### 2. Upload Code

```bash
# From project directory
rsync -avz --exclude node_modules --exclude .git --exclude dist \
  ./ USERNAME_SITENAME@ssh.phx.nearlyfreespeech.net:/home/protected/a11y-mcp-server
```

#### 3. SSH Setup

```bash
ssh USERNAME_SITENAME@ssh.phx.nearlyfreespeech.net

# Navigate to project
cd /home/protected/a11y-mcp-server

# Check Node.js version (should be 18+)
node --version

# Install dependencies
npm install --production

# Build
npm run build

# Make run.sh executable
chmod +x run.sh

# Test locally
./run.sh
# Ctrl+C to stop
```

#### 4. Configure NFSN Daemon

1. Go to NFSN site control panel
2. Sites → Your Site → Site Information → Daemons
3. Add daemon:
   - **Tag**: `node`
   - **Command Line**: `/home/protected/a11y-mcp-server/run.sh`
   - **Working Directory**: `/home/protected/a11y-mcp-server`

#### 5. Configure NFSN Proxy

1. Sites → Your Site → Site Information → Proxies
2. Add proxy:
   - **Protocol**: `http`
   - **Base URI**: `/mcp`
   - **Document Root**: (leave empty)
   - **Target Port**: `8080`

#### 6. Verify Deployment

```bash
# Check health endpoint
curl https://yoursite.nfshost.com/health

# Test MCP endpoint
curl -X POST https://yoursite.nfshost.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'
```

### Troubleshooting

**Check daemon logs:**
```bash
ssh USERNAME_SITENAME@ssh.phx.nearlyfreespeech.net
cat /home/protected/a11y-mcp-server/daemon.log
```

**Restart daemon:**
Via NFSN control panel: Sites → Daemons → Restart

**Check if daemon is running:**
```bash
ps aux | grep node
```

## Claude Code Configuration

Add to `~/.config/claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "a11y": {
      "url": "https://yoursite.nfshost.com/mcp"
    }
  }
}
```

Then restart Claude Code.

## Local Testing with Claude Code

For testing before NFSN deployment, run the server locally and configure Claude Code to connect:

1. Start the server:
```bash
npm start
```

2. Add to `~/.config/claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "a11y-local": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

3. Restart Claude Code

## Evaluation Questions

Use these questions to verify the server is working correctly:

1. **WCAG Lookup**: "What WCAG criterion covers keyboard navigation and what level is it?"
   - Expected: Returns 2.1.1 Keyboard (Level A) with full details

2. **Remediation Pattern**: "What's the remediation pattern for missing alt text on decorative images?"
   - Expected: Returns pattern with empty alt="" example

3. **Component Documentation**: "Generate accessibility documentation for a modal dialog component."
   - Expected: Returns keyboard interactions, ARIA attributes, screen reader expectations

4. **WCAG 2.2 Search**: "Which WCAG 2.2 criteria are specific to mobile/touch interactions?"
   - Expected: Returns 2.5.x Input Modalities criteria

5. **Common Failures**: "What are the common failures for criterion 1.4.3 Contrast?"
   - Expected: Returns F24, F83 failure techniques

## Usage Examples

### Look up WCAG criterion
```
Query: "What WCAG criterion covers keyboard navigation?"
Tool: a11y_lookup_wcag
Args: { "query": "keyboard" }
```

### Check HTML for issues
```
Query: "Check this HTML for accessibility issues"
Tool: a11y_check_pattern
Args: { "html": "<img src='logo.png'><button><svg>...</svg></button>" }
```

### Get remediation pattern
```
Query: "How do I fix missing alt text on decorative images?"
Tool: a11y_suggest_fix
Args: { "issueType": "missing-alt-decorative" }
```

### Generate component docs
```
Query: "Generate accessibility documentation for a modal dialog"
Tool: a11y_document_component
Args: { "componentType": "modal" }
```

## Updating WCAG Data

WCAG criteria are bundled in `src/data/wcag-criteria.json`. To update:

1. Edit the JSON file with new criteria
2. Rebuild: `npm run build`
3. Redeploy to NFSN

## License

MIT

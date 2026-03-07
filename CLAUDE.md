# CLAUDE.md

This file provides guidance to AI assistants (Claude Code and others) working in this repository.

## Repository Overview

**Repository**: SomersetMaugham-stack/Claude-stuff-
**Purpose**: A repository configured for Claude Code-assisted development workflows.

This repository is set up with Claude Code conventions including SSH commit signing, structured branch naming, and AI-assisted development practices.

## Git Configuration

The repository uses the following git setup:

- **Commit signing**: SSH key signing is enabled (`commit.gpgsign=true`). All commits are automatically signed — do not pass `--no-gpg-sign` or `--no-verify`.
- **Git user**: Claude (noreply@anthropic.com)
- **Remote**: Proxied via local proxy — push/pull commands should use `origin` as configured.

## Branch Naming Conventions

All Claude Code feature branches follow this pattern:

```
claude/<short-description>-<session-id>
```

Examples:
- `claude/add-claude-documentation-Kg7Y8`
- `claude/fix-auth-bug-Ab3Cd`
- `claude/refactor-api-client-Xy9Zw`

**Rules:**
- Always develop on the designated `claude/` branch for the session.
- Never push to `main` or `master` directly without explicit user permission.
- Create the branch locally if it does not yet exist: `git checkout -b claude/<description>-<id>`

## Development Workflow

### Starting Work

1. Verify you are on the correct `claude/` branch:
   ```bash
   git branch --show-current
   ```
2. If the branch does not exist, create it:
   ```bash
   git checkout -b claude/<description>-<session-id>
   ```

### Making Changes

- Read files before editing them — understand existing code before modifying it.
- Prefer editing existing files over creating new ones.
- Keep changes focused and minimal — only modify what is directly requested.
- Do not add comments, docstrings, or type annotations to code you did not change.

### Committing

- Stage specific files rather than `git add -A` or `git add .` to avoid accidentally including secrets or generated files.
- Write clear, descriptive commit messages that explain the *why*, not just the *what*.
- Commit format:

  ```
  <type>: <short summary>

  <optional body explaining motivation and context>
  ```

  Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

- Commit messages must include the Claude Code session URL as a trailer:
  ```
  https://claude.ai/code/session_<session-id>
  ```

### Pushing

Always push with the upstream flag:

```bash
git push -u origin claude/<description>-<session-id>
```

**Retry on network failure** using exponential backoff (2s, 4s, 8s, 16s) — up to 4 retries. Do not retry on non-network errors (e.g., HTTP 403 due to wrong branch name).

HTTP 403 on push almost always means the branch name does not match the expected `claude/` prefix pattern — check the branch name first.

## File and Code Conventions

### General

- Use the minimum complexity necessary — avoid premature abstractions and over-engineering.
- Do not add error handling for scenarios that cannot happen in practice.
- Do not create helpers or utilities for one-time operations.
- Remove dead code rather than commenting it out or leaving backwards-compatibility shims.

### Security

- Never commit secrets, credentials, `.env` files, or private keys.
- Validate input at system boundaries (user input, external APIs) but trust internal code.
- Avoid introducing OWASP Top 10 vulnerabilities: SQL injection, XSS, command injection, etc.

### Reversibility

Before taking any of the following actions, confirm with the user:

- Deleting files or branches
- Force-pushing (`--force`)
- Hard resets (`git reset --hard`)
- Dropping database tables or irreversible data operations
- Pushing to shared branches or opening/closing PRs
- Sending messages or posting to external services

## Pull Requests

When creating a PR:

1. Ensure all changes are committed and pushed to the `claude/` branch.
2. Use `gh pr create` with a clear title (under 70 characters) and a body that includes:
   - A brief summary (1–3 bullet points)
   - A test plan (checklist of what to verify)
   - The Claude Code session URL

```bash
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
- <bullet 1>

## Test plan
- [ ] <check 1>

https://claude.ai/code/session_<session-id>
EOF
)"
```

## Working with Claude Code Tools

Prefer dedicated tools over shell equivalents:

| Task | Use | Not |
|------|-----|-----|
| Read a file | `Read` tool | `cat`, `head`, `tail` |
| Edit a file | `Edit` tool | `sed`, `awk` |
| Create a file | `Write` tool | `echo >`, heredoc |
| Find files | `Glob` tool | `find`, `ls` |
| Search content | `Grep` tool | `grep`, `rg` |
| Multi-step tasks | `TodoWrite` tool | — |

Use parallel tool calls whenever operations are independent of each other.

## Adding to This Repository

As this repository grows, update this CLAUDE.md to reflect:

- New directories and their purposes
- Technologies and frameworks introduced
- Test commands and how to run them
- Build and deployment processes
- Environment variable requirements (document names, not values)
- Any new conventions adopted by the project

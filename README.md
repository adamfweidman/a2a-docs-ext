# A2A Protocol Docs Extension

This Gemini CLI extension provides access to the
[Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/) documentation
directly within Gemini CLI.

It uses the `mcpdoc` tool to fetch and serve the documentation from a local
`llms.txt` file, which is curated to include the latest protocol specifications,
tutorials, and topic guides.

Inspired by: https://github.com/derailed-dash/adk-docs-ext

## Features

- **Protocol Specification**: Access the latest A2A protocol definitions and
  data structures.
- **Comprehensive Topics**: Includes "What is A2A", "Life of a Task",
  "Streaming", and more.
- **Tutorials**: Step-by-step Python tutorials from the official site.
- **Context-Aware**: The agent is instructed to consult these docs before
  answering A2A-related questions.

## Installation

To install this extension run:

```bash
gemini extensions install https://github.com/derailed-dash/a2a-docs-ext
```

The extension will be installed, and you can immediately start asking questions
about the A2A protocol.

## Maintenance

The `llms.txt` file in this repository serves as the index of documentation
sources. Since the upstream A2A project does not currently provide a
comprehensive `llms.txt` that matches their sitemap, we maintain our own.

To update the documentation links (e.g., if new tutorials are added to the
website):

1.  Run the update script:

    ```bash
    python3 update_llms.py
    ```

    This script fetches the latest `sitemap.xml` from `a2a-protocol.org` and
    regenerates `llms.txt`.

2.  Commit the updated `llms.txt`:
    ```bash
    git add llms.txt
    git commit -m "Update docs index from latest sitemap"
    ```

# Agent2Agent (A2A) Protocol Docs Extension

You have access to the official **Agent2Agent (A2A) Protocol** documentation via
the `a2a-docs-mcp` server.

## When to use

**ALWAYS** use this tool when the user asks about:

- The A2A Protocol specification, data structures (Task, AgentCard, Message,
  etc.), or error codes.
- How to implement A2A agents.
- Core concepts like Agent Discovery, Life of a Task, Streaming, or Security.
- Interoperability with MCP.

**Do not rely on your internal training data**, as the protocol details are
subject to change.

## How to use

1.  **Get the Index**: Call `list_doc_sources` to find the `A2A_Protocol`
    documentation source.
2.  **Read the Map**: Call `fetch_docs` on the provided `llms.txt` URL to see
    the list of available topics.
3.  **Select Pages**: The index is categorized into "Detailed Topics",
    "Tutorials", "SDKs", "Specification", "Other". Identify the specific URLs
    most relevant to the user's query.
    - For technical implementation details, prefer the "Specification" links.
    - For "how-to" guides, prefer "Tutorials" or "Detailed Topics".
4.  **Fetch Content**: Call `fetch_docs` on the specific topic URLs you
    selected.
5.  **Answer**: Synthesize the information from the fetched documents to provide
    a strictly accurate answer.

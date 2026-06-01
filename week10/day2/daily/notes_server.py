from mcp.server.fastmcp import FastMCP

mcp = FastMCP("NotesServer")
_notes = []


@mcp.tool()
def add_note(title: str, content: str) -> str:
    """Add a note with a title and content. Returns confirmation."""
    _notes.append({"title": title, "content": content})
    return f"Note '{title}' saved. Total notes: {len(_notes)}"


@mcp.tool()
def list_notes() -> str:
    """List all saved notes. Returns them formatted."""
    if not _notes:
        return "No notes yet."
    return "\n".join(f"• {n['title']}: {n['content']}" for n in _notes)


if __name__ == "__main__":
    mcp.run()

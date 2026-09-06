# ♟ Chess Detective Agent

An MCP-powered chess investigation system that helps analyze chess positions, explore legal moves, compare decisions, and reconstruct games.

## The Idea

Chess Detective treats chess analysis as an investigation. Instead of putting every capability into one function, specialized chess capabilities are exposed as independent MCP tools.

## Architecture

```
User
  ↓
Chess Detective Agent
  ↓
MCP Client
  ↓
Chess Detective MCP Server
  ├── Inspect Position
  ├── Investigate Legal Moves
  ├── Compare Chess Moves
  └── Reconstruct Chess Game
  ↓
python-chess
```

## MCP Tools

### 1. Inspect Chess Position

Analyzes a FEN position and returns:

- Side to move
- Check and checkmate status
- Material distribution
- Number of legal moves
- Sample legal moves

### 2. Investigate Legal Moves

Examines the legal moves available in a position and identifies:

- SAN notation
- UCI notation
- Captures
- Checks

### 3. Compare Chess Moves

Investigates a played move against an alternative move.

### 4. Reconstruct Chess Game

Parses a PGN game and reconstructs:

- Game metadata
- Result
- Move sequence
- FEN before every move

## Tech Stack

- Python
- MCP (Model Context Protocol)
- FastMCP
- python-chess

## Installation

```bash
git clone https://github.com/Adarsh4777/chess-detective-agent.git
cd chess-detective-agent
python -m pip install -r requirements.txt
```

## Running the Agent

```bash
python agent.py
```

The agent starts a local MCP server and connects to it through an MCP client.

## Example Workflow

```text
Inspect Position
      ↓
Investigate Legal Moves
      ↓
Compare Candidate Moves
      ↓
Build Understanding of the Position
```

## Project Structure

```text
chess-detective-agent/
├── agent.py
├── server.py
├── chess_tools.py
├── requirements.txt
└── README.md
```

## Current Status

Working prototype with:

- Local MCP server
- MCP client
- Four specialized chess investigation tools
- FEN analysis
- Legal move investigation
- Move comparison
- PGN reconstruction

## Future Work

- Autonomous tool selection
- Chess engine evaluation
- Automatic critical moment detection
- Full game post-mortem reports

## Author

Adarsh Choudhary
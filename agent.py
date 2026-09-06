import asyncio
import json
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run_agent():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\n♟ CHESS DETECTIVE AGENT")
            print("=" * 50)
            print("An agent that investigates chess positions using MCP tools.")
            print("\nAvailable actions:")
            print("1. Inspect a chess position")
            print("2. Investigate legal moves")
            print("3. Compare two moves")
            print("4. Reconstruct a PGN game")
            print("5. Exit")

            while True:
                choice = input("\nChoose an action (1-5): ").strip()

                if choice == "1":
                    fen = input("\nEnter FEN: ").strip()

                    result = await session.call_tool(
                        "inspect_chess_position",
                        {"fen": fen}
                    )

                    print("\nDETECTIVE REPORT")
                    print("-" * 50)
                    for item in result.content:
                        print(item.text)

                elif choice == "2":
                    fen = input("\nEnter FEN: ").strip()

                    result = await session.call_tool(
                        "investigate_legal_moves",
                        {"fen": fen}
                    )

                    print("\nLEGAL MOVE INVESTIGATION")
                    print("-" * 50)
                    for item in result.content:
                        print(item.text)

                elif choice == "3":
                    fen = input("\nEnter FEN: ").strip()
                    actual_move = input("Enter actual move: ").strip()
                    alternative_move = input("Enter alternative move: ").strip()

                    result = await session.call_tool(
                        "compare_chess_moves",
                        {
                            "fen": fen,
                            "actual_move": actual_move,
                            "alternative_move": alternative_move
                        }
                    )

                    print("\nMOVE COMPARISON REPORT")
                    print("-" * 50)
                    for item in result.content:
                        print(item.text)

                elif choice == "4":
                    print("\nPaste PGN below.")
                    print("Press Enter on an empty line when finished:\n")

                    lines = []

                    while True:
                        line = input()

                        if not line.strip():
                            break

                        lines.append(line)

                    pgn_text = "\n".join(lines)

                    result = await session.call_tool(
                        "reconstruct_chess_game",
                        {"pgn_text": pgn_text}
                    )

                    print("\nGAME RECONSTRUCTION")
                    print("-" * 50)
                    for item in result.content:
                        print(item.text)

                elif choice == "5":
                    print("\nChess Detective Agent signing off.")
                    break

                else:
                    print("Invalid choice. Please choose 1-5.")


if __name__ == "__main__":
    asyncio.run(run_agent())
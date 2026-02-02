"""
D&D Character Generator - Main Entry Point

This module serves as the entry point for the entire D&D character generation and
management application. It provides a simple main loop that routes user input to
appropriate CLI functions and handles errors gracefully.

The application follows this flow:
1. Display main menu to user
2. Route to character creation, loading, or exit based on user choice
3. Handle errors and keyboard interrupts gracefully
4. Loop until user chooses to exit

Main features handled by this module:
- Graceful error handling with user-friendly messages
- Keyboard interrupt handling (Ctrl+C)
- Application lifecycle management
"""

import sys
from cli_utils import main_menu, cli_new_character, cli_load_and_level, cli_view_character


def main():
    """
    The main application loop.
    
    Continuously displays the main menu and routes the user to appropriate
    functions based on their selection. The loop persists until the user
    explicitly chooses to exit.
    
    Handles two types of exceptions:
    - KeyboardInterrupt: User pressed Ctrl+C (graceful shutdown)
    - Generic Exception: Unexpected errors during operation (recovery prompt)
    """
    while True:
        try:
            choice = main_menu()
            
            # Route to appropriate CLI function based on user choice
            if choice == "new":
                cli_new_character()
            
            elif choice == "load":
                cli_load_and_level()
            
            elif choice == "view":
                cli_view_character()
            
            elif choice == "exit":
                print("\nFarewell, traveler! Your legend awaits.")
                sys.exit()
                
        except KeyboardInterrupt:
            # Gracefully handle Ctrl+C by notifying user and exiting
            print("\n\nProgram interrupted. Saving progress and exiting...")
            sys.exit()
        except Exception as e:
            # Catch-all for unexpected errors; allow user to return to menu
            print(f"\n[ERROR] An unexpected glitch occurred: {e}")
            input("Press Enter to return to the menu...")


if __name__ == "__main__":
    # Entry point: runs the main application loop
    main()
#!/usr/bin/env python3
"""LucidX CLI — interactive menu and argument handling."""

import os
import signal
import sys

from .banr import *
from .colors import *
from .modulex import *
from .genx import *

def handle_interrupt(sig, frame):
    print(f"\n{RED}[!] Interrupted by user. Exiting...{RESET}")
    if os.path.isfile(LAST_STYLE_FILE):
        try:
            os.remove(LAST_STYLE_FILE)
        except Exception as e:
            print(f"{RED}[!] Error: {e}")
    else:
        pass
    lucid_exit()
    exit()
signal.signal(signal.SIGINT, handle_interrupt)

def show_version():
    """Display version information"""
    print(f"{GREEN}LucidX - AI-Powered Image Synthesis Engine{RESET}")
    print(f"{WHITE}Version: {VALUE}1.0.5{RESET}")
    print(f"{WHITE}Author: {VALUE}Alex @ VritraSec{RESET}")
    print(f"{WHITE}GitHub: {VALUE}https://github.com/MrHacker-X/LucidX{RESET}")
    print(f"{WHITE}Platform: {VALUE}Linux, Termux (Android){RESET}")
    print(f"{WHITE}Engine: {VALUE}Stability AI API + Python{RESET}")

def show_help():
    """Display help information"""
    print(f"{GREEN}LucidX - AI-Powered Image Synthesis Engine{RESET}")
    print(f"{WHITE}Usage: {VALUE}python lucidx.py [OPTION]{RESET}\n")
    
    print(f"{WHITE}OPTIONS:{RESET}")
    print(f"{GREEN}  --help, -h     {WHITE}Show this help message and exit{RESET}")
    print(f"{GREEN}  --version, -v  {WHITE}Show version information and exit{RESET}")
    print(f"{GREEN}  (no arguments) {WHITE}Launch interactive menu{RESET}\n")
    
    print(f"{WHITE}DESCRIPTION:{RESET}")
    print(f"{GRAY}  LucidX is an AI-powered image synthesis engine that leverages{RESET}")
    print(f"{GRAY}  the Stability AI API to transform text prompts into stunning,{RESET}")
    print(f"{GRAY}  high-resolution images with multiple artistic styles.{RESET}\n")
    
    print(f"{WHITE}EXAMPLES:{RESET}")
    print(f"{GREEN}  python lucidx.py          {GRAY}# Launch interactive menu{RESET}")
    print(f"{GREEN}  python lucidx.py --help   {GRAY}# Show this help message{RESET}")
    print(f"{GREEN}  python lucidx.py --version{GRAY}# Show version information{RESET}\n")
    
    print(f"{WHITE}For more information, visit: {VALUE}https://github.com/MrHacker-X/LucidX{RESET}")

def parse_arguments():
    """Parse command line arguments"""
    args = sys.argv[1:]  # Remove script name
    
    # Check if more than one argument is provided
    if len(args) > 1:
        print(f"{RED}[!] Error: Multiple arguments detected.{RESET}")
        print(f"{WHITE}Please use only one argument at a time.{RESET}")
        print(f"{WHITE}Use 'python lucidx.py --help' for usage information.{RESET}")
        sys.exit(1)
    
    # Handle single argument
    if len(args) == 1:
        arg = args[0].lower()
        
        if arg in ['--help', '-h']:
            show_help()
            sys.exit(0)
        elif arg in ['--version', '-v']:
            show_version()
            sys.exit(0)
        else:
            print(f"{RED}[!] Error: Unknown argument '{args[0]}'{RESET}")
            print(f"{WHITE}Use 'python lucidx.py --help' for available options.{RESET}")
            sys.exit(1)
    
    # No arguments - proceed with interactive menu
    return True

def lucidx_main_menu():

    while True:
        os.system("clear" if os.name != "nt" else "cls")
        print(lucid_Main_logo())
        MAIN_MENU = f"""
{GREEN}..:: MAIN MENU ::..

{GREEN} › [1] {WHITE}Image Generation
{GREEN} › [2] {WHITE}Configure API Key
{GREEN} › [3] {WHITE}Connect With Us
{GREEN} › [4] {WHITE}About LucidX
{GREEN} › [5] {WHITE}Help / Documentation
{GREEN} › [6] {WHITE}Exit

{GRAY}:: Select option (1–6): {GREEN}"""

        main_choice = input(MAIN_MENU).strip()

        if main_choice == "":
            continue

        elif main_choice == "1":
            main_genx()
            exit()

        elif main_choice == "2":
            configure_api_key()

        elif main_choice == "3":
            lucid_connect()

        elif main_choice == "4":
            about_lucidx()

        elif main_choice == "5":
            lucid_help()

        elif main_choice == "6":
            lucid_exit()
            break

        else:
            print(GRAY + "! Invalid option. Please try again.\n")

def main():
    """CLI entry point (console_scripts + python -m lucidx)."""
    from .remote_control import RemoteControl

    with RemoteControl(tool_id="lucidx"):
        if parse_arguments():
            lucidx_main_menu()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3

import os
os.system('') #Kicks windows into ANSI mode

import argparse
import sys
from shells.payloads import PAYLOADS

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

BANNER = (
    f"{RED}{BOLD}\n"
    r" ___     _ ___      " + "\n"
    r"| _ \___| / __|_  _ " + "\n"
    r"|  _/ _ \ \__ \ || |" + "\n"
    r"|_| \___/_|___/\_,_|" + "\n"
    f"{RESET}"
    f"{CYAN}Educational use only. Dont be a skid!{RESET}"
)

def list_shells():
    print(BANNER)
    print(f"  {'TYPE':<20} {'DESCRIPTION'}")
    print(f"  {'-'*20} {'-'*40}")
    for name, data in PAYLOADS.items():
        print(f"  {YELLOW}{name:<20}{RESET} {data['description']}")
    print()

def generate(ip: str, port: int, shell_type: str):
    if shell_type not in PAYLOADS:
        print(f"{RED}[!] Unknown shell type: '{shell_type}'{RESET}")
        print(f"    Run with --list to see available types.")
        sys.exit(1)

    payload = PAYLOADS[shell_type]
    cmd = payload["cmd"].format(ip=ip, port=port)

    print(BANNER)
    print(f"  {BOLD}Type   :{RESET}  {YELLOW}{shell_type}{RESET}")
    print(f"  {BOLD}Target :{RESET}  {ip}:{port}")
    print(f"  {BOLD}Info   :{RESET}  {payload['description']}")
    print()
    print(f"  {GREEN}{'─'*60}{RESET}")
    print(f"\n  {cmd}\n")
    print(f"  {GREEN}{'─'*60}{RESET}")
    print()
    print(f"  {CYAN}[*] Listener:{RESET}  nc -lvnp {port}")
    print()

def main():
    parser = argparse.ArgumentParser(
        prog="rshell",
        description=f"{CYAN}Simple reverse shell payload generator. Developed to learn python and prevent Google reverse shell rabbit holes{RESET}",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-i", "--ip",
        help="listener IP address (e.g. 10.10.14.5)",
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        help="listener port (e.g. 4444)",
    )
    parser.add_argument(
        "-t", "--type",
        help="Shell type to generate (use --list to see all)",
        default="bash",
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List all available shell types",
    )

    args = parser.parse_args()

    if args.list:
        list_shells()
        sys.exit(0)

    if not args.ip or not args.port:
        print(BANNER)
        parser.print_help()
        print(f"\n{RED}[!] Missing required arguments: --ip or --port, use --help for more info{RESET}")
        sys.exit(1)

    generate(args.ip, args.port, args.type)

if __name__ == "__main__":
    main()

#Feel free to edit as you please. Feedback and contributions are always welcome, keep in mind this is a learning project and not meant to be a comprehensive payload generator.
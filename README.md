# rshell-gen

A simple CLI tool for generating ready-to-use reverse shell payloads.  
No more googling for one liners!.

---

## Usage

```bash
python rshell.py -i <LISTENER_IP> -p <LISTENER_PORT> -t <TYPE>
```

### List all available shell types
```bash
python rshell.py --list
```

### Example
```bash

# PHP exec shell
python rshell.py -i 10.10.14.5 -p 8008 -t php

```

---

## Available Shell Types

| Type | Description |
|------|-------------|
| `bash` | Bash TCP reverse shell |
| `bash-mkfifo` | Bash mkfifo (more reliable) |
| `python` | Python 3 reverse shell |
| `python2` | Python 2 reverse shell |
| `php` | PHP exec reverse shell |
| `php-system` | PHP system (useful in webshells) |
| `nc` | Netcat with -e flag |
| `nc-mkfifo` | Netcat without -e (busybox/older nc) |
| `powershell` | PowerShell reverse shell (Windows) |
| `perl` | Perl reverse shell |
| `ruby` | Ruby reverse shell |
| `lua` | Lua reverse shell |

---

## Installation

```bash
git clone https://github.com/P0lSu/rshell-gen
cd rshell-gen
python rshell.py --help
```

No external dependencies.

---

## Disclaimer

This tool is intended for use in educational purposes only.  
Do not use against systems you do not have explicit permission to test. 

---


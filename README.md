# Reverse Shell Python Program

This is a Python-based reverse shell program that allows you to establish a connection between an attacker machine and a victim machine, giving you control over the victim's system. It consists of two Python scripts, one for the attacker side and the other for the victim side. CUrrently this program does do much other than being able to upload or download file from victim's computer and run other windows cmd commands. Plus there is a bug in the program that it break if some wrong input is given like cd to_some_direcory_that_doesnt_exists etc.

## Attacker Side Program

The attacker side program (`attacker.py`) is responsible for setting up a listener and handling incoming connections from the victim machine. It provides a simple shell interface to interact with the connected victim. The attacker can execute commands on the victim's machine, download files from the victim, and upload files to the victim.

**Prerequisites:**

- Python 3.x

**Usage:**

1. Edit the IP address and replace it with your IP address
2. Run the attacker script (`attacker.py`) on your machine.
3. It will start listening for incoming connections on the specified IP address and port (IP: `<Your IP>`, port: 5555).
4. Once a victim machine connects to the listener, the attacker can interact with the victim's machine through the shell interface.

**Commands:**

- `quit`, `exit`, `bye`, `deactivate`, `logout`: Terminate the connection with the victim.
- `clear` or `cls`: Clear the screen on the attacker side.
- `cd <directory>`: Change the current directory on the victim machine.
- `download <file>`: Download a file from the victim's machine to the attacker's machine.
- `upload <file>`: Upload a file from the attacker's machine to the victim's machine.
- Or any other Windows commands.

## Victim Side Program (Payload)

The victim side program (`payload.py`) is the payload that the attacker needs to run on the victim's machine. It connects back to the attacker's machine, allowing the attacker to execute commands on the victim's machine.

**Prerequisites:**

- Python 3.x

**Usage:**

1. Compile the payload script using a tool like pyinstaller on a Windows machine to create an executable binary.
   ```
   pyinstaller payload.py --onefile --noconsole
   ```
2. Transfer the compiled binary (`payload.exe`) to the victim's machine.
3. Run the `payload.exe` on the victim's machine.
4. It will establish a connection back to the attacker's machine and wait for commands.

**Commands:**
The commands sent from the attacker will be executed on the victim's machine, and the results will be sent back to the attacker.

## Disclaimer

This program is intended for educational and ethical purposes only. Unauthorized use of this program on systems you don't own or have explicit permission to use is illegal. The authors are not responsible for any misuse or damage caused by this program.

## Notes

- For testing purposes, make sure both the attacker and victim machines are on the same local network.
- Use this program responsibly and only on systems you have explicit permission to access.

## Author

This program was created by Abhinav Yadav.

**# SSH Tunnel Manager**



A Python-based Windows tool that monitors Gmail and manages SSH reverse tunnel connections through Serveo.



**## Features**



*- Gmail IMAP monitoring.*

*- Automatic SSH tunnel initialization.*

*- Forwarding port detection.*

*- Gmail SMTP notifications.*

*- Background execution (`.pyw`).*



**## Requirements**



*- Windows 10/11*

*- Python 3*

*- Gmail account with App Password*

*- Internet connection*



**## OpenSSH Installation**



1. Open PowerShell as Administrator:


run this command:

Add-WindowsCapability -Online -Name OpenSSH.Server\~\~\~\~0.0.1.0





2. Restart Windows.



3. Open PowerShell as Administrator again:


run theese commands:


Add-WindowsCapability -Online -Name OpenSSH.Client\~\~\~\~0.0.1.0

Start-Service sshd

Set-Service -Name sshd -StartupType Automatic




**## Configuration**



Open `tunnel.pyw` with Notepad or another text editor and change these variables:



```

EMAIL\_USER = "your-email@gmail.com"

EMAIL\_PASS = "your-app-password"

CARTELLA = r"C:\\Tunnel"

NAME = "YourWindowsUsername"

```



Replace them as follows:



\- EMAIL\_USER: Your Gmail address (example: `example@gmail.com`).

\- EMAIL\_PASS: Your Google App Password, NOT your normal Gmail password.

\- CARTELLA: The folder where you want the tunnel log saved. Example: `r"C:\\Tunnel"`. Create this folder beforehand.

\- NAME: Your Windows account username (the username of the PC running the script).



Save the file after making the changes.



\*\*Important:\*\* Never publish your Gmail address together with your App Password on GitHub. Use placeholders in publicly shared code.



**## Usage**



1\. Install Python from python.org.

2\. Complete OpenSSH installation.

3\. Configure Gmail credentials.

4\. Save the script as `tunnel.pyw`.

5\. Open your automatic execution folder with WINDOWS+R and type shell:startup in the executer.

6\. Create a shortcut with the python path and file path ("PYTHON\_PATH" "FILE\_PATH").



**## Troubleshooting**



\- \*\*Gmail errors:\*\* Check IMAP and App Password settings.

\- \*\*SSH errors:\*\* Verify OpenSSH installation.

\- \*\*No forwarding port:\*\* Check `tunnel.log` and Serveo availability.

\- \*\*No notification:\*\* Check SMTP credentials.



**## Security**



\- Never upload credentials to GitHub.

\- Use only on systems you own or have permission to access.

\- Authenticate incoming commands.

\- Verify SSH host keys.

\- Avoid exposing unnecessary services.



**## Disclaimer**



For educational purposes and authorized remote administration only. The author is not responsible for misuse or unauthorized access.


import imaplib, smtplib, time, subprocess, re, os
from email.message import EmailMessage

EMAIL_USER = "EMAIL-USER"
EMAIL_PASS = "APP-PASSWORD" 
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
CARTELLA = r"TUNNEL-FOLDER"
LOG_FILE = os.path.join(CARTELLA, "tunnel.log")
NAME = "YOUR-NAME"

def kill_ssh():
    subprocess.run(["taskkill", "/F", "/IM", "ssh.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def avvia_tunnel():
    kill_ssh()
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    cmd = f'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 0:localhost:22 serveo.net > "{LOG_FILE}" 2>&1'
    subprocess.Popen(cmd, shell=True)
    print("Tunnel in avvio...")
    for i in range(30):
        time.sleep(1)
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", errors="ignore") as f:
                t=f.read()
                m=re.search(r"Forwarding.*?:(\d+)", t)
                if m: 
                    return m.group(1)
    return "0"

def invia_email(porta):
    msg = EmailMessage()
    msg["From"]=EMAIL_USER
    msg["To"]=EMAIL_USER
    msg["Subject"]=f"Tunnel ready - door {porta}"
    logtxt = open(LOG_FILE, encoding='utf-8', errors='ignore').read() if os.path.exists(LOG_FILE) else ""
    
    
    comando_termux = f'ssh -p {porta} "{NAME}"@serveo.net'

    msg.set_content(f"""Tunnel active!

Door: {porta}
Windows user: {NAME}

Termux command:
{comando_termux}

Log:
{logtxt}
""")
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as s:
        s.starttls()
        s.login(EMAIL_USER, EMAIL_PASS)
        s.send_message(msg)

print("Email watcher started...")
while True:
    try:
        mail=imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("INBOX")
        _, data = mail.search(None, '(SUBJECT "new" UNSEEN)')
        for num in data[0].split():
            print("Received command")
            mail.store(num, '+FLAGS', '\\Seen')
            porta=avvia_tunnel()
            invia_email(porta)
        mail.logout()
    except Exception as e:
        print(f"Errore: {e}")
    time.sleep(15)
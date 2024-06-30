import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, attachment_path, config):
    from_addr = config['Email']['Email']
    to_addr = config['Email']['Recipient']
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        msg.attach(part)

    server = smtplib.SMTP(config['Email']['SMTP_Server'], config['Email']['SMTP_Port'])
    server.starttls()
    server.login(from_addr, config['Email']['Password'])
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def check_email_response(config):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(config['Email']['Email'], config['Email']['Password'])
    mail.select('inbox')

    result, data = mail.search(None, '(UNSEEN)')
    mail_ids = data[0].split()
    print(f"Found {len(mail_ids)} unread emails.")
    for mail_id in mail_ids:
        result, message_data = mail.fetch(mail_id, '(RFC822)')
        raw_email = message_data[0][1].decode('utf-8')
        msg = email.message_from_string(raw_email)
        from_address = email.utils.parseaddr(msg['From'])[1]

        if from_address == config['Email']['Recipient']:
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode('utf-8').strip().split('\n')[0].strip().upper()
                    print(body)
                    if body == 'Y':
                        return True
                    elif body == 'N':
                        return False
    return None
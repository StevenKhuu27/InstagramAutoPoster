import os
import smtplib  # For sending emails
import imaplib  # For receiving emails
import email  # For processing email messages
from email.mime.multipart import MIMEMultipart  # For creating multipart email messages
from email.mime.text import MIMEText  # For creating plain text email messages
from email.mime.base import MIMEBase  # For creating base MIME types
from email import encoders  # For encoding attachments

def send_email(subject, body, attachment_path, config):
    # Set up the sender and recipient addresses
    from_addr = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')
    # Uncomment below if run locally with config.ini
    # from_addr = config['Email']['Email']
    to_addr = config['Email']['Recipient']

    # Create the email header
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    # Attach the file
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        msg.attach(part)
    # Set up the SMTP server through gmail and send the email
    server = smtplib.SMTP(config['Email']['SMTP_Server'], config['Email']['SMTP_Port'])
    server.starttls()
    # Uncomment below if run locally with config.ini
    # server.login(from_addr, config['Email']['Password'])
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def check_email_response(config):
    email = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')

    # Connect to the email server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    # mail.login(config['Email']['Email'], config['Email']['Password'])
    mail.login(email,password)
    mail.select('inbox')

    result, data = mail.search(None, '(UNSEEN)')
    mail_ids = data[0].split()
    print(f"Found {len(mail_ids)} unread emails.")
    # Process each unread email
    for mail_id in mail_ids:
        result, message_data = mail.fetch(mail_id, '(RFC822)')
        if result != 'OK':
            print(f"Error fetching email ID {mail_id}.")
            continue
        
        raw_email = message_data[0][1].decode('utf-8')
        msg = email.message_from_string(raw_email)
        from_address = email.utils.parseaddr(msg['From'])[1]
        # Check if the email is from the intended recipient
        if from_address == config['Email']['Recipient']:
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    # Get the body of the email and check the response
                    body = part.get_payload(decode=True).decode('utf-8').strip().split('\n')[0].strip().upper()
                    print(body)
                    if body == 'Y':
                        return True
                    elif body == 'N':
                        return False
    return None
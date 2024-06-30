import configparser
import datetime
import os
from posts import create_image
from quote import get_quote
from instagram_poster import post_to_instagram
from email_sender import send_email, check_email_response

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    while True:
        quote = get_quote()
        date_str = datetime.date.today().strftime('%Y-%m-%d')
        # image_path = f"/app/posts/{date}.jpeg"
        local_path = 'C:/Users/Steven/Documents/All things Code/Insta Poster/posts'
        image_path = os.path.join(local_path, f'{date_str}.jpeg')
        create_image(quote)
        send_email(
            subject="New Instagram Post Preview",
            body="Please review the attached image. Reply with 'Y' to post or 'N' to regenerate.",
            attachment_path=image_path,
            config=config
        )

        response = None
        while response is None:
            response = check_email_response(config)

        if response:
            post_to_instagram(image_path, config)
            print(f"Posted {image_path} to Instagram.")
            break
        else:
            print(f"Received 'N', regenerating image and sending email again.")

if __name__ == '__main__':
    main()
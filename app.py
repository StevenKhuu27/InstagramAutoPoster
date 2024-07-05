import configparser
import datetime
import os
import shutil
import time
from posts import create_image
from quote import get_quote
from instagram_poster import post_to_instagram
from email_sender import send_email, check_email_response

def main():
    # We store our SMTP variables in the config.ini. If run locally, I would store my password and email variables in here too.
    # Otherwise, store this within the Github Secrets: Repo > Settings > Secrets and variables > Actions > Repostiory secrets.
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Removing residual cookies folder that was preventing login errors
    workspace_path = "config"
    if os.path.exists(workspace_path):
        shutil.rmtree(workspace_path)

    while True:
        quote = get_quote()
        date_str = datetime.date.today().strftime('%Y-%m-%d')
        #Using this for Github Actions
        path = 'posts'
        # Using this for Local Run
        # path = 'C:/Users/Steven/Documents/All things Code/Insta Poster/posts'
        # Using this for DockerFile
        # path = '/app/posts'
        image_path = os.path.join(path, f'{date_str}.jpeg')
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
            try:
                post_to_instagram(image_path, config)
                print(f"Posted {image_path} to Instagram.")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(300)  # Sleep for 5 minutes before retrying
        # else:
        #     print(f"Received 'N', regenerating image and sending email again.")

if __name__ == '__main__':
    main()
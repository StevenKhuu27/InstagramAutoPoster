
from instabot import Bot
import datetime
import random
import os
import logging


def post_to_instagram(file_path, config):
    cookie = os.path.join('config', 'theyoungfrugal_uuid_and_cookie.json')
    if os.path.exists(cookie):
        os.remove(cookie)
    # Initialize the bot
    bot = Bot()

    # If run locally, use this and store username and password in the config.ini
    # username = config['Credentials']['Username']
    # password = config['Credentials']['Password']
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')

    if not username or not password:
        print("Credentials not found or there was an error reading the config file.")

    backoff_time = 60
    max_backoff_time = 3600
    login_success = False

    while not login_success:
        try:
            # Login to Instagram
            bot.login(username=username, password=password)
            login_success = True
        except Exception as e:
            print(f"Login Failed: {e}. Retrying in {backoff_time} seconds')
            time.sleep(backoff_time)
            backoff_time = min(backoff_time * 2, max_backoff_time)
        

    # Have a range of different quotes that are chosen randomly.
    caption = ["I always like to gain some inspiration from other successful people. Hopefully, these can bring guidance and keep you on the path of saving, investing, or whatever your goal may be.",
    "Finding inspiration in the wisdom of others is always uplifting. May these words guide you on your journey towards your financial goals.",
    "I find motivation in the successes of others. Let these quotes inspire and guide you in achieving your own dreams.",
    "Inspiration from others can often light the way. I hope these quotes help you stay focused on your path, whatever it may be.",
    "Learning from the wisdom of others is always a source of strength. May these words inspire you to keep pushing towards your financial aspirations.",
    "Gaining inspiration from successful people is always enlightening. I hope these quotes provide the guidance you need to stay on track with your goals.",
    "I love drawing inspiration from the success stories of others. Let these quotes encourage and guide you on your journey to financial success.",
    "Finding wisdom in the words of others is a true gift. May these quotes inspire and keep you moving towards your financial dreams.",
    "I often look to successful people for inspiration. Hopefully, these quotes will guide you and keep you motivated on your journey.",
    "The success of others can be incredibly inspiring. I hope these quotes offer guidance and help you stay focused on your path to achieving your goals."]  # Replace with your caption
    tags = text = '''
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -
    #invest #debtfree #inspiration #finance #saving #investing 
    #Wealthbuilding #financialfreedom #moneymanagement #goals
    '''
    # Lucky Dips a caption from the caption array and adds the tags.
    today_caption = caption[random.randint(0,9)] + tags
    # Uploads the photo
    backoff_timer = 60
    try:
        bot.upload_photo(file_path, caption=today_caption)
    except Exception as e:
        logging.error(f"Error uploading photo: {e}")
        time.sleep(backoff_timer)
        backoff_time = min(backoff_time * 2, max_backoff_time)

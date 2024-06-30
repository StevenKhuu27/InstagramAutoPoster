import configparser
from instabot import Bot
import datetime
import random
import os
import logging


def post_to_instagram(file_path, config):
    cookie = os.path.join('C:/Users/Steven/Documents/All things Code/Insta Poster/config', 'theyoungfrugal_uuid_and_cookie.json')
    if os.path.exists(cookie):
        os.remove(cookie)
    # Initialize the bot
    bot = Bot()

    # Read credentials from a config file
    # config = configparser.ConfigParser()
    # config.read('config.ini')

    username = config['Credentials']['Username']
    password = config['Credentials']['Password']

    if username and password:
        # Use credentials in your script
        print(f"Username: {username}, Password: {password}")
    else:
        print("Credentials not found or there was an error reading the config file.")
    # Login to Instagram

    bot.login(username=username, password=password)
    # date_str = datetime.date.today().strftime('%Y-%m-%d')
    # Upload an image
    # local_path = 'C:/Users/Steven/Documents/All things Code/Insta Poster/posts'
    # file_path = os.path.join(local_path, f'{date_str}.jpeg')
    # file_path = os.path.join('/app/posts', f'{date_str}.jpeg')
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

    today_caption = caption[random.randint(0,9)] + tags

    # bot.upload_photo(file_path, caption=today_caption)
    try:
        bot.upload_photo(file_path, caption=today_caption)
    except Exception as e:
        logging.error(f"Error uploading photo: {e}")

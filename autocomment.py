# Imports
import instabot
import schedule
import time
from datetime import datetime

# Importing Config

from config import USERNAME, PASSWORD, COMMENT, COMMENT_ON

# Initializing Bot Class And Logging in
bot = instabot.Bot()
bot.login(
    username=USERNAME,
    password=PASSWORD,
)


# Initializing some variables
now = datetime.now()
last_commented = ""


# Creating Comment Function
def comment_last_post(last_post, comment):
    global last_commented
    if last_post != last_commented:
        bot.comment(last_post, comment)
        last_commented = last_post
        print(now.strftime("%Y-%m-%d %H:%M:%S")+" - AutoCommenterLogs - SUCCESS - Just commented on "+bot.get_link_from_media_id(last_post))


# Getting the last post of the page
try:
    last_post = bot.get_user_medias(COMMENT_ON, is_comment=True)[0]
except IndexError:
    print(now.strftime("%Y-%m-%d %H:%M:%S") + " - AutoCommenterLogs - ERROR - Invalid account username")
    print(now.strftime("%Y-%m-%d %H:%M:%S") + " - AutoCommenter - QUIT - Quitting...")
    exit()
# Checks every 60 seconds if the account has a new post
schedule.every(60).seconds.do(comment_last_post, last_post, COMMENT)

# Scheduling task
while 1:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        exit()

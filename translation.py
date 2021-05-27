from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} , I'am a YouTube uploader bot with permanent thumbnail support.

<b>Only Channel Subscribers are allowed to use this bot 🔒</b>

<b>➡️  So Join @PyJeBots 🔑</b>

Made by ❤️ in 🇮🇳
"""
    HELP_TEXT = """
<b><u>Link to Media or File</u></b>
➠ Send a youtube video link for upload to telegram file or media.

<b><u>Set Thumbnail</u></b>
➠ Send a photo to make it as permanent thumbnail.

<b><u>Deleting Thumbnail</u></b>
➠ Send /delthumb to deleting thumbnail.

<b><u>Show Thumbnail</u></b>
➠ Send /showthumb to view custom thumbnail.

b><u>Important 📢</u></b>
➠ You Must Subscribe [PyJeBots©](https://t.me/PyJeBots)
"""
    ABOUT_TEXT = """
- **Bot :** `YouTube URL Uploader`
- **Creator :** [Jack](https://telegram.me/PyJeDeveloper)
- **Channel :** [PyJeBots](https://telegram.me/PyJeBots)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel 📢', url='https://telegram.me/PyJeBots'),
        InlineKeyboardButton('Feedback 🖨️', url='https://telegram.me/PyJeDeveloper')
        ],[
        InlineKeyboardButton('Help 🗣️', callback_data='help'),
        InlineKeyboardButton('About 📝', callback_data='about'),
        InlineKeyboardButton('Close ❌', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('About 📝', callback_data='about'),
        InlineKeyboardButton('Close ❌', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('Help 🗣️', callback_data='help'),
        InlineKeyboardButton('Close ❌', callback_data='close')
        ]]
    )
    BLOCK_LIST_TEXT = "This url is blocked so I can not upload this URL."
    FORMAT_SELECTION = """<b>Select the desired format📦:</b> <a href='{}'>file size might be approximate</a>
 
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>🖱️"
    BANNED_USER_TEXT = "<code>Your Access to the Bot is Denied ❌</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to Encrypt Your Videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>Downloading To My server 📥</code>"    
    UPLOAD_START = "<code>Uploading into Telegram 📤</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "✅Downloaded in {} seconds. \n✅Uploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> [PyJeBots©](https://t.me/PyJeBots)"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Went Wrong ❌ Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<b>I already told You that You cannot use this bot without Subscribing My Channel ❌ \n\n➡️  So Join @PyJeBots 🔑</b>"
    FREE_USER_LIMIT_Q_SZE = "<b>Sorry Dear 😔, Free users can only send 1 request per {} minutes. Please try again after {} seconds later.\n\nContact [Jack](https://t.me/PyJeDeveloper) For Upgrading Your Subscription 📦 </b> "

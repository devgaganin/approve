#Gagan Only

from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

teamspy=Client(
    "Auto Approved Bot",
    bot_token = environ["6941701784:AAGToFyQaFMdtRH7QlPWOqZKO9rAO4mWigw"],
    api_id = int(environ["24490919"]),
    api_hash = environ["d1b3b15126c47dd4cb491553ee1db910"]
)

CHAT_ID = [int(teamspy) for teamspy in environ.get("CHAT_ID", '-1001938200996').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nTeam SPY")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@teamspy.on_message(filters.private & filters.command(["start"]))
async def start(client: teamspy, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("📦 Repo", url="https://github.com/amthespy/approve/"), InlineKeyboardButton("Updates 📢", url="https://t.me/+W7557it1iB9kMDU1") ],
              [ InlineKeyboardButton("➕️ Add Me To Your Chat ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"**__Hello {message.from_user.mention} I am Auto Approver Join Request Bot designed and maintained by Team SPY Just [Add Me To Your Group Channnl](http://t.me/{approvedbot.username}?startgroup=botstart) || Repo https://https://github.com/amthespy/approve/||**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@teamspy.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: teamspy, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
    #   print("Welcome....")

print("Auto Approved Bot")
teamspy.run()

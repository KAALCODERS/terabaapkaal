import os
import asyncio
import sys
import git
import heroku3
from OfficialSameer import SAM, SAM2, SAM3, SAM4, SAM5 , SAM6, SAM7, SAM8, SAM9, SAM10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, deadlyversion
from OfficialSameer import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from OfficialSameer import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

SAM_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/13bccc62e5a1531ed8988.jpg"
  

DEADLY = "✯ 𝙆𝘼𝘼𝙇 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **𝙆𝘼𝘼𝙇𝘽𝙊𝙏 ᴠᴇʀsɪᴏɴ**  : `{kaalbotversion}`\n"
DEADLY += f"═══════════════════\n\n"   

                                  
@SAM.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await SAM.send_file(event.chat_id,
                                  SAM_PIC,
                                  caption=deadly,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/KAAL_NETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/HEAVEN_ARMY")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/GARWMISHRA/TERABAAPKAAL")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"😁 🇵 🇴 🇳 🇬 !\n\n♡︎ `{ms}` 𝗺𝘀 ♡︎")
        
        

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**𝙍𝙀𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂 𝙔𝙊𝙐𝙍 𝙆𝘼𝘼𝙇 𝙐𝙎𝙀𝙍𝘽𝙊𝙏𝙎**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await SAM.disconnect()
        except Exception:
            pass
        try:
            await SAM2.disconnect()
        except Exception:
            pass
        try:
            await SAM3.disconnect()
        except Exception:
            pass
        try:
            await SAM4.disconnect()
        except Exception:
            pass
        try:
            await SAM5.disconnect()
        except Exception:
            pass
        try:
            await SAM6.disconnect()
        except Exception:
            pass
        try:
            await SAM7.disconnect()
        except Exception:
            pass
        try:
            await SAM8.disconnect()
        except Exception:
            pass
        try:
            await SAM9.disconnect()
        except Exception:
            pass
        try:
            await SAM10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        DEADLY = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[DEADLY] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target

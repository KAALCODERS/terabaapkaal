import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import SAM, SAM2, SAM3, SAM4, SAM5, SAM6, SAM7, SAM8, SAM9, SAM10, ALIVE_PIC, OWNER_ID

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/be526220ab16ee5504652.jpg"

Deadly_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/kaal_network")
        ],
        [
        Button.url("• ᴄᴍᴅs •", "https://t.me/its_heaven_king")
        ]
        ]
               
DeadlyX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/kaal_network"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/heaven_army")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/garwmishra/terabaapkaal")
        ]
        ]
        
        
#USERS 


@SAM.on(events.NewMessage(pattern="/start"))
@SAM2.on(events.NewMessage(pattern="/start"))
@SAM3.on(events.NewMessage(pattern="/start"))
@SAM4.on(events.NewMessage(pattern="/start"))
@SAM5.on(events.NewMessage(pattern="/start"))
@SAM6.on(events.NewMessage(pattern="/start"))
@SAM7.on(events.NewMessage(pattern="/start"))
@SAM7.on(events.NewMessage(pattern="/start"))
@SAM8.on(events.NewMessage(pattern="/start"))
@SAM9.on(events.NewMessage(pattern="/start"))
@SAM10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DeadlyBot = await event.client.get_me()
       bot_id = DeadlyBot.first_name
       bot_username = DeadlyBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheDeadly = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Kaal Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own kaal Spam Bots You Can Deploy From Button Below.** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=ownermsg, 
                  buttons=Deadly_Button)
       else:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=usermsg, 
                  buttons=DeadlyX_Button)
                

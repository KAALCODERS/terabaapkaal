from OfficialSameer import SAM, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from OfficialSameer import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/be526220ab16ee5504652.jpg"

SAM_Help = "🔥 𝙆𝘼𝘼𝙇 𝙎𝙋𝘼𝙈 𝘽𝙊𝙏 🔥\n\n"
 
SAM_Help += f"_ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ 𝙆𝘼𝘼𝙇 𝙎𝙋𝘼𝙈__\n\n"

SAM_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

SAM_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots \n `.addecho` - to addecho \n `.rmecho` - To remove Echo \n `.addsudo` - To add sudo user using spam bot \n\n"
 
SAM_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

SAM_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
SAM_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

SAM_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n `.pornspam` - this cmd is use for porn spam\n\n"

SAM_Help += f"© @KAAL_NETWORK\n"


@SAM.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await SAM.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=SAM_Help,
                                  buttons=[
        [
        Button.url("ᴀʟʟ ᴄᴍᴅs", "ITS_HEAVEN_KING")
        ],
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/KAAL_NETWORK")
        ] 
        ]
        )                                                         

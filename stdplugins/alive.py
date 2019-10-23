""".alive Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions =       "i am ON My Mastor \n\n"
                     " \n\n"
                     "botdo is ON \n\n"
                     f"Telethon version: {version.__version__} \n"
                     f"Python: {python_version()} \n"
                     f"--------------------------- \n"
                     f"User: {DEFAULTUSER} \n"
                     " \n\n"
                     f"Creator: Mayur Karaniya \n"
                     " \n\n"
                     f"Owner: 3Cube TeKnoways \n"
                     " \n\n"
                     f"Userbot: testuserbot "
                     f" \n\n"
                     f"Database Status: Telegram Databases functioning normally!`"
                    
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

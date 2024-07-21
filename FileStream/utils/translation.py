from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 Hᴇʏ, </b>{}\n
<b> ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴍᴇᴅɪᴀ ᴛᴏ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.

📝 Rᴇᴀᴅ Mʏ Fᴇᴀᴛᴜʀᴇs 👇
● ɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ʜɪɢʜ sᴘᴇᴇᴅ ᴍᴇᴅɪᴀ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ.
● ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴅɪʀᴇᴄᴛ sᴛʀᴇᴀᴍ (ᴡᴀᴛᴄʜɪɴɢ ᴠɪᴅᴇᴏ ᴡɪᴛʜᴏᴜᴛ ᴅᴏᴡɴʟᴏᴀᴅ) ʟɪɴᴋ
● sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴍᴇᴅɪᴀ/ᴅᴏᴄᴜᴍᴇɴᴛs/ᴠɪᴅᴇᴏ ᴇᴛᴄ.. ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ
● ᴍʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʟɪɴᴋ ᴡɪʟʟ sᴜᴘᴘᴏʀᴛ ʏᴏᴜʀ ʙʀᴏᴡsᴇʀ (ɢᴏᴏɢʟᴇ ᴄʜʀᴏᴍᴇ, ʙʀᴀᴠᴇ, ᴏᴘᴇʀᴀ, sᴀғᴀʀɪ)
● ʟɪɴᴋ ᴡᴏɴ'ᴛ ᴇxᴘɪʀᴇ ᴛɪʟʟ ᴍʏ ᴀᴅᴍɪɴ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ꜰɪʟᴇ
❗Nᴏᴛᴇ: Gᴇɴᴇʀᴀᴛɪɴɢ Lɪɴᴋ Oғ Aᴅᴜʟᴛ Oʀ Pᴏʀɴᴏɢʀᴀᴘʜɪᴄ Cᴏɴᴛᴇɴᴛ Usɪɴɢ Tʜɪs Bᴏᴛ Is  Sᴛʀɪᴄᴛʟʏ Pʀᴏʜɪʙɪᴛᴇᴅ 🚫 Iғ Yᴏᴜ'ʟʟ Dᴏ Yᴏᴜ Wɪʟʟ Bᴇ Bᴀɴɴᴇᴅ.

ᴘʟᴇᴀsᴇ sʜᴀʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ ᴜs❤️
🍁 Bᴏᴛ Bʏ @MisterBrutal </b>"""

    HELP_TEXT = """
<b>- ᴀᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ᴏɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ</b>
<b>- sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴍᴇᴅɪᴀ</b>
<b>- ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ</b>\n

<i><b> Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ <a href='https://Instagram.com/mrbrutal_141'>Bʀᴜᴛᴀʟ 😎</a></b></i>
🦋 Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ @Ig_1Venom"""

    ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : {}</b>\n
<b>✦ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ : <a href='https://Instagram.com/mrbrutal_141' >Bʀᴜᴛᴀʟ 😎</a></b>
<b>✦ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://telegram.me/Ig_1Venom'>Bʀᴜᴛᴀʟ 😎</a></b>\n

🦋 Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ @Ig_1Venom
"""

    STREAM_TEXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>📺 Wᴀᴛᴄʜ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""


    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[  InlineKeyboardButton('🔥 ʙᴏᴛꜱ ᴄʜᴀɴɴᴇʟ ', url=f'https://t.me/MisterBrutal'),
            InlineKeyboardButton('🦋 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ', url=f'https://t.me/Brutal_Support')
        ],[
            InlineKeyboardButton('🍁 ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('📝 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
            InlineKeyboardButton("🦋 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🌿 ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ & ꜰᴇᴇᴅʙᴀᴄᴋ', url=f'https://t.me/Brutal_Support')
        ],[  
            InlineKeyboardButton('🔥 ʙᴏᴛꜱ ᴄʜᴀɴɴᴇʟ ', url=f'https://t.me/MisterBrutal'),
            InlineKeyboardButton('🦋 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ', url=f'https://t.me/Brutal_Support')
        ],[
            InlineKeyboardButton('🏠 ʜᴏᴍᴇ', url=f'https://t.me/'),
            InlineKeyboardButton('📝 ᴀʙᴏᴜᴛ', callback_data='about')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔥 ʙᴏᴛꜱ ᴄʜᴀɴɴᴇʟ ', url=f'https://t.me/MisterBrutal'),
            InlineKeyboardButton('🦋 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ', url=f'https://t.me/Brutal_Support')
        ][  
            InlineKeyboardButton('🍁 ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('🌿 ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ', url=f'https://instagram.com/mrbrutal_141')
        ],[
            InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='home')
        ]]
    )

from pyrogram import Client, filters 

@Client.on_message(filters.private & filters.command('get_media'))
async def get_media(bot, message):
  

# Respondendo com arquivos de mídia...
from pyrogram import Client, filters

app = Client(
    'tesoubot_app'
)

@app.on_message(filters.command('photo'))
async def photo(client, message):
    await app.send_photo( # não usa mais o Reply nesse caso
        message.chat.id,  # ID do chat, por ex: '459457431'  + link da foto
        'https://images.pexels.com/photos/12641780/pexels-photo-12641780.jpeg?cs=srgb&dl=pexels-stayhereforu-12641780.jpg&fm=jpg'
    )

@app.on_message(filters.sticker)
async def sticker(client, message):
    await app.send_sticker( # não usa mais o Reply nesse caso
        message.chat.id, # ID do chat, por ex: '459457431' 
        message.sticker.file_id  # ID do sticker
    )
    
app.run() # executa

# para conferir outros sends:
"https://docs.pyrogram.org/api/methods/#messages"
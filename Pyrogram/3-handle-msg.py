# Lindando com mensagens
from pyrogram import Client

app = Client(
    'tesoubot_app'
)

# função assíncrona
@app.on_message() # quando receber uma mensagem...
async def resposta(client, message): 
    print(message.chat.username, message.text) #Pessoa, oq a pessoa diz ao bot
    await message.reply('me sorry yo no hablo tu language D:') # resposta do bot

app.run() # executa
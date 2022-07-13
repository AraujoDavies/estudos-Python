# Usando os Filtros para ajudar o bot entender
from pyrogram import Client, filters

app = Client(
    'tesoubot_app'
)


# 4 Existem milhares de filtros confere ai:
"https://docs.pyrogram.org/api/filters#module-pyrogram.filters"

@app.on_message(filters.sticker) # Sticker
async def resposta(client, message): 
    await message.reply(f'opa, {message.chat.username} Gostei da figurinha AHAHAHHAHAHAHA') # resposta do bot



# 4.1 Filtros podem ter operadores: 
"""
E &
OU |
Não ~

~filter.text => msgs q não sejam de text
"""
@app.on_message(filters.photo | filters.video) # Foto ou video
async def resposta(client, message): 
    await message.reply(f'opa, {message.chat.username} q foto horrorosa') # resposta do bot




# 4.2 A Ordem dos Handlers importa... se colocar a msg genérica na frente o filters não vai funcionar, raciocine!!
@app.on_message(filters.command('futebol')) # MSG COM FILTRO /FUTEBOL
async def resposta(client, message): 
    print(message.chat.username, message.text) #Pessoa, oq a pessoa diz ao bot
    await message.reply(f'opa, {message.chat.username} segue a lista com os **melhores jogos da semana**') # resposta do bot

@app.on_message() # MSG GENÉRICA
async def resposta(client, message): 
    print(message.chat.username, message.text) #Pessoa, oq a pessoa diz ao bot
    await message.reply('me sorry yo no hablo tu language D:') # resposta do bot

app.run() # executa
# PASSANDO CHAVES DO TELEGRAM
from pyrogram import Client

app = Client(
    'tesoubot_app', # App title
    api_id='ID', # info q nao pode ser repassada
    api_hash='HASH', # info q nao pode ser repassada
    bot_token='Falar com o BOTFATHER' # pega com o botfather
)

# APÓS COLOCAR ESSES DADOS ELE GERA UM ARQUIVO 'nome_bot.session'
# esse arquivo armazena as credenciais acima e entao pode apaga-las
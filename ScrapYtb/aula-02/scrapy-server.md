# Dicas para evitar erros e para não forçar o servidor:

**Mudar robots.txt rules para FALSE**
Obey robots.txt rules
ROBOTSTXT_OBEY = True (Vira False)
-- evita esbarrar no robots.txt --

**alterar UserAgent**
#USER_AGENT = 'mercado_livre (+http://www.yourdomain.com)' 
vira:
#USER_AGENT = 'My User agent como sei meu userAgent ? (google)'
-- me idenfiticando para o site q não aceita um agent invalido --

**mudar AUTOTHROTTLE_ENABLED para True**
#AUTOTHROTTLE_ENABLED = True
vira
AUTOTHROTTLE_ENABLED = True
--não agredir o servidor--
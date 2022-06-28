Criando ambiente virtual para as libs de PYTHON(é melhor do que instalar ele global) no Windows: 

step 1: navegar até a pasta do projeto
step 2: Liberar a política de execução de scripts com o seguinte comando: "Set-ExecutionPolicy AllSigned"
setp 3: Criar o ambiente virtual: "python -m venv pasteName"
step 4: Ativa o ambiente virtual com o seguinte comando: "pasteName\Scripts\activate"
step 5: Instalar Scrap 'pip install scrapy'
step 6: criar pasta do framework 'scrapy startproject pasteName' (segue o terminal)

obs: 
-"python 'localArquivo'" para rodar o script
- **digite scrapy no terminal para ver os comandos e a descrição**
-'scrapy shell '\URL(facultativo)' para rodar o script em modo interativo
- extensão selectorGadget ajuda a encontrar itens por css_selector
- scrapy runspider 'diretório/' -s HTTPCACHE_ENABLED=1 **salva requisições em cache** 

crawl só funciona na pasta do projeto:
-'scrapy crawl nomeProjeto' rodar o arquivo
-'scrapy crawl nomeProjeto -o novoArquivo.extensão(csv, json)' add informação ao arquivo  
-'scrapy crawl nomeProjeto -O novoArquivo.extensão(csv, json)' cria novo arquivo
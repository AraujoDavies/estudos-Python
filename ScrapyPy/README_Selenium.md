Criando ambiente virtual para o Selenium(é melhor do que instalar ele global) no Windows: 

step 1: navegar até a pasta do projeto
step 2: Liberar a política de execução de scripts com o seguinte comando: "Set-ExecutionPolicy AllSigned"
setp 3: Criar o ambiente virtual: "python -m venv pasteName"
step 4: Ativa o ambiente virtual com o seguinte comando: "pasteName\Scripts\activate"
step 5: instalar o Selenium "pip install selenium"

obs: 
-"python -m selenium" verifica se está rodando
-"python 'localArquivo'" para rodar o script
-"python -i 'nameArquivo'" para rodar o script em modo interativo

LEIA: 
https://penseallen.github.io/PensePython2e/
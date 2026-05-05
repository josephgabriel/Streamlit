Como Executar o Projeto

Siga os passos abaixo para clonar este repositório e configurar o ambiente em sua máquina local.
```bash
### 1. Clone o repositório

Abra seu terminal e execute o comando para fazer uma cópia do projeto:

git clone https://github.com/josephgabriel/Streamlit.git

2. Acesse a pasta do projeto
Navegue até o diretório que foi criado:

cd Streamlit

3. Crie e ative o ambiente virtual
Para isolar as dependências do projeto, crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual:

Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

4. Instale as dependências
Com o ambiente virtual ativado, instale todas as bibliotecas listadas no arquivo requirements.txt:

pip install -r requirements.txt

5. Execute a aplicação
Após a instalação das dependências, inicie a aplicação Streamlit:

streamlit run app.py

Substitua app.py pelo nome do arquivo principal da sua aplicação, se for diferente.

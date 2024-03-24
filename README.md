# Projeto CRUD de Cadastro de Personagens de Harry Potter

<div align="center">
    <img src="./static/img/Captura de tela 2023-11-20 201203.png" width="600px">
</div>

<div align="center">
    <img src="./static/img/Captura de tela 2023-11-20 201231.png" width="600px">
</div>

<div align="center">
    <img src="./static/img/Captura de tela 2023-11-20 201245.png" width="600px">
</div>

### Descrição do Projeto
Este projeto consiste em uma aplicação CRUD (Create, Read, Update, Delete) para o cadastro de personagens com a temática de Harry Potter. A aplicação permite que os usuários realizem operações básicas de manipulação de dados, como criar novos personagens, visualizar informações existentes, atualizar dados e deletar registros.

### Tecnologias Utilizadas
- HTML
- CSS
- Bootstrap
- JavaScript
- Python
- Flask
- SQLite (Banco de dados)

### Estrutura do Projeto

1 - app: Contém os arquivos da aplicação Flask.

- static: Armazena arquivos estáticos como folhas de estilo CSS e scripts JavaScript.
- templates: Contém os arquivos HTML para renderização das páginas.
- app.py: Arquivo principal que define a lógica da aplicação.

2 - database: Armazena o arquivo do banco de dados SQLite.

3 - venv: Ambiente virtual para isolar as dependências do projeto.

4 - .gitignore: Lista de arquivos e pastas a serem ignorados pelo Git.

5 - README.md: Este arquivo, fornecendo informações sobre o projeto.

6 - requirements.txt: Lista de dependências do Python necessárias para o projeto.

### Configuração do Ambiente
1: Clone o repositório para sua máquina local:
```sh
git clone https://github.com/alissonwr/crud_harrypotter.git
```
2: Crie e ative o ambiente virtual:
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
./venv/Scripts/activate   # Windows
```
3: Instale as dependências do projeto:
```sh
pip install -r requirements.txt
```
4: Execute a aplicação:
```sh
python app/app.py
```
Acesse a aplicação em http://127.0.0.1:5000/ em seu navegador.

### Funcionalidades da Aplicação
- Listar Personagens: Visualize todos os personagens cadastrados.
- Cadastrar Novo Personagem: Adicione novos personagens à base de dados.
- Atualizar Informações: Modifique os detalhes de um personagem existente.
- Deletar Personagem: Remova um personagem da base de dados.

### Contribuições
- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.

### Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

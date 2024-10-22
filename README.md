# Livrobox

Livrobox é um aplicativo web desenvolvido em Django para gerenciar uma coleção de livros. Com ele, os usuários podem adicionar, visualizar e organizar informações sobre seus livros favoritos.

## Funcionalidades

- Adicionar novos livros à coleção
- Visualizar detalhes dos livros
- Listar todos os livros cadastrados
- Interface amigável e responsiva

## Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **Django**: Framework web
- **HTML/CSS**: Estrutura e estilo da aplicação
- **SQLite**: Banco de dados (pode ser alterado para outro, se desejado)

## Instalação

Para executar o Livrobox em sua máquina local, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/jvdellolio/Livrobox.git
   cd Livrobox
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv env
   ```
   ```bash
   source env/bin/activate  # Para Linux/Mac
   env\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. Acesse o aplicativo no navegador:
   ```bash
   http://127.0.0.1:8000/
   ```

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga estas etapas:

1. **Fork o projeto**:
   - Acesse a página do repositório [Livrobox](https://github.com/jvdellolio/Livrobox).
   - Clique no botão **Fork** no canto superior direito da página.
   - Escolha onde deseja criar o fork (na sua conta pessoal ou em uma organização, se aplicável).

2. **Clone o seu fork**:
   - Após o fork ser criado, vá para o seu repositório forked.
   - Clique no botão **Code** e copie o URL (HTTPS ou SSH).
   - Execute o seguinte comando no terminal:
     ```bash
     git clone https://github.com/seu-usuario/Livrobox.git
     ```
     (Substitua `seu-usuario` pelo seu nome de usuário do GitHub.)

3. **Crie uma nova branch**:
   ```bash
   git checkout -b feature/nome-da-feature
   ```

4. **Faça suas alterações e commit**:
   ```bash
   git commit -m 'Adiciona nova feature'
   ```

5. **Faça push para a branch**:
   ```bash
   git push origin feature/nome-da-feature
   ```

6. **Abra um Pull Request**:
   - Vá para a página do seu repositório forked no GitHub.
   - Clique no botão **Compare & pull request**.
   - Descreva suas alterações e clique em **Create pull request**.



## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

João Vitor Lima Dell'Olio - [jvdellolio](https://github.com/jvdellolio)

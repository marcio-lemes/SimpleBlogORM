## **Gerenciamento de Blog com SQLAlchemy e PostgreSQL**  
Este projeto é um sistema de blog simples que utiliza **SQLAlchemy** como ORM (Object-Relational Mapping) para interagir com um banco de dados **PostgreSQL**. Ele permite a criação de usuários, a publicação de posts e a consulta de posts associados a cada usuário. O projeto foi desenvolvido para demonstrar o uso de ORMs em Python e a integração com bancos de dados relacionais.

---

## **Funcionalidades**  
- **Cadastro de Usuários**: Adiciona novos usuários ao banco de dados.  
- **Publicação de Posts**: Permite que usuários cadastrados publiquem posts.  
- **Consulta de Dados**: Exibe todos os usuários e seus respectivos posts.  
- **Validação de E-mail**: Verifica se o e-mail fornecido é válido.  
- **Relacionamento entre Tabelas**: Usuários e Posts são relacionados através de chaves estrangeiras.  

---

## **Tecnologias e Habilidades Utilizadas**
- Linguagem: Python
- ORM: SQLAlchemy
- Banco de Dados: PostgreSQL
- Bibliotecas:
    - SQLAlchemy: Para mapeamento objeto-relacional e gerenciamento de sessões.
- Habilidades:
    - Modelagem de banco de dados.
    - Uso de ORMs para abstrair operações SQL.
    - Validação de dados e tratamento de exceções.

---

## **Requisitos**  
Para executar este projeto, você precisará ter instalado:  
- Python 3.x  
- Biblioteca `SQLAlchemy` (`pip install sqlalchemy`)  
- PostgreSQL rodando localmente.  

---

## **Como Usar**  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/blog-sqlalchemy.git

2. Instale as dependências:  
   ```bash
   pip install sqlalchemy

3. Configure o banco de dados PostgreSQL:
- Crie um banco de dados chamado **blog**;
- Atualize as credenciais no arquivo **conexao_orm.py**.

4. Execute o script principal:
    ```bash
   python App_blog.py

---

## **Estrutura do Projeto**
### **Arquivos Principais**
- conexao_orm.py: Configura a conexão com o banco de dados e define a base para os modelos.
- user.py: Define a classe User, que representa a tabela de usuários.
- post.py: Define a classe Post, que representa a tabela de posts.
- blog.py: Contém a lógica do blog, incluindo funções para adicionar usuários, posts e consultar dados.
- App_blog.py: Script principal que inicia a aplicação e exibe o menu interativo.

---

## **Contato**
- Márcio Simões Lemes
- GitHub: marcio-lemes
- Email: devmarciolemes@gmail.com
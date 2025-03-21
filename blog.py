from sqlalchemy.exc import IntegrityError
from conexao_orm import Base, engine, session
from user import User
from post import Post
import re

#Cria as tabelas
Base.metadata.create_all(engine)

#Função para validar email
def is_email_valid(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

#Função para exibir o menu de opções
def show_menu():
    print("Menu de opções:")
    print("1. Adicionar Usuário")
    print("2. Adicionar Post")
    print("3. Consultar Usuários e seus Posts")
    print("4. Sair")
    
#Função para adicionar usuário
def add_user():
    print("Adicionar novo usuário")
    name = input("Nome:\n")
    if not name:
        print("O nome não pode ser vazio")
        return
    email = input("Email:\n")
    if not is_email_valid(email):
        print("Erro: E-mail inválido.")
        return
    user = User(name, email) #Instancia a classe User que criamos com os atributos passados pelo usuário
    try:
        session.add(user) #Adiciona o usuário no banco de dados (sem comandos SQL)
        session.commit() #Realiza a mudança
        print("Usuário adicionado com sucesso!")
    except IntegrityError:
        session.rollback()
        print("Erro: E-mail já cadastrado")
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar usuário: {e}")


#Função para adicionar post  
def add_post():
    print("Adicionar novo post:")
    title = input("Título:\n")
    content = input("Conteúdo:\n")
    author_id = input("Id do Autor:\n")
    try:
        user = session.query(User).filter_by(id=author_id).first() #Verifica na tabela se o id passado pelo usuário em author_id existe
        if user:
            post = Post(title=title, content=content, author=user)
            session.add(post)
            session.commit()
            print("Post adicionado com sucesso!")
        else:
            print("Usuário não encontrado.")
    except Exception as e:
        print(f"Erro ao adicionar post: {e}")
        
#Função para consultar usuários e posts
def query_users_posts():
    try:
        users = session.query(User).join(User.posts).order_by(User.name).all() #Realiza uma consulta na tabela "User", faz a junção com a tabela posts pelo relacionamento que existe na tabela "User" (User.posts), ordena pelo nome e por fim, solicita o retorno de todos os resultados (.all()) 
        for user in users:
            print(f"User: {user.name}, Email: {user.email}")
            for post in user.posts:
                print(f"Post: {post.title}, Conteúdo: {post.content}")
    except Exception as e:
        print(f"Erro ao consultar usuários e posts: {e}")
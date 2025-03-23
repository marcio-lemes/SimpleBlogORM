from sqlalchemy.exc import IntegrityError
from conexao_orm import Base, engine, session
from user import User
from post import Post
import re

#Cria as tabelas
Base.metadata.create_all(engine)

#Função para validar email
def is_email_valid(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" #Define o "padrão" obrigatório que um email tem que ter
    return re.match(pattern, email) #Retorna se o email inserido como parâmetro está dentro do padrão (True/False)

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
    name = input("Nome:\n") #Pede para o usuário o nome do novo usuário
    if not name: #Valida se o nome não está vazio
        print("O nome não pode ser vazio")
        return
    email = input("Email:\n") #Pede para o usuário o novo email
    if not is_email_valid(email): #Usa a função de validar o email e se tiver dado False, retorna a mensagem de erro
        print("Erro: E-mail inválido.")
        return
    user = User(name, email) #Instancia a classe User que criamos com os atributos passados pelo usuário
    try:
        session.add(user) #Adiciona o usuário no banco de dados (sem comandos SQL)
        session.commit() #Realiza a mudança
        print("Usuário adicionado com sucesso!")
    except IntegrityError: #Caso haja algum erro de integridade na tentativa de adicionar o usuário
        session.rollback() #Reverte toda a operação
        print("Erro: E-mail já cadastrado")
    except Exception as e:
        session.rollback() #Reverte toda a operação
        print(f"Erro ao adicionar usuário: {e}")


#Função para adicionar post  
def add_post():
    print("Adicionar novo post:")
    title = input("Título:\n") #Pede para o usuário digitar o título do post
    content = input("Conteúdo:\n") #Pede para o usuário digitar o conteúdo do post
    if not title.strip() or not content.strip(): #Valida se o título ou o conteúdo estão vazios
        print("Erro: Título e Conteúdo não podem estar vazios.")
        return
    author_id = input("Id do Autor:\n") #Pede para o usuário digitar o ID do autor
    if not author_id.isdigit(): #Valida se o que foi digitado é um número
        print("O ID do autor deve ser um número.")
        return
    try:
        user = session.query(User).filter_by(id=author_id).first() #Pesquisa na tabela de usuários o autor que tem o ID que foi passado pelo usuário
        if user: #Valida se o autor existe, se existir:
            post = Post(title=title, content=content, author=user) #Cria um objeto da classe Post, com os atributos que foram passados pelo usuário
            session.add(post) #Adiciona o Post no banco de dados
            session.commit() #Realiza a mudança
            print("Post adicionado com sucesso!")
        else: #Se não foi encontrado nenhum autor com esse ID:
            print("Usuário não encontrado.")
    except Exception as e:
        print(f"Erro ao adicionar post: {e}")
        
#Função para consultar usuários e posts
def query_users_posts():
    try:
        users = session.query(User).join(User.posts).order_by(User.name).all() #Realiza uma consulta na tabela "User", faz a junção com a tabela posts pelo relacionamento que existe na tabela "User" (User.posts), ordena pelo nome e por fim, solicita o retorno de todos os resultados (.all()) 
        for user in users: #Itera sobre a lista de usuários
            print(f"User: {user.name}, Email: {user.email}")
            for post in user.posts: #Itera sobre a lista de posts do usuário da vez
                print(f"Post: {post.title}, Conteúdo: {post.content}")
    except Exception as e:
        print(f"Erro ao consultar usuários e posts: {e}")
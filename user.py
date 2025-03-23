from conexao_orm import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users' #Define o nome da tabela
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    posts = relationship('Post', back_populates='author') #Relacionamento com a classe "Post". 'back_populates=author' indica que a classe "Post" terá um atributo chamado 'author' que se relaciona com esta classe 'User'
    
    def __init__(self, name, email): #Método construtor, faz com que esses atributos (name, email) devam ser passados como parâmetro na hora da criação do objeto dessa classe
        self.name = name
        self.email = email
from conexao_orm import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id')) #Relaciona o post com o seu autor
    author = relationship('User', back_populates='posts') #Relacionamento com a classe "User". 'back_populates=posts' indica que a classe "User" terá um atributo chamado 'posts' que se relaciona com esta classe "Post"    
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Fornecedor(Base):
    __tablename__ = 'fornecedor'

    id = Column("pk_fornecedor", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    descricao = Column(String(4000))
    telefone = Column(String(15))
    categoria = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, descricao:str, telefone:str,
                 categoria: str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Fornecedor

        Arguments:
            nome: nome do fornecedor.
            descricao: descrição do fornecedor.
            telefone: contato do fornecedor
            categoria: identifica a categoria do fornecedor
            data_insercao: data de quando o fornecedor foi inserido à base
        """
        self.nome = nome
        self.descricao = descricao
        self.telefone = telefone
        self.categoria = categoria
        if data_insercao:
            self.data_insercao = data_insercao

from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base 


class Material(Base):
    __tablename__ = 'material'

    id = Column("pk_material", Integer, primary_key=True)
    nome = Column(String(50))
    quantidade = Column(Integer)
    custo = Column(Float)
    nf = Column(String(20))
    data_aquisicao = Column(DateTime, default=datetime.now())
    
  
    def __init__(self, nome:str, quantidade:int, custo:float, nf:str, data_aquisicao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: nome do material.
            quantidade: quantidade de itens em estoque
            custo: preço de custo do material
            data_aquisicao: data de aquisição do produto
            nf: guarda o número da nota fical
        """
        self.nome = nome
        self.quantidade = quantidade
        self.custo = custo
        self.nf = nf

        # se não for informada, será o data exata da inserção no banco
        if data_aquisicao:
            self.data_aquisicao = data_aquisicao

   


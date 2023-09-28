from pydantic import BaseModel
from typing import Optional, List
from model.material import Material


class MaterialSchema(BaseModel):
    """ Define como um novo material a ser inserido deve ser representado
    """
    nome: str = "Tijolo"
    quantidade: int = 12
    custo: float = 12.50
    nf: str = "005030358-1"


class MaterialBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Será feita apenas com base no nome do material.
    """
    nome: str = "Tijolo"


class ListagemMateriaisSchema(BaseModel):
    """ Define como uma listagem de materiais será retornada.
    """
    materiais:List[MaterialSchema]


def apresenta_materiais(materiais: List[Material]):
    """ Retorna uma representação do material seguindo o schema definido em
        MaterialViewSchema.
    """
    result = []
    for material in materiais:
        result.append({
            "nome": material.nome,
            "quantidade": material.quantidade,
            "custo": material.custo,
            "nf": material.nf
        })

    return {"materiais": result}


class MaterialViewSchema(BaseModel):
    """ Define como um material será retornado.
    """
    id: int = 1
    nome: str = "Tijolo"
    quantidade: int = 12
    custo: float = 12.50
    nf: str = ""


class MaterialDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    menssagem: str
    nome: str

def apresenta_material(material: Material):
    """ Retorna uma representação do material seguindo o schema definido em
        MaterialViewSchema.
    """
    return {
        "id": material.id,
        "nome": material.nome,
        "quantidade": material.quantidade,
        "custo": material.custo,
        "nf": material.nf
    }

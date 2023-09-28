from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List


class FornecedorSchema(BaseModel):
    nome: str = "Telhas LTDA"
    descricao: Optional[str] = "Trabalha apenas com Telhas. "
    categoria: str = "Telhado"
    telefone: str = "(61 99000-0000)"


class FornecedorBuscaSchema(BaseModel):
    id: Optional[int] = 1
    nome: Optional[str] = "Telhas LTDA"


class FornecedorViewSchema(BaseModel):
    id: int = 1
    nome: str = "Telhas LTDA"
    descricao: Optional[str] = "Trabalha apenas com Telhas. "
    categoria: str = "Telhado"
    telefone: str = "(61 99000-0000)"
    total_cometarios: int = 1
    nota_media: int = 0


class FornecedorDelSchema(BaseModel):
    mesage: str
    id: int

def apresenta_fornecedor(fornecedor):
    nota_media = 0
     
    return {
        "id": fornecedor.id,
        "nome": fornecedor.nome,
        "categoria": fornecedor.categoria,
        "descricao": fornecedor.descricao,
        "telefone": str(fornecedor.telefone),
        "nota_media": nota_media,
    }


class FornecedorListaViewSchema(BaseModel):
    fornecedores: List[FornecedorViewSchema]


def apresenta_lista_fornecedor(fornecedores):
    result = []
    for fornecedor in fornecedores:
        result.append(apresenta_fornecedor(fornecedor))
    return {"fornecedores": result}

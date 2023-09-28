from email.mime import base
from sqlalchemy.exc import IntegrityError

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask_cors import CORS
from flask import redirect
from model import Session, Fornecedor
from logger import logger
from schemas import *


info = Info(title="API microserviço", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
fornecedor_tag = Tag(name="Fornecedor", description="Adição, visualização e remoção de fornecedores à base")


@app.get('/')
def home():
    return redirect('/openapi')


@app.post('/fornecedor', tags=[fornecedor_tag],
          responses={"200": FornecedorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_fornecedor(form: FornecedorSchema):
    """Adiciona um novo Fornecedor à base de dados

    Retorna uma representação dos fornecedores.
    """
    session = Session()
    fornecedor = Fornecedor(
        nome=form.nome,
        descricao=form.descricao,
        telefone=form.telefone,
        categoria=form.categoria
        )
    logger.debug(f"Adicionando fornecedor de nome: '{fornecedor.nome}'")
    try:
        # adicionando fornecedor
        session.add(fornecedor)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado fornecedor de nome: '{fornecedor.nome}'")
        return apresenta_fornecedor(fornecedor), 200
    except IntegrityError as e:
        error_msg = "Fornecedor de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar fornecedor '{fornecedor.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar fornecedor '{fornecedor.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/fornecedor', tags=[fornecedor_tag],
         responses={"200": FornecedorViewSchema, "404": ErrorSchema})
def get_fornecedor(query: FornecedorBuscaSchema):
    """Faz a busca por um Fornecedor a partir do id do fornecedor

    Retorna uma representação dos fornecedores.
    """
    fornecedor_id = query.id
    logger.debug(f"Coletando dados sobre fornecedor #{fornecedor_id}")
    session = Session()
    fornecedor = session.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
    if not fornecedor:
        error_msg = "Fornecedor não encontrado na base :/"
        logger.warning(f"Erro ao buscar fornecedor '{fornecedor_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Fornecedor econtrado: '{fornecedor.nome}'")
        return apresenta_fornecedor(fornecedor), 200


@app.get('/fornecedores', tags=[fornecedor_tag],
         responses={"200": FornecedorListaViewSchema, "404": ErrorSchema})
def get_fornecedores():
    """Lista todos os fornecedores cadastrados na base

    Retorna uma lista de representações de fornecedores.
    """
    logger.debug(f"Coletando lista de fornecedores")
    session = Session()
    fornecedores = session.query(Fornecedor).all()
    print(fornecedores)
    if not fornecedores:
        error_msg = "Fornecedor não encontrado na base :/"
        logger.warning(f"Erro ao buscar por lista de fornecedores. {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retornando lista de fornecedores")
        return apresenta_lista_fornecedor(fornecedores), 200


@app.delete('/fornecedor', tags=[fornecedor_tag],
            responses={"200": FornecedorDelSchema, "404": ErrorSchema})
def del_fornecedor(query: FornecedorBuscaSchema):
    """Deleta um Fornecedor a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    fornecedor_id = query.id
    fornecedor_nome = query.nome

    logger.debug(f"Deletando dados sobre fornecedor #{fornecedor_id}")
    session = Session()

    if fornecedor_id:
        count = session.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).delete()
    else:
        count = session.query(Fornecedor).filter(Fornecedor.nome == fornecedor_nome).delete()

    session.commit()
    if count:
        logger.debug(f"Deletado fornecedor #{fornecedor_id}")
        return {"mesage": "fornecedor removido", "id": fornecedor_id}
    else: 
        error_msg = "Fornecedor não encontrado na base :/"
        logger.warning(f"Erro ao deletar fornecedor #'{fornecedor_id}', {error_msg}")
        return {"mesage": error_msg}, 400


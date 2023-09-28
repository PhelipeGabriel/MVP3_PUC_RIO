from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

#from sqlalchemy.exc import IntegrityError

from model import Session, Material 
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API da GerMat", version="1.0.2")
app = OpenAPI(__name__, info=info,)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
material_tag = Tag(name="Material", description="inserção, visualização e remoção de materiais")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/material', tags=[material_tag], responses={"200": MaterialViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_material(form: MaterialSchema):
    """Adiciona um novo Material à base de dados

    Retorna uma representação dos materiais.
    """
    material = Material(
        nome=form.nome,
        quantidade=form.quantidade,
        custo=form.custo,
        nf=form.nf)
    logger.debug(f"Adicionando material de nome: '{material.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(material)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado material de nome: '{material.nome}'")
        return apresenta_material(material), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar material '{material.nome}', {error_msg}")
        return {"menssagem": error_msg}, 400


@app.get('/materiais', tags=[material_tag], responses={"200": ListagemMateriaisSchema, "404": ErrorSchema})
def get_materiais():
    """Faz a busca por todos os materiais cadastrados

    Retorna uma representação da listagem de materiais.
    """
    logger.debug(f"Coletando materiais ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    materiais = session.query(Material).all()

    if not materiais:
        # se não há materiais cadastrados
        return {"materiais": []}, 200
    else:
        logger.debug(f"%d materiais encontrados" % len(materiais))
        # retorna a representação de material
    #    print(materiais)
        return apresenta_materiais(materiais), 200


@app.get('/material', tags=[material_tag], responses={"200": MaterialViewSchema, "404": ErrorSchema})
def get_material(query: MaterialBuscaSchema):
    """Faz a busca por um material a partir do seu id

    Retorna uma representação do material.
    """
    material_id = query.id
    logger.debug(f"Coletando dados sobre material #{material_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    material = session.query(Material).filter(Material.id == material_id).first()

    if not material:
        # se o material não foi encontrado
        error_msg = "Material não encontrado :/"
        logger.warning(f"Erro ao buscar material '{material_id}', {error_msg}")
        return {"menssagem": error_msg}, 404
    else:
        logger.debug(f"Material encontrado: '{material.nome}'")
        # retorna a representação de material
        return apresenta_material(material), 200


@app.delete('/material', tags=[material_tag], responses={"200": MaterialDelSchema, "404": ErrorSchema})
def del_material(query: MaterialBuscaSchema):
    """Deleta um material a partir do nome do material informado

    Retorna uma menssagem de confirmação da remoção.
    """
    material_nome = unquote(unquote(query.nome))
 #   print(material_nome)
    logger.debug(f"Deletando dados sobre material #{material_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Material).filter(Material.nome == material_nome).delete()
    session.commit()

    if count:
        # retorna a representação da menssagem de confirmação
        logger.debug(f"Deletado material #{material_nome}")
        return {"menssagem": "Material removido", "id": material_nome}
    else:
        # se o material não foi encontrado
        error_msg = "Material não encontrado :/"
        logger.warning(f"Erro ao deletar material #'{material_nome}', {error_msg}")
        return {"menssagem": error_msg}, 404



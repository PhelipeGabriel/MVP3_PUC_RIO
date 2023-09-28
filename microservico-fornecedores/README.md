# Meu Microserviço Fornecedor

Este é um projeto que faz parte do material diático do **MVP3** 

Vamos continuar o desenvolvimento da single page application (SPA) iniciada lá na segunda aula, mas desta vez consumindo o dado de um microserviço ligado a um banco de dados proprio em vez do acesso aos dados estáticos de um arquivo JSON.

---
## Como instalar e executar o microserviço

Será necessário abrir um novo terminal!

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar o microserviço  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 8000
```

Abra o [http://localhost:8000/#/](http://localhost:8000/#/) no navegador para verificar o status da API em execução.

Boa Sorte!
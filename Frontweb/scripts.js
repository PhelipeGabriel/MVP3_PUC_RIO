/*
  --------------------------------------------------------------------------------------
  Obter a lista de MATERIAIS existentes no banco de dados via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/materiais';
  fetch(url, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      data.materiais.forEach(item => insertList(item.nome, item.quantidade, item.custo, item.nf))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}



/*
  --------------------------------------------------------------------------------------
  Carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()

/*
  --------------------------------------------------------------------------------------
  Colocar um material na lista via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (nome, quantidade, custo, nf) => {
  const formData = new FormData();
  formData.append('nome', nome);
  formData.append('quantidade', quantidade);
  formData.append('custo', custo);
  formData.append('nf', nf);

  let url = 'http://127.0.0.1:5000/material';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}



/*
  --------------------------------------------------------------------------------------
  Cria um botão "close" para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


/*
  --------------------------------------------------------------------------------------
  Remover um item da lista ao clicar no botão "close"
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeMaterial = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Tem certeza?")) {
        div.remove()
        deleteItem(nomeMaterial)
        alert("Removido!")
      }
    }
  }
}


/*
  --------------------------------------------------------------------------------------
  Deletar um material da lista via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (nome) => {
  console.log(nome)
  let url = 'http://127.0.0.1:5000/material?nome=' + nome;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    })
}


/*
  ---------------------------------------------------------------------------------------
  Adicionar um novo material com nome, quantidade, custo e nota fiscal! 
  ---------------------------------------------------------------------------------------
*/
const newItem = () => {
  let nome = document.getElementById("matNome").value;
  let quantidade = document.getElementById("matQuant").value;
  let custo = document.getElementById("matCusto").value;
  let nf = document.getElementById("matNF").value;

  if (!nome) {
    alert("Informe o Nome do Material!");
  } else if (isNaN(quantidade) || !quantidade) {
    alert("Você precisa inserir um valor numerico na quantidade do Material!");
  } else if (isNaN(custo) || !custo) {
    alert("Você precisa inserir um valor decimal no custo do Material!");
  } else if (!nf) {
    alert("Você precisa colocar a Nota Fiscal!");
  } else {
    insertList(nome, quantidade, custo, nf);
    postItem(nome, quantidade, custo, nf);
    alert("Material Adicionado!");
  
  }
  
}

/*
  --------------------------------------------------------------------------------------
  Insere items na lista e a apresenta
  --------------------------------------------------------------------------------------
*/

const insertList = (nome, quantidade, custo, nf) => {
  var material = [nome, quantidade, custo, nf];

  var table = document.getElementById('mytable');
  var row = table.insertRow();

  for (var i = 0; i < material.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = material[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("nome_mat").value = "";
  document.getElementById("quant_mat").value = "";
  document.getElementById("cust_mat").value = "";
  document.getElementById("nf_mat"). value = "";

  removeElement()

}

/*
  --------------------------------------------------------------------------------------
  Scripts da área dos FORNECEDORES!!!!!!!
  --------------------------------------------------------------------------------------
*/

/*
  --------------------------------------------------------------------------------------
  Obter a lista de FORNECEDORES existentes no banco de dados via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList1 = async () => {
  let url = 'http://127.0.0.1:8000/fornecedores';
  fetch(url, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      data.fornecedores.forEach(item => insertList1(item.nomeF, item.descricao, item.telefone, item.categoria))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}



/*
  --------------------------------------------------------------------------------------
  Carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList1()

/*
  --------------------------------------------------------------------------------------
  Colocar um FORNECEDOR na lista via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem1 = async (nome, descricao, telefone, categoria) => {
  const formData = new FormData();
  formData.append('nome', nome);
  formData.append('descrição', descricao);
  formData.append('telefone', telefone);
  formData.append('categoria', categoria);

  let url = 'http://127.0.0.1:8000/fornecedor';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}



/*
  --------------------------------------------------------------------------------------
  Cria um botão "close" para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton1 = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


/*
  --------------------------------------------------------------------------------------
  Remover um FORNECEDOR da lista ao clicar no botão "close"
  --------------------------------------------------------------------------------------
*/
const removeElement1 = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeFornecedor = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Tem certeza?")) {
        div.remove()
        deleteItem1(nomeFornecedor)
        alert("Removido!")
      }
    }
  }
}


/*
  --------------------------------------------------------------------------------------
  Deletar um FORNECEDOR da lista via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem1 = (nome) => {
  console.log(nome)
  let url = 'http://127.0.0.1:8000/fornecedor?nome=' + nome;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    })
}


/*
  ---------------------------------------------------------------------------------------
  Adicionar um novo FORNECEDOR com Nome, Categoria, Telefone e Descrição 
  ---------------------------------------------------------------------------------------
*/
const newItem1 = () => {
  let nomeF = document.getElementById("FornNome").value;
  let descricao = document.getElementById("FornDesc").value;
  let telefone = document.getElementById("FornTel").value;
  let categoria = document.getElementById("FornCat").value;

  if (!nomeF) {
    alert("Informe o Nome do Fornecedor!");
  } else if (!descricao) {
    alert("Você precisa inserir uma descrição do Fornecedor!");
  } else if (!telefone) {
    alert("Você precisa inserir um número para Contato!");
  } else if (!categoria) {
    alert("Você precisa colocar a Categoria!");
  } else {
    insertList1(nomeF, descricao, telefone, categoria);
    postItem1(nomeF, descricao, telefone, categoria);
    alert("Fornecedor Adicionado!");
  
  }
  
}

/*
  --------------------------------------------------------------------------------------
  Insere Fornecedores na lista e a apresenta
  --------------------------------------------------------------------------------------
*/

const insertList1 = (nome, descricao, telefone, categoria) => {
  var fornecedor = [nome, descricao, telefone, categoria];

  var table = document.getElementById('mytable1');
  var row = table.insertRow();

  for (var i = 0; i < fornecedor.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = fornecedor[i];
  }
  insertButton1(row.insertCell(-1))
  document.getElementById("nome_Forn").value = "";
  document.getElementById("cat_Forn").value = "";
  document.getElementById("tel_Forn").value = "";
  document.getElementById("desc_Forn"). value = "";

  removeElement1()

}

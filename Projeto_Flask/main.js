document.getElementById('meuFormulario').addEventListener('submit', function(event){
    event.preventDefault();
    var nome = document.getElementById('nome').value;
    var preco = document.getElementById('preco').value;
    var dados = {
        name: nome,
        price: preco
    };
    console.log(dados)
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:5000/criar',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    // tratamento da resposta da requisição
    .then(response => response.text())
    .catch(error =>{
        //exibir mensagem de erro
        document.getElementById('resposta').innerHTML = 'Erro ao processar a requisição.';
        console.log('Erro', error);
    });
});
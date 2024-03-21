--select*from Veiculo;
--select*from Marca;--

SELECT Pessoa.nome, Marca.nome FROM Pessoa 
JOIN Veiculo ON Pessoa.cpf = Veiculo.Proprietario 
JOIN Marca ON Marca.id = Veiculo.marca 
WHERE Marca.nome = 'Marca B';
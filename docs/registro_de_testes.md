# Registro de testes da TechBairro

Versão testada: 3.3.2  
Data: 26/10/2026  
Responsável: Fernanda  

Sistema operacional e versão do Python: Windows 11 · Python 3.12

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos certos | Cliente cadastrado com sucesso | Cliente cadastrado com sucesso | PASSOU |
| CT02 | RF01 | Salvar com Nome e Endereço vazios | Exibir mensagem informando os campos que precisam ser preenchidos | Preencha o(s) campo(s): Nome, Endereço | PASSOU |
| CT03 | RF02 | Telefone 61 9999 0000 (com espaços) | Exibir mensagem "Telefone inválido: use somente números." | Telefone inválido: use somente números. | PASSOU |
| CT04 | RF03 | E-mail ana@email (sem ponto) | Exibir mensagem "E-mail inválido: use o formato nome@dominio.com" | E-mail inválido: use o formato nome@dominio.com | PASSOU |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar | Cliente atualizado com sucesso | Cliente atualizado com sucesso | PASSOU |
| CT06 | RF06 | Excluir um cliente: responder Não, depois Sim | Cancelar a primeira tentativa e excluir o cliente na segunda | Primeira tentativa cancelada; cliente excluído na segunda confirmação | PASSOU |

## Testes automáticos

Saída do `python testar_validacao.py`:

A preencher com a saída exibida no terminal.

## Defeitos encontrados

Nenhum.
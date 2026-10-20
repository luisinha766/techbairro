# Changelog da TechBairro

## v3.2 (Aula 16)

### Alterado

* O banco agora é aberto pelo caminho completo, sempre na pasta do projeto.
* Os scripts foram organizados na pasta `scripts/`.

### Adicionado

* Mensagem "Banco em uso" no terminal, mostrando qual banco está sendo usado.

## v3.1 (Aula 15)

### Corrigido

* Corrigida a validação do telefone para aceitar somente números.
* Corrigida a validação do e-mail.
* Corrigida a verificação dos campos obrigatórios.
* Corrigida a exibição das mensagens de erro.
* Corrigida a limpeza dos campos depois do cadastro ou cancelamento.

## v3.0 (Aula 14)

### Alterado

* O `GerenciadorClientes` deixou de guardar os clientes somente em uma lista em memória e passou a gravar no banco SQLite `techbairro.db`.
* A edição dos clientes passou a usar o `id` do cliente.
* A exclusão dos clientes também passou a usar o `id`.

### Adicionado

* Banco de dados SQLite `techbairro.db`.
* Cadastro, consulta, edição e exclusão dos clientes usando o banco.

## v2.0 (Aulas 11 e 12)

### Adicionado

* Foram criadas classes para organizar melhor o sistema.
* Foi criada a tela de Consulta.
* A tela permite visualizar e consultar os clientes cadastrados.

## Antes da v2.0 (Aulas 5 a 10)

* Foram criadas as primeiras telas do sistema e seus eventos.
* Foram adicionadas validações para os campos do cadastro.
## v3.3.1 (Aula 21)

- Organização da TechBairro em camadas.
- Separação das responsabilidades em módulos.
- Criação do ValidadorCliente e dos testes de validação. 
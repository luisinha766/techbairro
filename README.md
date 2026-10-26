# TechBairro

A TechBairro é um sistema para cadastro e gerenciamento de clientes da associação de moradores. Ela permite cadastrar, consultar, alterar e excluir clientes por meio de uma interface simples.

**Versão atual:** v3.3.2 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastro de clientes com nome, telefone, e-mail e endereço.
- Consulta, alteração e exclusão de clientes cadastrados.
- Armazenamento dos dados em um banco de dados SQLite.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows |
| Python | Python 3 (versão testada: 3.12) |
| Tkinter | Necessário e disponível na instalação do Python |
| Bibliotecas externas | Nenhuma |
| Internet | Necessária para baixar o projeto; não é necessária para usar o programa depois de instalado |

## Instalação

### Opção 1 — Baixando com Git

É necessário ter o Git instalado.

No terminal, use:

```bash
https://github.com/luisinha766/techbairro
```

Depois entre na pasta do projeto:

```bash
cd TechBairro
```

O arquivo `requirements.txt` não possui pacotes externos para instalar, pois a TechBairro utiliza apenas recursos da biblioteca padrão do Python.

Para executar o programa:

```bash
python techbairro.py
```

Ao abrir o programa, aparecerá a janela **"Cadastro de Cliente"**. No terminal também aparecerá uma mensagem começando com **"Banco em uso:"**, mostrando o caminho do banco utilizado.

### Opção 2 — Baixando pelo GitHub

No GitHub, abra o repositório da TechBairro.

1. Clique em **Code**.
2. Clique em **Download ZIP**.
3. Extraia o arquivo ZIP.
4. Abra a pasta extraída da TechBairro.
5. Abra o terminal nessa pasta.
6. Execute:

```bash
python techbairro.py
```

A janela **"Cadastro de Cliente"** será aberta e o terminal mostrará a mensagem **"Banco em uso:"**.

## Configuração do banco de dados

A TechBairro utiliza o banco de dados SQLite chamado `techbairro.db`.

O banco fica na pasta do projeto e é criado automaticamente quando a TechBairro é executada pela primeira vez, caso ainda não exista.

O programa mostra no terminal a mensagem **"Banco em uso:"**, seguida do caminho completo do arquivo de banco que está sendo utilizado.

O arquivo `techbairro.db` não deve ser enviado para o GitHub porque pode conter dados pessoais dos clientes cadastrados.

Para fazer uma cópia de segurança, feche a TechBairro e copie o arquivo `techbairro.db` para outro local seguro. Para restaurar os dados, o arquivo pode ser colocado novamente na pasta do projeto com o programa fechado.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

- `techbairro.py` — arquivo principal que abre a tela e permite utilizar o sistema.
- `cliente.py` — contém a estrutura dos dados de um cliente.
- `banco.py` — responsável pelo armazenamento e consulta dos clientes no banco SQLite.
- `validacao.py` — contém as regras para verificar os dados preenchidos.
- `CHANGELOG.md` — registra as mudanças realizadas em cada versão.
- `requirements.txt` — informa que o projeto não possui dependências externas.
- `docs/` — contém documentos do projeto e o manual de utilização.
- `scripts/` — contém scripts auxiliares do projeto.
- `.gitignore` — define arquivos que não devem ser enviados para o repositório.

## Autor

**[SEU NOME]**  
Curso: Desenvolvimento de Sistemas  
Instituição: SENAC DF
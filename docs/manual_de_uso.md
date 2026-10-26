# Manual de uso da TechBairro

## A tela principal

Ao abrir a TechBairro, aparece a janela **"Cadastro de Cliente"**.

A tela possui quatro campos para preencher:

- **Nome**
- **Telefone**
- **E-mail**
- **Endereço**

Também aparecem os botões:

- **Salvar**
- **Cancelar**
- **Consultar**

A tela mostra uma mensagem de status e o contador de clientes cadastrados.

Na parte inferior da janela aparece a versão do sistema.

## Cadastrar um cliente

1. Abra a TechBairro.
2. Preencha o campo **Nome**.
3. Preencha o campo **Telefone** usando somente números.
4. Preencha o campo **E-mail** no formato de e-mail.
5. Preencha o campo **Endereço**.
6. Clique em **Salvar**.
7. Se os dados estiverem corretos, aparecerá uma mensagem informando que o cliente foi salvo com sucesso.
8. O contador de clientes cadastrados será atualizado.

## Consultar os clientes cadastrados

1. Na tela principal, clique em **Consultar**.
2. Será aberta a janela **"Consulta de Clientes"**.
3. Os clientes cadastrados serão mostrados na lista.
4. Se não houver clientes cadastrados, aparecerá a mensagem **"Nenhum cliente cadastrado"**.
5. Para fechar a consulta, feche a janela de consulta.

## Alterar os dados de um cliente

1. Clique em **Consultar**.
2. Na lista, selecione o cliente que deseja alterar.
3. Clique em **Editar selecionado**.
4. Os dados do cliente aparecerão novamente nos campos da tela principal.
5. Faça as alterações necessárias.
6. Clique em **Salvar**.
7. Se a alteração for realizada corretamente, aparecerá uma mensagem informando que o cliente foi atualizado com sucesso.

## Excluir um cliente

1. Clique em **Consultar**.
2. Selecione o cliente que deseja excluir.
3. Clique em **Excluir selecionado**.
4. O sistema perguntará se você tem certeza que deseja excluir o cadastro.
5. Confira o nome do cliente.
6. Confirme a exclusão.
7. O cliente será removido da lista e aparecerá uma mensagem informando que a exclusão foi realizada com sucesso.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Não pode ficar vazio. |
| Telefone | Sim | Não pode ficar vazio e deve conter somente números. |
| E-mail | Sim | Não pode ficar vazio e deve ter um formato de e-mail, contendo `@` e um ponto no domínio. |
| Endereço | Sim | Não pode ficar vazio. |

## Mensagens do sistema

| Mensagem | O que significa | O que fazer |
|---|---|---|
| **"Cliente 'nome' salvo com sucesso!"** | O cadastro foi realizado corretamente. | Continue usando o sistema ou cadastre outro cliente. |
| **"Cliente 'nome' atualizado com sucesso!"** | Os dados do cliente foram alterados corretamente. | Continue usando o sistema. |
| **"Cliente 'nome' excluído com sucesso!"** | O cliente foi excluído. | Se necessário, faça um novo cadastro. |
| **"Formulário limpo"** | Os campos da tela foram apagados. | Preencha os dados novamente se quiser fazer um cadastro. |
| **"Preencha o(s) campo(s): ..."** | Um ou mais campos obrigatórios estão vazios. | Preencha os campos indicados e tente salvar novamente. |
| **"Telefone inválido: use somente números."** | O telefone possui caracteres que não são números. | Apague os caracteres diferentes de números e tente novamente. |
| **"E-mail inválido: use o formato nome@dominio.com"** | O e-mail não está em um formato válido. | Corrija o e-mail e tente salvar novamente. |
| **"Selecione um cliente antes de editar."** | Nenhum cliente foi selecionado para alteração. | Selecione um cliente na lista e clique novamente em **Editar selecionado**. |
| **"Selecione um cliente antes de excluir."** | Nenhum cliente foi selecionado para exclusão. | Selecione um cliente na lista e clique novamente em **Excluir selecionado**. |
| **"Nenhum cliente cadastrado"** | Não existem clientes cadastrados para mostrar. | Cadastre um cliente usando a tela principal. |

## Dúvidas frequentes

**Como faço para cadastrar um cliente?**

Preencha Nome, Telefone, E-mail e Endereço e clique em **Salvar**.

**Por que meu telefone aparece como inválido?**

O telefone deve conter somente números. Retire letras, espaços ou outros caracteres e tente novamente.

**Como faço para alterar os dados de um cliente?**

Clique em **Consultar**, selecione o cliente, clique em **Editar selecionado**, altere os dados e clique em **Salvar**.

**Como faço para excluir um cliente?**

Clique em **Consultar**, selecione o cliente e clique em **Excluir selecionado**. Depois confirme a exclusão.

**O que faço se aparecer "Nenhum cliente cadastrado"?**

Isso significa que ainda não existem clientes cadastrados. Volte para a tela principal e cadastre um cliente.
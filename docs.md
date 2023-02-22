# API do CONTA[AI]

## Visão geral

A API do CONTA[AI] foi construída usando o modelo arquitetural RESSTful, e expõe os dados vindo do banco de dados do sistema através dos serializers do Django Rest Framework.

O acesso a esses dados se dá através de um token de autorização, que pode ser gerado para qualquer usuário válido no banco de dados.

## Regras de negócio

O CONTA[AI] é um sistema que permite aos usuários fazerem registros da movimentação do seu caixa pessoal.

Os registros incluem:
- Relatórios
- Movimentações
- Fluxos de caixa

### Relatórios

Os relatórios são documentos que registram as movimentações, tendo data e descrição. Na API, eles ficam expostos em /api/relatorio/.

### Movimentações

As movimentações são registros de entradas ou saídas monetárias em determinado dia. Eles compõem os relatórios. Na API, eles ficam expostos em /api/movimentacao/.

### Fluxos de caixa

Os fluxos de caixa são coleções de movimentações, tendo um título e uma descrição. Na API, eles ficam expostos em /api/fluxosdecaixa/.

## Permissão

Para que a API permita que você obtenha um token, você precisa ter um usuário Django válido. Para conferir se você já tem um, faça uma requisição POST para /auth/signup/, com o seguinte corpo:

```json
{
    "username": "<seu-nome-de-usuario-django>",
    "password": "<a-senha-deste-usuario>",
    "email": "<o-email-do-usuario>",
    "first_name": "<primeiro-nome-do-usuario>",
    "last_name": "<ultimo-nome-do-usuario>"
}
```

O objetivo desta requisição é criar um usuário Django.

### Sucesso

Se a resposta vier com um código 201, significa que o usuário Django foi criado. O corpo da resposta deve ter essa estrutura:

```json
{
    "username": "<seu-nome-de-usuario-django>",
    "password": "<a-senha-deste-usuario>",
    "email": "<o-email-do-usuario>",
    "first_name": "<primeiro-nome-do-usuario>",
    "last_name": "<ultimo-nome-do-usuario>"
}
```

### Falha

Se a resposta vier com um código 400, significa que o usuário Django já existe. Portanto, você já pode se autenticar e pegar um token.

Para seguir para a autenticação, você precisará dos seguintes dados validados: 

```json
{
    "username": "<seu-nome-de-usuario-django>",
    "password": "<a-senha-deste-usuario>"
}
```

## Autenticação

Para obter acesso aos dados que a API expõe, note que é importante se identificar. Dessa forma, o servidor consegue determinar se você tem autorização para acessar os recursos ou não.

Para se autenticar, faça uma requisição POST para /auth/token/. No corpo da requisição, coloque o seguinte arquivo JSON:

```json
{
    "username": "<seu-nome-de-usuario-django>",
    "password": "<a-senha-deste-usuario>"
}
```

### Sucesso

Em caso de sucesso, a API deve retornar uma resposta 200, com o seguinte corpo:

```json
{
    "token": "<token-gerado>"
}
```

Isto é: existe um usuário válido com os dados recebidos pelo servidor. Portanto, a API responde com um token. Este token deverá estar presente nas requisições para os endpoints.

### Falha

Em caso de falha, a API deve retornar uma resposta 400, com o seguinte corpo:

```json
{
    "non_field_errors": [
        "Impossível fazer login com as credenciais fornecidas."
    ]
}
```

## Recursos e endpoints

### Relatórios

Para ter acesso a lista de relatórios cadastrados no banco de dados, faça uma requisição GET para /api/relatorio/. Cada movimentação possui um id, que é útil quando se quer fazer uma requisição GET para um único recurso: /api/relatorio/{id}/.
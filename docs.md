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

## Autenticação

Para obter acesso aos dados que a API expõe, note que é importante se identificar. Dessa forma, o servidor consegue determinar se você tem autorização para acessar os recursos ou não.

Para se autenticar, faça uma requisição POST para /api-auth-token/. No corpo da requisição, coloque o seguinte arquivo JSON:

```json
{
    "username": "<your-django-username>",
    "password": "<your-django-password>"
}
```

Note que você precisa registrar um usuário Django antes de fazer a requisição, caso contrário, você receberá um erro 401.

## Recursos e endpoints

### Relatórios

Para ter acesso a lista de relatórios cadastrados no banco de dados, faça uma requisição GET para /api/relatorio/. Cada movimentação possui um id, que é útil quando se quer fazer uma requisição GET para um único recurso: /api/relatorio/{id}/.
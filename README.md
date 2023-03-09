# CONTA[AI]
Registro de fluxo de caixa para pequenos comerciantes


``
O CONTA[AI] é um sistema que auxilia no registro do fluxo de caixa de pequenos comerciantes. Atualmente, o sistema está em fase de testes.
``

## Início rápido
Para tentar agilizar o processo de execução do projeto, há a possibilidade de executar o script [ativar-servidor.sh](assets/scripts/ativar-servidor.sh). Ele tenta instalar as dependências do projeto e iniciar o servidor.

```console
➜ conta-ai (main) ✔ source assets/scripts/ativar-servidor.sh 
```

O script assume que o host hospedeiro tenha `python3` instalado, com a possibilidade de criar virtualenvs e instalar pacotes pelo pip.

Lembre-se que a execução desse script não substitui a leitura da documentação.

## Início

Estas instruções permitem que você obtenha uma cópia local do projeto e o configure em seu computador para desenvolvimento e testes. Elas assumem que o sistema operacional hospedeiro seja uma distribuição GNU/Linux, portanto, os comandos podem ter pequenas variações caso o sistema seja hospedado em um servidor baseado em outro sistema operacional.

### Pré-requisitos

Para baixar, compilar e executar o projeto em seu computador, você deve ter instalado:

- Sistema de controle de versões [git](https://www.git-scm.com/);
- Kit de Desenvolvimento [Python](https://www.python.org/) (versão 3), com o gerenciador de pacotes pip.

### Cópia local do sistema

Para obter uma cópia local do sistema, realize um clone do projeto. Isso pode ser feito através da interface do sistema em que este repositório se encontra, juntamente ao uso da linha de comandos do seu computador.

### Projeto Django

A partir deste ponto, este arquivo assume que os terminais CLIs estejam em operação no seguinte diretório:

`conta-ai/api/`

O diretório acima hospeda o núcleo do sistema.

### Criar ambiente de desenvolvimento
Para que o sistema não entre em conflito com outros processos do próprio sistema operacional, recomenda-se que você crie um ambiente de desenvolvimento virtual Python. Rodando o comando abaixo, você terá uma nova instalação Python dedicada ao desenvolvimento do conta-ai.
```
python3 -m venv <nome-da-venv>
```

substituindo `<nome-da-venv>` pelo nome que você deseja para o ambiente virtual.

#### Ativar novo ambiente
Para ativar o novo ambiente, você terá que rodar um script chammado `activate`. Para isso, rode o seguinte comando:
```
./<nome-da-venv>/bin/activate
```

#### Desativar novo ambiente
Para desativar o novo ambiente, simplesmente rode:
```
deactivate
```

### Dependências
Para que o sistema funcione corretamente, é preciso instalar as dependências Python, com o pip.
Para isso, com o ambiente virtual ativado, rode o seguinte comando:
```
pip install -r requirements.txt
```

### Banco de dados local
Para que o sistema funcione corretamente, é preciso criar um banco de dados local. Para isso, com o ambiente virtual ativado, rode o seguinte comando na linha de comandos do seu computador:
```
python3 manage.py migrate
```

### Testando o sistema
Para conferir se o sistema roda normalmente nas situações previstas pelos requisitos, desenvolvemos alguns testes automatizados. Para rodá-los, com o ambiente virtual ativado, rode o seguinte comando:
```
python3 manage.py test
```

O retorno deve informar que está tudo OK. Se os testes não derem OK, provavelmente você esqueceu de algum comando acima ou modificou alguma coisa no software.

#### [OPICIONAL] Superusuário para interface administrativa
Para que o desenvolvedor use uma interface administrativa do sistema, terá que criar um superusuário. Para isso, após realizadas todas as instruções anteriores (e com o ambiente virtual ativado), rode o seguinte comando na linha de comandos:
```
python3 manage.py createsuperuser
```

O terminal guiará o desenvolvedor através dos passos necessários para a criação do superusuário.

### Executar o servidor em modo desenvolvimento

Para executar o sistema em modo de desenvolvimento, com o ambiente virtual ativado, rode o seguinte comando na linha de comandos do seu computador:
```
python3 manage.py runserver
```

Em caso de problemas ao executar o servidor, certifique-se de que não esqueceu de seguir nenhum passo descrito neste documento. Ao persistirem os erros, consulte a documentação do [Django](https://www.djangoproject.com/) ou descreva seu problema através de uma [issue](https://github.com/cannudo/conta-ai/issues).


## Equipe de desenvolvimento

* **Luan da Costa Redmann** — *https://github.com/cannudo/*

## Licença

Este projeto é licenciado pela GNU [GPL 3](LICENSE.md).

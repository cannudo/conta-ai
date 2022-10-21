# CONTA[AI]
Registro de fluxo de caixa para pequenos comerciantes


``
O CONTA[AI] é um sistema que auxilia no registro do fluxo de caixa de pequenos comerciantes. Atualmente, em testes e em elaboração.
``

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

### Banco de dados local
Para que o sistema funcione corretamente, é preciso criar um banco de dados local. Para isso, rode o seguinte comando na linha de comandos do seu computador:
```
python3 manage.py migrate
```

#### [OPICIONAL] Superusuário para interface administrativa
Para que o desenvolvedor use uma interface administrativa do sistema, terá que criar um superusuário. Para isso, após realizadas todas as instruções anteriores, rode o seguinte comando na linha de comandos:
```
python3 manage.py createsuperuser
```

O terminal guiará o desenvolvedor através dos passos necessários para a criação do superusuário.

### Executar o servidor em modo desenvolvimento

Para executar o sistema em modo de desenvolvimento, rode o seguinte comando na linha de comandos do seu computador:
```
python3 manage.py runserver
```

Em caso de problemas ao executar o servidor, certifique-se de que não esqueceu de seguir nenhum passo descrito neste documento. Ao persistirem os erros, consulte a documentação do [Django](https://www.djangoproject.com/)

## Equipe de desenvolvimento

* **Luan da Costa Redmann** — *https://github.com/cannudo/*

## Licença

Este projeto é licenciado pela GNU [GPL 3](LICENSE.md).

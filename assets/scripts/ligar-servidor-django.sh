#!/bin/bash

case "$1" in
    '--make-venv')
        python3 -m venv venv
        source venv/bin/activate

        echo "Virtual Enviroment criado e ativado."
        echo "Para instalar as dependências do projeto, rode $0 --install-requirements"
        ;;
        
    '--install-requirements')
        cd djangoroot/
        pip install -r requirements.txt  
        ;;
    '--help')
        echo "Uso: $0 [--make-venv|--install-requirements|--help]"
        echo "  --make-venv: cria e ativa um ambiente virtual"
        echo "  --install-requirements: instala as dependências do projeto"
        echo "  --help: exibe esta ajuda"
        return 0
        ;;
    '')
        code ./
        python3 manage.py runserver

        ;;
    *)
        echo "Opção inválida: $1"
        echo "Uso: $0 [void|--make-venv|--install-requirements|--help]"
        return 1
        ;;
esac

code ./
python3 manage.py runserver

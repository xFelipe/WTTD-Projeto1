# Eventex

Sistema de eventos encomendado pela Morena disponível em https://eventex-felipegomes.herokuapp.com/

[![Build Status](https://travis-ci.org/xFelipe/WTTD-Projeto1.svg?branch=master)](https://travis-ci.org/xFelipe/WTTD-Projeto1)


## Como desenvolver?

1. Clone o repositório.
2. Crie uma virtualenv com python 3.6.
3. Ative a virtualenv.
4. Instale as dependências.
5. Configure a instância com .env
6. Execute os testes

```console
git clone https://github.com/xFelipe/xFelipe.github.io.git wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma `SECRET_KEY` segura para a instância.
4. Defina `DEBUG=False`.
5. Configure o serviço de e-mail.
6. Envie o código para o Heroku.

```console
heroku create minha instancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o e-mail
git push heroku master --force
```

# Embeddings Microservice

A very simple service to embed input strings

There is no current structure because of how small the service is, but
if we want to expand this, we can easily create a few folders

├── embeddings
│   ├── __init__.py
│   ├── main.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   └── users.py
│   └── schemas
│       ├── __init__.py
│       └── embeddings.py


Routers will hold the actual organized routes, schemas hold the Pydantic classes
see [here](https://fastapi.tiangolo.com/tutorial/bigger-applications/) for more information


## Development

Create a python environment
```
python -m venv .venv
source .venv/bin/activate
```
Install requirements
```
pip install -r requirements.txt && pyenv rehash
```
Run app
```
python main.py
```
Go to the [hosted docs](http://localhost:8088/docs) to try it
or POST
```
curl -X 'POST' \
  'http://localhost:8088/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "strings": [
    "test 1",
    "test 2",
    "foo",
    "bawsr"
  ]
}'
```

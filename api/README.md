# Deploying your API for on-premise LLM model inference

Objective of this workshop is to :

- get familiar with using huggingface transformers
- build an API around falcon-7B using huggingface pipelines and fastapi
- deploy this API on the remote machine using docker
- call this API from a react app

## requiremnts

Fimliarity with using python.
Being cosy from your terminal.

- `python 3.8+`
- `git`
- `docker`

## setup

create a virtual env and activate it

```bash
python -m venv .venv
source .venv/bin/activate
```

install dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

## build the API

build with docker

```bash
docker build -t falcon-api .
```

run the API

```bash
docker run -d -p 8000:8000 falcon-api
```

## Resources

- [Huggingface transformers](https://huggingface.co/transformers/)
- [Fastapi documentation](https://fastapi.tiangolo.com/)
- [Intro to docker](https://docker-curriculum.com/)

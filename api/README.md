# Deploying your API for on-premise LLM model inference

Objective of this workshop is to 

- build an API around LLama-2
- deploy this API on the remote machine using docker
- secure this api
- call this API from a react app


## requiremnts

Fimliarity with using python.
Being cosy from your terminal.

- `python 3.8+`
- `git`
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

## Resources
- [intro to docker](https://docker-curriculum.com/)
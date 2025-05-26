# FROM scratch
FROM python:3.13.3-slim

WORKDIR /app

# copy from to 
COPY ./src /app/src 
COPY ./pyproject.toml /app/pyproject.toml

RUN python -m pip install -e .

# snake case here we specified it in the pyproject.toml
# project script wrappers
ENTRYPOINT [ "dev2il-devops-app" ] 


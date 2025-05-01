# dbt-on-cloud-run

Execute DBT core on Cloud Run Job

## Prerequisites

- Python 3.11+
- Poetry
- Docker
- Load the seed data under `dbt/seeds`
- Update the following in `dbt/profiles.yml` to match to your environment:
    - project: `<change to yours>`
    - dataset: `<change to yours>`

## How to run locally

```
poetry update
poetry shell
cd dbt
dbt run
```

## Build

```
gcloud builds submit --config cloudbuild_build.yaml . --substitutions _REPO_NAME=repositorioportifolioacademias
```

## Create the Cloud Run Job

> this uses the `deploy` command which manages both create and update

```
gcloud builds submit --config cloudbuild_create.yaml . --substitutions _REPO_NAME=repositorioportifolioacademias
```

## Trigger execution, including overriding
See [cloudrun/execute_cloud_run_job.py](cloudrun/execute_cloud_run_job.py)


# Minhas adições ao README

## Caso faça alterações no dbt precisa fazer o rebuild da imagem para o Job exectar a nova vesrsão
1- Rebuild da imagem com o mesmo nome. Substitua SEU-PROJETO-ID e NOME-DA-IMAGEM pelos valores que você usou anteriormente:

```
gcloud builds submit --config cloudbuild_build.yaml . --substitutions _REPO_NAME=repositorioportifolioacademias
```

2- (Opcional) Forçar atualização do Job. Se o job já estiver apontando para essa mesma imagem, tecnicamente você não precisa rodar gcloud run jobs update.Mas às vezes o Cloud Run pode cachear a versão anterior, então você pode forçar a atualização assim:

```
gcloud run jobs update MEU-JOB \
  --image gcr.io/SEU-PROJETO-ID/NOME-DA-IMAGEM \
  --region us-central1
``` 
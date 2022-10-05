modelo_ativação_totvs
==============================

In this repository I will show you how to use Azure Databricks for the development and training of articial intelligence models letting them available in an integration and continuous delivery process (CI/CD).

The main idea is to build an end-to-end project for developing, training, deploying and monitoring machine learning models.

Steps: <br>
1. [DONE] Train a churn prediction model using Azure Databricks
2. [DONE] Deploy the machine learning model
3. [...] Build a MLOps Pipeline
4. [...] Monitor your machine learning model

![Front](imgs/arquitetura_databricks.png)

------------
Project Organization
------------

```
├── imgs
|
├── notebooks
│
├── src                <- nosso código para uso neste projeto.
|   |
│   ├── features       <- Scripts para transformar dados brutos em recursos para modelagem
│   │   └── build_churn_features.py
|   |
│   ├── models         <- Scripts para treinar modelos e, em seguida, usar modelos treinados para fazer previsões
│   │   │                 previsões
│   │   ├── predict_model.py
│   │   ├── train_model.py
│   │   └── xgboost-automl.py
|   |
│   ├── monitoring  <- Scripts para monitorar modelos em produção
|   |
│   ├── tests
|   |
│   |── utils  <- Scripts com funções utils para ajudar no carregamento de dados, armazenamento de recursos, mlflow
|   |     
│   |── __init__.py    <- Torna src um módulo Python
│   |
│   └── config_env.py
│ 
|── Azure Databricks - Documentação passo a passo 
|
├── README.md          <- O README de nível superior para desenvolvedores que usam este projeto.
|
├── requirements.txt   <- O arquivo de requisitos para reproduzir o ambiente de análise, e.g.
│                         gerado com `pip freeze > requirements.txt`
|
```
--------
# Databricks notebook source
path_raw_data = '/dbfs/FileStore/shared_uploads/mlengineer.poc@gmail.com/E_Commerce_Dataset.xlsx'

# COMMAND ----------

# Database Feature Store and Feature Table
feature_store_db_name = ''
feature_store_db_name_and_table = ''

# COMMAND ----------

# Criando camada gold
sqlContext.sql(f"CREATE DATABASE IF NOT EXISTS gold;")

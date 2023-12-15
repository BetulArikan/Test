# Databricks notebook source
import pyspark.sql.functions as F

# COMMAND ----------

display(
  spark.read.load('/mnt/SandBox/Data_Science/DemandTransfer/dev/validation/tables/tiv')
  .filter(F.col('MpcBase') == 1156763)
)

# COMMAND ----------



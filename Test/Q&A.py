# Databricks notebook source
# MAGIC %md 
# MAGIC Access the mount point

# COMMAND ----------

dbutils.fs.ls('/mnt/trn05/project.png')



# COMMAND ----------

#spark.conf.set("fs.azure.account.key.training05.blob.core.windows.net","mbeYrZQAukTdgqyH7sqQ7Cl2oe0G9XUU8/3FHRU2KFqyTTzsEp11E7gRIcG3ERUyOyhd60dcz1wm+ASt0TFdUQ==")


# COMMAND ----------


dbutils.fs.ls('wasbs://input@training05.blob.core.windows.net/')

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ```
# MAGIC Create flder in blob
# MAGIC
# MAGIC ```

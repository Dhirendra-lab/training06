# Databricks notebook source
# MAGIC %md #Dbutils Databricks utilities

# COMMAND ----------

dbutils.help()

# COMMAND ----------

# MAGIC %md #Dbutils File system utlities

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls('/FileStore/files')

# COMMAND ----------

dbutils.fs.cp('/FileStore/files/project.jpg','/tmp/project_test.jpg',True)

# COMMAND ----------

# dbutils.fs.mv('/FileStore/files/project.jpg','/tmp/project_test.jpg')

# COMMAND ----------

# dbutils.fs.rm('/FileStore/files/project.jpg')

# COMMAND ----------

# MAGIC %md #Create Mount Point
# MAGIC
# MAGIC ```
# MAGIC dbutils.fs.mount(
# MAGIC   source: str,
# MAGIC   mount_point: str,
# MAGIC   encryption_type: Optional[str] = "",
# MAGIC   extra_configs: Optional[dict[str:str]] = None
# MAGIC )
# MAGIC ```

# COMMAND ----------

# MAGIC %md ## Through Account Key

# COMMAND ----------

configs = {"fs.azure.account.key.training05.blob.core.windows.net": "mbeYrZQAukTdgqyH7sqQ7Cl2oe0G9XUU8/3FHRU2KFqyTTzsEp11E7gRIcG3ERUyOyhd60dcz1wm+ASt0TFdUQ=="}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "wasbs://input@training05.blob.core.windows.net/",
  mount_point = "/mnt/trn05",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls('/mnt/trn05/project.png')



# COMMAND ----------

spark.conf.set("fs.azure.account.key.training05.blob.core.windows.net","mbeYrZQAukTdgqyH7sqQ7Cl2oe0G9XUU8/3FHRU2KFqyTTzsEp11E7gRIcG3ERUyOyhd60dcz1wm+ASt0TFdUQ==")


dbutils.fs.ls('wasbs://input@training05.blob.core.windows.net/')

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "<application-id>",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="<scope-name>",key="<service-credential-key-name>"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/",
  mount_point = "/mnt/<mount-name>",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md ##UnMount

# COMMAND ----------

# dbutils.fs.unmount("/mnt/trn05")

# COMMAND ----------

# MAGIC %md ## Through SAS Key

# COMMAND ----------

configs = {"fs.azure.sas.input.training05.blob.core.windows.net": "?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-11-25T16:31:59Z&st=2023-11-25T08:31:59Z&spr=https&sig=W9QV7IQYlg18%2BzK%2BAc64x4xiIqxbovU9Exqyg%2BtXSKw%3D"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "wasbs://input@training05.blob.core.windows.net/",
  mount_point = "/mnt/trn051",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.mkdirs('/mnt/trn051/output')

# COMMAND ----------

dbutils.fs.cp('/tmp/project.jpg','/mnt/trn051/output',True)

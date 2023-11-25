# Databricks notebook source
# MAGIC %md # Create Widget 

# COMMAND ----------

dbutils.widgets.text(name="Text", defaultValue="Hello")
dbutils.widgets.dropdown(name="DropDown", defaultValue="2022", choices=["2022", "2021", "2020"])
dbutils.widgets.combobox(name="CheckBox", defaultValue="P1", choices=["P1", "P2", "P3"])
dbutils.widgets.multiselect(name="Multi Select", defaultValue="1", choices=[str(x) for x in range(1, 13)])

# COMMAND ----------

dbutils.widgets.get(<"widget_name">)

# COMMAND ----------

# MAGIC %md ## Remove Widget

# COMMAND ----------

dbutils.widgets.remove("Text")


# COMMAND ----------

# MAGIC %md ## Remove All Widget

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

# MAGIC %md #Create Widget through SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE WIDGET TEXT txt_p1 DEFAULT 'Hello';
# MAGIC CREATE WIDGET DROPDOWN dd_p1 DEFAULT '2022' CHOICES SELECT DISTINCT t_year FROM demo_widget_table;
# MAGIC CREATE WIDGET COMBOBOX cbx_p1 DEFAULT 'P1' CHOICES SELECT DISTINCT product_name FROM demo_widget_table LIMIT 5
# MAGIC CREATE WIDGET MULTISELECT mst_p1 DEFAULT '1' CHOICES SELECT DISTINCT t_month_number FROM demo_widget_table
# MAGIC SELECT * FROM demo_widget_2 
# MAGIC WHERE transaction_year = getArgument("dd_p1") 
# MAGIC #alternative (= '%$dd_p1%')
# MAGIC REMOVE WIDGET <name>

# COMMAND ----------

!pip install pandas

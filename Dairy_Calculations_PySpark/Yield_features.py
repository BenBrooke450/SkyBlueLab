def get_yield_stats(year : int):

    from pyspark.sql import functions as F
    import plotly.express as px
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, lit, contains, when, sum, avg, round, max, row_number, desc
    from pyspark.sql.window import Window
    from pyspark.sql.types import IntegerType
    import requests
    from pyspark.sql.types import StructType, StructField, StringType, DoubleType
    import pandas as pd
    from pyjstat import pyjstat
    import os
    import sys

    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    spark_graph = SparkSession.builder \
        .appName("Dairy_Price") \
        .master("local[1]") \
        .config("spark.driver.memory", "512m") \
        .config("spark.executor.memory", "512m") \
        .config("spark.memory.offHeap.enabled", "false") \
        .config("spark.sql.shuffle.partitions", "1") \
        .config("spark.ui.enabled", "false") \
        .getOrCreate()

    year = str(year)

    url = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/apro_mk_pobta?time={year}"

    dataset = pyjstat.Dataset.read(url)

    df_pandas = dataset.write('dataframe')

    df_spark = spark_graph.createDataFrame(df_pandas)

    df = df_spark.dropna()

    df = df.filter(col("Dairy and other animal products (except meat)").isin("Raw cows' milk delivered to dairies", "Hard cheese"))

    df = df.withColumn("total_milk_collected",
                       when((
                                        col("Dairy and other animal products (except meat)") == "Raw cows' milk delivered to dairies") &
                            (col("Item of milk") == "Products obtained (1 000 t)"), col("value"))).withColumn(
        "total_milk_collected", col("total_milk_collected") * 1000)

    df = df.withColumn("total_milk_collected", max(col("total_milk_collected")).over(
        Window.partitionBy("Geopolitical entity (reporting)", "Time")))

    df = df.withColumn("total_milk_fat",
                       when((
                                        col("Dairy and other animal products (except meat)") == "Raw cows' milk delivered to dairies") &
                            (col("Item of milk") == "Fat content (t)"), col("value")))

    df = df.withColumn("total_milk_fat",
                       max(col("total_milk_fat")).over(Window.partitionBy("Geopolitical entity (reporting)", "Time")))

    df = df.withColumn("total_milk_Protein",
                       when((
                                        col("Dairy and other animal products (except meat)") == "Raw cows' milk delivered to dairies") &
                            (col("Item of milk") == "Protein content (t)"), col("value")))

    df = df.withColumn("total_milk_collected", max(col("total_milk_collected")).over(
        Window.partitionBy("Geopolitical entity (reporting)", "Time")))

    df = df.withColumn("total_hard_cheese",
                       when((col("Dairy and other animal products (except meat)") == "Hard cheese") &
                            (col("Item of milk") == "Products obtained (1 000 t)"), col("value")))

    df = df.withColumn("total_hard_cheese", max(col("total_hard_cheese")).over(
        Window.partitionBy("Geopolitical entity (reporting)", "Time")))

    df = df.withColumn("milk_fat_pct", col("total_milk_fat") / col("total_milk_collected"))

    df = df.withColumn("casein_pct", (col("total_milk_Protein") / col("total_milk_collected") * 0.78))

    df = df.withColumn("hist_yield_ratio", col("total_hard_cheese", ) / col("total_milk_collected"))

    df = df.toPandas()

    spark_graph.stop()

    return df

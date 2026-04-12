def get_energy_price(year : int):

    import os
    import sys

    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, lit, contains, when, sum, avg, round, max, row_number, desc, regexp_replace, concat, to_date
    from pyspark.sql.window import Window
    from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
    import pandas as pd
    import requests
    import plotly.express as px
    from pyjstat import pyjstat

    spark = SparkSession.builder \
        .appName("Dairy_Project") \
        .master("local[1]") \
        .config("spark.driver.memory", "512m") \
        .config("spark.executor.memory", "512m") \
        .config("spark.memory.offHeap.enabled", "false") \
        .config("spark.sql.shuffle.partitions", "1") \
        .config("spark.ui.enabled", "false") \
        .getOrCreate()

    year = str(year)

    url = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_205?lang=EN"

    dataset = pyjstat.Dataset.read(url)

    df_pandas = dataset.write('dataframe')

    df_spark = spark.createDataFrame(df_pandas)

    df_energy = df_spark.dropna()

    df_energy = df_energy.drop("Taxes", "Unit of measure","Standard international energy product classification (SIEC)", "Energy consumption")

    df_energy = df_energy.filter(col("Time").contains(year))

    final_df_for_table = df_energy.toPandas()

    spark.stop()

    fig = px.scatter(
        final_df_for_table,
        x="Time",
        y="value",
        color="Geopolitical entity (reporting)",
        symbol="Currency",
        hover_data=["Time frequency"]
    )

    return fig, final_df_for_table


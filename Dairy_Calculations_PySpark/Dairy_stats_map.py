def get_dairy_stats(year : int, country : str):

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

    df = df.dropna()

    df_filtered = df.filter(
        (F.col("Geopolitical entity (reporting)") == country)
    )

    df_filtered = df_filtered.select(
        F.col("Dairy and other animal products (except meat)").alias("dairyprod"),
        F.col("Item of milk").alias("unit"),
        F.col("Time").alias("time"),
        F.col("value")
    )

    df_agg = df_filtered.groupBy(
        "dairyprod",
        "unit"
    ).agg(
        F.sum("value").alias("value")
    )

    df_filtered = df_filtered.toPandas()

    pdf = df_agg.toPandas()

    spark_graph.stop()

    pdf["dairyprod_short"] = pdf["dairyprod"].str.slice(0, 10)

    fig = px.bar(
        pdf,
        x="dairyprod_short",
        y="value",
        color="unit",
        barmode="group",
        title=f"Dairy System Breakdown — {country}"
    )

    fig.update_layout(
        xaxis_title="Dairy Category",
        yaxis_title="Value",
        xaxis_tickangle=-45
    )

    fig.update_yaxes(type="log")

    fig.update_layout(
        width=1700,
        height=600
    )

    return fig, df_filtered


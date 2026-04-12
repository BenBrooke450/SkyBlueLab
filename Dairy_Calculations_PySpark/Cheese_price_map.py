def get_cheddar_price(year : int):

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

    spark = SparkSession.builder \
        .appName("Dairy_Project") \
        .master("local[*]") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .getOrCreate()

    year = str(year)

    url = f"https://ec.europa.eu/agrifood/api/dairy/prices?years={year}"

    df_pandas = pd.read_json(url)

    df_spark = spark.createDataFrame(df_pandas)

    df_drop_na = df_spark.dropna()

    df_cheese = df_drop_na.filter(col("product").isin("CHEDDAR","EDAM","GOUDA","EMMENTAL"))

    df = df_cheese.withColumn("Numbers",row_number().over(Window.partitionBy("memberStateName","product").orderBy("beginDate")))


    df_transformed = df.withColumn("Price_Numeric", regexp_replace(col("Price"), "[€,]", "").cast("double")).withColumn(
        "Date_Parsed", to_date(col("beginDate"), "dd/MM/yyyy")).withColumn("Plot_Group",
                                                                           concat(col("memberStateName"), lit(" - "),
                                                                                  col("product")))

    pdf = df_transformed.select("Date_Parsed", "Price_Numeric", "memberStateName", "product", "weekNumber").toPandas()

    fig = px.line(
        pdf,
        x="Date_Parsed",
        y="Price_Numeric",
        color="memberStateName",
        facet_row="product",
        markers=True,
        hover_name="memberStateName",
        hover_data={
            "Date_Parsed": "|%b %d, %Y",
            "Price_Numeric": ":.2f€",
            "weekNumber": True,
            "product": False
        },
        title="Interactive Dairy Price Trends"
    )

    fig.update_yaxes(matches=None, title_text="Price (€)")
    fig.update_layout(
        hovermode="x unified",
        height=800,
        legend_title="Countries",
        template="plotly_white"
    )

    return fig, df_cheese







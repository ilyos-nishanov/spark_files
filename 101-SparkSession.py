#%%
from pyspark.sql import SparkSession

#%%
spark = SparkSession.builder.appName("DataFrameSQL").getOrCreate()
# %%
print(spark)
# %%
spark
# %%
myRange = spark.range(1000).toDF("number")
myRange.collect()
# %% transformation egsample
divsByTwo=myRange.where("number % 2 = 0")
# divsByTwo.collect()
# will return no output bc we specified only an abstract transformation
# %% action example
divsByTwo.count()

# %%
flightData2015=spark\
                .read\
                .option("inferSchema", "True")\
                .option("header", "True")\
                .csv("/Users/ilyosnishanov/Spark-The-Definitive-Guide/data/flight-data/csv/2015-summary.csv")
# %% reading is also lazy transformation bc spark will not do anything
# unless we take an action e.g. show, take(into Python, Scala native dataframe) or
# write
flightData2015.count()
# %%
flightData2015.take(3)
# %%
flightData2015.sort("count").explain()
# %% change shuffle range from default 200 to 5
spark.conf.set("spark.sql.shuffle.partitions", "50")
# %%
flightData2015.sort("count").take(2)
# %% query with SQL
flightData2015.createOrReplaceTempView("flight_data_2015")

sqlWay = spark.sql("""
  SELECT DEST_COUNTRY_NAME, count(1)
  FROM flight_data_2015
  GROUP BY DEST_COUNTRY_NAME
  """)

dataFrameWay = flightData2015\
    .groupBy("DEST_COUNTRY_NAME")\
    .count()


sqlWay.explain()
dataFrameWay.explain()
'''
    as you can see the executing plan is the same for both
    sql and dataframe ways
'''
#%%
spark.sql("SELECT max(count) from flight_data_2015").take(1)

# %%
from pyspark.sql.functions import max
flightData2015.select(max("count")).take(1)
# %%
maxSql = spark.sql("""
SELECT DEST_COUNTRY_NAME, sum(count) as destination_total
FROM flight_data_2015
GROUP BY DEST_COUNTRY_NAME
ORDER BY sum(count) DESC
LIMIT 5
""")
maxSql.show()
# %%
from pyspark.sql.functions import desc
flightData2015\
    .groupBy("DEST_COUNTRY_NAME")\
    .sum("count")\
    .withColumnRenamed("sum(count)", "destination_total")\
    .sort(desc("destination_total"))\
    .limit(5)\
    .show()
# %% 
flightData2015

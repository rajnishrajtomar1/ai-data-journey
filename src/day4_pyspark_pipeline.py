from pyspark.sql import SparkSession
from pyspark.sql.functions import when, avg

# Create Spark session
spark = SparkSession.builder \
    .appName("Day4Pipeline") \
    .master("local[*]") \
    .config("spark.driver.host", "127.0.0.1") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    "data/sample.csv",
    header=True,
    inferSchema=True
)

# Add salary band column
df = df.withColumn(
    "salary_band",
    when(df.salary < 55000, "Low")
    .when(df.salary < 65000, "Medium")
    .otherwise("High")
)

# Filter rows
filtered = df.filter(df.age > 28)

# Aggregation
grouped = df.groupBy("salary_band") \
    .agg(avg("salary").alias("avg_salary"))

print("Full Data")
df.show()

print("Filtered Data")
filtered.show()

print("Average Salary By Band")
grouped.show()

# Stop Spark
spark.stop()
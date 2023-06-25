from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DoubleType,TimestampType


spark = SparkSession.builder.appName("ALS").getOrCreate()
# review_header = ["userId","movieId","rating","time_stamp"]
review_header = StructType([       
    StructField('userId', IntegerType(), True),
    StructField('movieId', IntegerType(), True),
    StructField('rating', DoubleType(), True),
    StructField('time_stamp', StringType(), True)])

def delimiter_split(line):
    arr = line.split("::")
    arr[0] = int(arr[0])
    arr[1] = int(arr[1])
    arr[2] = float(arr[2])
    # arr[0] = arr[3]
    return arr

review_df = spark.sparkContext.textFile("./ratings.dat").map(delimiter_split).toDF(schema = review_header)

# Split the ratings dataframe into training and test data
(training_data, test_data) = review_df.randomSplit([0.6, 0.4], seed=1234)

# Set the ALS hyperparameters
from pyspark.ml.recommendation import ALS
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", rank = 3, maxIter = 18, regParam = 0.1, coldStartStrategy="drop", nonnegative = True, implicitPrefs = False)

# Fit the mdoel to the training_data
model = als.fit(training_data)

# Generate predictions on the test_data
test_predictions = model.transform(test_data)

# pint("test_predictions")
# test_predictions.show()


# Import RegressionEvaluator
from pyspark.ml.evaluation import RegressionEvaluator

evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", 
predictionCol="prediction")

# Evaluate the "test_predictions" dataframe
RMSE = evaluator.evaluate(test_predictions)
print("RMSE ---->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",RMSE)

print("--------------- done successfully --------------- ")
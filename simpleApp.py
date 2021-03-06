"""simpleApp.py"""
from pyspark import SparkContext

logFile = "/Users/ErnestWu/Spark/spark-2.0.2-bin-hadoop2.7/README.md"
sc = SparkContext("local", "simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" %(numAs, numBs))

sc.stop()
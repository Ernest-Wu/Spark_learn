#! usr/bin/env bash

SPARK_HOME=/Users/ErnestWu/Spark/spark-2.0.2-bin-hadoop2.7

$SPARK_HOME/bin/spark-submit \
--master local[4] \
simpleApp.py

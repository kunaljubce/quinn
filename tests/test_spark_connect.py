import chispa
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

import quinn
from .spark import spark


def test_create_df():
    rows_data = [("abc", 1), ("lu", 2), ("torrence", 3)]
    col_specs = [("name", StringType()), ("age", IntegerType())]

    expected_schema = StructType(
        [
            StructField("name", StringType(), True),
            StructField("age", IntegerType(), True),
        ],
    )
    actual = quinn.create_df(spark, rows_data, col_specs)
    expected = spark.createDataFrame(rows_data, expected_schema)
    chispa.assert_df_equality(actual, expected)

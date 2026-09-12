from pyspark.sql.functions import unix_timestamp, col

def get_trip_duration_mins(spark, df, start_col, end_col, output_col):
    """
    Adds a column to the DataFrame calculating the difference in minutes between two timestamp columns.

    Parameters:
        spark: SparkSession object
        df: Spark DataFrame
        start_col (str): name of the column containing the start timestamp
        end_col (str): name of the column containing the end timestamp
        output_col (str): name of the resulting column
    
    Returns:
        Spark DataFrame with the additional column showing the difference in minutes
    """

    return df.withColumn(
        output_col,
        (unix_timestamp(col(end_col)) - unix_timestamp(col(start_col))) / 60
    )
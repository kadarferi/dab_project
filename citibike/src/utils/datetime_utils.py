from pyspark.sql.functions import current_timestamp, to_date, col

def timestamp_to_date_col(spark, df, timestamp_col, output_col):
    """
    Extracts the date from a timestamp column and adds it as a new column in the DataFrame.

    Parameters:
        spark: SparkSession object
        df (DataFrame): Input Spark DataFrame containing the timestamp.
        timestamp_col (str): The name of the timestamp column.
        output_col: The name of the new column with the ride date to be added.

    Returns:
        DataFrame: The modified DataFrame with the additional ride date column.
    """
    # Use to_date to extract the date part of the timestamp
    return df.withColumn(output_col, to_date(col(timestamp_col)))
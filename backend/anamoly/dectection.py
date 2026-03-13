#Here we detect anamolies from log data by comparing current errors and normal behavior using stastics 

import dask.dataframe as dd


def detect_anomaly(log_df, z_threshold=3):
    log_df["timestamp"] = dd.to_datetime(log_df["timestamp"])

    error_logs = log_df[log_df["level"] == "ERROR"]

    if error_logs.shape[0].compute() == 0:
        return error_logs.head(0)

    error_logs["minute"] = error_logs["timestamp"].dt.floor("min")

    error_counts = (
        error_logs
        .groupby("minute")
        .size()
        .rename("error_count")
        .reset_index()
    )

    mean = error_counts["error_count"].mean().compute()
    std = error_counts["error_count"].std().compute()

    if std == 0:
        return error_counts.head(0).compute()

    error_counts["anomaly_score"] = (error_counts["error_count"] - mean) / std
    error_counts["is_anomaly"] = error_counts["anomaly_score"].abs() > z_threshold

    return error_counts[error_counts["is_anomaly"]].compute()
#threshold value, error count based on minute and time stamp and absolute value
#in log level we have info,debug,errors and warning from log data in the part of levels
#level :
# 1. auth
# 2. errors
# 3. debug
# 4. warnings
#before filtering:
#10:01 ERROR
#10:01 INFO
#10:01 ERROR
#10:02 ERROR
#10:02 ERROR
#10:02 DEBUG
#After filtering:
#10:01 ERROR
#10:01 ERROR
#10:02 ERROR
#10:02 ERROR
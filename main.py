from backend.config.dask_config import create_dask_client
from backend.pipeline.processing import process_pipeline
from backend.anomaly.detection import detect_anomaly
from backend.config.email_config import send_anomaly_email
import time


ADMIN_EMAIL = "admin@example.com" 


def main():
    client = create_dask_client()
    print(client)
    print(f"Dashboard link: {client.dashboard_link}")
    print("\n" + "=" * 50)

    start = time.time()

    # Build log processing pipeline
    log_df = process_pipeline("backend/Sample_data/log_data.log")

    total_logs = log_df.count().compute()
    end = time.time()

    print("Total logs parsed:", total_logs)
    print("Time taken:", round(end - start, 2), "seconds")

    print("\n Running anomaly detection...")

    # Detect anomalies
    anomalies_df = detect_anomaly(log_df)

    #anomalies = anomalies_df.compute()
    anomalies = anomalies_df
    #print("Anomalies:",)
    if anomalies.empty:
        print("No anomalies detected")
    else:
        print(f"🚨 {len(anomalies)} anomalies detected!")

        for _, row in anomalies.iterrows():
            anomaly_data = {
                "timestamp": row["timestamp"],
                "error_count": row["error_counts"],
                "z_score": row["z_score"]
            }

            send_anomaly_email(
                to_email=ADMIN_EMAIL,
                anomaly=anomaly_data
            )

            print(
                f"📧 Alert sent | Time: {row['timestamp']} | "
                f"Errors: {row['error_count']}"
            )

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
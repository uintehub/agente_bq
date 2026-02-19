# tools.py
import os
import google.auth
from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset

def get_bigquery_toolset():
    """
    Creates and returns a configured BigQuery toolset.
    """

    credentials, default_project = google.auth.default()
    target_project_id = os.getenv("BQ_PROJECT_ID", default_project)
    
    if not os.getenv("BQ_DATASET_ID"):
        raise ValueError("BQ_DATASET_ID environment variable is missing.")

    print(f"--- Initializing BQ Tools for Project: {target_project_id} ---")

    if target_project_id:
        os.environ["GOOGLE_CLOUD_PROJECT"] = target_project_id

    credentials_config = BigQueryCredentialsConfig(
        credentials=credentials
    )

    return BigQueryToolset(
        credentials_config=credentials_config
    )
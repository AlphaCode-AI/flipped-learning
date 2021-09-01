import pandas as pd
from google.cloud import bigquery
from google.cloud import storage
import os


def upload_blob(GCS_BUCKET, storage_client, source_file_name, destination_blob_name):
    bucket_name = GCS_BUCKET
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


def load_gcs_to_bigquery(client, uri, table_id):
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    # job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    job_config.allow_quoted_newlines=True  ## Debbie & Charlie 
    job_config.autodetect=True
    if uri.split('.')[-1] == "json":
        job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    
    else:
        job_config.source_format = bigquery.SourceFormat.CSV

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  
    return load_job.result()  


def load_bigquery_to_excel_sheets(INPUT_DATA_PATH, OUTPUT_DATA_PATH, PROJECT_ID, GOOGLE_SERVICE_ACCOUNT_FILE, GCS_BUCKET, BIG_QUERY_DATASET, BIG_QUERY_TABLE):
    
    dataframe_of_multi_sheet = pd.read_excel(
        INPUT_DATA_PATH, 
        sheet_name=None, 
        header=None
    )
    sheets = dataframe_of_multi_sheet.keys()
    storage_client = storage.Client.from_service_account_json(
        GOOGLE_SERVICE_ACCOUNT_FILE
    )
    client = bigquery.Client.from_service_account_json(
        GOOGLE_SERVICE_ACCOUNT_FILE
    )

    if not os.path.isdir(OUTPUT_DATA_PATH):                                                           
        os.mkdir(OUTPUT_DATA_PATH)

    for i, sheet in enumerate(sheets):
        target_dataframe = dataframe_of_multi_sheet.get(sheet)
        new_columns = ["col_{}".format(i) for i in target_dataframe.columns]
        target_dataframe.columns = new_columns
        target_dataframe = target_dataframe.astype(str)
        server_output_path = "{}/{}_{}.csv".format(
            OUTPUT_DATA_PATH, 
            BIG_QUERY_TABLE,
            i+1
        )
        target_dataframe.to_csv(
            server_output_path,
            index=False, 
            encoding='utf-8-sig'
        )
        path_suffix = "pupledog/{}_{}.csv".format(
            BIG_QUERY_TABLE,
            i+1
        )
        upload_blob(
            GCS_BUCKET, 
            storage_client,
            source_file_name=server_output_path, 
            destination_blob_name=path_suffix
        )
        print("{} saving into GCS is done".format(
            i+1
        ))
        load_gcs_to_bigquery(
            client,
            uri='gs://{}/{}'.format(
                GCS_BUCKET, 
                path_suffix
            ), 
            table_id = '{}.{}.{}_{}'.format(
                PROJECT_ID, 
                BIG_QUERY_DATASET,
                BIG_QUERY_TABLE,
                i+1
            )
        )
        print("{} saving into BigQuery is done".format(i+1))


def main():

    # INPUT_DATA_PATH = "./data/wine_product.xlsx"  # Multi Sheet Excel File 
    INPUT_DATA_PATH = "./data/구독 배정 회원 리스트(21년)_20년 10월 이후.xlsx"
    INPUT_DATA_PATH = "./data/구독 배정 회원 리스트(20년)_10월이전.xlsx"
    
    OUTPUT_DATA_PATH = "./data_output"  # 아무거나 
    PROJECT_ID = "utopian-surface-268707"
    GOOGLE_SERVICE_ACCOUNT_FILE="./config/{}-service-account.json".format(PROJECT_ID) # Service Account File Name
    GCS_BUCKET = "automl_usc_inseon" # Bucket Name 
    BIG_QUERY_DATASET = "IS_USC" # BigQuery Dataset name
    BIG_QUERY_TABLE = "ASSIGNMENT_BEFORE" # BigQuery Table name / Name 

    load_bigquery_to_excel_sheets(
        INPUT_DATA_PATH, 
        OUTPUT_DATA_PATH, 
        PROJECT_ID, 
        GOOGLE_SERVICE_ACCOUNT_FILE, 
        GCS_BUCKET, 
        BIG_QUERY_DATASET,
        BIG_QUERY_TABLE
    )


if __name__ == "__main__":
    main()

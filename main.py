from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():

    data = extract_data()

    df = transform_data(data)

    load_data(df)

    print("ETL Pipeline executed successfully")

if __name__ == "__main__":
    run_pipeline()
from sqlalchemy import create_engine
from config import DB_SERVER, DB_NAME

def load_data(df):

    connection_string = f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

    engine = create_engine(connection_string)
    
    df.to_sql("weather_data", engine, if_exists="append", index=False)
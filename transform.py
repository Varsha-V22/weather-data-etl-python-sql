import pandas as pd 

def transform_data(data):
    df = pd.DataFrame([data])

    df["city"] = "Mumbai"

    df = df[["city","temperature","wind_speed"]]

    return df

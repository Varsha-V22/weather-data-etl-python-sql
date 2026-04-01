
CREATE TABLE weather_data (
    city VARCHAR(50),
    temperature FLOAT,
    wind_speed FLOAT,
    created_at DATETIME DEFAULT GETDATE()
);
CREATE TABLE IF NOT EXISTS divvy_database.public."raw_ride_data"(
ride_id VARCHAR(20)  NOT NULL PRIMARY KEY, 
rideable_type VARCHAR(20)  NULL, 
started_at TIMESTAMP  NOT NULL,
ended_at TIMESTAMP  NOT NULL,
start_station_name VARCHAR(20) NULL,
start_station_id VARCHAR(20) NULL,
end_station_name VARCHAR(20) NULL,
end_station_id VARCHAR(20) NULL,
start_lat DOUBLE PRECISION NULL,
start_lng DOUBLE PRECISION NULL,
end_lat DOUBLE PRECISION NULL,
end_lng DOUBLE PRECISION NULL,
member_casual VARCHAR(20) NULL
);

CREATE TABLE IF NOT EXISTS divvy_database.public."raw_station"(
station_id VARCHAR(20)  NOT NULL PRIMARY KEY, 
station_name VARCHAR(50)  NULL);

-- DROP TABLE divvy_database.public."raw_ride_data";

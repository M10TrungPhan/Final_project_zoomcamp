import os

# Download for Cycle data 
for year in [2022, 2023]:
    for month in range(1,13):
        month = "{:02}".format(month)
        name_file = f"{str(year)}{month}-divvy-tripdata.zip"
        if name_file in os.listdir():
            continue
        url = f"https://divvy-tripdata.s3.amazonaws.com/{name_file}"
        if url is not None:
            print(f"--- Data is crawling {name_file} ---")
            os.system(f"curl {url} -o {name_file}")
            os.system(f"tar -xf {name_file}")
            print(f"--- Crawl {name_file} has done ---")
        # break

# Download for Categoridata
url = "https://divvy-tripdata.s3.amazonaws.com/Divvy_Stations_Trips_2013.zip"
name_file = "Divvy_Stations_Trips_2013.zip"
os.system(f"curl {url} -o {name_file}")
os.system(f"tar -xf {name_file}")


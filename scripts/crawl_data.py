import os
import time 
folder_data = './data/raw/'
# print(os.getcwd())
# print(os.listdir(folder_data))
# time.sleep(10)
# Download for Cycle data 
for year in [2022, 2023]:
    for month in range(1,13):
        month = "{:02}".format(month)
        name_file_download = f"{str(year)}{month}-divvy-tripdata.zip"
        name_file_format = f"{str(year)}{month}-divvy-tripdata.csv"
        
        if name_file_download not in os.listdir(folder_data):
            print(f"--- Data is crawling {name_file_download} ---")
            url = f"https://divvy-tripdata.s3.amazonaws.com/{name_file_download}"
            # os.system(f"curl {url} -o {folder_data}{name_file_download}")
            os.system(f"wget {url} -O {folder_data}{name_file_download}")

            
        if name_file_format not in os.listdir(folder_data):
            print(f"--- Extract file {name_file_download} to {name_file_format} ---")
            # os.system(f"tar -xf {folder_data}{name_file_download} -C {folder_data}{name_file_download}")
            os.system(f"unzip -u {folder_data}{name_file_download} -d {folder_data}")

            # unzip -o 202209-divvy-tripdata.zip -d ./

        name_file_alias = f"{str(year)}{month}-divvy-publictripdata.csv"
        if name_file_alias in os.listdir(folder_data):
            os.system(f"mv {folder_data}{name_file_alias} {folder_data}{name_file_format}")
            
        print(f"--- Crawl {name_file_download} has done ---")
        print("_________________________________________________________________________________")
        # break
    # break

os.system(f"rm -r {folder_data}__MACOSX")
# Download for Categoridata
# url = "https://divvy-tripdata.s3.amazonaws.com/Divvy_Stations_Trips_2013.zip"
# name_file = "Divvy_Stations_Trips_2013.zip"
# os.system(f"curl {url} -o {name_file}")
# os.system(f"unzip -u {folder_data}{name_file_download} -d {folder_data}{name_file_download}")


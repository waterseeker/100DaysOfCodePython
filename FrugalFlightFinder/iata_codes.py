import pandas as pd
import numpy as np

# ident,type,name,elevation_ft,continent,iso_country,iso_region,municipality,gps_code,iata_code,local_code,coordinates

iata_data = pd.read_csv("airport-codes_csv.csv", sep=",")
cleaned = iata_data.drop(columns=["ident", "elevation_ft", "continent", "iso_region", "gps_code", "local_code", "coordinates"]).dropna()
# drop rows where "type" == "closed"
df = cleaned[cleaned.type != "closed"]
df.drop(df.index)
index_names = df[df['type'] == 'heliport'].index
df.drop(index_names, inplace=True)
df.to_csv("cleaned.csv", header=True, index=False)

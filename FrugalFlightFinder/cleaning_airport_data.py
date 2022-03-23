import pandas as pd

# ident,type,name,elevation_ft,continent,iso_country,iso_region,municipality,gps_code,iata_code,local_code,coordinates

iata_data = pd.read_csv("airport-codes.csv", sep=",")
# drop columns that aren't needed
dropped_columns = iata_data.drop(columns=["ident", "elevation_ft", "continent", "iso_region", "gps_code", "local_code", "coordinates"]).dropna()
# drop heliport, seaplane base, and closed types of airports
drop_values = ["heliport", "seaplane_base", "closed"]
cleaned_df = dropped_columns[~dropped_columns.type.isin(drop_values)]
cleaned_df.to_csv("cleaned_airport_data.csv", header=True, index=False)

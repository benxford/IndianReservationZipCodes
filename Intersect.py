import geopandas as gpd
import json

g1 = gpd.GeoDataFrame.from_file("Census_ZIP_Code_Tabulation_Areas_2010_v1_1429771311909979270\\Census_ZIP_Code_Tabulation_Areas.shp")
g2 = gpd.GeoDataFrame.from_file("Federal_American_Indian_Reservations_v1_-572380202586076551\\Federal_American_Indian_Reservations.shp")
data = []
for index, ir in g2.iterrows():
    for index2, zc in g1.iterrows():
       if ir['geometry'].intersects(zc['geometry']):
          data.append({'IndianReservation':ir['BASENAME'], 'ZipCode': zc['BASENAME']})
with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
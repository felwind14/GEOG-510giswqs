print("hello world")


import geopandas as gpd

# Read in the two shapefiles that you want to merge
file1 = gpd.read_file('path/to/file1.shp')
file2 = gpd.read_file('path/to/file2.shp')

# Merge the two shapefiles together
merged_file = gpd.GeoDataFrame(pd.concat([file1, file2], ignore_index=True), crs=file1.crs)

# Write the merged shapefile to disk
merged_file.to_file('path/to/merged_file.shp', driver='ESRI Shapefile')


import arcpy

# Set workspace
arcpy.env.workspace = "C:/path/to/geodatabase.gdb"

# Input feature class name
input_fc = "feature_class_name"

# Output shapefile
output_shapefile = "C:/path/to/output/folder/output_shapefile.shp"

# Convert feature class to shapefile
arcpy.FeatureClassToShapefile_conversion(input_fc, output_shapefile)

    
import geopandas as gpd

# Read KML file using the KML driver
gdf = gpd.read_file("Japan.kml", driver='KML')

# Extract coordinates
coordinates = []
for geometry in gdf.geometry:
    if geometry.type == 'Point':
        coordinates.append((geometry.x, geometry.y))  # For Point geometry
    elif geometry.type == 'LineString':
        coordinates.extend(geometry.coords)  # For LineString geometry
    elif geometry.type == 'Polygon':
        coordinates.extend(geometry.exterior.coords)  # For Polygon geometry

# Print or process the coordinates as needed
for coord in coordinates:
    print(coord)
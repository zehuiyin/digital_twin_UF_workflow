import arcgis

gis = arcgis.GIS(url=<organization_arcgis_portal>>, username='', password='', profile='learn_user')
gis = arcgis.GIS("pro", profile='learn_user')
print("authentication from ArcGIS pro complete")

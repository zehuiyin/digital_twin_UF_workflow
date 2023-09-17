cd <directory where you store your download_request_example.py>
call "%PROGRAMFILES%\ArcGIS\Pro\bin\Python\Scripts\propy" download_request_example.py
cd <directory where you store your converters>
call "%PROGRAMFILES%\ArcGIS\Pro\bin\Python\Scripts\propy" Json2GeoJSON.py <location of your downloaded json file>
cd <directory where you store your OverwriteFS.py and auth_arcgis_locally.py>
call "%PROGRAMFILES%\ArcGIS\Pro\bin\Python\Scripts\propy" auth_arcgis_locally.py
call "%PROGRAMFILES%\ArcGIS\Pro\bin\Python\Scripts\propy" OverwriteFS.py learn_user <ID> <Name> <location of your downloaded json file>
#!/bin/bash

for file in $(find ~/jjfast/brasil/*shp); do
    echo $file
    #unzip $file -d ~/jjfast/brasil/
    ogr2ogr -f 'GPKG' -update -append ~/jjfast/brasil_deforestation.gpkg $file
done;



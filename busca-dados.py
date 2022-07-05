"""

Version 0:

    - almost automatizaded
    - Input needed of coordinates
    - Connection problem.
    - Files names of the loops in the directory of the latitude names

Version 01:

    - Json file; All brazil's coordinates
    - Less script in the main file
    - Automatization process
    - Files with the real name, in a unique directory (facilitation to polygonize or open in Qgis with terminal)
    - Solve connection problem
    - Pep8 Formatation
    - Translate to English
    - Comment Project


"""
#  IMPORTAÇÕES
import json
import requests
from bs4 import BeautifulSoup
from functions_Objects import GetLink, downloads, jsonfile, CreateDir, downLinks, openable

path = CreateDir()

for loopname, latitude in jsonfile('file.json'):

    print(latitude)

    # get all longitudes and return a list, and respective url.
    soup, url = downLinks(latitude)

    file = open("longfile.json")
    x = json.load(file)
    longname = x[loopname]  # json dictionary name

    if soup.find(longname):
        print('Value found')
        longitudes = longname.split(' ')

        #years_url = []
        #fileYearPaths = []
        for i in longitudes:
            print(i)
            try:
                fileYearPath = url + i + '/'
                print(fileYearPath)
                view = requests.get(fileYearPath)
                status = view.status_code

                if status == 404:
                    print("Not exists")
                    continue
                else:
                    html = view.text
                    year_url = BeautifulSoup(html, 'html.parser')

                    # get all the files (between 2021 - 2022),  the subdir(brasil) path and return
                    dates, subdir = openable(year_url, path)

                    # Check if the file alwery exists in local file and if not download.
                    downloads(dates, subdir, fileYearPath)

            except Exception as e:
                print(e)
    else:
        print("Something is Wrong. This Longitude isn't exists: %s" % longname)

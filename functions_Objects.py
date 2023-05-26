"""
function in used, pay attention when modify names or change something

"""
import json
import os
import errno
from bs4 import BeautifulSoup
import requests
import sys

def jsonfile(name):
    k = open(name)
    file = json.load(k)
    for i in file:
        listar = file['%s' % (i)]
        y = listar.split(' ')
        yield (i, y)


def CreateDir():
    try:
        mylocal = str(os.path.expanduser('~'))
        directory = "jjfast"
        path = os.path.join(mylocal, directory)
        os.mkdir(path)
    except OSError as err:
        if err.errno == errno.EEXIST:
            print("Directory Alredy exist")
        return path
    return path


def downLinks(lista):
    for i in lista:
        url_t = 'https://www.eorc.jaxa.jp/jjfast/data_private/shape/'+i + '/'
        visualizar_url = requests.get(url_t)
        print(visualizar_url.status_code)
        view1 = visualizar_url.text
        soup = BeautifulSoup(view1, 'html.parser')
        return GetLink(soup), url_t


def GetLink(bs4):
    string = ''
    for links in bs4.find_all('a'):
        string += links.get('href')
    return string


def openable(soup, path):
    links = []
    loop = 0
    for a in soup.find_all('a'):
        links.append(a.get('href'))

    count = 0
    dates = []
    for y in links:
        name = links[count]
        searchfor = name.find('_21')
        searchfor2 = name.find('_22')
        searchfor3 = name.find('_23')

        if searchfor != -1 or searchfor2 != -1 or searchfor3 != -1:
            print(name)
            dates.append(name)
        count += 1
    try:
        name_subdir = 'brasil'
        subdir = os.path.join(path, name_subdir)
        os.mkdir(subdir)
    except OSError as err:
        if err.errno == errno.EEXIST:
            print("Directory Alredy exist")
    return dates, subdir


def downloads(dates, subdir, fileYearPath):
    loop = 0
    for names in dates:
        try:
            filepath = subdir + '/' + names
            print(filepath)

            if os.path.isfile(filepath) == True:
                print('this file alredy exists')
                continue

            else:
                url = fileYearPath + '/' + names
                print(url)
                result = requests.get(url, allow_redirects=True, verify=False)
                open(filepath, 'wb').write(result.content)

        except Exception as e:
            print(e, '\n')
            sys.exit("exiting")

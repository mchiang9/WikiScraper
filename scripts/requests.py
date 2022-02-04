import json
import requests
from bs4 import BeautifulSoup

def getCharacterNamesFromListFist(mediaName: str) -> [str]:
    with open("config/fistListConfig.json", "r") as jsonFile:
        data = json.load(jsonFile)
        print("Read fistListConfig.json successfully")
        url = data[mediaName]["url"]
        tableId = data[mediaName]["tableId"]
        nameType = data[mediaName]["nameType"]
        nameClass = data[mediaName]["nameClass"]
        jsonFile.close()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find(id=tableId)
    characterElements = table.find_all(nameType, class_=nameClass)

    names = []
    for characterElement in characterElements:
        names.append(characterElement.text)

    return names

def getCharacterImageUrlFromFandomWiki(url: str) -> str:
    page = requests.get(url)
    if page.status_code != 200:
        raise Exception('Page does not exist')
    soup = BeautifulSoup(page.content, "html.parser")

    content = soup.find(id="content")
    imageTabs = content.find_all("div", class_="wds-tab__content wds-is-current")
    if imageTabs is not None:
        images = imageTabs[0].find_all("img", class_="pi-image-thumbnail")
        imageUrl = images[0]["src"]
    else:
        image = content.find_all("img", class_="pi-image-thumbnail")[0]
        imageUrl = image[0]["src"]
    return imageUrl

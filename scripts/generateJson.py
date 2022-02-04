import json

from scripts.requests import getCharacterImageUrlFromFandomWiki

def getFandomWikiUrl(mediaName: str) -> str:
    with open("config/fandomWikiaConfig.json", "r") as jsonFile:
        data = json.load(jsonFile)
        print("Read fandomWikiaConfig.json successfully")
        baseUrl = data[mediaName]["url"]
        jsonFile.close()
    return baseUrl

def getCharacterImages(mediaName: str, names: str) -> dict:
    nameImageUrlDic = {}
    baseUrl = getFandomWikiUrl(mediaName)
    for name in names:
        url = baseUrl + name
        try:
            imageUrl = getCharacterImageUrlFromFandomWiki(url)
            nameImageUrlDic[name] = imageUrl
        except Exception:
            continue
    return nameImageUrlDic

def updateJsonFile(fileName: str, nameImageUrlDic: dict) -> None:
    with open(fileName, "w") as jsonFile:
        json_object = json.dump(nameImageUrlDic, jsonFile) 
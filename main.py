import argparse

from scripts.requests import getCharacterNamesFromListFist
from scripts.generateJson import getCharacterImages, updateJsonFile

def main():
    parser = argparse.ArgumentParser(description="Scrape names from ListFist website and pull imageUrls from Fandom Wiki for a particular media.\nCurrently only medias in the Config files are supported.")
    parser.add_argument("mediaName", type=str, default="OnePiece", help="Name of media franchise. Must have a ListFist and Fandom Wiki site.\nWill also need to update fistListConfig and fandomWikiaConfig files before running script if adding new media franchises.")
    parser.add_argument("outputFile", type=str, help="Json Output file name to dump names and image urls")
    args = parser.parse_args()
    mediaName = args.mediaName
    outputFile = args.outputFile
    print("Fetching character names from ListFist for {}".format(mediaName))
    names = getCharacterNamesFromListFist(mediaName)
    print("Fetching character image from Fandom Wiki and mapping to each name")
    nameImageUrlDic = getCharacterImages(mediaName, names)
    print("Saving results in output json file")
    updateJsonFile(outputFile, nameImageUrlDic)

if __name__ == "__main__":
    main()
import re

strList = ["tên quốc gia", "tiêu ngữ"]
countryList = ['Armenia']


def getLocation(text):
    y = text.title()
    result = ""
    for country in countryList:
        if re.findall(country, y):
            result = country
    return result


def getDetermine(text):
    index = -1
    for i in strList:
        if re.match(i, text.lower()):
            index = strList.index(i)
    return index

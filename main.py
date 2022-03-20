import json
from pprint import pprint
import xml.etree.ElementTree as ET

def read_json():
    with open("newsafr.json", encoding="utf-8") as js:
        data = json.load(js)
    news = data["rss"]["channel"]["items"]
    set_news = set()
    list_all = []
    for new in news:
        list_new = new["description"].split(" ")
        for word in list_new:
            if len(word) > 6:
                set_news.add(word)
                list_all.append(word)
    list_count = []
    for set_word in set_news:
        list_count.append([set_word, list_all.count(set_word)])
    list_count = sorted(list_count, key=lambda x: x[1], reverse=True)
    print("ТОП 10 слов длиннее 6 букв из JSON:")
    for i in range(10):
        print(list_count[i][0])
    return

def read_xml():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    # print(root.attrib)
    news_xml = root.findall("channel/item")
    # print(len(news_xml))
    set_news_xml = set()
    list_all_xml = []
    for news in news_xml:
        list_new_xml = news.find("description").text.split()
        # print(list_new)
        for word in list_new_xml:
            if len(word) > 6:
                set_news_xml.add(word)
                list_all_xml.append(word)
    list_count_xml = []
    for set_word_xml in set_news_xml:
        list_count_xml.append([set_word_xml, list_all_xml.count(set_word_xml)])
    list_count_xml = sorted(list_count_xml, key=lambda x: x[1], reverse=True)
    print("ТОП 10 слов длиннее 6 букв из XML:")
    for i in range(10):
        print(list_count_xml[i][0])
        # print(news.find("description").text)
        # print()
    return

if __name__ == '__main__':
    read_json()
    print()
    read_xml()






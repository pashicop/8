import json
from pprint import pprint

if __name__ == '__main__':
    with open("newsafr.json", encoding="utf-8") as js:
        # data = js.readlines()
        data = json.load(js)
    # pprint(data)
    # for news in data:
    news = data["rss"]["channel"]["items"]
    # print(news)
    # print(news["description"])
    set_news = set()
    list_all = []
    for new in news:
        list_new = new["description"].split(" ")
        for word in list_new:
            if len(word) > 6:
                set_news.add(word)
                list_all.append(word)
    # print(len(set_news))
    # print(len(list_all))
    list_count = []
    for set_word in set_news:
        list_count.append([set_word, list_all.count(set_word)])
    list_count = sorted(list_count, key=lambda x: x[1], reverse=True)
    print("ТОП 10 слов длиннее 6 букв")
    for i in range(10):
        print(list_count[i][0])





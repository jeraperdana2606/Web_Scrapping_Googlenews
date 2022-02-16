from pygooglenews import GoogleNews
import pandas as pd



gn = GoogleNews(lang = 'id',country = 'ID')


def get_titles(search):
    datas = []
    search = gn.search(search)
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'title' : item.title,
            'link': item.link
        }
        datas.append(story)
    return datas

datas = get_titles('edukasi')
pd.DataFrame(datas).to_csv("result_list.csv")
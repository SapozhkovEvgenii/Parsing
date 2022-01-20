from modules import class_parent, show


class NewsFCArsenal(class_parent.Parse):

    def parser(self):
        list_news = []
        news = self.response()
        for elem_news in news:
            elem_news = elem_news.find("span", class_="field-content")
            list_news.append(elem_news.text)
        return list_news

    def __iter__(self):
        self.cursor = 0
        self.lenght = len(self.parser())
        return self

    def __next__(self):
        if self.cursor < self.lenght:
            try:
                return self.parser()[self.cursor]
            finally:
                self.cursor += 1
        raise StopIteration


my_url = "https://fc-arsenal.com/news/all"
my_selector = "#views-bootstrap-arkhiv-novostey-page-1 > div > div"

with NewsFCArsenal(my_url, my_selector) as news_fcarsenal:
    news_fcarsenal.parser()

for el in news_fcarsenal:
    show.show(el)

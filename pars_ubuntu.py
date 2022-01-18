from modules import class_parent, show


class InfoUbuntu(class_parent.Parse):

    def parser(self):
        list_news = []
        news = self.response()
        for elem_news in news:
            elem_news = elem_news.find_all("div", class_="level2")[0]
            for i in elem_news:
                list_news.append(i.text)
        return list_news

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor < len(self.parser()):
            try:
                return self.parser()[self.cursor]
            finally:
                self.cursor += 1
        raise StopIteration


my_url = "https://ubuntu.ru/about"
my_selector = "#__main > div.content > div"

with InfoUbuntu(my_url, my_selector) as info_ubuntu:
    info_ubuntu.parser()

for el in info_ubuntu:
    show.show(el)


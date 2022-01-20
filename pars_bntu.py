from modules import class_parent, show


class InfoBNTU(class_parent.Parse):

    def parser(self):
        list_news = []
        news = self.response()
        for elem_news in news:
            elem_news = elem_news.find("b")
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


my_url = "https://bntu.by/faculties/atf/specialties"
my_selector = "body > content > div.container.faculty.blockWithColumn > div.facultyLeft > div.fsdescblock > div"

with InfoBNTU(my_url, my_selector) as info_bntu:
    info_bntu.parser()

for el in info_bntu:
    show.show(el)

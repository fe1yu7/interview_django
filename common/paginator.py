from django.core import paginator


class Page(object):
    def __init__(self, objs, page, size):
        self.objs = objs
        self.paginator = paginator.Paginator(objs, size)
        self.page = self.paginator.page(page)
        self.count = self.paginator.count
        self.num_pages = self.paginator.num_pages
        self.per_page = self.paginator.per_page
        self.data = self.page.object_list
        self.cur_page = self.page.number


pages = Page

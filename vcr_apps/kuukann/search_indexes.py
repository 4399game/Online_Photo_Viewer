from haystack import indexes

from .models import Img, Pic

class ImgIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    tiny_img = indexes.CharField(model_attr = 'tiny_img')

    def get_model(self):
        return Img
    def index_queryset(self, using=None):
        return self.get_model().manager_one.all()

class PicIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr = 'name')

    def get_model(self):
        return Pic
    def index_queryset(self, using=None):
        return self.get_model().manager_one.all()
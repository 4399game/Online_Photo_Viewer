from haystack import indexes

from .models import Station

class StationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    station_pic = indexes.CharField(model_attr = 'pic')
    station_img = indexes.CharField(model_attr = 'img')

    def get_model(self):
        return Station

    def index_queryset(self, using=None):
        return self.get_model().manager_one.filter(status = True)
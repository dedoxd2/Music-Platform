import django_filters
from .models import Album


class AlbumFilter(django_filters.FilterSet):
 #   cost = django_filters.RangeFilter()

    class Meta:
        model = Album
        fields = {"name": ['icontains'], "cost": ["lte", 'gte']}

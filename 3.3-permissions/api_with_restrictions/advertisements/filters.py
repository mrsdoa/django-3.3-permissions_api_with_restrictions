from django_filters import rest_framework as filters
from django_filters import rest_framework as filters

from advertisements.models import Advertisement

User = get_user_model()

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    creator = filters.ModelChoiceFilter(queryset=User.objects.all())
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
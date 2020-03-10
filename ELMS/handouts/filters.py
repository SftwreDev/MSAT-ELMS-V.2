import django_filters


from .models import Handouts

class HandoutsSearch(django_filters.FilterSet):
    class Meta:
        model = Handouts
        fields = {'name' : ['icontains']}

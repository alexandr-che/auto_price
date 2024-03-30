from django.core.paginator import Paginator
from django.shortcuts import render
from adverts.filters import SmallFilterAdverts
from adverts.models import Advert


def index(request):
    adverts = Advert.objects.all()
    new_adverts = Advert.objects.order_by('-date_published')[:5]
    car_filter = SmallFilterAdverts(request.GET, queryset=adverts)

    paginator = Paginator(adverts.order_by('-pk'), 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Auto Price',
        'cars': adverts,
        'new_adverts': new_adverts,
        'car_filter': car_filter,
        'page_obj': page_obj
    }
    return render(request, 'index/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'description': 'Здесь какое-то описание для страницы "О нас"'
    }
    return render(request, 'index/about.html', context)

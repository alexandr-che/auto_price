from django.db.models import Q
from adverts.models import Advert


def q_search(query):
    
    words = [word for word in query.split() if len(word) > 2]

    q_obj = Q()

    for word in words:
        if word.isdigit() and len(word) == 4:
            q_obj &= Q(year=word)
        q_obj |= Q(brand__name__icontains=word)
        q_obj |= Q(model__name__icontains=word)

    return Advert.objects.filter(q_obj)

#Полнотекстовый поиск от Django. Умеет искать не просто по вхождению, а по вероятному совпадению слов
#Отлично подходит для описания товаров и сложных названий товаров

# from django.contrib.postgres.search import SearchVector
# return Car.objects.annotate(search=SearchVector('brand', 'model', 'year')).filter(search=query)
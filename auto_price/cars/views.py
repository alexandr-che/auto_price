# from django.core.paginator import Paginator
# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib import messages
# from cars.forms.create_advert import CreateAdvertForm
# from cars.forms.load_photo import LoadPhotoForm
# from cars.filters import SmallCarFilter, BigCarFilter
# from cars.search import q_search
# from cars.models import Car, ImageAuto


# def create_advert(request):
#     if request.method == "POST":
#         form = CreateAdvertForm(request.POST)
#         form_load_photo = LoadPhotoForm(request.POST, files=request.FILES)

#         print(form.is_valid(), form_load_photo.is_valid())

#         if form.is_valid() and form_load_photo.is_valid():

#             files = request.FILES.getlist('image')
#             car_id = form.save().pk
#             car = Car.objects.get(pk=car_id)

#             for file in files:
#                 ImageAuto(car=car, image=file).save()

#             messages.success(request,'Объявление успешно добавлено')
#             return redirect("index:index")
#     else:
#         form = CreateAdvertForm()
#         form_load_photo = LoadPhotoForm()

#     context = {
#         "title": "Создать объявление",
#         "form": form,
#         "form_load_photo": form_load_photo,
#     }

#     return render(request, "cars/create_advert.html", context)


# def filter_cars(request):

#     car_filter = SmallCarFilter(request.GET, queryset=Car.objects.all())

#     paginator = Paginator(car_filter.qs, 8)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     context = {
#         "title": "Поиск по фильтрам",
#         "page_obj": page_obj,
#         "car_filter": car_filter,
#     }

#     return render(request, "cars/filter_cars.html", context)


# def big_filter_car(request):
    
#     query = request.GET.get('q')

#     if query:
#         qs = q_search(query)

#     else:
#         qs = Car.objects.all()

#     if request.method == "POST":
#         big_filter_car = BigCarFilter(request.POST, queryset=Car.objects.all())
#     else:
#         big_filter_car = BigCarFilter(request.GET, queryset=qs)

#     paginator = Paginator(big_filter_car.qs, 8)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     context = {
#         "title": "Поиск по фильтрам", 
#         "big_filter_car": big_filter_car,
#         "page_obj": page_obj
#         }

#     return render(request, "cars/big_filter_cars.html", context)


# def car(request, slug):

#     car = get_object_or_404(Car, slug=slug)

#     context = {"title": f"{car.brand} {car.model}", "car": car}

#     return render(request, "cars/car.html", context)


# def car_add(request): ...

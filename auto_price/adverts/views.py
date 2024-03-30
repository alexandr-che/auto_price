from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from adverts.forms import CreateAdvertForm
from adverts.models import Advert, ImageAdvert, FavoriteAdvert
from adverts.filters import SmallFilterAdverts, BigFilterAdverts
from adverts.search import q_search


class AdvertCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = ''
    model = Advert
    form_class = CreateAdvertForm
    template_name = 'adverts/create_advert.html'
    success_url = reverse_lazy('index:index')
    success_message = 'Объявление добавлено!'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить новое объявление'
        return context

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('image')
        if form.is_valid():
            advert = form.save()
            user = self.request.user
            advert.user = user
            advert.save()
            if files:
                for f in files:
                    ImageAdvert(advert=advert, image=f).save()
            return self.form_valid(form)
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
        

class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'adverts/detail_advert.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        obj = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = f'{obj.brand} {obj.model}'
        context['car_filter'] = SmallFilterAdverts(self.request.GET, queryset=Advert.objects.all())
        if self.request.user.is_authenticated:
            context['user_favorite_adverts'] = [fav.advert.id for fav in self.request.user.favorite_user.all()]
        return context


class AdvertListView(ListView):
    model = Advert
    paginate_by = 8 
    template_name = 'adverts/list_adverts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все объявления'
        context['car_filter'] = SmallFilterAdverts(self.request.GET, queryset=Advert.objects.all())
        if self.request.user.is_authenticated:
            context['user_favorite_adverts'] = [fav.advert.id for fav in self.request.user.favorite_user.all()]
        return context
    
    def get_queryset(self):
        return SmallFilterAdverts(self.request.GET, queryset=Advert.objects.all()).qs    


class AdvertUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    redirect_field_name = ''
    model = Advert
    template_name = 'adverts/update_advert.html'
    form_class = CreateAdvertForm
    success_url = reverse_lazy('users:profile')
    success_message = 'Объявление изменено!'

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise Http404
        return obj



class AdvertDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = ''
    model = Advert
    template_name = 'adverts/delete_advert.html'
    success_url = reverse_lazy('users:profile')
    success_message = 'Объявление удалено!'
    

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise Http404
        return obj


def big_filter_ad(request):
        
    query = request.GET.get('q')

    if query:
        qs = q_search(query)
    else:
        qs = Advert.objects.all()

    if request.method == "POST":
        big_filter_car = BigFilterAdverts(request.POST, queryset=Advert.objects.all())
    else:
        big_filter_car = BigFilterAdverts(request.GET, queryset=qs)

    paginator = Paginator(big_filter_car.qs, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "title": "Поиск по фильтрам", 
        "big_filter_car": big_filter_car,
        "page_obj": page_obj,
        }
    
    if request.user.is_authenticated:
        context["user_favorite_adverts"] = [fav.advert.id for fav in request.user.favorite_user.all()]

    return render(request, 'adverts/filters/big_filter.html', context)


#работа с избранными объявлениями
def del_advert_from_favorites(request):
    id = request.POST.get('advert_id')
    user = request.user
    FavoriteAdvert.objects.get(user=user, advert=id).delete()

    return redirect(request.META['HTTP_REFERER'])


def add_advert_from_favorites(request):
    id = request.POST.get('advert_id')
    advert = Advert.objects.get(pk=id)
    user = request.user
    FavoriteAdvert.objects.create(user=user, advert=advert).save()

    return redirect(request.META['HTTP_REFERER'])
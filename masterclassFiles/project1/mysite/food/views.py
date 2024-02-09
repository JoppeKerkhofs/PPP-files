from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    food_list = Item.objects.all()
    return render(request, 'food/index.html', {'food_list': food_list})

def item(request, id):
    # get the item by id
    item = Item.objects.get(id=id)
    return render(request, 'food/item.html', {'item': item})

class IndexClassView(ListView):
    template_name = 'food/index.html'
    context_object_name = 'food_list'

    def get_queryset(self):
        return Item.objects.all()
    
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/item.html'
from django.shortcuts import render, get_object_or_404
from .models import ItemSet

def home(request):
    sets = ItemSet.objects.all()
    template_vars = { 'sets': sets }
    return render(request, 'prioritize/home.html', template_vars)

def set_home(request, set_id):
    item_set = get_object_or_404(ItemSet, id=set_id)
    items = item_set.items.all()
    template_vars = {
        'items': items,
        'set': item_set,
    }
    return render(request, 'prioritize/set_home.html', template_vars)

def compare(request, set_id):
    item_set = get_object_or_404(ItemSet, id=set_id)
    items=item_set.items.all().order_by('?')

    template_vars = {
        'items': items,
        'set': item_set,
    }
    return render(request, 'prioritize/compare.html', template_vars)

from django.shortcuts import render, get_object_or_404
from .models import ItemSet, Item

def home(request):
    if request.method=='POST':
        item_set = ItemSet(
            title=request.POST['title'],
            question=request.POST['question']
        )
        item_set.save()
    sets = ItemSet.objects.all()
    template_vars = { 'sets': sets }
    return render(request, 'prioritize/home.html', template_vars)

def set_home(request, set_id):
    item_set = get_object_or_404(ItemSet, id=set_id)

    if request.method=='POST':
        item = Item(
            title=request.POST['title'],
            description=request.POST['description'],
            set=item_set
        )
        item.save()

    items = item_set.items.all().order_by('-score')
    template_vars = {
        'items': items,
        'set': item_set,
    }
    return render(request, 'prioritize/set_home.html', template_vars)

def compare(request, set_id):
    if request.method=='POST':
        winner = get_object_or_404(
            Item,
            id=request.POST['winner']
        )
        loser = get_object_or_404(
            Item,
            id=request.POST['loser']
        )
        process_elo_compare(winner, loser)

    item_set = get_object_or_404(ItemSet, id=set_id)
    items=list(item_set.items.order_by('?')[0:2])

    template_vars = {
        'items': items,
        'set': item_set,
    }
    return render(request, 'prioritize/compare.html', template_vars)

def process_elo_compare(winner, loser):
    '''
    From wikipedia:
    Ea = 1/(1 + 10 ^ ((Rb-Ra) / 400) )
    Eb = 1/(1 + 10 ^ ((Ra-Rb) / 400) )
    Ex is the expected probability that X will win the match. Ea + Eb = 1. Rx is the rating of X, which changes after every match, according to the formula:

    Rx = Rx(old) + 32 * ( W - Ex )
    where W=1 if X wins and W=0 if X loses.
    '''
    winner_expected = 1/(1.0 + 10**((loser.score-winner.score) / 400.0))
    loser_expected = 1/(1.0 + 10**((winner.score-loser.score) / 400.0))

    winner.score = winner.score + 32.0 * ( 1.0 - winner_expected)
    loser.score = loser.score + 32.0 * ( 0.0 - loser_expected)
    
    winner.save()
    loser.save()

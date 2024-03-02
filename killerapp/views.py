from django.shortcuts import render, redirect
from .models import Killer


# Create your views here.


def main(request):
    killers = Killer.objects.all()
    return render(request, "killerapp/mainfolder/main.html", {'killers': killers})

def update_counter(request, killer_id):
    killer = Killer.objects.get(pk=killer_id)
    killer.counter += 1
    killer.save()
    return redirect('main')

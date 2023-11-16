from django.shortcuts import render, redirect

from app_hw.models import *


def profile_list_view(request):
    human = Human.objects.all()
    reg_human = RegHuman.objects.all()
    context = {'human_list': human, 'reg_human_list': reg_human}

    return render(request, 'profile_list.html', context)


def profile_detail_view(request, pk):
    context = {'human_pk': Human.objects.get(pk=pk), 'reg_human_pk': RegHuman.objects.get(pk=pk)}

    return render(request, 'profile_detail.html', context)


def human_create_view(request):
    context = {'human_create': RegHuman.objects.all()}
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        address = request.POST.get('address')
        favorite_music = request.POST.get('favorite_music')
        favorite_hobbies = request.POST.get('favorite_hobbies')
        favorite_anime = request.POST.get('favorite_anime')

        RegHuman.objects.create(name=name, surname=surname, age=age, address=address,
                                favorite_music=favorite_music, favorite_hobbies=favorite_hobbies,
                                favorite_anime=favorite_anime)

        return redirect('profile_list')

    return render(request, 'profile_create.html', context)

from django.shortcuts import render, redirect
from .models import *
from .forms import MusicianForm

def homePage(request):
    musicians = Musician.objects.all()
    groups = Group.objects.all()
    albums = Album.objects.all()
    contract_status = MusicianContractStatus.objects.all()

    total_musician = musicians.count()
    total_album = albums.count()
    accepted = contract_status.filter(status='A').count()
    pending = contract_status.filter(status='P').count()

    context = {
        'musicians':musicians,
        'groups':groups,
        'total_album':total_album,
        'total_musician':total_musician,
        'accepted':accepted,
        'pending':pending,
        
    }
    return render(request, 'pages/home.html', context)

def aboutPage(request):
    return render(request, 'pages/about.html')

def profilePage(request, pk):
    musician = Musician.objects.get(id=pk)
    albums = musician.album_set.all()
    tracks = Track.objects.filter(album__in=albums)

    context = {
        'musician':musician,
        'albums':albums,
        'tracks':tracks,
    }
    return render(request, 'pages/profile.html', context)

def trackPage(request, pk):
    musician = Musician.objects.get(id=pk)
    albums = Album.objects.filter(musician=musician)
    tracks = Track.objects.filter(album__in=albums)

    context = {
        'musician': musician,
        'albums': albums,
        'tracks': tracks,
    }
    return render(request, 'pages/track.html', context)

def createMusicianPage(request):
    form = MusicianForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homePage')


    context = {'form':form}
    return render(request, 'pages/musician_form.html',context)


def updateMusician(request, pk):
    musician = Musician.objects.get(id=pk)
    form = MusicianForm(instance=musician)

    if request.method == 'POST':
        form = MusicianForm(request.POST,request.FILES, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homePage')
        
    context = {'form':form}
    return render(request, 'pages/musician_form.html', context)



def deleteMusician(request, pk):
    musician = Musician.objects.get(id=pk)
    if request.method == 'POST':
        musician.delete()
        return redirect('homePage')
    
    context = {'musician': musician}
    return render(request, 'pages/delete_musician.html', context)

from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.contrib import messages
from createprofile.models import CreateProfile


def profiles(request):
    profile = CreateProfile.objects.order_by("id")
    context = {
        'profile': profile
    }
    return render(request, 'createprofile/profiles.html', context)

def cprofiles(request):
    if request.method == 'POST':
        # Get form values
        name = request.POST['name']
        age = request.POST['age']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        if CreateProfile.objects.filter(name=name).exists():
            messages.error(request, 'That name is already exists')
            return render(request, 'createprofile/createprofiles.html')
        else:
            cprofiles = CreateProfile(name=name, age=age, dob=dob, photo=photo)
            cprofiles.save()
            return redirect('/profiles/')
    else:
        return render(request, 'createprofile/createprofiles.html')

def delete(request, id):
      member = CreateProfile.objects.get(id=id)
      member.delete()
      return redirect('/profiles/')

def update(request, id):
    member = CreateProfile.objects.get(id=id)
    template = loader.get_template('createprofile/updateprofile.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))  

def updateprofile(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        member = CreateProfile.objects.get(id=id)
        member.name = request.POST['name']
        member.age = request.POST['age']
        member.dob =  request.POST['dob']
        member.photo = request.FILES['photo']
        member.save()
        return redirect('/profiles/')
    else:
        member = CreateProfile.objects.get(id=id)
        template = loader.get_template('createprofile/updateprofile.html')
        context = {
            'member': member,
        }
        return HttpResponse(template.render(context, request))
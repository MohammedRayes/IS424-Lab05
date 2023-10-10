from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class NewPersonForm(forms.Form):
    username = forms.CharField(label="Username:")
    password = forms.CharField(label="Password:")


people = []


def add(request):
    if request.method == "POST":
        form = NewPersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            person = Person(username, password)
            people.append(person)
            print("Person appended")

            return HttpResponseRedirect("/")
        else:
            print("ESLED ")
            return render(request, "add.html", {"form":form})
        
    return render(request, "add.html", {"form":NewPersonForm()})

def default(request):
    return render(request, "default.html", {"people": people})

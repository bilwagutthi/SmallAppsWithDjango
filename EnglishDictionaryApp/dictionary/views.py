from django.shortcuts import render
from PyDictionary import PyDictionary
from django.http import HttpResponse, JsonResponse
# Create your views here.

dictionary = PyDictionary()

def index(request):
    return render(request,'index.html')

def word(request):
    print(request)
    if request.method=="POST":
        word= request.POST['word']
        response ={
        "meaning" : dictionary.meaning(word),
        "synonyms" : dictionary.synonym(word),
        "antonyms" : dictionary.antonym(word)
        }
        return JsonResponse(response)


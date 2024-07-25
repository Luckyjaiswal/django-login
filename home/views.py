from django.shortcuts import render

from django.http import HttpResponse
 

def home(request):
    peoples = [
      {'name':'Lucky jaiswal','age':24},
      {'name':'Aditi','age':23},
      {'name':'Neha sharma','age':15},
      {'name':'Abhijeet Tiwari','age':12},
      {'name':'Ajay Mali','age':35},
    ]
    
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore doloribus nemo unde recusandae, magnam id sapiente repellat maxime numquam doloremque animi maiores accusantium totam rerum voluptatum? Modi ratione necessitatibus culpa facilis non perspiciatis soluta est magni deserunt nisi, voluptatem dolores sunt aperiam facere odio quos?
"""
    

    return render(request, "home/index.html", context={ 'page':'home','peoples':peoples, 'text':text} )

def about(request):
  context = {'page' : 'About'}

  return render(request, 'home/about.html', context)

 

def contact(request):
  context = {'page' : 'Contact'}

  return render(request, 'home/contact.html', context)

 

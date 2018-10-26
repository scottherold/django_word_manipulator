from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.

def index(request):
    return render(request, "session_words/index.html")

def process(request):
    if request.method == "POST":
        if "words" in request.session:
            word_list = request.session['words']
        else:
            word_list = []
        if "big_font" in request.POST:
            big_font = 1
        else:
            big_font = 0        
        word_list.append({"word": request.POST['new_word'], "color": request.POST['color'], "big_font": big_font, "timestamp":strftime("%I:%M %p, %b %d, %Y ", gmtime())})
        request.session['words'] = word_list
        request.session.modified = True
        print("*"*60)
        for word in request.session['words']:
            print(word)
        print("*"*60)
        return redirect("/")
    else:
        return redirect("/")

def destroy(request):
    request.session.flush()
    return redirect("/")
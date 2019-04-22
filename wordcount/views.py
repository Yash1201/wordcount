
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def contact(request):
    return HttpResponse('<h1>Contact</h1><br>My Contact Number is')

def count(request):
    data=request.GET['text']
    dat=data.split()
    wordlen=len(dat)
    word_dic={}
    for i in dat:
        if i in word_dic:
            word_dic[i]+=1
        else:
            word_dic[i]=1

    word_di=sorted(word_dic.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'dic':data, 'lenword':wordlen , 'count':word_di })

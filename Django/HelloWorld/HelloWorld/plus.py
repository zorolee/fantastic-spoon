# coding: utf-8

from django.http import HttpResponse

def plus(request):
    if 'a' not in request.GET:
        return render_to_response('plus.html')
    else:
        a = request.GET['a']
        b = request.GET['b']
        c = int(a) + int(b)
        return render_to_response('plusresult.html',{
            'result':str(c)
        })
from django import http

def home(request):
    return http.HttpResponse('Hellooo World? hogehoge')

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

def index(request):
    response =  render(request, 'index.html')
    response.set_cookie('name', 'tajwar', expires=datetime.now() + timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'index.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'index.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name': 'tajwar',
        'age': 21,
        'lan': 'Bangla'
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'index.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name')
        age = request.session.get('age')
        lan = request.session.get('lan')
        request.session.modified = True
        return render(request, 'index.html', {'session': {'name': name, 'age': age, 'lan': lan}})
    else:
        return HttpResponse('Session not found')

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request, 'index.html')
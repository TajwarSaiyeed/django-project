from django.shortcuts import render


def home(req):
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        {
            "userId": 1,
            "id": 2,
            "title": "qui est esse",
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
        },
        {
            "userId": 1,
            "id": 3,
            "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
            "body": "et iusto sed quo iure\nvoluptuary evocative omnis diligent aut ad\nvoluptuary dolorous vel accusation quis paginator\nmolest poor emus odio et labor et veldt aut"
        }
    ]

    return render(req, 'index.html', {'data': data})


def about(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        select_value = request.POST.get('select_value')
        return render(request, 'about.html', {
            'name': name,
            'email': email,
            'select_value': select_value
        })
    return render(request, 'about.html')

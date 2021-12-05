from django.http import JsonResponse, response

def videos(request):
    if request.method == 'GET':
        video = {'id': 1, 'titulo': 'Moana', 'url':'www.videos.com', 'desc': 'Vídeo Infantil' }
        return JsonResponse(video)

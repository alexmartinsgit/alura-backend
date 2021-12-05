from django.http import JsonResponse, response

def videos(request):
    if request.method == 'GET':
        video = {'id': 1, 'titulo': 'Moana'}
        return JsonResponse(video)

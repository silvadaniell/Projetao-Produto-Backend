from django.http import JsonResponse

def some_view(request):
    data = {
        "message": "This is a response from some_view."
    }
    return JsonResponse(data)

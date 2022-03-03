from django.http import HttpResponse


def message(request):
    message = request.GET.get("message")
    name = request.GET.get("name")
    output = "<h3>Hello {0}!<br>{1}!</h3>".format(name, message)
    return HttpResponse(output)
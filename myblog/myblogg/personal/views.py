from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
    # print(request.headers)
    # context = {
    #     'some_string': "some string to pass to the view",
    # }
    # context['some_string'] = "some string to pass to the view"

    context = {}
    list_of_values = []
    list_of_values.append("1 entry")
    list_of_values.append("2 entry")
    list_of_values.append("3 entry")
    context['list_of_values'] = list_of_values


    return render(request, "personal/home.html", context)
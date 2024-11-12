from django.shortcuts import render

def Home(request):
    return render(request, 'diabetes_prediction/index.html')
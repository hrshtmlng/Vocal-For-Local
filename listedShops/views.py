from django.shortcuts import render

def listShop(request):
    return render(request, 'shops/post.html')
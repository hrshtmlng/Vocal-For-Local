from django.shortcuts import render, redirect

from shops.models import shop

def landingPage(request): return render(request, 'shops/vocalLanding.html')


def showShops(request):
    allShops = shop.objects.all()
    content = { 'data':allShops }
    return render(request, 'shops/vocal.html',content)

def filterByCity(request):
    city = request.POST['city']
    particularShops = shop.objects.filter(city=city)
    content = { 'data':particularShops }
    return render(request, 'shops/vocal.html',content)

def listShop(request):
    return render(request, 'shops/post.html')

def saveShopInfo(request):
    shopName = request.POST['shopName']
    city = request.POST['city']
    landmark = request.POST['landmark']
    category = request.POST['category']
    description = request.POST['description']
    image = request.FILES['img']
    shopObj = shop(
        shopName=shopName,description=description,landmark=landmark,city=city,shopCategory=category,shopImage=image
    )
    shopObj.save()
    return redirect('/shops/showShops')

def testCss(request): return render(request, 'shops/test.html')


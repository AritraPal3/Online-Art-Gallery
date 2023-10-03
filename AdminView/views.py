from django.shortcuts import render,redirect
import os
from django.contrib.auth import get_user_model
from myapp.models import Art,Artist,Tag,MyOrder
from django.core.files.storage import FileSystemStorage

def art_image_upload_path(instance, filename):
    if filename:
        return os.path.join('D:\Torr\Art-Gallery-Using-Django\Ardent\media', filename)
    else:
        return os.path.join('D:\Torr\Art-Gallery-Using-Django\Ardent\media', '')

def adminP(request):
    v=Art.objects.all();
    return render(request,'demo.html',{'arts':v})

def addPage(request):
    return render(request,'product.html')

def addP(request):
    if(request.method=="POST"):
        artname=request.POST['art_name']
        artext=request.POST['image_description']
        
        img=request.FILES.get('image_name')  ##saving img content
        image_name = request.POST.get('image_name')
        
        print(img)
        artprice=request.POST['price']
        if request.POST['instock']=="on":
            artstock=True
        else: artstock=False
        artist=request.POST['artist']
        artistsp=request.POST['artistsp']
        tag=request.POST['tag']
        
        temp=Artist.objects.filter(artist_name=artist).first()
        if temp is not None:
            if img:
                fss = FileSystemStorage()  ## saving to media 
                file = fss.save(image_name, img) ## saving to media
            pro=Art.objects.create(art_name=artname,
                               price=artprice,
                               instock=artstock,
                               description=artext,
                               image=art_image_upload_path(None, str(img)),
                               art_artist_id=int(temp.pk))
            pro.save()
            
            artid=Art.objects.filter(art_name=artname).first()
            imgtag=Tag.objects.create(tag=tag,artid_id=int(artid.pk))
            imgtag.save()
            
            return redirect('../adminView')
        else:
            newartist=Artist.objects.create(artist_name=artist,speciality=artistsp)
            newartist.save()
            temp=Artist.objects.filter(artist_name=artist).first()
            if img:
                fss = FileSystemStorage()  ## saving to media 
                file = fss.save(image_name, img) ## saving to media
            pro=Art.objects.create(art_name=artname,
                               price=artprice,
                               instock=artstock,
                               description=artext,
                               image=art_image_upload_path(None, str(img)),
                               art_artist_id=int(temp.pk))
            pro.save()
            
            artid=Art.objects.filter(art_name=artname).first()
            imgtag=Tag.objects.create(tag=tag,artid_id=int(artid.pk))
            imgtag.save()
            
            return redirect('../adminView')

    else:    
        return render(request,'product.html') 


def deleteP(request,id):
    v=Art.objects.filter(id=id)
    v.delete()
    return redirect('../')

def OrderH(request):
    orders = MyOrder.objects.all()
    arts = [Art.objects.get(id=i.art_id.id) for i in orders]
    users = [get_user_model().objects.get(id=i.user.id) for i in orders]
    
    context = {
        'order': zip(orders, arts, users),
    }
    return render(request, "historyOrder.html", context)



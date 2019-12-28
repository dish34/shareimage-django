from django.shortcuts import render,redirect,get_object_or_404
from .models import Image
from .forms import PostForm
# Create your views here.
def image_list_view(request):
    query = Image.objects.all()
    num_visit = request.session.get('num_visit',0)
    request.session['num_visit'] = num_visit+1
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
        return redirect('detailimage',pk=image.pk)
            
    else:
       form = PostForm()
    context ={
        'imgobj': query,
        'test' : "testing",
        'form' : form,
        'num_visits': num_visit
    }
    return render(request,"share/index.html",context)

def display_images(request):
    image = Image.objects.all()
    context={
        "images":image,
    }
    return render(request,"share/list_images.html",context)    

def image_detail(request, pk):
    image = get_object_or_404(Image,pk=pk)
    context ={
        'image':image,
    }
    return render(request,"share/image_detail.html", context)

def image_edit(request,pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=image)
        if form.is_valid():
            form.save()
        return redirect('detailimage',pk=image.pk)
    else:
        form = PostForm(instance = image)
    return render(request,"share/index.html",{'form':form})        




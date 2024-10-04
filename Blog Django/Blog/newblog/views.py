from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from newblog.models import blogEnquiry
from django.core.paginator import Paginator 

# Create your views here.

def homePage(request):   

    blog_data = blogEnquiry.objects.all()
   
    if request.method=="GET":
        st = request.GET.get('searchname')

        print(st)

        if st != None:
            blog_data = blogEnquiry.objects.filter(blog_title__icontains=st)    #__icontains

        paginator = Paginator(blog_data , 6)
        page_number = request.GET.get('page')
        final_page = paginator.get_page(page_number)
        total_page = final_page.paginator.num_pages
    
        data = {
            # 'blog_data' : blog_data,
            'blog_data' : final_page,
            'lastpage' : total_page,
            'totalpagelist' : [n+1 for n in range(total_page)]
        }
        
    return render(request , "index.html", data)

def DeatailsPage(request , id):
    blog = get_object_or_404(blogEnquiry , pk=id)

    return render(request, 'details.html', {'blog': blog})
    # return render(request , "details.html")

def AddPost(request):
    if request.method=="POST":
            
        blog_title = request.POST.get('blogTitle')
        blog_description = request.POST.get('blogDescription')
        blog_image = request.POST.get("blogImage")

        blog = blogEnquiry()

        blog.blog_title = blog_title
        blog.blog_text = blog_description
        blog.blog_file = blog_image

        blog.save()

        return redirect("/home/")

    return render(request , "AddPost.html" , {})


   
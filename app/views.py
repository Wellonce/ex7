from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
from .forms import ProductCreateForm, ProductUpdateForm, UserLoginForm, UserRegisterForm
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse



from .models import Author, Product

    

def homeView(request):
    products = Product.objects.all().order_by("ends_in")
    size = request.GET.get("size", 2)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, size)
    page_obj = paginator.page(page)
    context = {
        "products": page_obj.object_list, 
        "page_obj": page_obj, 
        "num_pages": paginator.num_pages
    }
    return render(request, "index.html", context=context)
    
class ExploreView(View):
    def get(self, request):
        products = Product.objects.all()
        authors = Author.objects.all()
        return render(request, 'explore.html', context={"products":products, "authors":authors})
    
    
class DetailsView(View):
    def get(self, request):
        products = Product.objects.all()
        authors = Author.objects.all()
        context = {
            'products': products,
            'authors': authors
        }
        return render(request, 'details.html', context=context)
    
class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        # products = Author.product_set.all()
        context = {
            'authors': authors,
            # 'products': products
        }
        return render(request, 'author.html', context=context)

    
class CreatView(View):
    def get(self, request):
        form = ProductCreateForm() 
        return render(request, 'create.html', {'form' : form})
    
    def post(self, request):
       form = ProductCreateForm(request.POST, request.FILES)
       if form.is_valid():
            product = form.save(commit=False)
            # product.owner = request.user
            product.save()
            return redirect ('home-page')
       else:
           return render (request, 'create.html', {'form' : form})

# class AuthorLoginview(View):
#     def get(self, request):
#         form = AuthorLoginForm()
#         return render(request, "login.html", {'form': form})
    
#     def post(self, request):
#         form = AuthorLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username = username, password = password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"you have logged in as {username}")
#                 return redirect ('home-page')
#             else:
#                 messages.error(request, "Wrong username or password")
#                 return render(request, "login.html", {"form": form})
#         else:
#             return render(request, "login.html", {"form": form})
        
# def AuthorLoginView(request):
#     if request.method == "POST":
#         form = AuthorLoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "user succesfully logged in")
#                 return redirect("home-page")
#             else:
#                 messages.warning(request, "User not found")
#                 return redirect("login-page")
#         else:
#             return render(request, "login.html", {"form": form})
#     else:
#         form = AuthorLoginForm()
#     return render(request, "login.html", {"form": form})



# class AuthorRegisterView(View):
#     def get(self, request):
#         form = AuthorRegisterForm()
#         return render (request, "register.html", {'form': form})
    
#     def post (self, request):
#         form = AuthorRegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Sucessfully registered")
#             return redirect("login-page")
#         else:
#             return render(request, "register.html", {'form':form})

# class UserLogout(View):
#     def get(self, request):
#         logout(request)
#         messages.success(request, "user successfully logged out!")
#         return redirect ('home-page')
    
class UserLoginview(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "login.html", {'form': form})
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f"you have logged in as {username}")
                return redirect ('create-page')
            else:
                messages.erorr(request, "Wrong username or password")
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})
        

class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render (request, "register.html", {'form': form})
    
    def post (self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Sucessfully registered")
            return redirect("login-page")
        else:
            return render(request, "register.html", {'form':form})

class UserLogout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "user successfully logged out!")
        return redirect ('home-page')
    

    
@login_required
def product_updateView(request, pk: int):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "post successfully updated")
            return redirect('detail-page', pk=pk)
    else:
        form = ProductUpdateForm(instance=product)
    return render(request, "update_product.html", {"form": form, "product":product})
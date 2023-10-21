from django.shortcuts import render
from .models import Product, Cart
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Making database empty
Product.objects.all().delete()
Cart.objects.all().delete()


# Adding Some Products
product1 = Product(name='Plant A', description='A beautiful plant pot', price=10.99, image='https://i.ibb.co/zFXpHW8/Lovepik-com-401298869-home-decoration-green-plant-pot.png')
product1.save()

product2 = Product(name='Globe decorative', description='An Attractive Globe', price=19.99, image='https://i.ibb.co/0nPBtsJ/Antique-Home-Decor-PNG-Download-Image.png')
product2.save()

product3 = Product(name='Night Lamp', description='An Glowing Night Lamp', price=12.99, image='https://i.ibb.co/mvCtxF3/Antique-Home-Decor-PNG-High-Quality-Image-1.png')
product3.save()

product4 = Product(name='Globe decorative', description='An Attractive Globe', price=19.99, image='https://i.ibb.co/0nPBtsJ/Antique-Home-Decor-PNG-Download-Image.png')
product4.save()

product5 = Product(name='Globe decorative', description='An Attractive Globe', price=19.99, image='https://i.ibb.co/0nPBtsJ/Antique-Home-Decor-PNG-Download-Image.png')
product5.save()

# Home page rendering function
def home(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'home.html', {'products': products})


# show product details
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})



# registration form using inbuillt django features
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})

# login form with inbuilt django features
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def cart(request, product_id):
    get_prod = Product.objects.get(id=product_id)
    prod = Cart(name = get_prod.name, description = get_prod.description, price = get_prod.price,image = get_prod.image)
    prod.save()
    print(prod)
    products_uf = Cart.objects.all()
    #Filtering
    seen_ids = set()
    products = [obj for obj in products_uf if obj.id not in seen_ids and not seen_ids.add(obj.id)]


    

    
    total_price = 0
    for i in products:
        total_price += i.price
    return render(request, 'cart.html', {'products': products, 'total_price' : total_price})
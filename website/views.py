from django.shortcuts import render , get_object_or_404, redirect , redirect
from urllib.parse import quote
from .models import Product , WarrantyRegistration , WarrantyApproval 
from .forms import WarrantyRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    ceiling = Product.objects.filter(category='Ceiling')
    
    context = {
        'ceiling': ceiling
        
    }

    return render(request, 'products.html', context)

def enquiry(request, product_id, color):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        phone = request.POST['phone']
        color = request.POST['color']

        message = f"""
Hello Sir/Madam , I am interested in your product. Here are my details:
Name: {name}
Place: {place}
Phone: {phone}
Product: {product.name}
Color: {color}
 """
        whatsapp_number = '917902907410'
        url = f"https://wa.me/{whatsapp_number}?text={quote(message)}"

        return redirect(url)
    
    return render(request, 'enquiry.html', {'product': product, 'color': color})



def products(request):
    sort_option = request.GET.get('sort', '')  # read ?sort=low/high/available
    ceiling = Product.objects.filter(category='Ceiling')

    if sort_option == 'low':
        ceiling = ceiling.order_by('price')
    elif sort_option == 'high':
        ceiling = ceiling.order_by('-price')
    elif sort_option == 'available':
        ceiling = ceiling.filter(available=True)

    context = {
        'ceiling': ceiling,
        'sort_option': sort_option
    }
    return render(request, 'products.html', context)

def register_warranty(request):
    if request.method == 'POST':
        form = WarrantyRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            return redirect('warranty_status' , serial_number=registration.serial_number)
    else:
    
        form = WarrantyRegistrationForm()
    return render(request, 'register.html', {'form': form})
    

def warranty_status(request, serial_number):
        
        try:
            registration = WarrantyRegistration.objects.get(serial_number=serial_number)
        except WarrantyRegistration.DoesNotExist:
                # Custom message instead of 404
                return render(request, 'no_serial.html')
        
        try:
            approval = registration.warrantyapproval
            if approval.approved:
                return render(request, 'certificate.html', {
                     'registration': registration,
                     'approval': approval,
                     'end_date':approval.warranty_end_date()
                })
            else:
                return render(request,'rejected.html',{'registration': registration})
        except WarrantyApproval.DoesNotExist:
            return render(request, 'pending.html', {'registration': registration})
        
def check_warranty(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        return redirect('warranty_status', serial_number=serial_number)
    return render(request, 'check_status.html')

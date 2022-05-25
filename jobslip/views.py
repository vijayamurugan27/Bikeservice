from django.shortcuts import redirect, render
from jobslip.forms import CustomerForms
from jobslip.models import Customer

# Create your views here.
def show(request):
    customer=Customer.objects.all()
    return render(request,'index.html',{'customer':customer})
    
def create(request):
    form = CustomerForms
    if request.method == 'POST':
        form = CustomerForms(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/show')
    return render(request,'create.html',{'form':form})

def delete(request,jno):
    customer=Customer.objects.get(jno=jno)
    customer.delete()
    return redirect ('/show')


def update(request,jno):
    customer=Customer.objects.get(jno=jno)
    if request.method =='POST':
        form=CustomerForms(request.POST,instance=customer)
        if form.is_valid:
            form.save()
            return redirect('/show') 
    return render(request,'update.html',{'customer':customer})
    

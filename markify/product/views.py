from django.contrib.auth.decorators import login_required
from .models import Product, Advertisement
from .forms import AddProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



@login_required
def products_list(request):
    products = Product.objects.filter(team=request.user.userprofile.active_team)
    return render(request, 'product/product_list.html', {
        'products': products,
    })

@login_required
def product_add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.team = request.user.userprofile.active_team
            product.save()
            
            
            messages.success(request, "The product was created.")
                    
            return redirect('products:list')
    else:    
        form = AddProductForm()
    return render(request, 'product/product_add.html',{
        'form': form,
        'team':request.user.userprofile.active_team,        
    })   

@login_required
def products_detail(request,pk):
    product = get_object_or_404(Product, pk=pk, team = request.user.userprofile.active_team)
         
    return   render(request, 'product/product_detail.html', {
         'product':product,
         })    
    
    
@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, team=request.user.userprofile.active_team, pk=pk)    
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, "The changes were saved.")
                    
            return redirect('products:list')
    else:    
        form = AddProductForm(instance=product)        
    
    return render(request, 'product/product_edit.html',{
        'form': form,
    })    
    
    
@login_required
def product_delete(request, pk):
        product = get_object_or_404(Product, team = request.user.userprofile.active_team, pk=pk)
        product.delete()
        
        messages.success(request, "The product was deleted.")
        return redirect('products:list')
       
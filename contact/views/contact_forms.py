from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact
from contact.forms import ContactForm
from django import forms
from django.urls import reverse
# Create your views here.



def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(request, 'contact/create.html', {'form':form, 'form_action':form_action})
    
    return render(request, 'contact/create.html', {'form': ContactForm(), 'form_action':form_action})




def update (request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(request, 'contact/create.html', {'form':form, 'form_action':form_action})
    
    return render(request, 'contact/create.html', {'form': ContactForm(instance=contact), 'form_action':form_action}) 


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirm = request.POST.get('confirm', 'no')
    if confirm == 'yes':
        contact.delete()
        return redirect('contact:index')
    return render(request, 'contact/contact.html', {'contact': contact, 'confirm': confirm})
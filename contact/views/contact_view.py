from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contact/index.html', {'contacts': contacts})


def contact(request, contact_id):
    single = get_object_or_404(Contact, pk=contact_id, show=True)
    return render(request, 'contact/contact.html', {'contact': single})


def search(request):
    value = request.GET.get('search', '').strip()
    if value:
        contacts = Contact.objects.filter(Q(first_name__icontains=value) |  Q(last_name__icontains=value) | Q(phone__icontains=value) | Q(email__icontains=value), show=True).order_by('first_name')
        paginator = Paginator(contacts, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, 'contact/index.html', {'contacts': contacts})
    return redirect('index')

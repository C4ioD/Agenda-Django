from django.shortcuts import render, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q

# Create your views here.


def index (request):

  contatos = Contact.objects.all().filter(show=True).order_by('-id')[:10]

  context = {
    'contatos':contatos,
    'site_title':'Contatos - ',
          
             }

  return render(request,'index.html',context)

def search (request):

  search_value = request.GET.get('q','').strip()
  if search_value == '':
    return redirect('contact:index')

  contatos = Contact.objects.all().filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) | Q(phone__icontains=search_value) | Q(email__icontains=search_value)).order_by('-id') 

  context = {
    'contatos':contatos,
    'site_title':'Search - ',
          
             }

  return render(request,'index.html',context)


def contact (request, contact_id):

  single_contato = Contact.objects.filter(pk=contact_id).first()

  if single_contato is None or single_contato.show == False:
    raise Http404()

  contact_name = f'{single_contato.first_name} {single_contato.last_name} - '

  context = {
    'contato':single_contato,
    'site_title': contact_name,
    }

  return render(request,'contact.html',context)
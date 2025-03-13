from django.shortcuts import render
from contact.models import Contact
from django.http import Http404

# Create your views here.


def index (request):

  contatos = Contact.objects.all().filter(show=True).order_by('-id')[:10]

  context = {
    'contatos':contatos,
    'site_title':'Contatos - ',
          
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
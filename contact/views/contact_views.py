from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def index (request):

  contatos = Contact.objects.all()

  context = {'contatos':contatos}

  return render(request,'index.html',context)
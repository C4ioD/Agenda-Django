from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def index (request):

  contatos = Contact.objects.all().filter(show=True).order_by('-id')[:10]

  context = {'contatos':contatos}

  return render(request,'index.html',context)
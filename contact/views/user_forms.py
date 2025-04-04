from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm 
from contact.forms import RegisterForm


def register(request):
  form = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request,'Usuário registrado')
      return redirect('contact:index')

  return render(
    request,
    'register.html',
    {
      'form':form
    }
  )

def login_view(request):

  form = AuthenticationForm(request)

  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      user = form.get_user()
      auth.login(request,user)
      messages.success(request,'Login realizado com sucesso!')
      return redirect('contact:index')
    else:
      messages.error(request,'Login invalido!')

  return render(
    request,
    'login.html',
    {
      'form':form
    }
  )


def logout_view(request):

  form = AuthenticationForm(request)

  auth.logout(request)
  messages.info(request,'Logout realizado.')
  return redirect('contact:login')

from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
  ## METODO DE MUDAR OS ATRIBUTOS RECRIANDO O CAMPO
  first_name = forms.CharField(
        widget=forms.TextInput(
          attrs={
              'class':'classe-a classe-b',
              'placeholder':'Escreva aqui',
          }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para o usuário'
    )
  
  ## CRIANDO UM NOVO CAMPO QUE NAO EXISTE NO MODEL
  qualquer = forms.CharField(
        widget=forms.TextInput(
          attrs={
              'class':'classe-a classe-b',
              'placeholder':'Escreva aqui',
          }
        ),
        help_text='Texto de ajuda para o usuário'
    )

 
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

 ## METODO DE MUDAR OS ATRIBUTOS ATUALIZANDO O WIDGET JA EXISTENTE
    # self.fields['first_name'].widget.attrs.update({
    #         'class':'classe-a classe-b',
    #        'placeholder':'Escreva aqui',
    # })

  class Meta:
    model = models.Contact
    fields = ('first_name', 'last_name','phone')
  
    ## METODO DE MUDAR OS ATRIBUTOS CRIANDO UM NOVO WIDGET
    # widgets = { 
    ###muda os atributos do HTML
    #   'first_name':forms.TextInput(
    #     
    #     attrs={
    #       'class':'classe-a classe-b',
    #       'placeholder':'Escreva aqui'
    #     }
    #   )
    # }


  def clean(self):
    #cleaned_data= self.cleaned_data

    self.add_error(
      'first_name',
      ValidationError(

        'Mensagem de erro',
        code='invalid'
      )
    )

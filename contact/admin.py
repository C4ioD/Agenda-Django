from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContacAdmini(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name','phone','show',) # Insere visualização das colunas
  search_fields = ('id','first_name','last_name',) # campos a serem pesquisados
  list_filter = ('create_date',) # insere um campo de filtro da data
  list_per_page = 10 # quantidade de valores exibidos por pagina
  list_max_show_all = 200 # maximo de valores a serem mostrados 'mostrar tudo'
  list_editable =  'show',

@admin.register(models.Catagory)
class CategoryAdmini(admin.ModelAdmin):
  list_display = 'name',
  orderin = '-id',
  
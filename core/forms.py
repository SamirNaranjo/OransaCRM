from cProfile import label
from datetime import datetime
from django.forms import DateInput, ModelForm, PasswordInput, TextInput, Textarea
from .models import BaseModel, Category,Product,Client

class CategoryForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus']= True
    

    class Meta:
        model = Category
        fields = ('__all__')
        widgets={
            'name': TextInput(
                attrs={
                    'placeholder':'Ingrese Descripcion'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder':'Ingrese Descripcion',
                    'rows':3,
                    'cols':3
                }
            ),

        }
    

    #  def clean(self):
    #      cleaned=super().clean()
    #      if len(cleaned['name']) <= 50:
    #          self.add_error('name', 'Faltan Caracteres')
    #      return cleaned    

class ProductForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus']= True
    

    class Meta:
        model = Product
        fields = ('__all__')
        widgets={
            'name': TextInput(
                attrs={
                    'placeholder':'Ingrese Descripcion'
                }
            ),
        }

class ClientForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus']= True
    

    class Meta:
        model = Client
        fields = ('__all__')
        widgets={
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dni',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d',
                                       attrs={
                                           'value': datetime.now().strftime('%Y-%m-%d'),
                                       }
                                       ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
        }

# class UserForm(ModelForm):
#      def __init__(self, *args, **kwargs):
#         #  super().__init__(*args, **kwargs)
#          self.fields['first_name'].widget.attrs['autofocus'] = True

#      class Meta:
#          model = BaseModel
#          fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image',
#          widgets = {
#              'first_name': TextInput(
#                  attrs={
#                      'placeholder': 'Ingrese sus nombres',
#                  }
#              ),
#              'last_name': TextInput(
#                  attrs={
#                      'placeholder': 'Ingrese sus apellidos',
#                  }
#              ),
#              'email': TextInput(
#                  attrs={
#                      'placeholder': 'Ingrese su email',
#                  }
#              ),
#              'username': TextInput(
#                  attrs={
#                      'placeholder': 'Ingrese su username',
#                  }
#              ),
#              'password': PasswordInput(render_value=True,
#                  attrs={
#                      'placeholder': 'Ingrese su password',
#                  }
#              ),
#          }
#          exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']



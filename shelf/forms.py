from  django.forms import ModelForm
from .models import * 
    
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
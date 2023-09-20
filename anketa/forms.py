from django import forms

class Nashaforma(forms.Form):
    name = forms.CharField(label='Ваше имя')
    num = forms.IntegerField(label='Номер')

class Forma3(forms.Form):
    k1 = forms.DecimalField(label='десятичные числа',decimal_places=2)
    k2 = forms.EmailField(label='email')
    # k3 = forms.Textarea()
    k3 = forms.BooleanField(label='поставте галочку')
    k4 = forms.NullBooleanField(label='вы человек')
    k5 = forms.URLField(label='адресс в интернете',help_text='http://www.cl.ru')
    k6 = forms.GenericIPAddressField(label='id')
    k7 = forms.FilePathField(label='выберите фаил',path='C:\\Program Files\\SQLiteStudio',allow_folders=True,match='.*\.txt')
    k8 = forms.ImageField(label='картинка')
    k9 = forms.FileField(label='фаил')
    vibor = ((1,'En'),(2,'Ru'),(3,'Fr'))
    k10 = forms.TypedChoiceField(choices=vibor)
# ,required=False,max_value=100,\
# widget=forms.Textarea,initial=12,\
# help_text='напишите сколько вам лет',disabled=True
class Uploadforma(forms.Form):
    name = forms.CharField(label='имя')
    img = forms.ImageField(label='картинка')

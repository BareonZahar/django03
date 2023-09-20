from django import forms
from PIL import Image

class Nashaforma2(forms.Form):
    name = forms.CharField(label='Имя животного')
    poroda = forms.CharField(label='порода животного')
    num = forms.IntegerField(label='возраст животного')
    cvet = forms.CharField(label='цвет животного')
    eda = forms.CharField(label='любимая еда ')
    img = forms.ImageField(label='фото животного')

    # def img_img(self):
    #     if self.img:
    #         return ('<img src="{5}"').format(self.img.label)

# ,required=False,max_value=100,\
# widget=forms.Textarea,initial=12,\
# help_text='напишите сколько вам лет',disabled=True

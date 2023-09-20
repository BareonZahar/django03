from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
from  .forms import Nashaforma
def forma1(request):
    if request.method=='POST':
        name = request.POST.get('name')
        num = request.POST.get('num')
        output = '''<h1>Спасибо</h1>
        <h2>Ваше имя -- {0}</h2>
        <h2>Ваше число -- {1}</h2>'''.format(name,num)

        # output = f'<h1> cpasibo,{name}! za vashu:{num}<h1>'

        # output = f'<h1>Спасибо!</h1>'\
        # f'<h2>Ваше имя -- {name}</h2>'\
        # f'<h2>Ваше число -- {num}</h2>'

        return HttpResponse(output)
    else:
        anketa1 = Nashaforma()
        data = {'form':anketa1}
        return render(request,'forma.html',context=data)

from  anketa.forms2 import Nashaforma2
def forma2(request):
    if  request.method=='POST':
        name = request.POST.get('name')
        poroda = request.POST.get('poroda')
        num = request.POST.get('num')
        cvet = request.POST.get('cvet')
        eda = request.POST.get('eda')
        img = request.FILES.get('img').read()
        file = open('anketa/static/fo2/{0}.jpg'.format(name), 'wb')
        file.write(img)
        fpath = 'fo2/{0}.jpg'.format(name)
        output = '''<h1>Спасибо</h1>
               <h2>Имя животного -- {0}</h2>
               <h2>порода животного -- {1}</h2>
               <h2>возраст животного -- {2} -- лет</h2>
               <h2>цвет животного -- {3}</h2>
               <h2>любимая еда животного -- {4}</h2>
               <h2>фото животного -- </h2>{5}'''.format(name,poroda,num,cvet,eda,img)
        # some_file = open('keit.jpg', 'w')
        # some_file.write(img)
        # some_file.close()
        data = {'k1': name,'k2':poroda,'k3':num,'k4':cvet,'k5':eda,'k6': fpath}
        return render(request, 'fro2.html', context=data)
    else:
        anketa2 = Nashaforma2()
        data = {'form' : anketa2}
        return render(request, 'forma.html', context=data)
from  anketa.forms import Forma3
def forma3(request):
    if request.method == 'POST':
        k1 = request.POST.get('k1')
        k2 = request.POST.get('k2')
        k3 = request.POST.get('k3')
        k4 = request.POST.get('k4')
        k5 = request.POST.get('k5')
        k6 = request.POST.get('k6')
        k7 = request.POST.get('k7')
        k8 = request.POST.get('k8')
        k9 = request.POST.get('k9')
        k10 = request.POST.get('k10')

        print(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10)
        output = '''<h1>Спасибо</h1>
           <h2>первое -- {0}</h2>
           <h2>второе-- {1}</h2>
           <h2>третье -- {2}</h2>
           <h2>четвертое -- {3}</h2>
           <h2>пятое-- {4}</h2>
           <h2>шестое -- {5}</h2>
           <h2>седьмое -- {6}</h2>
           <h2>восьмое-- {7}</h2>
           <h2>девятое -- {8}</h2>
           <h2>десятое -- {9}</h2>
           '''.format(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10)
        return HttpResponse(output)
    anketa = Forma3()
    data = {'form' : anketa}
    return render(request,'forma.html',context=data)

from  anketa.forms import Uploadforma
def upload(request):
    if request.method=='POST':
        name = request.POST.get('name')
        img = request.FILES.get('img').read()
        print('написали')
        file = open('anketa/static/upload/{0}.jpg'.format(name),'wb')
        file.write(img)
        print('записали')
        fpath = 'upload/{0}.jpg'.format(name)
        data = {'k1':name,'k2':fpath}
        print('готовы к отправке')
        return render(request, 'endpage.html', context=data)
    else:
        anketa = Uploadforma()
        data = {'form' : anketa}
        return render(request, 'forma.html', context=data)
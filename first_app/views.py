from django.shortcuts import render
import datetime

# Create your views here.
def home( request):
    d= { 'author': 'Rahim', 'age' : 20 ,'lst':['python ','is','good '], 'birthday':datetime.datetime.now()
        
    ,'cap':'capfirst', 'cut':'String with spaces',

    'dicsort':[
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
],

'first':['Apple', 'Mango', 'Orange'],
'second':{
        'cat',
        'dog',
        'horse',
},


'lower':'I Am Master Yoda',
'upper':'Happy coding!' ,
'value ':'Its a new day',
'random':['Banana', 'Mango', 'Orange'],
'timesl':'2022-01-02T10:30:00.000123',
'turn':'Happy coding',
'test':'<b>I</b> <button>love</button> <span>dogs</span>',
'list':'Earthly',





        
         }
    return render (request,'home.html',d)
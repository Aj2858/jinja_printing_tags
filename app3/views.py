from django.shortcuts import render

# Create your views here.

def ifcondtion(request):
    d = {'a':20 , 'b': 45}
    return render(request, 'if_else.html', context=d)

def if_elif_condtion(request):
    d = {'a':20 , 'b': 75, 'c': 56}
    return render(request, 'if_elif_else.html', context = d)

def nestedif(request):
    d = {'a':20 , 'b': 75, 'c': 86}
    return render(request, 'nested_if.html', context=d)

def forloop(request):
    d = {'name' : 'Ajay', 'age' : 24, 'Hobbies' : ['cricket', 'volleyball', 'Badmanition', 'chess']}
    return render(request, 'for_loop.html', context = d)
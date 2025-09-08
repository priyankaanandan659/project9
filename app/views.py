from django.shortcuts import render

# Create your views here 
def condition(request):
    d={'a':400,'b':500}
    return render(request,'condition.html',context=d)
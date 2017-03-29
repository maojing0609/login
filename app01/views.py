from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('rmb'):
                request.session.set_expiry(10)
                #设置10s超时，django默认session超时时间是2周
            return  redirect('/index/')
        else:
            return render(request, 'login.html')

def index(request):
    if request.session.get('is_login',None):
        #取不到is_login就返回None，防止500错误
        return render(request,'index.html')
    else:
        return HttpResponse("滚")

def hello(request):

    return HttpResponse("helloworld")

def logout(request):
    request.session.clear()
    return redirect('/login')

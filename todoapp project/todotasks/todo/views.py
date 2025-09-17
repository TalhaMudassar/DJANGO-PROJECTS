from django.shortcuts import render, redirect, get_object_or_404
from todo.models import TODOO
from todo.forms import Customsigninform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def custom_sigin(request):
    if request.method == 'POST':
        form = Customsigninform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save() 
            return redirect('login')
    else:
        form=Customsigninform()
    return render(request,'todo/signin.html',{'form':form}) 



def login_page(request):
    error_message = None
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        pwd= request.POST.get('pwd')
        print(f"username :{fnm}  password: {pwd}")
        userr = authenticate(request,username=fnm ,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('todopage')
        else:
            error_message = "Invalid username or password!"
        
        
    return render(request,'todo/login.html',{'error_message':error_message})



@login_required(login_url='login')
def todo_page(request):
    if request.method == 'POST':
        obj = request.POST.get('title')
        if obj:
            TODOO.objects.create(
                title = obj,
                user = request.user
            )
            return redirect('todopage')
    
    todos = TODOO.objects.filter(user = request.user).order_by('-date')     
    return render(request,'todo/todo.html',{'res':todos})



@login_required(login_url='login')
def edit_todo(request,srno):
    todo = get_object_or_404(TODOO,srno=srno,user = request.user)
    if request.method == 'POST':
        obj = request.POST.get('title')
        if obj:
            todo.title = obj
            todo.save()
            return redirect('todopage')
    return render(request, "todo/edit_todo.html", {"todo": todo})

@login_required(login_url='login')
def delete_todo(request, srno):
    todo = get_object_or_404(TODOO,srno = srno,user = request.user)
    todo.delete()
    return redirect('todopage')


@login_required(login_url='login')
def toggle_status(request, srno):
    todo = get_object_or_404(TODOO, srno=srno, user=request.user)

    if request.method == "POST":
        # Toggle the checkbox
        status_value = request.POST.get("status")
        todo.status = True if status_value == "on" else False
        todo.save()

    return redirect('todopage')


# Logout
@login_required(login_url='login')
def signout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')




# # Show all todos + add new todo
# @login_required(login_url='login')
# def todo_page(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         if title:  # simple validation
#             TODOO.objects.create(
#                 title=title,
#                 user=request.user
#             )
#             return redirect('todopage')

#     # Show only current user’s tasks
#     todos = TODOO.objects.filter(user=request.user).order_by('-date')
#     return render(request, "todo/todo.html", {"res": todos})
            
# # Edit Todo
# @login_required(login_url='login')
# def edit_todo(request, srno):
#     todo = get_object_or_404(TODOO, srno=srno, user=request.user)

#     if request.method == "POST":
#         title = request.POST.get("title")
#         if title:
#             todo.title = title
#             todo.save()
#             return redirect('todopage')

#     return render(request, "todo/edit_todo.html", {"todo": todo})


# # Delete Todo
# @login_required(login_url='login')
# def delete_todo(request, srno):
#     todo = get_object_or_404(TODOO, srno=srno, user=request.user)
#     todo.delete()
#     return redirect('todopage')


# # Logout
# @login_required(login_url='login')
# def signout(request):
#     from django.contrib.auth import logout
#     logout(request)
#     return redirect('login')

    
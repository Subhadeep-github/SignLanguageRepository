from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, "authentication/index.html")

# def signup(request):
#     if request.method == 'POST':
#         firstNamevar = request.POST.get("firstName")
#         lastNamevar = request.POST.get("lastName")
#         usernamevar = request.POST.get("username")
#         emailvar = request.POST.get("email")
#         passwordvar = request.POST.get("password")
#         confirmPasswordvar = request.POST.get("confirmPassword")
        
#         # Check if passwords match
#         if passwordvar != confirmPasswordvar:
#             messages.error(request, "Passwords do not match.")
#             return redirect("signup")

#         # Create user
#         myuser = User.objects.create_user(usernamevar, emailvar, passwordvar)
#         myuser.first_name = firstNamevar
#         myuser.last_name = lastNamevar
#         myuser.save()

#         messages.success(request, "Your account has been successfully created!")
#         return redirect("signin")
        
#     return render(request, "authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print("USR DETAILS")
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            # return redirect('profilepage')  # Redirect to profile page after successful sign-in
            return JsonResponse({'success': True, 'redirect_url': '/profilepage/'})  # Adjust profile page URL as needed
        else:
            # messages.error(request, 'Invalid username or password.')
              return JsonResponse({'success': False, 'error': 'Invalid username or password.'})
    
    
    return render(request, "authentication/signin.html")
    # return render(request, "authentication/signin.html")

@login_required
def profilepage(request):
    user = request.user
    return render(request, "authentication/profilepage.html")


def signout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('signin')

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('File uploaded successfully!')
    else:
        form = UploadForm()
    
    return render(request, 'upload.html', {'form': form})

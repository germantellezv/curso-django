# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.urls import reverse
# Models
from django.contrib.auth.models import User
from posts.models import Post
# Forms
from users.forms import ProfileForm, SignupForm

# Create your views here.

class UserDetailView(LoginRequiredMixin,DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context 

@login_required
def update_profile(request):
    """ Update user's profile using Django forms"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.picture = data['picture']
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.save()
            url = reverse('users:detail',kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name = 'users/update_profile.html',
        context={
            'profile':profile,
            'user': request.user,
            'form':form
        })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html',{'error':'Invalid username or password'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

def signup(request):
    """ Sign up view """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form}
    )















# Models
# from django.contrib.auth.models import User
# from users.models import Profile
# Exceptions
# from django.db.utils import IntegrityError
""" def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html',{'error':'Password confirmation does not match'})
        # Crear el usuario
        try:    
            user = User.objects.create_user(username = username, password = passwd)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            
            user.email = request.POST['email']
            user.save()
        except IntegrityError:
            return render(request, 'users/signup.html',{'error':'This username is already in use'})

        # Crear el perfil al usuario
        profile = Profile(user=user)
        profile.save()
        return redirect('login')

    return render(request, 'users/signup.html') """
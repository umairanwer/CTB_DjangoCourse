from django.shortcuts import redirect, render
from .models import Profile
from .forms import ContactForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def ProfileListView(request):
    profiles= Profile.objects.all()
    return render(request, 'matrimony/profile_list.html', {'profiles': profiles})

def ProfileDetailView(request, profile_id):
    profile= Profile.objects.get(id=profile_id)
    return render(request, 'matrimony/profile_detail.html', {'profile':profile})

def ProfileDeleteView(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    profile.delete()
    profiles = Profile.objects.all()
    return render(request, 'matrimony/profile_list.html',
                  {'profiles':profiles})

def ContactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Message: {form.cleaned_data['message']}")

    else:
        form = ContactForm()
    return render(request, 'matrimony/contact.html', {'form':form})

@login_required
def NewProfileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('matrimony:profile_list')

    else:
        form = ProfileForm()

    return render(request, 'matrimony/new_profile.html', {'form':form})
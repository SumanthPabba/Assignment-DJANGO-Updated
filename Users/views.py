from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User 
from .models import Profile
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.http import HttpResponse
from .forms import UserUpdateForm, ProfileForm


# Create your views here.

def register(request):
    """
    
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            user = User.objects.get(username=username)
            user_data = Profile.objects.create(user=user,username=user.username.capitalize(), password = user.password, email=user.email, phone_number=phone_number, address=address)
            user_data.save()
            messages.success(request, 'Account created!')
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)


        if u_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
    'u_form' : u_form,
    'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "users/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'sunnycool1811@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					# messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("/password_reset_done/")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="users/password_reset.html", context={"password_reset_form":password_reset_form})


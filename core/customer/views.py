from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.customer import forms


# Create your views here.

@login_required()
def home(request):
    return redirect(reverse('customer:profile'))


@login_required(login_url="/sign-in/?next=/customer/")
def profile_page(request):
    user_form = forms.BasicUserForm(instance=request.user)
    customer_form = forms.BasicCustomerForm(instance=request.user.customer)

    if request.method == 'POST':
        user_form = forms.BasicUserForm(
            request.POST, instance=request.user)
        customer_form = forms.BasicCustomerForm(
            request.POST, request.FILES, instance=request.user.customer)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect(reverse('customer:profile'))

    return render(request, 'customer/profile.html', {"user_form": user_form, "customer_form": customer_form})

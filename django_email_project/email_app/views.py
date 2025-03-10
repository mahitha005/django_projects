from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email='mahitha2005.mahi@zohomail.in',  # Must match EMAIL_HOST_USER
                recipient_list=[form.cleaned_data['recipient_email']],
                fail_silently=False,
            )
            return render(request, 'email_sent.html', {'message': "Email sent successfully!"})
    else:
        form = EmailForm()
        
    return render(request, 'email_app/send_email.html', {'form': form})

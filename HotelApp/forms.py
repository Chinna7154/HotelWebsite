from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ['name', 'email', 'message']


from django.core.mail import send_mail
from django.shortcuts import render
from HotelApp.forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject='Contact Form Submission',
                message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
                from_email='hotel@example.com',
                recipient_list=['hotel@example.com'],
                fail_silently=False,
            )
            return render(request, 'thanks.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

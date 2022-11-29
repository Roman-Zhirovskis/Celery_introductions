from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.core.mail import send_mail

from proj.settings import EMAIL_HOST_USER
from task2.forms import ReviewForm

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponse(msg)

class ContactFormView(FormView):
    form_class = ReviewForm
    template_name = 'contact.html'
    success_url = HttpResponse('Vse Ok')

    def form_valid(self, form):
        print(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['review'])
        user = self.request.user
        print(user)
        text_massage = f'Обратная связь от пользователя\n' \
                       f'Текст обращения: {form.cleaned_data["review"]}'
        send_mail(form.cleaned_data['name'], text_massage,
                  EMAIL_HOST_USER, [form.cleaned_data['email']], fail_silently=False)
        return self.success_url
# Create your views here.

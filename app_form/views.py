from django.shortcuts import render
from django.views import View
from .form import FormUser
from django.http import HttpResponse, Http404
from datetime import date


# Create your views here.
def check_valid_name(user_input):
    return user_input.isalpha()


def check_valid_age(user_input):
    if not user_input:
        return False

    for str in user_input:
        if not str.isdigit():
            return False
    if int(user_input) <= 0 or int(user_input) > 100:
        return False

    return True


def check_valid_birthday(user_input, age):
    if not user_input:
        return False

    today = date.today()
    current_year = today.year

    number_of_nondigits = 0
    for str in user_input:
        if not str.isdigit():
            if str != '/':
                return False
            else:
                number_of_nondigits = number_of_nondigits + 1

    if number_of_nondigits != 2:
        return False

    word = user_input.split('/')

    if int(word[0]) > 31 or int(word[0]) <= 0:
        return False
    elif int(word[1]) > 12 or int(word[0]) <= 0:
        return False
    elif current_year - int(word[2]) != age or int(word[2]) <= 1970:
        return False

    return True


def check_file_type(file_object):
    if not file_object:
        return False

    file_extension = file_object.name.split('.')
    if file_extension[-1] != 'pdf':
        return False
    return True


def check_phone_number(phone_number):
    if not phone_number:
        return False

    if len(phone_number) != 11:
        return False

    if not phone_number.isnumeric():
        return False
    return True


def check_picture_type(picture):
    if not picture:
        return False

    file_extension = picture.name.split('.')
    if file_extension[-1] != "jpg" and file_extension[-1] != 'png':
        return False
    return True


class FormView(View):
    def get(self, request):
        form = FormUser(initial={'phone_number': '0'})
        return render(request, 'form_page.html', {'form': form})

    def post(self, request):
        form = FormUser(request.POST, request.FILES)

        if form.is_valid():

            bool_checks = check_valid_name(form.cleaned_data['first_name']) and \
                          check_valid_name(form.cleaned_data['last_name']) and \
                          check_valid_age(form.cleaned_data['age']) and \
                          check_valid_birthday(form.cleaned_data['date_of_birth'], int(form.cleaned_data['age'])) and \
                          check_file_type(form.cleaned_data['candidate_cv']) and \
                          check_phone_number(form.cleaned_data['phone_number']) and \
                          check_picture_type(form.cleaned_data['picture'])

            if not bool_checks:
                return render(request, 'error.html')

            return HttpResponse('Well done')




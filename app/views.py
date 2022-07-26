import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserInfo

ALLOWED_FORMATS = [
    '+79001234567',
    '+7(900)123-45-67',
    '84951002030',
    '8(343)100-40-50',
    '8(34342)1-23-45'
]


def check_parenthesis(number: str):
    '''Проверка на корректную расстановку скобок'''
    if '(' in number and ')' not in number:
        return False
    if ')' in number and '(' not in number:
        return False
    return True


def check_length(number: str):
    '''Проверка на ограничение длины номера'''
    number = number.replace(
        '-', '').replace(' ', '').replace('(', '').replace(')', '')
    if number.startswith('+'):
        if len(number) - 1 > 13 or len(number) < 12:
            return False
    else:
        if len(number) != 11:
            return False
    return True


def validate_name(name: str):
    ''' Проверка не пустое ли поле "имя" '''
    if not len(name):
        error = '* Имя не может быть пустым'
        return error

    return True


def validate_phone_number(phone_number: str):
    '''Проверка номера телефона на соответствие реглярному вырадению'''
    regexp = r'^(\+\d{1,3}|8).?\s?[\(\-]?\d{3,5}[\)\-]?\s?\d{1,3}[\-]?\d{2}[\-]?\d{2}$'
    if not bool(re.match(regexp, phone_number)) or not check_parenthesis(phone_number) or not check_length(phone_number):
        error = '* Введен некорретный номер. Возможные варианты формата: '
        return error
    return True


def index(request):
    '''Рендеринг шаблона страницы'''
    context = {'errors': list()}
    context['users'] = UserInfo.objects.all()
    if request.method == 'POST':
        validated_name = validate_name(
            request.POST['name'])
        validated_phone = validate_phone_number(request.POST['phone_number'])
        if validated_name != True:
            context['errors'].append(validated_name)
            context['name'] = request.POST['name']
            context['phone_number'] = request.POST['phone_number']
            print(request.POST['phone_number'])
            context['success'] = 'ERROR'
        if validated_phone != True:
            context['errors'].append(validated_phone)
            context['fmts'] = ALLOWED_FORMATS
            context['name'] = request.POST['name']
            context['phone_number'] = request.POST['phone_number']
            context['success'] = 'ERROR'
        if context['errors']:
            return render(request, 'app/index.html', context)
        context['success'] = 'OK'
        new_user = UserInfo(
            name=request.POST['name'], phone_number=request.POST['phone_number'].replace('-', '').replace(' ', '').replace('(', '').replace(')', ''))
        new_user.save()

    return render(request, 'app/index.html', context)

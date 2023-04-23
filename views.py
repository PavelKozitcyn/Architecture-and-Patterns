from design_framework.templator import render
#import datetime
#import os


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))


class Examples:
    def __call__(self, request):
        return '200 OK', render('examples.html', date=request.get('date', None))


class Page:
    def __call__(self, request):
        return '200 OK', render('page.html', date=request.get('date', None))


class Another:
    def __call__(self, request):
        return '200 OK', render('another.html', date=request.get('date', None))


class MessageView:
    def __call__(self, request):
        return '200 OK', render('contact_lesson2.html', date=request.get('date', None))
    # def __call__(self, request):
    #     # Проверка метода запроса
    #     if request['method'] == 'POST':
    #         now = datetime.datetime.now()
    #         data = request['data']
    #         title = data['title']
    #         text = data['text']
    #         email = data['email']
    #         if not os.path.exists('messages'):
    #             os.mkdir('messages')
    #         # print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
    #         with open(f'messages/message_{now.strftime("%d%m%Y")}_{now.strftime("%H%M%S")}.txt', 'w',
    #                   encoding='utf-8') as file:
    #             file.write(f'Нам пришло сообщение от {now.strftime("%d.%m.%Y")} в {now.strftime("%H:%M:%S")}!\n'
    #                        f'Отправитель: {email}\n'
    #                        f'Тема: {title}\n'
    #                        f'Текст: {text}')
    #         return '200 OK', render('contact_lesson2.html', date=request.get('date', None))
    #     else:
    #         return '200 OK', render('contact_lesson2.html', date=request.get('date', None))



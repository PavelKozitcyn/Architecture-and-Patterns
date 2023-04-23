from datetime import date
from views import Index, Contact, Another, Examples, Page, MessageView


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/another/': Another(),
    '/examples/': Examples(),
    '/page/': Page(),
    '/message/': MessageView(),
}

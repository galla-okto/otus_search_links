from bs4 import BeautifulSoup
from search.input_data import  input_datas
from search.output_data import output_datas
from search.find import find_links, get_request

def search_links():
    input_questions = {'request_text': 'Enter request text: ',
                   'search_system': 'Enter search system (google.com, yandex.ru, ...): ',
                   'number_results': 'Enter number of results: ',
                   'is_recursive_search': 'Is recursive search (Y/N)?: ',
                   'output_format': 'Enter output format (1-console/2-json/3-csv): '}

    setup_search_system = {'google': [{'id': 'main'}, {'class': 'kCrYT'}],
                           'yandex': [{}, {}]}
    input_answers = {}
    input_datas(input_questions, input_answers)

    q = '+'.join(input_answers['request_text'].split())
    if input_answers['search_system'] == 'google.com':
        link = 'http://' + input_answers['search_system'] + '/search?q=' + q + '&ie=utf-8&oe=utf-8'
    elif input_answers['search_system'] == 'yandex.ru':
        link = 'http://' + input_answers['search_system'] + '/search/?lr=10313&text=' + q

    r = get_request(link)

    links = []
    soup = BeautifulSoup(r.content, 'html.parser')

    find_links(soup, input_answers, setup_search_system, links)

    output_datas(input_answers, links)

if __name__ == '__main__':
    search_links()
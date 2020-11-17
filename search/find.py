from bs4 import BeautifulSoup
import requests

def get_request(link):
    # q = '+'.join(input_answers['request_text'].split())
    # URL = 'http://' + input_answers['search_system'] + '/search?q=' + q + '&ie=utf-8&oe=utf-8'
    return requests.get(link)

def find_links_further(link, links, input_answers):
    if len(links) <= int(input_answers['number_results']) - 1:
        links.append(link)

        r = get_request(link)

        soup = BeautifulSoup(r.content, 'html5lib')

        table = soup.find('div', attrs={'id': 'main'})

        for row in table.findAll('div', attrs=''):
            try:
                link = {}
                link['url'] = row.a['href']

                find_links_further(link, links)
            except:
                continue
    else:
        return

def find_links(soup, input_answers, setup_search_system, links):
    main_tag = {'id': 'main'}
    link_tag = {'class': ''}
    if input_answers['search_system'] == 'google.com':
        main_tag = {'id': 'main'}
        link_tag = {'class': 'kCrYT'}
    elif input_answers['search_system'] == 'yandex.ru':
        main_tag = {'id': 'main'}
        link_tag = {'class': 'serp-item'}

    table = soup.find('div', attrs=main_tag)

    for row in table.findAll('div', attrs=link_tag):
        try:
            link = {}
            link['url'] = row.a['href']

            if input_answers['is_recursive_search'] == 'N':
                if len(links) <= int(input_answers['number_results']) - 1:
                    links.append(link)
                else:
                    break
            else:
                find_links_further(link, links, input_answers)
                break
        except:
            continue
from bs4 import BeautifulSoup as BS
import requests

main_url = 'https://read.amazon.com/notebook/'
site = 'https://www.amazon.com/gp/sign-in.html'

#read credentials from file
user, password = open("credentials.txt", "r").read().rstrip().split()

login_data = dict(email=user, password=password)
session = requests.session()
'''define session headers'''
session.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': main_url
}


login_page = session.get(main_url).text

'''scrape login page to get all the needed inputs required for login'''
login_soup = BS(login_page, 'html.parser')
data = {}
form = login_soup.find('form', {'name': 'signIn'})
for field in form.find_all('input'):
    try:
        data[field['name']] = field['value']
    except:
        pass

'''add username and password to the data for post request'''
data['email'] = user
data['password'] = password
print(data)

highlight_page = session.post(main_url, data=data).content

soup = BS(highlight_page, 'html.parser')
print(soup.title)
print(soup.find_all('h2'))
#print(soup)
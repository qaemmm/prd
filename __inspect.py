from pathlib import Path
from bs4 import BeautifulSoup
soup = BeautifulSoup(Path('index.html').read_text(encoding='utf-8'), 'html.parser')
profile = soup.find(id='profile-page')
preview_wrapper = profile.find('div', class_='px-4 pb-4')
print('preview wrapper classes', preview_wrapper.get('class') if preview_wrapper else 'none')
if preview_wrapper:
    print(preview_wrapper.prettify()[:500])
client_list_page = soup.find(id='client-list-page')
print(client_list_page.prettify()[:500])

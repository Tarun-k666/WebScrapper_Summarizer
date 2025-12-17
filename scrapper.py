from bs4 import BeautifulSoup
import requests

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
def get_page_content(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup=BeautifulSoup(response.content, 'html.parser')
        title=soup.title.string if soup.title else 'No title found'
        if soup.body:
            for irrelevant in soup(['script', 'style', 'img', 'input']):
                irrelevant.decompose()
            text=soup.body.get_text(separator='\n', strip=True)
        else:
            text='No body content found'
        return (title+ '\n\n' + text)[:2_000]
    else:
        print(f"Failed to retrieve page content. Status code: {response.status_code}")
        return None
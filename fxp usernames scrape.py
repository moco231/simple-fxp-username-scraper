from urllib import response
import requests
from bs4 import BeautifulSoup

    



# here i will write the part the parse through the pages
def member_parser():
    url = "https://www.fxp.co.il/member.php?u="
    for page in range(1671170, 1680000):
        result = f"{url}{page}"
        statres = requests.get(result)
        print(statres)        
        if statres.status_code == 200:
            print("member exists!")
            member_username_extr(statres)
        else:
            print("member does not exist!")

def member_username_extr(response):
    print("trying to extract usernames to a list!")
    soup = BeautifulSoup(response.content, "html.parser")
    for text in soup.select('span.user_nick_s1'):
        with open('out1.txt', 'a',encoding="utf-") as f:  # Open file in append mode ('a')
            for text in soup.select('span.user_nick_s1'):
                print(text.get_text(), file=f)
        
member_parser()
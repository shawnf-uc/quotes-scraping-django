from bs4 import BeautifulSoup
import os
import sys
sys.path.append('/QuotesApp')
os.environ["DJANGO_SETTINGS_MODULE"] = "QuotesApp.settings"
print(os.environ["DJANGO_SETTINGS_MODULE"])
import django
django.setup()
from Quotes.models import Author,Quote,QuoteJunction,Tag
import requests



def insert_author(aut_link,quote_txt,tag_list):
    auther_page = requests.get(aut_link)
    auther_soup = BeautifulSoup(auther_page.text, 'html.parser')
    # print(auther_soup.prettify())
    details = auther_soup.find("div",class_="author-details")

    author_details_list = details.find("h3",class_="author-title").text.split('\n')
    author_name = author_details_list[0]
    author_dob = details.find("span",class_="author-born-date").string
    author_des = details.find("div",class_="author-description").string

    author, created = Author.objects.get_or_create(description=author_des,name=author_name,dob=author_dob)
    quote, created = Quote.objects.get_or_create(author=author,quote_text=quote_txt)
    for tag_nme in tag_list:
        tag , created = Tag.objects.get_or_create(tag_name = tag_nme)
        qoute_junction, created = QuoteJunction.objects.get_or_create(quote=quote,tag=tag)


# def get_page_data(actual_link):


# def get_page_links(page_link):

#     nxt_page = requests.get(page_link)
#     soup = BeautifulSoup(nxt_page.text, 'html.parser')
#     all_links = []
#     all_links.append(page_link)
#
#     # while_loop_iter =
#     # while()

def main():
    url = 'http://toscrape.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # gettin the Quotes page link
    quotes_link = soup.select_one('a[href="http://quotes.toscrape.com/"]')
    link = quotes_link['href']
    actual_link = link[:len(link) - 1]

    quotes_page = requests.get(actual_link)
    quo_soup = BeautifulSoup(quotes_page.text, 'html.parser')

    # getting the data from the website
    for quo in quo_soup.find_all("div", class_="quote"):
        quote_txt = quo.find("span", class_="text").string
        author_link = quo.select_one('a[href*=author]')
        # print(qoute_txt)
        # print(author_link['href'])
        actual_author_link = author_link['href']
        tag_list = []
        for tag in quo.find("div", class_="tags"):
            if tag.string == "Tags:" or tag.string == None:
                continue
            else:
                tag_list.append(tag.string.lstrip("\n"))
        new_tags = []
        for tag in tag_list:
            if tag == '':
                continue
            else:
                new_tags.append(tag)
        new_tags = new_tags[1::]

        # print(new_tags)
        author_page_url = actual_link + actual_author_link
        # print(author_page_url)
        insert_author(author_page_url, quote_txt, new_tags)
    # end


    #end
    print("Data uploaded to database")

main()
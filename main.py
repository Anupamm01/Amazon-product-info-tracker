from bs4 import BeautifulSoup
import requests
import pandas 
import numpy

def get_title(soup):
    try:
        title = soup.find("span", id = "productTitle").text.strip()
    except AttributeError:
        title = ""
    
    return title

def get_price(soup):
    try:
        price = soup.find("span", class_="aok-offscreen").text.strip()
    except AttributeError:
        price = ""
    
    return price[:6]

def get_rating(soup):
    try:
        rating = new_soup.find("span", class_="a-icon-alt").text.strip()
    except AttributeError:
        rating = ""
    
    return rating

def get_review_count(soup):
    try:
        review_count = new_soup.find("span",id = "acrCustomerReviewText").text.strip()
    except AttributeError:
        review_count = ""

    return review_count


def get_availablity(soup):
    try:
        availability = new_soup.find("span", class_="a-size-medium a-color-success").text.strip()
    except AttributeError:
        availability = "Not available"
    
    return availability


if __name__=="__main__":
    url = "https://www.amazon.com/s?k=keyboard&crid=KM3OLR2CENUM"

    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Accept-Language' : 'en=US,en;q=0.9'
    }

    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text,"html.parser")

    links = soup.find_all("a", class_ = ["a-link-normal s-line-clamp-2 s-link-style a-text-normal"])

    link_lists = []

    for link in links:
        href = link["href"]
        product_link = f"http://amazon.com{href}"
        link_lists.append(product_link)



    d = {'Title':[], 'Price':[], 'Rating':[], 'Availability':[], 'Reviews':[]}
    c = 1
    for link in link_lists:
        new_response = requests.get(link,headers=HEADERS)

        new_soup = BeautifulSoup(new_response.text,"html.parser")

        d['Title'].append(get_title(new_soup))
        d['Price'].append(get_price(new_soup))
        d['Rating'].append(get_rating(new_soup))
        d['Availability'].append(get_availablity(new_soup))
        d['Reviews'].append(get_review_count(new_soup))


    amazon_df = pandas.DataFrame.from_dict(d)
    amazon_df['Title'].replace('',numpy.nan,inplace=True)
    amazon_df = amazon_df.dropna(subset=['Title'])
    amazon_df.to_csv("amazon_data.csv",header=True,index=False)
    amazon_df.to_excel("amazon_data.xlsx",sheet_name="Amazon Data", index=False)

        




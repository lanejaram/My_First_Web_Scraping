import requests 
from bs4 import BeautifulSoup 
from requests.adapters import HTTPAdapter 
from urllib3.util.retry import Retry
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import time



def extract_last_page_number():
    url = "https://www.citymall.com.mm/citymall/en/Categories/Home-%26-Living-Lifestyle/Electronics/c/id05011?q=%3Arelevance&page=" 
    headers = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
    "AppleWebKit/537.36 (KHTML, like Gecko) " 
    "Chrome/120.0.0.0 Safari/537.36", 
    "Accept-Encoding": "identity" 
    }
    session = requests.Session() 
    retry = Retry( 
    total=5, 
    backoff_factor=1, 
    status_forcelist=[429, 500, 502, 503, 504] 
    ) 
    session.mount("https://", HTTPAdapter(max_retries=retry)) 
    response = session.get(url, headers=headers, timeout=30) 
    print(response.status_code) 
    soup = BeautifulSoup(response.text, "html5lib")

    # Extract Last Page Number
    # find tag that contains all page numbers
    page_nums_tag = soup.find('div', class_='col-xs-6 col-sm-6 col-md-6 pagination-wrap')
    # find all page number tags
    page_num_tag_list = soup.find_all('span', class_='page-link')
    last_page_num_tag = page_num_tag_list[-0] # get the last tag
    last_page_num = int(last_page_num_tag.text)
    
    return last_page_num

def extract_product_name(tag):
    """Extract product name from the dummy tag."""
    # extract product's name tag
    product_name_tag = tag.find('a', class_='name')
    # extract product's name using text attribute
    product_name = product_name_tag.text
    return product_name

def extract_product_price(tag):
    """Extract product price from the dummy tag."""
    # extract product's price tag
    product_price_tag = tag.find('p', class_='product-price mt-1')
    #product_price = product_price_tag.text
    if product_price_tag.text=="":
        product_price_tag = tag.find('span', class_='product-sale-price')
        # extract product's price using text attribute
    product_price = product_price_tag.text
        # remove unwanted characters from price
    product_price = product_price.replace("Ks", "")
    product_price = product_price.replace(",", "")   
    #product_price = float(product_price) # change str to int type
    return product_price
# Create empty lists to store extracted data
product_name_list = [] # to store extracted product name
product_price_list = []

def main():
    # Extract Last Page Number
    #last_page_number = extract_last_page_number()

    for page_num in tqdm(range(0, 20+1)):
        url = "https://www.citymall.com.mm/citymall/en/Categories/Home-%26-Living-Lifestyle/Electronics/c/id05011?q=%3Arelevance&" + "page=" + str(page_num)   
        headers = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
        "AppleWebKit/537.36 (KHTML, like Gecko) " 
        "Chrome/120.0.0.0 Safari/537.36", 
        "Accept-Encoding": "identity" 
        }
        session = requests.Session() 
        retry = Retry( 
        total=5, 
        backoff_factor=1, 
        status_forcelist=[429, 500, 502, 503, 504] 
        ) 
        session.mount("https://", HTTPAdapter(max_retries=retry)) 
        response = session.get(url, headers=headers, timeout=30) 
        print(response.status_code) 
        soup = BeautifulSoup(response.text, "html5lib")
       
        # find main div tags
        main_tags = soup.find_all('div', class_='product-info')

        for dummy_tag in main_tags:
            try:
                product_name_2 = extract_product_name(dummy_tag)
                product_name_list.append(product_name_2)

                product_price_2 = extract_product_price(dummy_tag)
                product_price_list.append(product_price_2)
                              
                time.sleep(0)
            except:
                print(dummy_tag)
                raise
                break

    # Export data as an Excel file.
    data_dic = {"Product Name":product_name_list,
                "Product Price":product_price_list
                }

    # Create a dataframe
    df = pd.DataFrame(data_dic)
    # Create filename version and save as excel file.
    time_str = datetime.now().strftime("%H-%M-%S")
    df.to_excel("Output " + time_str + ".xlsx", index=False)

    print("All steps are completed!")
    
if __name__=="__main__":
    main()

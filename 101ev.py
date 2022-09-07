import requests
from bs4 import BeautifulSoup
import time
import aiohttp
import asyncio


def remove_all_spaces(string):
    return "".join(string.split())


def accepted_currency(currency):
    acceptedCurrency = {
        'euro': False,
        'pounds': False,
        'usd': False,
        'lira': False
    }
    if(currency == '£'):
        acceptedCurrency['pounds'] = True

    if(currency == '₺'):
        acceptedCurrency['lira'] = True

    if(currency == '$'):
        acceptedCurrency['usd'] = True

    if(currency == '€'):
        acceptedCurrency['euro'] = True

    return acceptedCurrency

def get_page_data(link):
    BASE_URL = 'https://www.101evler.com'
    images_urls = []
    LINK = BASE_URL+link
    images_page = requests.get(LINK)
    images_soup = BeautifulSoup(images_page.content, "html.parser")
    slider = images_soup.find("ul", class_="splide__list")
    images_list_item = slider.find_all("img")
    if len(images_list_item) > 0:
        images_urls.append(images_list_item[0]['src'])
        
    rent_container = images_soup.find('div', class_="div-block-363 zebra-rows")
    rent_string = rent_container.find('strong', string=lambda x: ('Month'.lower() in x.lower() or 'Year'.lower() in x.lower()))
    

    desc = images_soup.find('div', class_="f-s-16")
    deposit = None
    if not desc == None:
        details = desc.find_all('p', string=lambda x: (
            "dep" in x.lower()) if not x == None else None)
        if(not details == None):
            for det in details:
                indx = det.text.lower().index('dep')
                if not indx == None:
                    deposit = det.text[indx-2]


    whatsapp = images_soup.find("a", id="btn-send-whatsapp-rp-a")

    whatsapp_number = '+'+whatsapp["href"].split("?")[0][-12:]
    if(not whatsapp_number[1] == '0'):
        whatsapp_number = None

    for image in images_list_item[1:]:
        images_urls.append(image["data-splide-lazy"])

    return {"images": images_urls, "phone": whatsapp_number, "deposit": deposit, "link": LINK, 'rents': rent_string.text }


def parse_rents(duration):
    try:
        if duration == 'Monthly':
            return 1

        if duration == "Yearly":
            return 12

        return int(duration[0])
    except:
        return 0

def load_101evler_apartments(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = []

    # apartments = []

    apartment_elements = soup.find_all("div", class_="ilanitembasic")

    for i in apartment_elements:
        link = i.find("a", class_="hover-black")
        links.append(link["href"])

    return links

 
async def get_apartments(url):

    links = load_101evler_apartments(url)
    page_data = []
    
    async with aiohttp.ClientSession() as s:
        for i in links:
           task = asyncio.create_task(get(s,i))
           page_data.append(task)
        page = await asyncio.gather(*page_data)

    
    


    return page







def extract_data(page):
 
    for apt in page:
        link = apt.find("a", class_="hover-black")
        uid = "JEmJr2Qu00XZyFJqtCROFP0Nnm23"
        title = apt.find("h4", class_="text-block-129")
        price = apt.find("div", class_="basicprice")
        date_area = apt.find("div", class_="div-block-332")
        loc_info_div = apt.find("div", class_="locationpremiumdiv")
        date = remove_all_spaces(date_area.text.split('#')[0])
        id = "#" + remove_all_spaces(date_area.text.split('#')[1])
        area = apt.find("div", class_="text-block-131 ilanListe131")
        area = remove_all_spaces(area.text)
        living_space = loc_info_div.find_all("div", class_="text-block-130")[1]
        if(title):
            title = {
                    "translations": {"en_us": " ".join(title.text.split())}
                }

        if(price):
            price_string = remove_all_spaces(price.text)

            if('/' in price_string):
                price = price_string[1:].split('/')[0]
                rents = parse_rents(price_string[1:].split('/')[1])
            else:
                rents = 0
                price = price_string[1:]
            

            currency = accepted_currency(price_string[0])
            get_page = get_page_data(link['href'])
            images = get_page["images"]
            phone = get_page["phone"]

            if(rents == 0):
                rent = remove_all_spaces(get_page['rents'])
                rents = parse_rents(rent)
        data = {
            "id":id,
            "UID": uid,
            "link": get_page['link'],
            "images": images,
            "contact": {"phone": phone},
            "living_space": [living_space.text],
            "address":{ "area": area },
            "price":int("".join(price.split(","))),
            "title": title,
            "features":{
                "acceptedCurrency":currency,
                "deposit": get_page["deposit"],
                "rents": rents
            }

        }
        apartments.append(data)
    return apartments


async def get(s,url):
  url = f"https://www.101evler.com{url}"
  try:

    async with s.get(url) as resp:
        
                return await resp.text()
  except Exception as e:
    return f"Invalid URL passed {url} :>> {e}"






def get_third_party_houses_filtered(data):
    # {'data': {'option': 'Apartments', 'min_rent': 50, 'max_rent': 494.8, 'bedrooms': ['Studio', 1], 'bathrooms': ['Any', 1], 
    #     'furnished': ['Any', 'Furnished', 'Unfurnished'], 'facilities': [{'title': 'Has Aircondition', 'name': 'hasAC'}, 
    #         {'title': 'Has Cleaners', 'name': 'hasCleaners'}, {'title': 'Close To Market', 'name': 'closeToMarket'}], 'minsToBus': 
    #         [16.7], 'sortBy': [], 'currency': [{'title': '$', 'name': 'usd'}, {'title': '£', 'name': 'pounds'}], 'area': ['Lefkosia', 'Deraboyu', 'Kucukaymacli'], 
    #         'rent': [1, 2, 3], 'distance': 27600, 'position': {'longitude': 33.3639, 'latitude': 33.3639}}}

    min_rent = data['min_rent']
    max_rent = data['max_rent']
    bedrooms = data['bedrooms']
    bathrooms = data['bathrooms']
    furnished = data['furnished']
    facilities = data['facilities']
    currency = data['currency']
    area = data['area']
    rent = data['rent']
    url = 'https://www.101evler.com/north-cyprus/property-to-rent/kyrenia?room-type%5B0%5D=1&room-type%5B1%5D=2&room-type%5B2%5D=3&room-type%5B3%5D=4&room-type%5B4%5D=5&room-type%5B5%5D=6&s-r=R&property_type=1&min_price=100&max_price=1000&currency=1&min_m2=&max_m2=&p-furnish%5B0%5D=1&p-furnish%5B1%5D=2&p-furnish%5B2%5D=3&search_keyword=&publish_date='




def main():
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  start = time.time()
  res = asyncio.run(get_apartments("https://www.101evler.com/north-cyprus/property-to-rent/"))
  end = time.time()
#   print("returned: ", len(res))
  print(f"Finished in: {end - start}")
  return res




start = time.time()
print(main())
end = time.time()

print (f" \n\n\n\n\n\nthis process took : {end -start} seconds")
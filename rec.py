import requests
from bs4 import BeautifulSoup
import time
import aiohttp
import asyncio
import re

# DEPENDENCIES
    # pip install aiohttp


# I broke down the codes into smaller functions
# this is the order they are being called: Main -> get_apartments -> itr ->  get_page_data && intemediary (passes the res of getpagedata to intemediary) -> contd get_pagedata -> get;  the results re sent to intemediary
# contd intemediary -> info_binding; the results of type list are returned to get_page_data 



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

    elif (currency == '₺'):
        acceptedCurrency['lira'] = True

    elif(currency == '$'):
        acceptedCurrency['usd'] = True

    elif(currency == '€'):
        acceptedCurrency['euro'] = True

    else:
        acceptedCurrency['lira'] = True

    return acceptedCurrency


# this func replace requests with httpio; it runs async
async def get(s,url):
  try:

    async with s.get(f"https://www.hangiev.com{url}") as resp:
        
         return await resp.text()
  except Exception as e:
    return f"Invalid URL passed {url} :>> {e}"

# this func calls get func with all the urls; multiple request at once; async and returns all the response as an iterable of type list
async def get_page_data(s,link):
    
    page_data = []
    for i in link:
        task = asyncio.create_task(get(s,i))
        page_data.append(task)
    page = await asyncio.gather(*page_data)

    return page

# calls the info_binding
def intemediary (page):
    print("pages: ",len(page))

    res = info_binding(page)
    return res

# this line iterates the responses and collects the infos needed returns a list
def info_binding(pages):
    
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # page = await asyncio.run(get(url))
  page_info = []
  for page in pages:
   try:
    # print(page, end="==================================================== \n\n\n\n\n")
    soup = BeautifulSoup(page, "html.parser")
    image_list = []

    images_container = soup.find_all("div", class_="item-photos-box d-flex flex-wrap")
    big_photo = images_container[0].find("div",class_="big-image")
    image_list.append(big_photo.find("img")["src"])
    photos = images_container[0].find_all("div","small-images d-flex flex-row flex-wrap")
    a = photos[0].find_all('div')
    
    for i in a:
        image_list.append(i.find("img")["src"]) 
         
    contact = soup.find("a", class_="btn call mask")["data-phone"]
    address = soup.find("h2").text
    price_text = soup.find("h3","price").text
    price = price_text.split("/")[0] if 'TL'.lower() in price_text.split("/")[0].lower() else price_text.split("/")[0][1:]

    currency = accepted_currency(remove_all_spaces(price_text)[0])
    rents_table = soup.find_all("ul","item-table item-table-strong list-unstyled d-flex flex-column flex-wrap")
    rents_text = rents_table[0].find_all("li")[4].find("span").text
    rents = rents_text.split(" ")[0]
    features_string = soup.find("div","item-rooms-detail d-flex justify-content-start").text
    deposit = None
    living_space = features_string.lower().replace("\n","").split("bedroom")
    features = str(living_space[0]).replace(" ","")+"+1"   

    deposit_table = soup.find_all("div","item-detail-box")
    deposit_string = deposit_table[1].find_all("p")
    for i in deposit_string:
        
        if "Deposit".lower() in i.text.lower() or "Dep".lower() in i.text.lower():
            string = []
            string.append(i.text.lower().split(" "))
            if "deposit" in string:
                index =  string[0].index("deposit")
                deposit = string[0][index-1]
            else:
                deposit = None
            break
    page_info.append({"contact":contact,"image":image_list,"address":address,"price":price,"currency":currency,"rents":rents, "features":features,"deposit":deposit })
   except Exception as e:
    raise f"Binding error {e}" 

  return page_info

#calls the get_page_data which returns itrable from info binding, iterates the infos from info binding and seralize in dict
async def itr(links):
    apartments = []

    async with aiohttp.ClientSession() as session:
       page = await get_page_data(session,links)
       page_datas = intemediary(page)
       for page_data in page_datas:



        id = None
        uid = None
        deposit = None
        link = None
        images = page_data["image"]
        contact = page_data["contact"]
        address = page_data["address"]
        price = page_data["price"]
        title_text = "place holder line 118"#links[i].find("a", class_="stretched-link").text
        title = {
                    "translations": {"en_us": " ".join(title_text.split())}
                }
        currency = page_data["currency"]
        if "deposit" in page_data:
            deposit = page_data["deposit"]
        rents = page_data["rents"]
        features = page_data["features"]
        
        price = ''.join(price[:-3].split(',')) if 'TL'.lower() in price.lower() else ''.join(price.split(','))

        try:
            rents = int(rents) 
        except:
            rents = 1
        


        data = {
                "id":id,
                "UID": uid,
                "link": link,
                "images": images,
                "contact": {"phone": contact},
                "living_space": [features],
                "address":{ "area": address },
                "price":float(price),
                "title": title,
                "features":{
                    "acceptedCurrency":currency,
                    "deposit": deposit,
                    "rents": rents
                }

            }

        apartments.append(data)
    print("apartments: ",len(apartments))
    return apartments

# makes sure the links are actual links   
def match(input):
    # pattern = re.compile(r"/[a-zA-Z]+-[a-zA-Z]+-.*([+-]?(?=\\.\\d|\\d)(?:\\d+)?(?:\\.?\\d*))(?:[eE]([+-]?\\d+))?", re.IGNORECASE)
    # res = 
    if re.match("/",input):
        return True
    else :
        return False

# the main function to call
async def get_apartments(location="north-cyprus", indx=None):

    if not indx:
        url = f"https://www.hangiev.com/{location}-properties-for-rent"
    else:
        url = f"https://www.hangiev.com/{location}-properties-for-rent?page={indx}"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    apartment_elements = soup.find_all("a", class_="stretched-link")
    
    links = []
    for i in apartment_elements[2:len(apartment_elements)-2]:
        
        if match(i.get('href')):
            links.append(i.get('href'))
        
    print("links: ",len(links))
    data = await itr(links)
    


    # start = time.time()
    # executor = ThreadPoolExecutor(50)
    # futures = [executor.submit(itr,apartment_elements)]
    # concurrent.futures.wait(futures)
    # apartments = itr(apartment_elements)
   
    
     
    # end = time.time()
    # print(f"Time: {end-start}")
    # print(futures)
    return data


# initialize the  async and runs the func get_apartment 
def main(main="north-cyprus",indx=None):
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  start = time.time()
  res = asyncio.run(get_apartments(main,indx))
  end = time.time()
  print("returned: ", len(res))
  print(f"Finished in: {end - start}")
  return res



if "__main__" == __name__:

     main()






import bs4,requests,webbrowser

print("Getting Deals of the day")

try:
    res = requests.get("https://www.flipkart.com")
    soup = bs4.BeautifulSoup(res.text)
    links = soup.select('div[data-tracking-id="Deals of the day "] a')
    print(len(links))
    print()
    for link in links:
        #print("https://www.flipkart.com/"+link.get("href"))
        webbrowser.open("https://www.flipkart.com/"+link.get("href"))
    
except:
    print("Connection Error!")

input()



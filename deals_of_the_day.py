#This program is solely meant for educational purposes.
#This program fetches the deals of the day from flipkart.com and opens them in new tabs in your default browser.
#The browser might crash sometimes as this is fully automated and a many tabs are opened at once.
#This program is not futureProof(may not work in the future) if the HTML markup of the host site changes.

#AUTHOR-Soumyadeep Jana

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



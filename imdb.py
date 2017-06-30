#This program is meant for educational purposes only.
#This program scraps the 250 odd images of top rated movies of TV shows based on user selection from IMDB's website
#and creates a collage of those images.
#This program is not futureProof(may not work in the future) if the HTML markup of the host site changes.

#AUTHOR-Soumyadeep Jana

from tkinter import *
import requests,bs4,os,time
from PIL import Image


class GUI():

    def __init__(self):
            window = Tk()
            window.title("IMDB Collager")
            self.v = IntVar()

            radio1 = Radiobutton(window, text="Movies", variable=self.v, value=1).pack(anchor=W)
            radio2 = Radiobutton(window, text="TV Shows", variable=self.v, value=2).pack(anchor=W)
            btn=Button(window,text="Result",fg="red",command=self.processbtn).pack()
            window.mainloop()


    def processbtn(self):

        if self.v.get() == 1:
             res = requests.get("http://www.imdb.com/chart/top?sort=ir,desc&mode=simple&page=1")
             res.raise_for_status()
             dirname = "IMDB/" + "Movies"
                

        if self.v.get() == 2:
            res = requests.get("http://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2671049662&pf_rd_r=1Y2M3MC06FTV7YKZB9XN&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_ql_6")
            res.raise_for_status()
            dirname = "IMDB/" + "TV Shows"

        canvas = Image.new("RGBA",(1125,670))
        os.makedirs(dirname,exist_ok = True)
        soup = bs4.BeautifulSoup(res.text)
        imgElements = soup.select("tbody img")

        for elements in imgElements:
            link = elements.get("src")
            try:
                result = requests.get(link)
                print("Downloading..")
            except:
                print("Connection error")
                time.sleep(2)
                continue
            imgFile = open(os.path.join(dirname,os.path.basename(link)),"wb")
            for chunk in result.iter_content(10000):
                imgFile.write(chunk)

        print("Downloading complete")

        fileList = []
        counter = 0
        files = os.listdir(dirname)
        canvasWidth,canvasHeight = canvas.size
        imgWidth,imgHeight = 45,67

        for file in files:
            fileList.append(file)

        
                    
        for left in range(0,canvasWidth,imgWidth):
                        
            for top in range(0,canvasHeight,imgHeight):
                try:
                 
                    image = Image.open(os.path.join(dirname,fileList[counter]))
                    counter += 1
                    canvas.paste(image,(left,top))

                except:
                    print("Problem opening image")
                    continue

                
                    
        canvas.save(os.path.join(dirname,"Collage.jpg"))
        canvas.show()
        #sys.exit()


        

    

GUI()
                    

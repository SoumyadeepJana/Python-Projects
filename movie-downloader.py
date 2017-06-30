from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os,requests,bs4,datetime


class GUI():

    
    def __init__(self):
            window = Tk()
            window.title("Auto Movie Downloader")
            frame1 = Frame(window)
            frame1.pack()
            labTitle = Label(frame1,text = "Enter the name of movie")
            self.movieTitle = StringVar()
            entryTitle = Entry(frame1,textvariable = self.movieTitle)
            labTitle.grid(row = 6,column = 10,columnspan=4)
            entryTitle.grid(row = 16,column = 10,columnspan=3)
            frame2=Frame(window)
            frame2.pack()
            btn=Button(frame2,text="Fetch",fg="red",command=self.processbtn)
            btn.grid(row=0,column=6)
            frame3 = Frame(window)
            frame3.pack()
            self.statusLabel = Label(frame3,text = "Waiting for movie to downoad")
            self.statusLabel.grid(row = 0,column = 8 )
            window.mainloop()

    def processbtn(self):

        while True:

            if datetime.datetime.now().hour >= 16 and datetime.datetime.now().minute >= 0:

               

                movie = self.movieTitle.get()
                movie = movie.title()
                try:
                    requests.get("http://oceanofmovies.ws/category/720p-hd/")
                except:
                    self.statusLabel["text"] = "No connection."
                    continue
                browser = webdriver.Chrome()
                browser.get("http://oceanofmovies.ws/category/720p-hd/")
                input = browser.find_element_by_tag_name("input")
                input.send_keys(movie)
                input.send_keys(Keys.ENTER)
                try:
                    link = browser.find_element_by_link_text(movie+" Full Movie Download Free 720p")
                    link.click()
                    downloadLink = browser.find_element_by_xpath('//input[@alt="Download Movie"]')
                    downloadLink.click()
                    self.statusLabel["text"] = "Downloading movie..."
                    
                except:
                    print("No such element found (first)")
                    self.statusLabel["text"] = "Not Downloaded"
                break    

            else:
                    self.statusLabel["text"] = "Movie will be downloaded in a while"
                    



        


GUI()
		

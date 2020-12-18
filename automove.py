"""
=====================================
Name: automove.py
Desc: Automatically sorts and moves
      WhatsApp files to the specified 
      folder with Termux.
Author: Ann 
=====================================
"""

# import the required modules to interact with files and dirs
import os, shutil 
from styl import * # styling output

# WhatsApp path directories
path = "/sdcard/WhatsApp/Media/"
wdirs = ["WhatsApp Video","WhatsApp Images","WhatsApp Audio","WhatsApp Documents","WhatsApp Animated Gifs"]

# destination directories for moved files
dest = "/sdcard/WA-Media/"
dirs = ["WA-Videos","WA-Images","WA-Audios","WA-Documents","WA-Apks","Others"]

# create destination folder 
for i in range(len(dirs)):
   if os.path.exists(dest+dirs[i]) == False:
      os.makedirs(dest+dirs[i])
      print(style.OKGREEN+"folder",style.OKBLUE+dest+dirs[i],style.ENDC+style.OKGREEN,"created!")

# declaring arrays of files' formats 
# you can add your desired file format
vid_formats = ["mp4","3gp","mkv","avi"]
img_formats = ["jpg","png","jpeg","gif"]
aud_formats = ["mp3","aac","m4a"]
doc_formats = ["pdf","docx","xlsx","bok","txt","doc","pptx"]
apk_formats = ["apk","xapk"]

# formats = [vid_formats,img_formats,aud_formats,doc_formats,apk_formats]

def automove():
   files = os.listdir('./') # get list of all files in the current dir
   for f in files:
      if os.path.isfile(f): # strict to moving files only, not folders

         # split fileName.extension 
         ext = (f.split(".")[-1]).lower() # convert exts to lowercase

         # begin to move all files
         if ext in vid_formats:
            shutil.move(f,dest+dirs[0])
            print(style.OKGREEN+"Successfully moved",style.HEADER+f,style.OKGREEN+"to", style.OKBLUE+dest+dirs[0])
         elif ext in img_formats:
            shutil.move(f,dest+dirs[1])
            print(style.OKGREEN+"Successfully moved",style.HEADER+f,style.OKGREEN+"to", style.OKBLUE+dest+dirs[1])
         elif ext in aud_formats:
            shutil.move(f,dest+dirs[2])
            print(style.OKGREEN+"Successfully moved",style.HEADER+f,style.OKGREEN+"to", style.OKBLUE+dest+dirs[2])
         elif ext in doc_formats:
            shutil.move(f,dest+dirs[3])
            print(style.OKGREEN+"Successfully moved",style.HEADER+f,style.OKGREEN+"to", style.OKBLUE+dest+dirs[3])
         elif ext in apk_formats:
            shutil.move(f,dest+dirs[4])
            print(style.OKGREEN+"Successfully moved",style.HEADER+f,style.OKGREEN+"to", style.OKBLUE+dest+dirs[4])
         else:
            shutil.move(f,dest+dirs[5])
            print(style.OKGREEN+"Successfully moved",style.HEADER+f,style.OKGREEN+"to", style.OKBLUE+dest+dirs[5])

# logical statement
while True:
   print(style.WARNING+"\nDo you want to start moving files? [Yes/No] ")
   ans = input(f">{style.OKGREEN} ")
   ans = ans.lower()
   if ans == "y" or ans == "yes" or ans == "yes " or ans == "y ":
      # changing between all dirs inside WhatsApp path
      for i in range(len(wdirs)):
         os.chdir(path+wdirs[i])
         automove()
         
      print(style.OKGREEN+"\n+-+-+-+-+-+\nIt's DONE √\n+-+-+-+-+-+\n"+style.ENDC) 
      print(style.WARNING+"============================================================\n😊 you can find your files in 👉",style.BOLD+style.OKBLUE+"internal storage > WA-Media"+style.ENDC,style.WARNING+"\n============================================================"+style.ENDC)
      break
   elif ans == "n" or ans == "no" or ans == "no " or ans == "n ":
      print("\n____________________\n< see you later 👏 >\n--------------------\n        \   ^__^\n         \  (oo)\_______\n            (__)\       )\/\\\n                ||----w |\n                ||     ||w\n")
      break
   elif ans == "":
      print(style.FAIL+"[ERROR] no input! (yes/no/y/n) ???\n")
   elif ans != "y" or ans != "yes" or ans != "y " or ans != "yes " or ans != "n" or ans != "no" or ans != "n " or ans != "no ":
      print(style.FAIL+"\n[ERROR] input invalid. (yes/no/y/n)?!")
   

# make it possible to run on background








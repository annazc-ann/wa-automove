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

# WhatsApp path directories
path = "/sdcard/WhatsApp/Media/"
wdirs = ["WhatsApp Video","WhatsApp Images","WhatsApp Audio","WhatsApp Documents","WhatsApp Animated Gifs"]

# destination directories for moved files
dest = "/sdcard/WA-Media/"
dirs = ["WA-Videos","WA-Images","WA-Audios","WA-Documents","WA-Apks","Others"]

# declaring arrays of files' formats 
# you can add your desired file format
vid_formats = ["mp4","3gp","mkv","avi"]
img_formats = ["jpg","png","jpeg","gif"]
aud_formats = ["mp3","aac","m4a"]
doc_formats = ["pdf","docx","xlsx","bok","txt","doc","pptx"]
apk_formats = ["apk","xapk"]

formats = [vid_formats,img_formats,aud_formats,doc_formats,apk_formats]

def automove():
   files = os.listdir() # get list of all files in the current dir
   for f in files:
      if os.path.isfile(f): # strict to moving files only, not folders

         # split fileName.extension 
         ext = (f.split(".")[-1]).lower() # convert exts to lowercase

         # begin to move all files
         if ext in vid_formats:
            shutil.move(f,dest+dirs[0])
            print("Successfully moved",f,"to",dest+dirs[0])
         elif ext in img_formats:
            shutil.move(f,dest+dirs[1])
            print("Successfully moved",f,"to",dest+dirs[1])
         elif ext in aud_formats:
            shutil.move(f,dest+dirs[2])
            print("Successfully moved",f,"to",dest+dirs[2])
         elif ext in doc_formats:
            shutil.move(f,dest+dirs[3])
            print("Successfully moved",f,"to",dest+dirs[3])
         elif ext in apk_formats:
            shutil.move(f,dest+dirs[4])
            print("Successfully moved",f,"to",dest+dirs[4])
         elif ext != formats:
            shutil.move(f,dest+dirs[5])
            print("Successfully moved",f,"to",dest+dirs[5])
         else:
            print("Media not found")

# make it possible to run on background
while True:

  # changing between all dirs inside WhatsApp path
   os.chdir(path+wdirs[0])
   automove()

   os.chdir(path+wdirs[1])
   automove()

   os.chdir(path+wdirs[2])
   automove()

   os.chdir(path+wdirs[3])
   automove()

   os.chdir(path+wdirs[4])
   automove()







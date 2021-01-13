<h1>wa-automove</h1>
<p>Automatically sorts and moves files inside WhatsApp folders with Termux.</>

### Requirements
1. [Termux](https://play.google.com/store/apps/details?id=com.termux) app with storage access permission
2. Internet connection (installing python) 

### Usage
Open Termux app and then type:
```bash
$ pkg update && pkg upgrade -y
$ pkg install git python
```
clone this repository:
```bash
$ git clone https://github.com/annzc/wa-automove
$ cd wa-automove/
```
and then run the python script by typing:
```bash
$ python automove.py
```
<p>It will move the files inside your WhatsApp folder to the specified folders (according to the file extension) generated automatically by the script.</p>
<h3>🚨 ATTENTION 🚨</h3>
Running this script means that you will not be able to access 
your WhatsApp files inside the app. Otherwise, you can find and access your moved files inside 
<code>internal storage > WA-Media</code>.

### was inspired by:
https://youtu.be/JNl2krTKf-s


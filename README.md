<h1>wa-automove</h1>
<p>Automatically sorts and moves files inside WhatsApp folders with Termux.</>

### Requirements
1. [Termux app](https://play.google.com/store/apps/details?id=com.termux) with storage access permission
2. Internet connection (installing python) 

### Usage
Open Termux app and then type:
```bash
$ pkg update && pkg upgrade -y
$ pkg install git python 
$ git clone https://github.com/annazc-ann/wa-automove
$ cd wa-automove/
$ chmod +x *
$ sh mkdir.sh
```
and then run the python script by typing:
```bash
$ python automove.py
```
<p>It will move the files inside your WhatsApp folder to the specified folder (according to the file extension) created by <code>$ sh mkdir.sh</code>.
<br>Once it starts, it will always running in the background until you stop it by hit <code>ctrl+c</code> or
 the Termux app is closed</p>.

### 🚨🚨 ATTENTION 🚨🚨
Running this script means that you will not be able to access 
your WhatsApp files inside the app.<br>
Otherwise, you can find and access your moved files inside 
<code>/storage/emulated/0/WA-Media/</code>
<p>This project was inspired by:
https://youtu.be/JNl2krTKf-s
</p>

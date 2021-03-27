# Biblioteca Virtual Downloader
######A simple Python script to download ebooks from the website https://www.bvirtual.com.br/.
=====
This script was originally created some years ago to download the .png files from various ebooks. It worked flawlessly at the time.
The website has changed and now the .png files have a worse quality and awhite bar at the bottom to avoid piracy. Another thing is that some images are downloaded in a weird way, with the page occupying 1/4 os the total space, so it is not worth anymore (maybe).
I do not have access to the library anymore because I already graduated, so a do not guarantee that this script will work after the day it was uploaded.
=====
## Requirements
-  Python 3
-  Selenium API
-  Firefox x86
-  geckodriver
=====
## Instructions
Just run and write the url of the book you want. Before that there some things you need to check:
line 10 and 11 - input your email and password as strings for the login process;
line 22 - this is for a silent download. Without this line, Firefox will show all the process of download. It is a personal choice;
line 23 and 24 - location of Firefox in your computer for Linux and Windows, respectively. Use only one;
line 56 - depending on you internet speed, you might want to change this;
line 86 - this remove geckodriver.log after the process. Comment this if you want to keep the geckodriver.log.

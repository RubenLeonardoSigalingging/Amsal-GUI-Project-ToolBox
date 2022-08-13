#!/usr/bin/env python3


# Amsal 23:18 TB
# https://www.bible.com/id/bible/306/PRO.23.18.tb
# Karena masa depan sungguh ada, dan harapanmu tidak akan hilang.


# Created By Ruben Leonardo Sigalingging.
# Created On August 11, 2022, 7:50 PM
# Using Python Programming Language Version 3.8.10


import os
import sys
# Check Operating System
# https://www.delftstack.com/howto/python/python-detect-os/
if sys.platform=="win32" or sys.platform=="win64" or sys.platform=="cygwin":
	# pip install tk
	# https://pypi.org/project/tk/
	os.system("cls")
	# https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cls
	os.system("pip install tk")
	os.system("pip install pytube")
	os.system("pip install pywhatkit")
	os.system("pip install requests")
	os.system("pip install pyfiglet")
	os.system("pip install pycryptodome")
	os.system("cls")
elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
	os.system("clear")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("pip install tk")
	os.system("pip install pytube")
	os.system("pip install pywhatkit")
	os.system("pip install requests")
	os.system("pip install pyfiglet")
	os.system("pip install pycryptodome")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("clear")
elif sys.platform=="darwin":
	try:
		os.system("clear")
		os.system("pip install pywhatkit")
		os.system("pip install requests")
		os.system("pip install tk")
		os.system("pip install pytube")
		os.system("pip install pycryptodome")
		os.system("pip install pyfiglet")
	except:
		print("Something went wrong when downloading the module!!")
import tkinter
from tkinter import *
import tkinter.messagebox
# https://docs.python.org/3/library/tkinter.messagebox.html
from tkinter.messagebox import showinfo
import pywhatkit
# https://pypi.org/project/pywhatkit/
import pyfiglet
# https://pypi.org/project/pyfiglet/
import requests
# https://pypi.org/project/requests/
import pytube
# https://pypi.org/project/pytube/


def Coding_Tools(Created_By="Ruben Leonardo Sigalingging"):
	Root=tkinter.Tk()
	# Change program title
	Root.title("Amsal - Coding ToolBox for Developers")
	# Resize program
	Root.geometry("800x500")
	# Can be resized
	Root.resizable(width=True,height=True)
	# configure
	# https://www.colorhexa.com/000000
	Root.configure(bg="#000000",cursor="arrow")
	# https://www.tutorialspoint.com/python/tk_cursors.htm


	# Navigation bar
	# Python - Tkinter Frame
	# https://www.askpython.com/python-modules/tkinter/tkinter-padding-tutorial
	Navigation_bar=tkinter.Frame(Root,bg="#000000",bd=0,cursor="arrow",highlightbackground="#ffffff",highlightcolor="#a9a9a9")
	Navigation_bar.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=0,pady=0)


	Author_Label=tkinter.Label(Navigation_bar,anchor=tkinter.CENTER,bg="#008000",bd=0,cursor="pirate",font=("Ubuntu Condensed",33),fg="#ffffff",justify=tkinter.CENTER,text="Ruben Leonardo Sigalingging")
	Author_Label.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=0,pady=0)


	# Navbar Button
	Navbar_Frame=tkinter.Frame(Root,bg="#000000",bd=0,cursor="arrow",highlightbackground="#ffffff",highlightcolor="#a9a9a9")
	Navbar_Frame.pack(expand=False,fill=tkinter.BOTH,padx=0,pady=0)


	def Home_Function(Created_By="Ruben Leonardo Sigalingging"):
		quit()


	# Home Button
	Home_Button=tkinter.Button(Navbar_Frame,text="Home",activebackground="#ffffff",activeforeground="#008b8b",bd=0,bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",18),cursor="pirate",highlightcolor="#a9a9a9",justify=tkinter.CENTER,width=31,command=Home_Function)
	Home_Button.pack(expand=False,side=tkinter.LEFT,padx=0,pady=0)


	def Contact_Me(Created_By="Ruben Leonardo Sigalingging"):
		showinfo(title="Contact Me",message="Contact Me:\n\nrubenleonardosigalingging@proton.me")


	Contact_Button=tkinter.Button(Navbar_Frame,text="Contact",activebackground="#ffffff",activeforeground="#008b8b",bd=0,bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",18),cursor="pirate",highlightcolor="#a9a9a9",justify=tkinter.CENTER,width=31,command=Contact_Me)
	Contact_Button.pack(expand=False,side=tkinter.LEFT,padx=0,pady=0)


	def GitHub_Function(Created_By="Ruben Leonardo Sigalingging"):
		import webbrowser
		webbrowser.open(url="https://github.com/RubenLeonardoSigalingging",new=0,autoraise=True)


	GitHub_Button=tkinter.Button(Navbar_Frame,text="GitHub",activebackground="#ffffff",activeforeground="#008b8b",bd=0,bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",18),cursor="pirate",highlightcolor="#a9a9a9",justify=tkinter.CENTER,width=32,command=GitHub_Function)
	GitHub_Button.pack(expand=False,side=tkinter.LEFT,padx=0,pady=0)


	Left_Frame=tkinter.Frame(Root,bg="#a9a9a9",bd=0,cursor="arrow",highlightbackground="#ffffff",highlightcolor="#a9a9a9")
	Left_Frame.pack(expand=False,fill=tkinter.BOTH,side=tkinter.LEFT,padx=0,pady=0)


	def Checker_Function(Created_By="Ruben Leonardo Sigalingging"):
		import requests
		# Get_Variable=requests.get("https://api.ipify.org/").text


		IP_Address_Checker_Tool_Title=tkinter.Tk()
		IP_Address_Checker_Tool_Title.title("IP Address Checker Tool")
		IP_Address_Checker_Tool_Title.geometry("800x70")
		IP_Address_Checker_Tool_Title.configure(bg="#000000",cursor="arrow")
		IP_Address_Checker_Tool_Title.resizable(width=False,height=False)


		Coder=tkinter.Label(IP_Address_Checker_Tool_Title,anchor=tkinter.CENTER,bg="#008000",bd=0,cursor="arrow",font=("Ubuntu Condensed",35),fg="#ffffff",justify=tkinter.CENTER)
		Coder.configure(text="My IP Address: "+str(requests.get("https://api.ipify.org/").text))
		Coder.pack(expand=False,fill=tkinter.X,side=tkinter.TOP,padx=0,pady=0)


		IP_Address_Checker_Tool_Title.mainloop()

	IP_Address_Checker=tkinter.Button(Left_Frame,text="IP Address Checker\nTool",activebackground="#ffffff",activeforeground="#008b8b",bd=0,bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",18),highlightcolor="#008b8b",justify=tkinter.CENTER,command=Checker_Function,cursor="pirate")
	IP_Address_Checker.pack(expand=False,side=tkinter.TOP,padx=12,pady=12)


	def Hash_Tools(Created_By="Ruben Leonardo Sigalingging"):
		Title_Variable=tkinter.Tk()
		Title_Variable.title("Coding ToolBox for Developers")
		Title_Variable.geometry("1366x768")
		Title_Variable.configure(bg="#000000",cursor="arrow")
		Title_Variable.resizable(width=True,height=True)


		Label_Variable=tkinter.Label(Title_Variable,anchor=tkinter.CENTER,bg="#228b22",bd=0,cursor="pirate",font=("Ubuntu Condensed",33),fg="#ffffff",justify=tkinter.CENTER,text="Coding.Tools")
		Label_Variable.pack(expand=False,fill=tkinter.X,side=tkinter.TOP,padx=0,pady=0)


		Label_Variable2=tkinter.Label(Title_Variable,anchor=tkinter.CENTER,bg="#ffffff",bd=0,cursor="pirate",font=("Ubuntu Condensed",18),fg="#008b8b",justify=tkinter.CENTER,text="Coding ToolBox for Developers")
		Label_Variable2.pack(expand=False,fill=tkinter.X,side=tkinter.TOP,padx=0,pady=0)


		Variable_Label_3=tkinter.Label(Title_Variable,anchor=tkinter.CENTER,bg="#ff8c00",bd=0,cursor="pirate",font=("Ubuntu Condensed",15),fg="#ffffff",justify=tkinter.CENTER,text="Hash & Cryptography Related Tools",width=30)
		Variable_Label_3.pack(expand=False,side=tkinter.TOP,padx=25,pady=25)


		First_Frame=tkinter.Frame(Title_Variable,bg="#ffffff",bd=0,cursor="arrow",highlightbackground="#a9a9a9",highlightcolor="#008b8b")
		First_Frame.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP)


		MD5_Hash_Button=tkinter.Button(First_Frame,text="MD5 Hash Generator\nOnline Tool",activebackground="#ffffff",activeforeground="#008b8b",bd=0,bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",15),highlightcolor="#a9a9a9",justify=tkinter.CENTER)
		MD5_Hash_Button.pack(expand=False,side=tkinter.LEFT,padx=0,pady=0)


		SHA1_Hash_Generator_Button=tkinter.Button(First_Frame,text="SHA1 Hash Generator\nOnline Tool",activebackground="#ffffff",activeforeground="#008b8b",bd=0,bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",15),highlightcolor="#a9a9a9",justify=tkinter.CENTER)
		SHA1_Hash_Generator_Button.pack(expand=False,side=tkinter.LEFT,padx=3,pady=0)



		# expand=mengembangkan
		# fill = mengisi
		# side = samping
		# TOP = ATAS
		Title_Variable.mainloop()


	Hash_And_Cryptography_Related_Tools=tkinter.Button(Left_Frame,text="Hash & Cryptography\nRelated Tools",activebackground="#ffffff",activeforeground="#008b8b",bd=0,bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",18),highlightcolor="#a9a9a9",justify=tkinter.CENTER,cursor="pirate",command=Hash_Tools)
	Hash_And_Cryptography_Related_Tools.pack(expand=False,side=tkinter.TOP,padx=12,pady=12)

	Root.mainloop()
Coding_Tools()
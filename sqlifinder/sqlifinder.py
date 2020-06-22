#!/usr/bin/env python

from googlesearch import search
from colorama import init, Fore, Back, Style
import urllib.request
import pyfiglet
import time
import sys
import re

def main():
	init(autoreset=True)
	ascii_banner = pyfiglet.figlet_format('SQLi Finder')
	print(Fore.YELLOW + Back.RED + ascii_banner)
	print(Fore.RED + Back.WHITE + 'Author: Roberto Reigada Rodríguez - roberreigada@gmail.com')
	print(Fore.RED + Back.WHITE + 'Date: 17/06/2020')
	print()
	print(Fore.YELLOW + 'Usage: sqlifinder <Google Dork> <injectable parameter 1> <injectable parameter 2>...')
	print(Fore.YELLOW + 'Example: sqlifinder "shop inurl:"php?ID"" id item\n')
	
	arguments = len(sys.argv) - 1
	if arguments < 1:
		print(Fore.RED + 'ERROR: Not enough arguments. <Google Dork> <injectable parameters> are missing\n')
		exit(0)
	if arguments < 2:
		print(Fore.RED + 'ERROR: Not enough arguments. Please introduce the <injectable parameters>\n')
		exit(0)
	else:
		googledork = str(sys.argv[1])
	
	print(Fore.GREEN + 'Results obtained for Dork: ' + googledork)
	
	try:
		googleEntries = search(googledork, stop=100, pause=2)
	except urllib.error.HTTPError:
		print(Fore.BLACK + Back.YELLOW + 'HTTP Error 429: Too many requests. Please wait before running SQLiFinder again...')
		exit(0)
	
	for urlEntry in googleEntries:
		print(Back.YELLOW + urlEntry)
		urlSQLI = urlEntry + '\''
		req = urllib.request.Request(
			urlSQLI, 
			data=None, 
			headers={
			'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
			}
		)
		try:
			urlResponse = urllib.request.urlopen(req, timeout=20)
			htmlPage = urlResponse.readlines()
			vulnerable = False
			for htmlLine in htmlPage:
				if ('mysql'.encode() in htmlLine) or ('Incorrect syntax'.encode() in htmlLine) or ('SQL syntax'.encode() in htmlLine):
					vulnerable = True
					break
			if vulnerable:
				print(Fore.RED + '    ' + urlSQLI + ' MAY BE INJECTABLE')
			else:
				print('    ' + urlSQLI)
		except urllib.error.HTTPError as e:
			if e.code == 404:
				print(Fore.YELLOW + '    ' + urlSQLI + " HTTP Error 404: NOT FOUND")
			if e.code == 403:
				print(Fore.YELLOW + '    ' + urlSQLI + " HTTP Error 403: FORBIDDEN")
			if e.code == 302:
				print(Fore.YELLOW + '    ' + urlSQLI + " HTTP Error 302: FOUND")
		except urllib.error.URLError:
			print(Fore.YELLOW + '    ' + urlSQLI + " ERROR CONNECTING TO THE URL")
		except:
			print(Fore.YELLOW + '    ' + urlSQLI + " TIMEOUT")
		time.sleep(2)
		for i in range(2, arguments+1):
			injparam = str(sys.argv[i])
			injparam1 = '\?' + injparam + '='
			injparam2 = '\&' + injparam + '='
			paramURL1 = re.split(injparam1, urlEntry, flags=re.IGNORECASE)
			paramURL2 = re.split(injparam2, urlEntry, flags=re.IGNORECASE)
			finalurl = ''
			if len(paramURL1[0]) < len(urlEntry):
				charstoadd = 4
				for j in range(len(paramURL1[0])+4, len(urlEntry)):
					if urlEntry[j] != '&':
						charstoadd = charstoadd + 1
					else:
						break
				finalurl= urlEntry[0:len(paramURL1[0])+charstoadd]
			
			if len(paramURL2[0]) < len(urlEntry):
				charstoadd = 4
				for j in range(len(paramURL2[0])+4, len(urlEntry)):
					if urlEntry[j] != '&':
						charstoadd = charstoadd + 1
					else:
						break
				finalurl= urlEntry[0:len(paramURL2[0])+charstoadd]	
			if (finalurl != '') and (len(finalurl) != len(urlEntry)):
				urlSQLI = finalurl + '\''
				req = urllib.request.Request(
					urlSQLI, 
					data=None, 
					headers={
					'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
					}
				)
				try:
					urlResponse = urllib.request.urlopen(req, timeout=20)
					htmlPage = urlResponse.readlines()
					vulnerable = False
					for htmlLine in htmlPage:
						if ('mysql'.encode() in htmlLine) or ('Incorrect syntax'.encode() in htmlLine) or ('SQL syntax'.encode() in htmlLine):
							vulnerable = True
							break
					if vulnerable:
						print(Fore.RED + '    ' + urlSQLI + ' MAY BE INJECTABLE')
					else:
						print('    ' + urlSQLI)
				except urllib.error.HTTPError as e:
					if e.code == 404:
						print(Fore.YELLOW + '    ' + urlSQLI + " HTTP Error 404: NOT FOUND")
					if e.code == 403:
						print(Fore.YELLOW + '    ' + urlSQLI + " HTTP Error 403: FORBIDDEN")
					if e.code == 302:
						print(Fore.YELLOW + '    ' + urlSQLI + " HTTP Error 302: FOUND")
				except urllib.error.URLError:
					print(Fore.YELLOW + '    ' + urlSQLI + " ERROR CONNECTING TO THE URL")
				except:
					print(Fore.YELLOW + '    ' + urlSQLI + " TIMEOUT")
				time.sleep(2)
	exit(0)	

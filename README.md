# sqlifinder
**Program to scrape entries from Google using a dork and test each of those entries for basic SQL injection vulnerabilities**

![alt text](https://i.imgur.com/0oNKVMz.jpg)

**This tool has been shared with an educational purpose and to inform webmasters of the SQL vulnerabilities of their websites. I am not responsible of the possible missuses done by the users that have downloaded the tool**

## Overview
**sqlifinder** is a simple tool written in Python that allows you to retrieve the first 100 results from Google and check for basic SQL Injection vulnerabilities.
sqlifinder adds a **'** at the end of every URL retrieved from Google. Also, it searchs for the parameter that you specify. For example, 
if you get the following URL -> ww2.urlexample.com?id=1&page=2 and you had specified the parameter id, sqlifinder would do the 2 following tests:
  - ww2.urlexample.com?id=1&page=2'
  - ww2.urlexample.com?id=1'
  
  sqlifinder would send those 2 petitions to the server and check in the server response for SQL errors. If any SQL error is found, sqlifinder will mark that website as **INJECTABLE**
  
## Installation
  To install sqlifinder execute the following commands:
  
 `git clone https://github.com/roberreigada/sqlifinder.git`
 
 `cd sqlifinder`
 
 `sudo python3 setup.py install`
 
## How to use sqlifinder?
Once it is installed you can run:
 
`sqlifinder <GoogleDorkBetween""> <injectable parameter 1> <injectable parameter 2>`
 
Example:
`sqlifinder "inurl:"php?ID"" id`
 
	- inurl:"php?ID" would be the Google Dork 
 	- id would be the injectable parameter (not case sensitive)

## Limitations
If you get the "HTTP Error 429: Too many requests. Please wait before running SQLiFinder again..." it means that you have retrieved way too many results from Google in a short period of time. Please wait for 1 or 2 hours and then try again.

https://reigadaopsec.com/sqlifinder-a-python-program-to-find-websites-vulnerable-to-sql-injection/
#!/bin/python3
# ************************************************************************** */
#
#                                                        :::      ::::::::  
#   less33_p2_post.py                                  :+:      :+:    :+:
#                                                    +:+ +:+         +:+    
#   By: wmiyu <wmiyu@student.21-school.ru>         +#+  +:+       +#+   
#                                                +#+#+#+#+#+   +#+        
#   Created: 16.02.2023 A.D.                          #+#    #+#       
#                                                    #+#   #+#+#+#+#  
#   Description:
# ************************************************************************** */

from urllib import request, parse
import sys

myUrl = "http://www.google.com/search?"
valueToSearch = {'q': 'Ecole 42'}
fileOut = "google_result.html"

myHeader = {}
myHeader['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

try:
    myData = parse.urlencode(valueToSearch)
    print("===============================================")
    print(myData)
    print("===============================================")
    myUrl = myUrl + myData
    req = request.Request(myUrl, headers=myHeader)
    resp = request.urlopen(req)
    resp = resp.readlines()
    for line in resp:
        print(line)
    print("===============================================")
except Exception:
    print("(!) ERROR: ", sys.exc_info()[1])

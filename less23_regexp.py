# ************************************************************************** */
#
#                                                        :::      ::::::::  
#   less23_regexp.py                                   :+:      :+:    :+:
#                                                    +:+ +:+         +:+    
#   By: wmiyu <wmiyu@student.21-school.ru>         +#+  +:+       +#+   
#                                                +#+#+#+#+#+   +#+        
#   Created: 07.02.2023 A.D.                          #+#    #+#
#                                                    #+#   #+#+#+#+#
#   Description: Working with RegExp
# ************************************************************************** */

"""
\d  = [0-9]
\D  = not [0-9]
\w  = [A-Z, a-z or 0-9]
\W  = not Alphabet
\s  = space
\S  = nospace

[0-9]{3}                    = \d\d\d
[A-Z][a-z]+                 = search Name in Title format
@\w+\.\w+                   = search domain like intel.com
[\w.-]+@[A-Za-z-]+\.[\w.]+  = search email
[\w.-]+@(?!intel\.com)[A-Za-z-]+\.[\w.]+  = search email exclude intel.com

helpful site:              regex101.com
"""
import re

filein = open('dir20.txt', 'r', encoding='utf-8')

mytext = filein.read()
filein.close()
print(mytext)

# ================= searching date + time from dir output =========
# filterlookfor = r"\d\d.\d\d.\d\d\d\d\s+\d\d:\d\d"
filterlookfor = r"\w+\s\d+\s+\d\d:\d\d"

allresults = re.findall(filterlookfor, mytext)

for res in allresults:
    print(res)
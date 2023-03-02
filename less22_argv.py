# ************************************************************************** */
#
#                                                        :::      ::::::::
#   less22.py                                         :+:      :+:    :+:
#                                                    +:+ +:+         +:+
#   By: wmiyu <wmiyu@student.21-school.ru>         +#+  +:+       +#+
#                                                +#+#+#+#+#+   +#+
#   Created: 07.02.2023                               #+#    #+#
#   IDE: PyCharm -*- coding: utf-8 -*-               #+#   #+#+#+#+#
#
#   This program takes dir names as arguments and creates subfolder tree
# ************************************************************************** */

import os
import sys

if len(sys.argv) < 2:
    print("Not Enough arguments. Usage to create dirs: cmd <dir1> ... <dirX>")
    sys.exit(1)
else:
    arguments : [] = sys.argv[1:]
    print("Making dirs :" + str(arguments))
    for arg in arguments:
        try:
            os.mkdir(arg)
        except Exception:
            print(sys.exc_info()[1])
        else:
            os.chdir(arg)
            cmdstr = 'echo "This dir created by Python3 less22." >' + arg + '.txt'
            os.system(cmdstr)



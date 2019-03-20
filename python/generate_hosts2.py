for i in range(62):
  if i < 31:
    if i < 10:
      print ("10.10.85."+str(10+i) + "   id=ubuntu-hx-0"+str(i) + "  ucspe=10.10.85."+str(100+i))
    else:
      print ("10.10.85."+str(10+i) + "   id=ubuntu-hx-"+str(i) + "  ucspe=10.10.85."+str(100+i))
  
  else:
      print ("10.10.86."+str(i-20) + "   id=ubuntu-hx-"+str(i) + "  ucspe=10.10.86."+str(70+i))

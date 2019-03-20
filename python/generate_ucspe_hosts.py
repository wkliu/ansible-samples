for i in range(62):
  if i < 31:
    if i < 10:
      print ("10.10.85."+str(100+i) + "   id=ucspe0"+str(i)+"-1")
      print ("10.10.85."+str(130+i) + "   id=ucspe0"+str(i)+"-2")
      print ("10.10.85."+str(160+i) + "   id=ucspe0"+str(i)+"-3")
    else:
      print ("10.10.85."+str(100+i) + "   id=ucspe"+str(i)+"-1")
      print ("10.10.85."+str(130+i) + "   id=ucspe"+str(i)+"-2")
      print ("10.10.85."+str(160+i) + "   id=ucspe"+str(i)+"-3")

  else:
    print ("10.10.86."+str(70+i) + "   id=ucspe"+str(i)+"-1")
    print ("10.10.86."+str(100+i) + "   id=ucspe"+str(i)+"-2")
    print ("10.10.86."+str(130+i) + "   id=ucspe"+str(i)+"-3")
  

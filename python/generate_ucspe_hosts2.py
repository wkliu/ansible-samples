print("{")
for i in range(62):
  if i < 31:
    if i < 10:
      print ("\"ucspe0"+str(i)+"-1\": \"10.10.85."+str(100+i)+"\",")
      print ("\"ucspe0"+str(i)+"-2\": \"10.10.85."+str(130+i)+"\",")
      print ("\"ucspe0"+str(i)+"-3\": \"10.10.85."+str(160+i)+"\",")
    else:
      print ("\"ucspe"+str(i)+"-1\": \"10.10.85."+str(100+i)+"\",")
      print ("\"ucspe"+str(i)+"-2\": \"10.10.85."+str(130+i)+"\",")
      print ("\"ucspe"+str(i)+"-3\": \"10.10.85."+str(160+i)+"\",")
  else:
    print ("\"ucspe"+str(i)+"-1\": \"10.10.86."+str(70+i)+"\",")
    print ("\"ucspe"+str(i)+"-2\": \"10.10.86."+str(100+i)+"\",")
    print ("\"ucspe"+str(i)+"-3\": \"10.10.86."+str(130+i)+"\",")
print("}") 

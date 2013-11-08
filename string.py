import time;
print "Enter a string how long or short you want.....>"
str=raw_input(">")

elements=[]
Length=len(str)
if Length < 3:
  print str[::-1]
elif Length>3 and Length<6:
   print str  
elif Length>6:
  print "Your string is more than 6 characters!!"   


print "Thank You!"
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

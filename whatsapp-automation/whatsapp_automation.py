# import only the first library using pip
#pip install pywhatkit
# I used as in importing it to save my time while calling the libabries in my code.
#make sure you have your Whatsapp web active and connected to your phone
import pywhatkit as kt
import getpass as gp

#welcome message
print('Let'\s automate Whatsapp')
#p_num is the access point and automation, the Phonenumber, should be the receivers number
p_num = gp.getpass(prompt = 'Phonenumber: ', stream = None)
#message I want to send
msg = 'Time to code, Chryz'
#using the ypwhatkit as kt to send the message and adding the necessary parameters
#p_num is the automation using your number, msg, is the message you want to send, `9`,`35` is the time you want to send the message
kt.sendwhatmsg(p_num, msg, 9, 35)

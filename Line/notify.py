from line_notify import LineNotify

try:
    from config_dev import *

except:
    from config_prod import *

notify = LineNotify(LINE_NOTIFY_TOKEN)

def SendMsg(msg):
    notify.send(msg)



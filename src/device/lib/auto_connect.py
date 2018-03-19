import network
try:
  import urequests
  import ujson as json
except:
  print("Can't import libraries")

cred = {"AP_": "Novosedly"}

def auto_connect():
  try:
    f = open('cred.json', 'r')
    saved_cred = json.load(f)
    f.close()
    cred.update(saved_cred)
    saved_cred = None
  except Exception:
    pass
  sta_if = network.WLAN(network.STA_IF)
  sta_if.active(True)
  scanned_ap = sta_if.scan()
  found = False
  print("Known AP:%s" % (str(cred)))
  for ap in scanned_ap:
    print("checking %s" % (ap[0]))
    if(ap[0].decode('ascii') in cred):
      found = ap[0].decode('ascii')
      print("Known AP found %s %s" % (found, cred[found]))
      break
  if(found):
    sta_if.connect(found, cred[found])
    sta_if.isconnected()
  else:
    print("No AP found!")

def add_cred(name, passwd):
  try:
    f = open('cred.json', 'r')
    saved_cred = json.load(f)
    f.close()
  except Exception as e:
    saved_cred = {}
  saved_cred[name] = passwd
  f = open('cred.json', 'w')
  f.write(json.dumps(saved_cred))
  f.close()

def con_test():
  if not 'urequests' in locals():
    return None
  try:
    response = urequests.get('http://klusacek.tk')
    pass
  except Exception:
    return False
  return True

from TV import *


televisao = Tv()

televisao.tvon()
while True:
    televisao.tvstatus()
    if televisao.status is False:
        break

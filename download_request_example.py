# import package needed
import requests

# open new file or clear it up
open("gainData.json", "w").write('')
# the first link
URL = "http://riderts.app/bustime/api/v3/getvehicles?key=<your_key_here>=1,2,3,5,6,7,8,9,10,11&format=json"
f = open("gainData.json", "w")

# download json needed
response = requests.get(URL)
data = str(response.content)

# clean up the data
para = 0
cleaned = ''
for letter in data:
    if letter == "\\":
        cleaned += ''
        para = 1
    elif para == 1 or letter == ' ':
        cleaned += ''
        para = 0
    else:
        cleaned += letter

a = 0
b = 0
c = 0
for letter in cleaned:
    if letter == '[':
        b = a
    elif letter == ']':
        c = a
        break
    a += 1

f.write(cleaned[b:c])

# the second link
URL = "http://riderts.app/bustime/api/v3/getvehicles?key=<your_key_here>=12,13,15,16,17,20,23,24,25,26&format=json"

# download json needed
response = requests.get(URL)
data = str(response.content)

# clean up the data
para = 0
cleaned = ''
for letter in data:
    if letter == "\\":
        cleaned += ''
        para = 1
    elif para == 1 or letter == ' ':
        cleaned += ''
        para = 0
    else:
        cleaned += letter

a = 0
b = 0
c = 0
for letter in cleaned:
    if letter == '[':
        b = a
    elif letter == ']':
        c = a
        break
    a += 1

f.write(',' + cleaned[b+1:c])

# the third link
URL = "http://riderts.app/bustime/api/v3/getvehicles?key=<your_key_here>=27,33,34,35,37,38,43,46,75,119&format=json"

# download json needed
response = requests.get(URL)
data = str(response.content)

# clean up the data
para = 0
cleaned = ''
for letter in data:
    if letter == "\\":
        cleaned += ''
        para = 1
    elif para == 1 or letter == ' ':
        cleaned += ''
        para = 0
    else:
        cleaned += letter

a = 0
b = 0
c = 0
for letter in cleaned:
    if letter == '[':
        b = a
    elif letter == ']':
        c = a
        break
    a += 1

f.write(',' + cleaned[b+1:c])

# the fourth link
URL = "http://riderts.app/bustime/api/v3/getvehicles?key=<your_key_here>=122,125,126,127,150,711&format=json"

# download json needed
response = requests.get(URL)
data = str(response.content)

# clean up the data
para = 0
cleaned = ''
for letter in data:
    if letter == "\\":
        cleaned += ''
        para = 1
    elif para == 1 or letter == ' ':
        cleaned += ''
        para = 0
    else:
        cleaned += letter

a = 0
b = 0
c = 0
for letter in cleaned:
    if letter == '[':
        b = a
    elif letter == ']':
        c = a
        break
    a += 1

f.write(',' + cleaned[b+1:c])

# write a null bus position with N/A capacity to keep the layer active when the transit service is down at night

f.write(',{"vid": "null","tmstmp": "null","lat": "90","lon": "90","hdg": "0","pid": 0,"rt": "null","des": "null","pdist": 0,"dly": null,"spd": 0,"tatripid": "null","origtatripno": "null","tablockid": "null","zone": "null","mode": 0,"psgld": "N/A","stst": 0,"stsd": "null"}')

# write a null bus position with FULL capacity to keep legend with full bus entry

f.write(',{"vid": "null","tmstmp": "null","lat": "90","lon": "90","hdg": "0","pid": 0,"rt": "null","des": "null","pdist": 0,"dly": null,"spd": 0,"tatripid": "null","origtatripno": "null","tablockid": "null","zone": "null","mode": 0,"psgld": "FULL","stst": 0,"stsd": "null"}')

# write a null bus position with HALF_EMPTY capacity to keep legend with HALF_EMPTY bus entry

f.write(',{"vid": "null","tmstmp": "null","lat": "90","lon": "90","hdg": "0","pid": 0,"rt": "null","des": "null","pdist": 0,"dly": null,"spd": 0,"tatripid": "null","origtatripno": "null","tablockid": "null","zone": "null","mode": 0,"psgld": "HALF_EMPTY","stst": 0,"stsd": "null"}')

# write a null bus position with EMPTY capacity to keep legend with EMPTY bus entry

f.write(',{"vid": "null","tmstmp": "null","lat": "90","lon": "90","hdg": "0","pid": 0,"rt": "null","des": "null","pdist": 0,"dly": null,"spd": 0,"tatripid": "null","origtatripno": "null","tablockid": "null","zone": "null","mode": 0,"psgld": "EMPTY","stst": 0,"stsd": "null"}]')

# close the file
f.close()

# print a message
print("Download complete")

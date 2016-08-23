import os

def cmd (cmd):
    os.system(cmd)

services = ('front50', 'clouddriver', 'orca', 'rosco', 'gate')

cmd("rm -rf services")
cmd("mkdir services")

for service in services:
    cmd("git clone https://github.com/spinnaker/" + service + ".git services/" + service)
    cmd("rm services/" + service + "/" + service + "-web/config/" + service + ".yml")
    cmd("cp config/" + service + ".yml services/" + service + "/" + service + "-web/config/" + service + ".yml")

cmd("git clone https://github.com/spinnaker/deck.git services/deck")

print "building deck"
cmd('docker run --rm -v `pwd`/services/deck:/build -e AUTH_ENABLED=false -e API_HOST=/gate -e BAKERY_DETAIL_URL=/bakery quay.io/spinnaker/deck bash -c "cd /build; npm install; npm run build"')
print "deck built inside services/deck/build/webpack"
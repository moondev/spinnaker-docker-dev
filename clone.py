import os

def cmd (cmd):
    os.system(cmd)

services = ('front50', 'clouddriver', 'orca', 'gate')


cmd("mkdir services")

for service in services:
    cmd("git clone https://github.com/spinnaker/" + service + ".git services/" + service)
    cmd("rm services/" + service + "/" + service + "-web/config/" + service + ".yml")
    cmd("cp config/" + service + ".yml services/" + service + "/" + service + "-web/config/" + service + ".yml")

cmd("git clone https://github.com/spinnaker/deck.git services/deck")
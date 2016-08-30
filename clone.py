import os, shutil, stat, errno

services = ('front50', 'clouddriver', 'orca', 'rosco', 'gate')

def cmd (cmd):
    os.system(cmd)

def handleRemoveReadonly(func, path, exc): # Delete readonly files (windows)
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

if os.path.exists("services"):
    shutil.rmtree("services", ignore_errors=False, onerror=handleRemoveReadonly)

cmd("mkdir services")

for service in services:
    cmd("git clone https://github.com/spinnaker/" + service + ".git services/" + service)
    os.remove("services/" + service + "/" + service + "-web/config/" + service + ".yml")
    shutil.copy2("config/" + service + ".yml", "services/" + service + "/" + service + "-web/config/" + service + ".yml")

print "building deck"
cmd("git clone https://github.com/spinnaker/deck.git services/deck")
deckPath = os.path.abspath("services/deck")
cmd('docker run --rm -v ' + deckPath + ':/build -e AUTH_ENABLED=false -e API_HOST=/gate -e BAKERY_DETAIL_URL=/bakery quay.io/spinnaker/deck bash -c "cd /build; npm install; npm run build"')
print "deck built inside services/deck/build/webpack"

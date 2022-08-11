import json
import os.path

pathFile = "src\\backup-users.json"

def createBackup():
  isBackup = os.path.exists(pathFile)

  if not isBackup:
    with open(pathFile, "w") as backFile:
      backFile.write("[]")
      print("backup-users.json creado")

def saveBackup(newBackup):
  createBackup()
  with open(pathFile, "r+") as backFile:
    backup_str = backFile.read() or "[]"
    backup = json.loads(backup_str)

    backup = backup + newBackup
    
    backup_json = json.dumps(backup, indent=2)

    backFile.seek(0)
    backFile.write(backup_json)
    backFile.truncate()

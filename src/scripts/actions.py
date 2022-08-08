import requests
from pprint import pprint
from datetime import datetime

class Actions:
  url = "http://127.0.0.1:8000/users"
  temp_backup = []

  def __printJson(self, json):
    pprint(json, indent=2)
  
  def __printError(self, str):
    print('\033[41m ', str)

  def getAll(self, payload):
    resp = requests.get(self.url)

    if resp.ok:
      resp_json = resp.json()
      print("\nRespuesta:")
      self.__printJson(resp_json)
    else:
      self.__printError("Error obteniendo los usuarios")

  def getOne(self, payload):
    discriminant = payload["discriminant"]
    resp = requests.get(f"{self.url}/{discriminant}")
    
    if resp.ok:
      resp_json = resp.json()
      if not resp_json: return self.__printError("Usuario no encontrado")
      print("\nRespuesta:")
      self.__printJson(resp_json)
    else:
      self.__printError("Error obteniendo el usuario")

  def create(self, payload):
    data = {
      "discriminant": int(payload["discriminant"]),
      "username": payload["username"],
      "image": payload["image"],
      "status": int(payload["status"])
    }
    resp = requests.post(self.url, json=data)

    if resp.ok:      
      resp_json = resp.json()
      date = datetime.now()
      date_str = date.strftime('%x %X')
      reqBackup = {
        "type": "create",
        "date": date_str,
        "user": resp_json
      }
      self.temp_backup.append(reqBackup)

      print("\nUsuario creado!")
      self.__printJson(resp_json)
    else:
      self.__printError("Error creando el usuario")

  def update(self, payload):
    discriminant = payload["discriminant"]
    params={"status": payload["status"]}
    resp = requests.put(f"{self.url}/{discriminant}", params=params)

    if resp.ok:
      resp_json = resp.json()
      date = datetime.now()
      date_str = date.strftime('%x %X')
      reqBackup = {
        "type": "update",
        "date": date_str,
        "user": resp_json
      }
      self.temp_backup.append(reqBackup)

      print("\nUsuario actualizado!\n")
      self.__printJson(resp_json)
    else:
      self.__printError("Error actualizando el usuario")

  def delete(self, payload):
    discriminant = payload["discriminant"]
    resp = requests.delete(f"{self.url}/{discriminant}")

    if resp.ok:
      resp_json = resp.json()
      date = datetime.now()
      date_str = date.strftime('%x %X')
      reqBackup = {
        "type": "delete",
        "date": date_str,
        "user": resp_json
      }
      self.temp_backup.append(reqBackup)

      print("\nUsuario Eliminado!\n")
      self.__printJson(resp_json)
    else:
      self.__printError("Error eliminando el usuario")

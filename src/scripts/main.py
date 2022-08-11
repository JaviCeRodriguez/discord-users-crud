from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from backup import saveBackup
from actions import Actions
from enum import Enum
 
class RequestType(Enum):
	getALL = "get_users"
	getOne = "get_user"
	post = "create_user"
	put = "update_user"
	delete = "delete_user"

userActions = Actions()

def main():
	questions = [
		{
			"type": "list",
			"name": "type",
			"choices": [
				Choice(name="GET ALL", value=RequestType.getALL),
				Choice(name="GET ONE", value=RequestType.getOne),
				Choice(name="POST", value=RequestType.post),
				Choice(name="PUT", value=RequestType.put),
				Choice(name="DELETE", value=RequestType.delete),
				Separator(15 * "-"),
				Choice(value=None, name="Exit")
			],
			"message": "Elige el tipo de request:",
			"default": None,
		},
		{
			"type": "number",
			"name": "discriminant",
			"message": "Ingresar discriminante:",
			"min_allowed": 1,
			"default": None,
			"validate": lambda result: result != '',
			"invalid_message": "El discriminante es requerido",
			"when": lambda result: result["type"] and result["type"] != RequestType.getALL,
		},
		{
			"type": "input",
			"name": "username",
			"message": "Nombre:",
			"when": lambda result: result["type"] == RequestType.post,
			"validate": lambda result: len(result.strip()) > 0,
    	"invalid_message": "El nombre es requerido",
		},
		{
			"type": "input",
			"name": "image",
			"message": "Imagen:",
			"when": lambda result: result["type"] == RequestType.post,
		},
		{
			"type": "number",
			"name": "status",
			"message": "Estatus:",
			"min_allowed": 1,
			"max_allowed": 4,
			"validate": lambda result: result != '',
			"invalid_message": "El estatus es requerido",
			"default": None,
			"when": lambda result: result["type"] == RequestType.post or result["type"] == RequestType.put,
		},
		{
			"type": "confirm",
			"message": "Eliminar usuario?",
			"name": "proceed",
			"default": False,
			"when": lambda result: result["type"] == RequestType.delete
		}
	]

	result = prompt(questions)
	requestType = result["type"]
	request_confirmed = requestType != RequestType.delete or result["proceed"]
	
	actions = {
		RequestType.getALL: userActions.getAll,
		RequestType.getOne: userActions.getOne,
		RequestType.post: userActions.create,
		RequestType.put: userActions.update,
		RequestType.delete: userActions.delete,
	}

	if requestType:
		if request_confirmed:
			actions[requestType](result)
		main()
	else:
		saveBackup(userActions.temp_backup)

main()
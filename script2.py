import json
obj=json.load(open("test_payload.json"))
del(obj['outParams'])
del(obj['inParams']['appdate'])
open("updated-file.json","w").write(
	json.dumps(obj,sort_keys=True,indent=4))

from lib.files import makeFile, makeJson
from lib.i_o import getData

data = getData().getName().dpGetMcVersion()
data.namespace = data.name.lower().replace(" ", "_")

makeJson(
	f"{data.name}/pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion, "description": f"{data.name}"}}
)
makeJson(
	f"{data.name}/data/minecraft/tags/functions/load.json",
	{"values": [f"{data.namespace}:load"]}
)
makeJson(
	f"{data.name}/data/minecraft/tags/functions/tick.json",
	{"values": [f"{data.namespace}:tick"]}
)
makeFile(f"{data.name}/data/{data.namespace}/functions/tick.mcfunction", "")
makeFile(f"{data.name}/data/{data.namespace}/functions/load.mcfunction", "")

from lib.files import makeFile, makeJson
from lib.i_o import getData

data = getData().getDatapackName().getMcVersion()
data.namespace = data.datapackName.lower().replace(" ","_")

makeJson(
	f"{data.datapackName}/pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion,"description": f"{data.datapackName}"}}
)
makeJson(
	f"{data.datapackName}/data/minecraft/tags/functions/load.json",
	{"values": [f"{data.namespace}:load"]}
)
makeJson(
	f"{data.datapackName}/data/minecraft/tags/functions/tick.json",
	{"values": [f"{data.namespace}:tick"]}
)
makeFile(f"{data.datapackName}/data/{data.namespace}/functions/tick.mcfunction", "")
makeFile(f"{data.datapackName}/data/{data.namespace}/functions/load.mcfunction", "")

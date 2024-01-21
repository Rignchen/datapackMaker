from lib import getData, make_file, make_json

data = getData().getDatapackName().getMcVersion()
data.namespace = data.datapackName.lower().replace(" ","_")

make_json(
	f"{data.datapackName}/pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion,"description": f"{data.datapackName}"}}
)
make_json(
	f"{data.datapackName}/data/minecraft/tags/functions/load.json",
	{"values": [f"{data.namespace}:load"]}
)
make_json(
	f"{data.datapackName}/data/minecraft/tags/functions/tick.json",
	{"values": [f"{data.namespace}:tick"]}
)
make_file(f"{data.datapackName}/data/{data.namespace}/functions/tick.mcfunction", "")
make_file(f"{data.datapackName}/data/{data.namespace}/functions/load.mcfunction", "")

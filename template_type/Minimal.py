from lib import getData, make_file, make_json

data = getData().getDatapackName().getNamespace().getVersion().getAuthor()

make_json(
	f"{data.datapackName}/data/pack.mcmeta",
	{"pack":{"pack_format": data.version,"description": f"{data.datapackName} by {data.author}"}}
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

from lib.files import makeFile, makeJson, makeTree
from lib.i_o import getData

data = getData().getDatapackName().getNamespace().getMcVersion().getAuthor()

makeJson(
	f"{data.datapackName}/pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion,"description": f"{data.datapackName} by {data.author}"}}
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
makeFile(f"{data.datapackName}/data/{data.namespace}/functions/load.mcfunction", [f"say the {data.datapackName} Datapack successfully loaded!"])

for ns in ["minecraft",data.namespace]:
	makeTree({
		"advancements": {},
		"functions": {},
		"item_modifiers": {},
		"loot_tables": {},
		"predicates": {},
		"recipes": {},
		"structures": {},
		"chat_type": {},
		"damage_type": {},
		"tags": {
			"blocks": {},
			"entity_types": {},
			"fluids": {},
			"functions": {},
			"game_events": {},
			"items": {},
			"chat_type": {},
			"damage_type": {}
		},
		"dimension": {},
		"dimension_type": {},
		"worldgen": {
			"biome": {},
			"configured_carver": {},
			"configured_feature": {},
			"density_function": {},
			"noise": {},
			"noise_settings": {},
			"placed_feature": {},
			"processor_list": {},
			"structure": {},
			"structure_set": {},
			"template_pool": {},
			"world_preset": {},
			"flat_level_generator_preset": {}
		}
	},f"{data.datapackName}/data/{ns}")

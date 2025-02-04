from lib.files import addLicense, makeFile, makeJson, makeTree
from lib.i_o import getData

data = getData().getName().dpGetNamespace().dpGetMcVersion().getAuthor()

makeJson(
	f"{data.name}/pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion, "description": f"{data.name} by {data.author}"}}
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
makeFile(f"{data.name}/data/{data.namespace}/functions/load.mcfunction", [f"say the {data.name} Datapack successfully loaded!"])

addLicense()

for ns in ["minecraft", data.namespace]:
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
	},f"{data.name}/data/{ns}")

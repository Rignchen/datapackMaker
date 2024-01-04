from lib import getData, make_file, make_json, make_tree

data = getData().getDatapackName().getNamespace().getVersion().getAuthor()

make_json(
	f"{data.datapackName}/data/pack.mcmeta",
	{"pack":{"pack_format": data.version,"description": f"{data.datapackName} by {data.author}"}}
)
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
make_file(f"{data.datapackName}/data/{data.namespace}/functions/load.mcfunction", [f"say the {data.datapackName} Datapack successfully loaded!"])

for ns in ["minecraft",data.namespace]:
	make_tree({
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

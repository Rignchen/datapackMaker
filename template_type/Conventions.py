from lib import getData, make_json, make_tree

data = getData().getDatapackName().getNamespace().getVersion().getAuthor().getMcName()

make_tree({
	f"{data.datapackName}/data": {
		data.namespace: {
			"advancements": {},
			"functions": {
				"load.mcfunction": 'tellraw @a[tag=convention.debug] {"text": "' + data.datapackName + ' datapack loaded succesfully", "color": "green"}\n',
				"tick.mcfunction": "",
				"unload.mcfunction": 'tellraw @a[tag=convention.debug] {"text": "' + data.datapackName + ' datapack removed succesfully", "color": "green"}\n'
			},
			"item_modifiers": {},
			"loot_tables/i": {},
			"predicates": {},
			"recipes": {},
			"damage_type": {},
			"tags": {
				"blocks": {},
				"entity_types": {},
				"functions": {},
				"items": {}
			}
		},
		"load/functions/_private/init.mcfunction": [
			"# Reset scoreboards so packs can set values accurate for current load.",
			"scoreboard objectives add load.status dummy",
			"scoreboard players reset * load.status"
		]
	}
})

make_json( # pack.mcmeta
	f"{data.datapackName}/data/pack.mcmeta",
	{"pack":{"pack_format": data.version,"description": f"{data.datapackName} by {data.author}"}}
)
#global convention
make_json( # root.json
	f"{data.datapackName}/data/global/advancements/root.json",
	{"display": {"title": "Installed Datapacks","description": "","icon": {"item": "minecraft:knowledge_book"},"background": "minecraft:textures/block/gray_concrete.png","show_toast": False,"announce_to_chat": False},"criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
make_json( # author.json
	f"{data.datapackName}/data/global/advancements/{data.author.lower()}.json",
	{"display": {"title": data.author,"description": "","icon": {"item": "minecraft:player_head","nbt": "{SkullOwner:" + data.mcName + "}"},"show_toast": False,"announce_to_chat": False},"parent": "global:root","criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
make_json( # ns.json
	f"{data.datapackName}/data/{data.namespace}/advancements/{data.namespace}.json",
	{"display": {"icon": {"item": "minecraft:stone"},"title": data.datapackName,"description": "Minecraft DataPack","show_toast": False,"announce_to_chat": False},"parent": f"global:{data.author.lower()}","criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
#load convention
make_json( # pre load.json
	f"{data.datapackName}/data/load/tags/functions/pre_load.json",
	{"values": []}
)
make_json( # load.json
	f"{data.datapackName}/data/load/tags/functions/load.json",
	{"values": [f"{data.namespace}:load"]}
)
make_json( # post load.json
	f"{data.datapackName}/data/load/tags/functions/post_load.json",
	{"values": []}
)
make_json( # init.json
	f"{data.datapackName}/data/load/tags/functions/_private/init.json",
	{"values": ["load:_private/init"]}
)
make_json( # load.json
	f"{data.datapackName}/data/load/tags/functions/_private/load.json",
	{"values": ["#load:_private/init",{"id": "#load:pre_load", "required": False},{"id": "#load:load", "required": False},{"id": "#load:post_load", "required": False}]}
)
#minecraft
make_json( # load.json
	f"{data.datapackName}/data/minecraft/tags/functions/load.json",
	{"values": ["#load:_private/load"]}
)
make_json( # tick.json
	f"{data.datapackName}/data/minecraft/tags/functions/tick.json",
	{"values": [f"{data.namespace}:tick"]}
)

from lib.i_o import getData
from lib.files import makeJson, makeTree

data = getData().getName().dpGetNamespace().dpGetMcVersion().getAuthor().dpGetMcName()

makeTree({
	f"{data.name}/data": {
		data.namespace: {
			"advancements": {},
			"functions": {
				"load.mcfunction": 'tellraw @a[tag=convention.debug] {"text": "' + data.name + ' datapack loaded succesfully", "color": "green"}\n',
				"tick.mcfunction": "",
				"unload.mcfunction": 'tellraw @a[tag=convention.debug] {"text": "' + data.name + ' datapack removed succesfully", "color": "green"}\n'
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

makeJson(  # pack.mcmeta
	f"{data.name}/pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion, "description": f"{data.name} by {data.author}"}}
)
# global convention
makeJson(  # root.json
	f"{data.name}/data/global/advancements/root.json",
	{"display": {"title": "Installed Datapacks","description": "","icon": {"item": "minecraft:knowledge_book"},"background": "minecraft:textures/block/gray_concrete.png","show_toast": False,"announce_to_chat": False},"criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
makeJson(  # author.json
	f"{data.name}/data/global/advancements/{data.author.lower()}.json",
	{"display": {"title": data.author,"description": "","icon": {"item": "minecraft:player_head","nbt": "{SkullOwner:" + data.mcName + "}"},"show_toast": False,"announce_to_chat": False},"parent": "global:root","criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
makeJson(  # ns.json
	f"{data.name}/data/{data.namespace}/advancements/{data.namespace}.json",
	{"display": {"icon": {"item": "minecraft:stone"}, "title": data.name, "description": "Minecraft DataPack", "show_toast": False, "announce_to_chat": False}, "parent": f"global:{data.author.lower()}", "criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
# load convention
makeJson(  # pre load.json
	f"{data.name}/data/load/tags/functions/pre_load.json",
	{"values": []}
)
makeJson(  # load.json
	f"{data.name}/data/load/tags/functions/load.json",
	{"values": [f"{data.namespace}:load"]}
)
makeJson(  # post load.json
	f"{data.name}/data/load/tags/functions/post_load.json",
	{"values": []}
)
makeJson(  # init.json
	f"{data.name}/data/load/tags/functions/_private/init.json",
	{"values": ["load:_private/init"]}
)
makeJson(  # load.json
	f"{data.name}/data/load/tags/functions/_private/load.json",
	{"values": ["#load:_private/init",{"id": "#load:pre_load", "required": False},{"id": "#load:load", "required": False},{"id": "#load:post_load", "required": False}]}
)
# minecraft
makeJson(  # load.json
	f"{data.name}/data/minecraft/tags/functions/load.json",
	{"values": ["#load:_private/load"]}
)
makeJson(  # tick.json
	f"{data.name}/data/minecraft/tags/functions/tick.json",
	{"values": [f"{data.namespace}:tick"]}
)

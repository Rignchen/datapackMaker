from lib.files import addLicense, makeJson, makeTree
from lib.i_o import getData
from os import chdir, system

data = getData().getDatapackName().getNamespace().getMcVersion()
data.author = "Rignchen"
data.mcName = "Rignchen"

makeTree({
	data.datapackName: {
		"data": {
			data.namespace: {
				"advancements": {
					"action": {},
					"display": {}
				},
				"functions": {
					"items.mcfunction": [
						f"## function #{data.namespace}:load",
						"",
						'data modify storage %s:items data. set value {id:"minecraft:",Slot:16b,Count:1b,tag:{ctc: {from: "%s:%s", id: "", traits: {}},display: {Name: \'{"text": "", "italic": false}\', Lore: [\'{"text": "%s", "color": "blue"}\']}}}' % (data.namespace, data.author, data.namespace, data.namespace),
						""
					],
					"load.mcfunction": [
						"## function #load:load",
						"",
						"#load custom items",
						f"function {data.namespace}:items",
						"",
						"#scoreboard",
						f"scoreboard objectives add {data.namespace}.data dummy",
						"",
						"#define",
						"#define entity @a[tag=convention.debug]",
						"#define score_holder #temp",
						f"#define storage {data.namespace}:items",
						""
					],
					"tick.mcfunction": "## function #tick\n",
					"unload.mcfunction": [
						"## call by the player",
						"",
						"#storages",
						f"data remove storage {data.namespace}:items data",
						"",
						"#scoreboard",
						f"scoreboard objectives remove {data.namespace}.data",
						"",
						"#disable the pack",
						f"datapack disable \"file/{data.datapackName}\"",
						f"datapack disable \"file/{data.datapackName}.zip\"",
						""
					]
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
		},
		".gitignore": ".vscode\n",
		"zip_pack.bat": [
			"@echo off",
			'zip -i "pack.mcmeta", "data", "LICENSE", "README.md" -e "__pycache__"',
			"exit /b"
		]
	}
})

chdir(data.datapackName)
system("git init")

makeJson( # .vscode/settings.json
	".vscode/settings.json",
	{"files.exclude": {"data/global":True, "data/minecraft":True, "data/load/functions": True, "data/load/tags/functions/_private": True, "LICENSE":True, "pack.mcmeta": True}}
)
makeJson( # pack.mcmeta
	"pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion,"description": f"{data.datapackName} by {data.author}"}}
)
#global convention
makeJson( # root.json
	"data/global/advancements/root.json",
	{"display": {"title": "Installed Datapacks","description": "","icon": {"item": "minecraft:knowledge_book"},"background": "minecraft:textures/block/gray_concrete.png","show_toast": False,"announce_to_chat": False},"criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
makeJson( # author.json
	f"data/global/advancements/{data.author.lower()}.json",
	{"display": {"title": data.author,"description": "","icon": {"item": "minecraft:player_head","nbt": "{SkullOwner:" + data.mcName + "}"},"show_toast": False,"announce_to_chat": False},"parent": "global:root","criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
makeJson( # ns.json
	f"data/{data.namespace}/advancements/{data.namespace}.json",
	{"display": {"icon": {"item": "minecraft:stone"},"title": data.datapackName,"description": "Minecraft DataPack","show_toast": False,"announce_to_chat": False},"parent": f"global:{data.author.lower()}","criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
#load convention
makeJson( # load.json
	f"data/load/tags/functions/load.json",
	{"values": [f"{data.namespace}:load"]}
)
makeJson( # init.json
	f"data/load/tags/functions/_private/init.json",
	{"values": ["load:_private/init"]}
)
makeJson( # load.json
	f"data/load/tags/functions/_private/load.json",
	{"values": ["#load:_private/init",{"id": "#load:pre_load", "required": False},{"id": "#load:load", "required": False},{"id": "#load:post_load", "required": False}]}
)
#minecraft
makeJson( # load.json
	f"data/minecraft/tags/functions/load.json",
	{"values": ["#load:_private/load"]}
)
makeJson( # tick.json
	f"data/minecraft/tags/functions/tick.json",
	{"values": [f"{data.namespace}:tick"]}
)
#ns
makeJson( # loot table/i.json
	f"data/{data.namespace}/loot_tables/i/.json",
	{"pools": [{"rolls": 1,"entries": [{"type": "item","name": "","functions": [{"function": "copy_nbt","ops": [{"op": "merge","source": "data..tag","target": "{}"}],"source": {"type": "storage","source": f"{data.namespace}:items"}}]}]}]}
)

addLicense("Creative Commons Zero v1.0 Universal")

#commit
system("git add .")
system("git commit -m \"Create new datapack\"")

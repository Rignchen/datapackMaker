from lib.files import addLicense, makeFile, makeJson, makeTree
from lib.i_o import getData
from os import chdir, name, system

data = getData().getName().dpGetNamespace().dpGetMcVersion()
data.author = "Rignchen"
data.mcName = "Rignchen"

makeTree({
	data.name: {
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
						f"datapack disable \"file/{data.name}\"",
						f"datapack disable \"file/{data.name}.zip\"",
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
		".gitignore": ".vscode\n"
	},
	"README.md": f"# {data.name}\n\n## Installation\n1. Download the datapack\n2. Place the datapack in the `datapacks` folder of your world\n3. Run `/reload` or restart your world\n4. Enjoy!\n\n## Uninstallation\n1. Run `/function {data.namespace}:unload`\n2. Remove the datapack from the `datapacks` folder of your world\n\n## Usage\n"
})

chdir(data.name)
system("git init")

# zip script
if name == "nt":  # windows
	makeFile(
		"zip_pack.bat",
		[
			"@echo off",
			'zip -i "pack.mcmeta", "data\\", "LICENSE.md", "README.md" -e "__pycache__"',
			"exit /b"
		]
	)
else:  # linux
	makeFile(
		"zip_pack.bs",
		'zip -i "pack.mcmeta", "data/", "LICENSE.md", "README.md" -e "__pycache__"'
	)

makeJson(  # .vscode/settings.json
	".vscode/settings.json",
	{"files.exclude": {"data/global":True, "data/minecraft":True, "data/load/functions": True, "data/load/tags/functions/_private": True, "LICENSE.md":True, "pack.mcmeta": True, "zip_pack.*": True}}
)
makeJson(  # pack.mcmeta
	"pack.mcmeta",
	{"pack":{"pack_format": data.mcVersion,"description": f"{data.name} by {data.author}"}}
)
# global convention
makeJson(  # root.json
	"data/global/advancements/root.json",
	{"display": {"title": "Installed Datapacks","description": "","icon": {"item": "minecraft:knowledge_book"},"background": "minecraft:textures/block/gray_concrete.png","show_toast": False,"announce_to_chat": False},"criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
makeJson(  # author.json
	f"data/global/advancements/{data.author.lower()}.json",
	{"display": {"title": data.author,"description": "","icon": {"item": "minecraft:player_head","nbt": "{SkullOwner:" + data.mcName + "}"},"show_toast": False,"announce_to_chat": False},"parent": "global:root","criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
makeJson(  # ns.json
	f"data/{data.namespace}/advancements/{data.namespace}.json",
	{"display": {"icon": {"item": "minecraft:stone"}, "title": data.name, "description": "Minecraft DataPack", "show_toast": False, "announce_to_chat": False}, "parent": f"global:{data.author.lower()}", "criteria": {"trigger": {"trigger": "minecraft:tick"}}}
)
# load convention
makeJson(  # load.json
	f"data/load/tags/functions/load.json",
	{"values": [f"{data.namespace}:load"]}
)
makeJson(  # init.json
	f"data/load/tags/functions/_private/init.json",
	{"values": ["load:_private/init"]}
)
makeJson(  # load.json
	f"data/load/tags/functions/_private/load.json",
	{"values": ["#load:_private/init",{"id": "#load:pre_load", "required": False},{"id": "#load:load", "required": False},{"id": "#load:post_load", "required": False}]}
)
# minecraft
makeJson(  # load.json
	f"data/minecraft/tags/functions/load.json",
	{"values": ["#load:_private/load"]}
)
makeJson(  # tick.json
	f"data/minecraft/tags/functions/tick.json",
	{"values": [{"id": f"{data.namespace}:tick", "required": False}]}
)
# ns
makeJson(  # loot table/i.json
	f"data/{data.namespace}/loot_tables/i/.json",
	{"pools": [{"rolls": 1,"entries": [{"type": "item","name": "","functions": [{"function": "copy_nbt","ops": [{"op": "merge","source": "data..tag","target": "{}"}],"source": {"type": "storage","source": f"{data.namespace}:items"}}]}]}]}
)

addLicense("""# Attribution-NonCommercial-ShareAlike 4.0 International
By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.

## Section 1 – Definitions.
1. <ins>Adapted Material</ins> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.
2. <ins>Adapter's License</ins> means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.
3. <ins>BY-NC-SA Compatible License</ins> means a license listed at [creativecommons.org/compatiblelicenses](https://creativecommons.org/compatiblelicenses) , approved by Creative Commons as essentially the equivalent of this Public License.
4. <ins>Copyright and Similar Rights</ins> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section [2(b)(1)-(2)](#section-2--scope) are not Copyright and Similar Rights.
5. <ins>Effective Technological Measures</ins> means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.
6. <ins>Exceptions and Limitations</ins> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.
7. <ins>License Elements</ins> means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution, NonCommercial, and ShareAlike.
8. <ins>Licensed Material</ins> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.
9. <ins>Licensed Rights</ins> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.
10. <ins>Licensor</ins> means the individual(s) or entity(ies) granting rights under this Public License.
11. <ins>NonCommercial</ins> means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.
11. <ins>Share</ins> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.
12. <ins>Sui Generis Database Rights</ins> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.
13. <ins>You</ins> means the individual or entity exercising the Licensed Rights under this Public License. **Your** has a corresponding meaning.
## Section 2 – Scope.
1. **License grant .**
	1. Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:
		1. reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
		2. produce, reproduce, and Share Adapted Material for NonCommercial purposes only.
	2. **Exceptions and Limitations** . For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.
	3. **Term** . The term of this Public License is specified in Section [6(a)](#section-6--term-and-termination) .
	4. **Media and formats; technical modifications allowed** . The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section [2(a)(4)](#section-2--scope) never produces Adapted Material.
	5. Downstream recipients .
		1. Offer from the Licensor – Licensed Material . Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.
		2. Additional offer from the Licensor – Adapted Material . Every recipient of Adapted Material from You automatically receives an offer from the Licensor to exercise the Licensed Rights in the Adapted Material under the conditions of the Adapter’s License You apply.
		3. No downstream restrictions . You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.
	6. No endorsement . Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section [3(a)(1)(A)(i)](#section-3--license-conditions) .
2. Other rights .
	1. Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.
	2. Patent and trademark rights are not licensed under this Public License.
	3. To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.
## Section 3 – License Conditions.
Your exercise of the Licensed Rights is expressly made subject to the following conditions.

1. **Attribution** .
	1. If You Share the Licensed Material (including in modified form), You must:
		1. retain the following if it is supplied by the Licensor with the Licensed Material:
			1. identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);
			2. a copyright notice;
			3. a notice that refers to this Public License;
			4. a notice that refers to the disclaimer of warranties;
			5. a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
		2. indicate if You modified the Licensed Material and retain an indication of any previous modifications; and
		3. indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.
	2. You may satisfy the conditions in Section [3(a)(1)](#section-3--license-conditions) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.
	3. If requested by the Licensor, You must remove any of the information required by Section [3(a)(1)(A)](#section-3--license-conditions) to the extent reasonably practicable.
2. ShareAlike .<br><br>
In addition to the conditions in Section 3(a) , if You Share Adapted Material You produce, the following conditions also apply.

	1. The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.
	2. You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.
	3. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.
## Section 4 – Sui Generis Database Rights.
Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:

1. for the avoidance of doubt, Section [2(a)(1)](#section-2--scope) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only;
2. if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material, including for purposes of Section [3(b)](#section-3--license-conditions) ; and
3. You must comply with the conditions in Section [3(a)](#section-3--license-conditions) if You Share all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.

## **Section 5 – Disclaimer of Warranties and Limitation of Liability.**
1. **Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.**
2. **To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.**
3. The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.
## Section 6 – Term and Termination.
1. This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.
2. Where Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:

	1. automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or
	2. upon express reinstatement by the Licensor.

For the avoidance of doubt, this Section [6(b)](#section-6--term-and-termination) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.

3. For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.
4. Sections [1](#section-1--definitions) , [5](#section-5--disclaimer-of-warranties-and-limitation-of-liability) , [6](#section-6--term-and-termination) , [7](#section-7--other-terms-and-conditions) , and [8](#section-8--interpretation) survive termination of this Public License.
## Section 7 – Other Terms and Conditions.
1. The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.
2. Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.
## Section 8 – Interpretation.
1. For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.
2. To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.
3. No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.
4. Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.""")

# commit
system("git add .")
system("git commit -m \"Create new datapack\"")

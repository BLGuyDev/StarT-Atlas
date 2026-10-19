import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
from PIL import Image
import icons_model as im_

ids = sys.argv[1:] or ['gtceu:stone_barrel', 'gtceu:barrel', 'minecraft:furnace', 'minecraft:grass_block', 'exnihilosequentia:oak_sieve',
       'create:mechanical_press', 'create:crushing_wheel', 'create:windmill_bearing', 'create:mechanical_mixer', 'thermal:dynamo_stirling',
       'thermal:device_water_gen', 'gtceu:lv_assembler', 'gtceu:electric_blast_furnace', 'create_new_age:generator_coil',
       'create_new_age:carbon_brushes', 'gtceu:mechanical_sieve', 'gtceu:coke_oven', 'gtceu:steel_plate', 'minecraft:hopper',
       'functionalstorage:oak_1', 'create:shaft', 'create:smart_chute', 'gtceu:lv_super_chest', 'exnihilosequentia:oak_crucible',
       'gtceu:cupronickel_coil_block', 'minecraft:campfire', 'create:basin', 'createlowheated:basic_burner', 'gtceu:large_barrel', 'minecraft:chest']
s = Image.new('RGBA', (64 * 10, 64 * 3), (60, 64, 68, 255))
miss = []
for i, x in enumerate(ids):
    im = im_.icon64(x)
    if im is None:
        miss.append(x)
        continue
    s.alpha_composite(im, ((i % 10) * 64, (i // 10) * 64))
s.save('../test/icons64.png')
print('miss', miss)

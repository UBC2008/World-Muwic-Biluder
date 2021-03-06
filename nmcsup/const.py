# 音符:[MC音调, 声音频率, 方块名称, 数据值]
notes = {
    '....A' : [0.074, 27.5, 'wood', 8],
    '....A#' : [0.0787, 29.135, 'wood', 9],
    '....B' : [0.083, 30.868, 'wood', 10],
    '...C' : [0.088, 32.703, 'wood', 11],
    '...C#' : [0.094, 34.648, 'wood', 12],
    '...D' : [0.1, 36.708, 'wood', 13],
    '...D#' : [0.105, 38.891, 'log', 0],
    '...E' : [0.11, 41.203, 'log', 1],
    '...F' : [0.12, 43.654, 'log', 2],
    '...F#' : [0.125, 46.249, 'wood', 0],
    '...G' : [0.13, 48.999, 'wood', 1],
    '...G#' : [0.14, 51.913, 'wood', 2],
    '...A' : [0.15, 55.0, 'wood', 3],
    '...A#' : [0.16, 58.27, 'wood', 4],
    '...B' : [0.17, 61.735, 'wood', 5],
    '..C' : [0.18, 65.406, 'wool', 0],
    '..C#' : [0.19, 69.296, 'wool', 1],
    '..D' : [0.2, 73.416, 'wool', 2],
    '..D#' : [0.21, 77.782, 'wool', 3],
    '..E' : [0.22, 82.407, 'wool', 4],
    '..F' : [0.235, 87.307, 'wool', 5],
    '..F#' : [0.25, 92.499, 'concretepowder', 0],
    '..G' : [0.26, 97.999, 'concretepowder', 1],
    '..G#' : [0.28, 103.826, 'concretepowder', 2],
    '..A' : [0.3, 110.0, 'concretepowder', 3],
    '..A#' : [0.31, 116.541, 'concretepowder', 4],
    '..B' : [0.33, 123.471, 'concretepowder', 5],
    '.C' : [0.35, 130.813, 'concretepowder', 6],
    '.C#' : [0.37, 138.591, 'concretepowder', 7],
    '.D' : [0.4, 146.832, 'concretepowder', 8],
    '.D#' : [0.42, 155.563, 'concretepowder', 9],
    '.E' : [0.44, 164.814, 'concretepowder', 10],
    '.F' : [0.47, 174.614, 'concretepowder', 11],
    '.F#' : [0.5, 184.997, 'concretepowder', 12],
    '.G' : [0.53, 195.998, 'concretepowder', 13],
    '.G#' : [0.56, 207.652, 'concretepowder', 14],
    '.A' : [0.6, 220.0, 'concretepowder', 15],
    '.A#' : [0.63, 233.082, 'concrete', 0],
    '.B' : [0.67, 246.942, 'concrete', 1],
    'C' : [0.7, 261.626, 'concrete', 2],
    'C#' : [0.75, 277.183, 'concrete', 3],
    'D' : [0.8, 293.665, 'concrete', 4],
    'D#' : [0.84, 311.127, 'concrete', 5],
    'E' : [0.9, 329.628, 'concrete', 6],
    'F' : [0.94, 349.228, 'concrete', 7],
    'F#' : [1.0, 369.994, 'concrete', 8],
    'G' : [1.05, 391.995, 'concrete', 9],
    'G#' : [1.12, 415.305, 'concrete', 10],
    'A' : [1.2, 440.0, 'concrete', 11],
    'A#' : [1.25, 466.164, 'concrete', 12],
    'B' : [1.33, 493.883, 'concrete', 13],
    '`C' : [1.4, 523.251, 'concrete', 14],
    '`C#' : [1.5, 554.365, 'concrete', 15],
    '`D' : [1.6, 587.33, 'stained_hardened_clay', 0],
    '`D#' : [1.7, 622.254, 'stained_hardened_clay', 1],
    '`E' : [1.8, 659.255, 'stained_hardened_clay', 2],
    '`F' : [1.9, 698.456, 'stained_hardened_clay', 3],
    '`F#' : [2.0, 739.989, 'stained_hardened_clay', 4],
    '`G' : [2.1, 783.991, 'stained_hardened_clay', 5],
    '`G#' : [2.24, 830.609, 'stained_hardened_clay', 6],
    '`A' : [2.4, 880.0, 'stained_hardened_clay', 7],
    '`A#' : [2.5, 932.328, 'stained_hardened_clay', 8],
    '`B' : [2.67, 987.767, 'stained_hardened_clay', 9],
    '``C' : [2.83, 1046.502, 'stained_hardened_clay', 10],
    '``C#' : [3.0, 1108.731, 'stained_hardened_clay', 11],
    '``D' : [3.17, 1174.659, 'stained_hardened_clay', 12],
    '``D#' : [3.36, 1244.508, 'stained_hardened_clay', 13],
    '``E' : [3.56, 1318.51, 'stained_hardened_clay', 14],
    '``F' : [3.78, 1396.913, 'stained_hardened_clay', 15],
    '``F#' : [4.0, 1479.978, 'white_glazed_terracotta', 0],
    '``G' : [4.24, 1567.982, 'orange_glazed_terracotta', 0],
    '``G#' : [4.5, 1661.219, 'magenta_glazed_terracotta', 0],
    '``A' : [4.76, 1760.0, 'light_blue_glazed_terracotta', 0],
    '``A#' : [5.04, 1864.655, 'yellow_glazed_terracotta', 0],
    '``B' : [5.34, 1975.533, 'lime_glazed_terracotta', 0],
    '```C' : [5.66, 2093.005, 'pink_glazed_terracotta', 0],
    '```C#' : [6.0, 2217.461, 'gray_glazed_terracotta', 0],
    '```D' : [6.35, 2349.318, 'silver_glazed_terracotta', 0],
    '```D#' : [6.73, 2489.016, 'cyan_glazed_terracotta', 0],
    '```E' : [7.13, 2637.02, 'purple_glazed_terracotta', 0],
    '```F' : [7.55, 2793.826, 'blue_glazed_terracotta', 0],
    '```F#' : [8.0, 2959.955, 'brown_glazed_terracotta', 0],
    '```G' : [8.47, 3135.963, 'green_glazed_terracotta', 0],
    '```G#' : [8.98, 3322.438, 'red_glazed_terracotta', 0],
    '```A' : [9.51, 3520.0, 'black_glazed_terracotta', 0],
    '```A#' : [10.08, 3729.31, 'stained_glass', 0],
    '```B' : [10.68, 3951.066, 'stained_glass', 1],
    '````C' : [11.31, 4186.009, 'stained_glass', 2],
    '0' : [0.0, 0.0, 'glass', 0]
}

#方块
'''
blocks = {
    0.074 : ['stained_glass', 3],
    0.0787 : ['stained_glass', 4],
    0.083 : ['stained_glass', 5],
    0.088 : ['stained_glass', 6],
    0.094 : ['stained_glass', 7],
    0.1 : ['stained_glass', 8],
    0.105 : ['stained_glass', 9],
    0.11 : ['stained_glass', 10],
    0.12 : ['stained_glass', 11],
    0.125 : ['stained_glass', 12],
    0.13 : ['stained_glass', 13],
    0.14 : ['stained_glass', 14],
    0.15 : ['stained_glass', 15],
    0.16 : ['wool', 0],
    0.17 : ['wool', 1],
    0.18 : ['wool', 2],
    0.19 : ['wool', 3],
    0.2 : ['wool', 4],
    0.21 : ['wool', 5],
    0.22 : ['wool', 6],
    0.235 : ['wool', 7],
    0.25 : ['concretepowder', 0],
    0.26 : ['concretepowder', 1],
    0.28 : ['concretepowder', 2],
    0.3 : ['concretepowder', 3],
    0.31 : ['concretepowder', 4],
    0.33 : ['concretepowder', 5],
    0.35 : ['concretepowder', 6],
    0.37 : ['concretepowder', 7],
    0.4 : ['concretepowder', 8],
    0.42 : ['concretepowder', 9],
    0.44 : ['concretepowder', 10],
    0.47 : ['concretepowder', 11],
    0.5 : ['concretepowder', 12],
    0.53 : ['concretepowder', 13],
    0.56 : ['concretepowder', 14],
    0.6 : ['concretepowder', 15],
    0.63 : ['concrete', 0],
    0.67 : ['concrete', 1],
    0.7 : ['concrete', 2],
    0.75 : ['concrete', 3],
    0.8 : ['concrete', 4],
    0.84 : ['concrete', 5],
    0.9 : ['concrete', 6],
    0.94 : ['concrete', 7],
    1.0 : ['concrete', 8],
    1.05 : ['concrete', 9],
    1.12 : ['concrete', 10],
    1.2 : ['concrete', 11],
    1.25 : ['concrete', 12],
    1.33 : ['concrete', 13],
    1.4 : ['concrete', 14],
    1.5 : ['concrete', 15],
    1.6 : ['stained_hardened_clay', 0],
    1.7 : ['stained_hardened_clay', 1],
    1.8 : ['stained_hardened_clay', 2],
    1.9 : ['stained_hardened_clay', 3],
    2.0 : ['stained_hardened_clay', 4],
    2.1 : ['stained_hardened_clay', 5],
    2.24 : ['stained_hardened_clay', 6],
    2.4 : ['stained_hardened_clay', 7],
    2.5 : ['stained_hardened_clay', 8],
    2.67 : ['stained_hardened_clay', 9],
    2.83 : ['stained_hardened_clay', 10],
    3.0 : ['stained_hardened_clay', 11],
    3.17 : ['stained_hardened_clay', 12],
    3.36 : ['stained_hardened_clay', 13],
    3.56 : ['stained_hardened_clay', 14],
    3.78 : ['stained_hardened_clay', 15],
    4.0 : ['stained_glass_pane', 0],
    4.24 : ['stained_glass_pane', 1],
    4.5 : ['stained_glass_pane', 2],
    4.76 : ['stained_glass_pane', 3],
    5.04 : ['stained_glass_pane', 4],
    5.34 : ['stained_glass_pane', 5],
    5.66 : ['stained_glass_pane', 6],
    6.0 : ['stained_glass_pane', 7],
    6.35 : ['stained_glass_pane', 8],
    6.73 : ['stained_glass_pane', 9],
    7.13 : ['stained_glass_pane', 10],
    7.55 : ['stained_glass_pane', 11],
    8.0 : ['stained_glass_pane', 12],
    8.47 : ['stained_glass_pane', 13],
    8.98 : ['stained_glass_pane', 14],
    9.51 : ['stained_glass_pane', 15],
    10.08 : ['stained_glass', 0],
    10.68 : ['stained_glass', 1],
    11.31 : ['stained_glass', 2],
    0.0 : ['glass', 0]
}
'''
Blocks = {
    0.074: 'barrel', 
    0.0787: 'beacon', 
    0.083: 'bedrock', 
    0.088: 'black_glazed_terracotta', 
    0.094: 'blast_furnace', 
    0.1: 'blue_glazed_terracotta', 
    0.105: 'blue_ice', 
    0.11: 'bone_block', 
    0.12: 'bookshelf', 
    0.125: 'brick_block', 
    0.13: 'brown_glazed_terracotta', 
    0.14: 'cartography_table', 
    0.15: 'carved_pumpkin', 
    0.16: 'clay', 
    0.17: 'coal_block', 
    0.18: 'coal_ore', 
    0.19: 'cobblestone', 
    0.2: 'concrete', 
    0.21: 'crafting_table', 
    0.22: 'cyan_glazed_terracotta', 
    0.235: 'diamond_block', 
    0.25: 'diamond_ore', 
    0.26: 'white_glazed_terracotta', 
    0.28: 'dispenser', 
    0.3: 'dried_kelp_block', 
    0.31: 'dropper', 
    0.33: 'emerald_block', 
    0.35: 'emerald_ore', 
    0.37: 'end_bricks', 
    0.4: 'end_stone', 
    0.42: 'fletching_table', 
    0.44: 'furnace', 
    0.47: 'glass', 
    0.5: 'glowingobsidian', 
    0.53: 'glowstone', 
    0.56: 'gold_block', 
    0.6: 'gold_ore', 
    0.63: 'grass', 
    0.67: 'gray_glazed_terracotta', 
    0.7: 'green_glazed_terracotta', 
    0.75: 'hardened_clay', 
    0.8: 'hay_block', 
    0.84: 'iron_block', 
    0.9: 'iron_ore', 
    0.94: 'jukebox', 
    1.0: 'lapis_block', 
    1.05: 'lapis_ore', 
    1.12: 'light_blue_glazed_terracotta', 
    1.2: 'lime_glazed_terracotta', 
    1.25: 'lit_pumpkin', 
    1.33: 'log', 
    1.4: 'loom', 
    1.5: 'magenta_glazed_terracotta', 
    1.6: 'magma', 
    1.7: 'melon_block', 
    1.8: 'web', 
    1.9: 'mossy_cobblestone', 
    2.0: 'nether_brick', 
    2.1: 'nether_wart_block', 
    2.24: 'netherrack', 
    2.4: 'noteblock', 
    2.5: 'observer', 
    2.67: 'obsidian', 
    2.83: 'orange_glazed_terracotta', 
    3.0: 'pink_glazed_terracotta', 
    3.17: 'piston', 
    3.36: 'planks', 
    3.56: 'prismarine', 
    3.78: 'pumpkin', 
    4.0: 'purple_glazed_terracotta', 
    4.24: 'purpur_block', 
    4.5: 'quartz_block', 
    4.76: 'quartz_ore', 
    5.04: 'red_glazed_terracotta', 
    5.34: 'red_nether_brick', 
    5.66: 'red_sandstone', 
    6.0: 'redstone_block', 
    6.35: 'yellow_glazed_terracotta', 
    6.73: 'sandstone', 
    7.13: 'stonebrick', 
    7.55: 'silver_glazed_terracotta', 
    8.0: 'slime', 
    8.47: 'smithing_table', 
    8.98: 'smoker', 
    9.51: 'smooth_stone', 
    10.08: 'snow', 
    10.68: 'soul_sand', 
    11.31: 'sponge', 
    0.0: 'stone'
}


# 乐器
Instuments = {
    'banjo' : '班卓',
    'bass' : '低音',
    'bassattack' : '贝斯',
    'bd' : '鼓声',
    'bell' : '铃声',
    'bit' : '比特',
    'cow_bell' : '牛铃',
    'didgeridoo' : '迪吉',
    'flute' : '长笛',
    'guitar' : '吉他',
    'harp' : '竖琴',
    'hat' : '架鼓',
    'chime' : '钟声',
    'iron_xylophone' : '铁琴',
    'pling' : '叮叮',
    'snare' : '响弦',
    'xylophone' : '木琴'
}
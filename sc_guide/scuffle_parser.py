from collections import defaultdict
from sc_guide.constants import AttackTypes

def parse_scuffle_move(scuffle_string):
    split_string = [s.strip() for s in scuffle_string.split("|")]

    # scuffle prints blank for counter hit frames when they equal natural hit frames
    # so just copy natural hit frames in that case
    hit_frames = split_string[5]
    counter_frames = split_string[6]
    if counter_frames == '':
        counter_frames = hit_frames
    
    # assign properties to natural / counter hits if they exist
    property_list = ["LNC", "KND", "STN"]
    hit_property = None
    counter_property = None
    for move_property in property_list:
        if move_property in hit_frames:
            hit_property = move_property
        if move_property in counter_frames:
            counter_property = move_property
    
    # if property is set, then null out number of frames
    if hit_property is None:
        try:
            hit_frames = int(hit_frames)
        except ValueError:
            hit_frames = None
    else:
        hit_frames = None

    if counter_property is None:
        try:
            counter_frames = int(counter_frames)
        except ValueError:
            counter_frames = None
    else:
        counter_frames = None

    # determine move's attack type
    attack_types = []
    attack_type_string = split_string[3]
    for attack_type in attack_type_string.split(","):
        if "low" in attack_type and not "slow" in attack_type:
            attack_types.append(AttackTypes.low.value)
        elif "mid" in attack_type and not "smid" in attack_type:
            attack_types.append(AttackTypes.middle.value)
        elif "high" in attack_type:
            attack_types.append(AttackTypes.high.value)
        elif "sl" in attack_type or "slow" in attack_type:
            attack_types.append(AttackTypes.special_low.value)
        elif "sm" in attack_type or "smid" in attack_type:
            attack_types.append(AttackTypes.special_middle.value)

    damage_nums = split_string[7].split(",")

    try:
        impact_frames = int(split_string[2])
    except ValueError:
        impact_frames = None

    try:
        block_frames = int(split_string[4])
    except ValueError:
        block_frames = None

    return {
        "command": split_string[1],
        "attackTypes": attack_types,
        "impactFrames": impact_frames,
        "blockFrames": block_frames,
        "hitFrames": hit_frames,
        "hitProperty": hit_property,
        "counterFrames": counter_frames,
        "counterProperty": counter_property,
        "damage": damage_nums,
        "gapFramge": []
    }

def parse_scuffle_category(scuffle_string):
    start_index = scuffle_string.find('[') + 1
    end_index = scuffle_string.find(']')

    return scuffle_string[start_index:end_index]

def parse_scuffle_output(path):
    results = []
    category_name = None
    with open(path, "r") as f:
        for line in f.read().split("\n"):
            stripped_line = line.strip()

            if stripped_line == "":
                continue
            elif stripped_line.startswith("["):
                category_name = parse_scuffle_category(stripped_line)
            else:
                move = parse_scuffle_move(stripped_line)
                move["category"] = category_name
                results.append(move)
    
    return results

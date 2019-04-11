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
        hit_frames = int(hit_frames)
    else:
        hit_frames = None

    if counter_property is None:
        counter_frames = int(counter_frames)
    else:
        counter_frames = None

    # determine move's attack type
    attack_type = None
    attack_type_string = split_string[3]
    if "low" in attack_type_string and not "slow" in attack_type_string:
        attack_type = AttackTypes.low
    elif "mid" in attack_type_string and not "smid" in attack_type_string:
        attack_type = AttackTypes.middle
    elif "high" in attack_type_string:
        attack_type = AttackTypes.high
    elif "sl" in attack_type_string or "slow" in attack_type_string:
        attack_type = AttackTypes.special_low
    elif "sm" in attack_type_string or "smid" in attack_type_string:
        attack_type = AttackTypes.special_middle

    return {
        "command": split_string[1],
        "attackType": attack_type,
        "impactFrames": split_string[2],
        "blockFrames": split_string[4],
        "hitFrames": hit_frames,
        "hitProperty": hit_property,
        "counterFrames": counter_frames,
        "counterProperty": counter_property,
        "damage": split_string[7],
    }

def parse_scuffle_category(scuffle_string):
    start_index = scuffle_string.find('[') + 1
    end_index = scuffle_string.find(']')

    return scuffle_string[start_index:end_index]

def parse_scuffle_output(path):
    results = defaultdict(list)
    category_name = "Undefined"
    with open(path, "r") as f:
        for line in f.read().split("\n"):
            stripped_line = line.strip()

            if stripped_line == "":
                continue
            elif stripped_line.startswith("["):
                category_name = parse_scuffle_category(stripped_line)
            else:
                results[category_name].append(parse_scuffle_move(stripped_line))
    
    return results

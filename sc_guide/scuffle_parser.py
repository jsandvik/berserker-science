from collections import defaultdict

def parse_scuffle_move(scuffle_string):
    split_string = [s.strip() for s in scuffle_string.split("|")]

    # scuffle prints blank for counter hit frames when they equal natural hit frames
    # so just copy natural hit frames in that case
    hit_frames = split_string[5]
    counter_frames = split_string[6]
    if counter_frames == '':
        counter_frames = hit_frames
    
    # remove possible non-numbers from frame data
    # add these in elsewhere as properties later
    hit_frames = hit_frames.replace("LNC", "")
    counter_frames = counter_frames.replace("LNC", "")
    hit_frames = hit_frames.replace("KND", "")
    counter_frames = counter_frames.replace("KND", "")
    hit_frames = hit_frames.replace("STN", "")
    counter_frames = counter_frames.replace("STN", "")

    return {
        "command": split_string[1],
        "impactFrames": split_string[2],
        "blockFrames": split_string[4],
        "hitFrames": hit_frames,
        "counterFrames": counter_frames,
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

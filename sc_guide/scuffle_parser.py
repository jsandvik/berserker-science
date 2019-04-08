def parse_scuffle_string(scuffle_string):
    print(scuffle_string)
    split_string = [s.strip() for s in scuffle_string.split("|")]

    # scuffle prints blank for counter hit frames when they equal natural hit frames
    # so just copy natural hit frames in that case
    hit_frames = split_string[5]
    counter_frames = split_string[6]
    if counter_frames == '':
        counter_frames = hit_frames

    return {
        "command": split_string[1],
        "impactFrames": split_string[2],
        "blockFrames": split_string[4],
        "hitFrames": hit_frames,
        "counterFrames": counter_frames,
        "damage": split_string[7],
    }

def parse_scuffle_output(path):
    results = []
    with open(path, "r") as f:
        for line in f.read().split("\n"):
            results.append(parse_scuffle_string(line))
    
    return results

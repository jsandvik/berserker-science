def parse_scuffle_string(scuffle_string):
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

def parse_scuffle_output(path):
    results = []
    with open(path, "r") as f:
        for line in f.read().split("\n"):
            results.append(parse_scuffle_string(line))
    
    return results

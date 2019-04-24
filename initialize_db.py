from sc_guide.create_app import create_app
from os import listdir
from os.path import isfile, join, splitext, basename
from sc_guide.scuffle_parser import parse_scuffle_output
from sc_guide.models import Move

def main():
    # drop collections before rebuilding it
    print("Dropping collection")
    Move.drop_collection()

    path = join(app.root_path, "frame_data/")

    files = []
    for f in listdir(path):
        filepath = join(path, f)
        if isfile(filepath):
            files.append(filepath)
    
    print("Rebuilding collections")
    for f in files:
        print("Parsing: ", f)
        character_name = basename(splitext(f)[0])

        for move_data in parse_scuffle_output(f):
            move = Move(
                character=character_name,
                category=move_data["category"],
                command=move_data["command"],
                move_properties=move_data["moveProperties"],
                attack_types=move_data["attackTypes"],
                impact_frames=move_data["impactFrames"],
                block_frames=move_data["blockFrames"],
                hit_frames=move_data["hitFrames"],
                hit_property=move_data["hitProperty"],
                counter_frames=move_data["counterFrames"],
                counter_property=move_data["counterProperty"],
                damage=move_data["damage"],
                gap_frames=move_data["gapFrames"]
            )
            move.save()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        main()

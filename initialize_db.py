from sc_guide.create_app import create_app
from os import listdir
from os.path import isfile, join, splitext, basename
from sc_guide.scuffle_parser import (
    parse_scuffle_output, parse_combo_file, parse_lethal_hits
)
from sc_guide.models import Move, Combo

def main():
    # drop collections before rebuilding it
    print("Clearing database")
    Move.drop_collection()

    frame_data_path = join(app.root_path, "frame_data/")
    frame_data_files = []
    for f in listdir(frame_data_path):
        filepath = join(frame_data_path, f)
        if isfile(filepath):
            frame_data_files.append(filepath)
    
    combos_path = join(app.root_path, "combos/")
    combo_files = []
    for f in listdir(combos_path):
        filepath = join(combos_path, f)
        if isfile(filepath):
            combo_files.append(filepath)

    print("Parsing Combos")
    combos = {}
    for f in combo_files:
        print("Parsing: ", f)
        character_name = basename(splitext(f)[0]).lower()

        for starting_move, combo_data in parse_combo_file(f).items():
            combo_list = []
            for combo in combo_data:
                combo_list.append(Combo(
                    commands=combo["commands"],
                    damage=combo["damage"],
                    condition=combo["condition"],
                    notes=combo["notes"]
                ))
            combos[(character_name, starting_move)] = combo_list

    print("Parsing Lethal Hits")
    lethal_hit_data_path = join(app.root_path, "other_data/lethal_hits.txt")
    lethal_hits = parse_lethal_hits(lethal_hit_data_path)

    print("Parsing Frame Data")
    for f in frame_data_files:
        print("Parsing: ", f)
        character_name = basename(splitext(f)[0]).lower()

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
                gap_frames=move_data["gapFrames"],
                combos=combos.get((character_name, move_data["command"]), []),
                lethal_hit_condition=lethal_hits.get((character_name, move_data["command"]), None)
            )

            move.save()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        main()

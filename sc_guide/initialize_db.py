from create_app import create_app
from database import uses_db
from os import listdir
from os.path import isfile, join, splitext, basename
from scuffle_parser import parse_scuffle_output
from models import Move, Character

@uses_db
def main(session=None):
    path = join(app.root_path, "frame_data/")

    files = []
    for f in listdir(path):
        filepath = join(path, f)
        if isfile(filepath):
            files.append(filepath)

    for f in files:
        print("Parsing: ", f)
        character_name = basename(splitext(f)[0])

        character = Character(name=character_name)
        session.add(character)
        session.flush()

        output = parse_scuffle_output(f)
        for move_data in output:
            move = Move(
                character_id=character.character_id,
                command=move_data["command"],
                impact_frames=move_data["impactFrames"],
                block_frames=move_data["blockFrames"],
                hit_frames=move_data["hitFrames"],
                counter_frames=move_data["counterFrames"],
                damage=move_data["damage"]
            )
            session.add(move)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        main()

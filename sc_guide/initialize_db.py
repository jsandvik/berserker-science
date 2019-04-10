from create_app import create_app
from database import uses_db
from os import listdir
from os.path import isfile, join, splitext, basename
from scuffle_parser import parse_scuffle_output
from models import Move, Character, Category

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
        for category_name, moves in output.items():
            # add category if doesn't exist yet
            category = session.query(Category).filter_by(name=category_name).one_or_none()
            if category is None:
                category = Category(name=category_name)
                session.add(category)
                session.flush()

            for move_data in moves:
                move = Move(
                    character_id=character.character_id,
                    category_id=category.category_id,
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

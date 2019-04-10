from flask import jsonify
from sc_guide.create_app import create_app
from sc_guide.models import Move
from sc_guide.database import uses_db

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/moves/')
@uses_db
def moves(session=None):
    moves = [{
        "moveId": move.move_id,
        "character": {
            "characterId": move.character.character_id,
            "characterName": move.character.name
        },
        "command": move.command,
        "impactFrames": move.impact_frames,
        "blockFrames": move.block_frames,
        "hitFrames": move.hit_frames,
        "hitProperty": move.hit_property,
        "counterFrames": move.counter_frames,
        "counterProperty": move.counter_property,
        "damage": move.damage
    } for move in session.query(Move)]
    return jsonify(moves)

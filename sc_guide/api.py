from flask import jsonify
from sc_guide.create_app import create_app
from sc_guide.models import Move

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/moves/')
def moves(session=None):
    moves = [{
        "character": move.character,
        "category": move.category,
        "command": move.command,
        "attackTypes": move.attack_types,
        "impactFrames": move.impact_frames,
        "blockFrames": move.block_frames,
        "hitFrames": move.hit_frames,
        "hitProperty": move.hit_property,
        "counterFrames": move.counter_frames,
        "counterProperty": move.counter_property,
        "damage": move.damage
    } for move in Move.objects]
    return jsonify(moves)

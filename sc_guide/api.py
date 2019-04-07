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
        "notation": move.notation,
        "impactFrames": move.impact_frames
    } for move in session.query(Move)]
    return jsonify(moves)

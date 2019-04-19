from flask import jsonify, request
from sc_guide.create_app import create_app
from sc_guide.models import Move
import math

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/moves/')
def moves(session=None):
    size = request.args.get("size", None, int)
    page = request.args.get("page", None, int)
    character = request.args.get("character", None, str)

    filter_args = {}

    if character is not None:
        filter_args["character"] = character

    query = Move.objects(**filter_args)

    count = None
    if size is not None and page is not None:
        # get total pages for frontend to know how many pages exist
        count = query.count()
        num_pages = math.ceil(count / size)

        # slice current page results
        offset = page * size
        query = query.skip(offset).limit(size)

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
        "damage": move.damage,
        "gapFrames": move.gap_frames
    } for move in query]

    results = {
        "moves": moves
    }

    if count is not None:
        results["numPages"] = num_pages

    return jsonify(results)

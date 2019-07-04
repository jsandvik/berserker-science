from flask import jsonify, request
from sc_guide.create_app import create_app
from sc_guide.models import Move
import math

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/categories/')
def categories(session=None):
    character = request.args.get("character", "", str)

    moves = Move.objects(character__iexact=character)
    categories = []
    for move in moves:
        if move.category not in categories:
            categories.append(move.category)

    return jsonify({
        "categories": categories
    })

@app.route('/moves/')
def moves(session=None):
    size = request.args.get("size", None, int)
    page = request.args.get("page", None, int)
    character = request.args.get("character", None, str)
    command = request.args.get("command", None, str)
    category = request.args.get("category", None, str)
    order_by = request.args.getlist("order_by", str)

    filter_args = {}

    if character is not None:
        filter_args["character__iexact"] = character
    if command is not None:
        # think this through better... I'd like to be able to 
        # not have to input the move name exactly, but I also don't
        # want to return every move using 'A' when I type just 'A'
        filter_args["command__iexact"] = command
    if category is not None:
        filter_args["category__iexact"] = category

    query = Move.objects(**filter_args)

    # optional: handle sorting
    if order_by:
        query = query.order_by(*order_by)

    count = None
    if size is not None and page is not None:
        # get total pages for frontend to know how many pages exist
        count = query.count()
        num_pages = math.ceil(count / size)

        # slice current page results
        offset = page * size
        query = query.skip(offset).limit(size)

    # im tired and just want this to work. this is bad. replace later
    def temp(combos):
        return [{
            "commands": combo.commands,
            "damage": combo.damage,
            "condition": combo.condition,
            "notes": combo.notes,
        } for combo in combos]

    moves = [{
        "character": move.character,
        "category": move.category,
        "command": move.command,
        "attackTypes": move.attack_types,
        "moveProperties": move.move_properties,
        "impactFrames": move.impact_frames,
        "blockFrames": move.block_frames,
        "hitFrames": move.hit_frames,
        "hitProperty": move.hit_property,
        "counterFrames": move.counter_frames,
        "counterProperty": move.counter_property,
        "damage": move.damage,
        "gapFrames": move.gap_frames,
        "combos": temp(move.combos),
    } for move in query]

    results = {
        "moves": moves
    }

    if count is not None:
        results["numPages"] = num_pages

    return jsonify(results)

from sc_guide.constants import AttackTypes, MoveProperty
from mongoengine import connect, Document, StringField, IntField, ListField, EmbeddedDocumentField, EmbeddedDocument
import os

connect('berserker-science', host=os.getenv("MONGODB_URI"))

class Combo(EmbeddedDocument):
    commands = StringField(required=True)
    damage = IntField()
    condition = StringField(choices=["NC", "NCC", "LH", "B"])
    notes = StringField()

class Move(Document):
    command = StringField(required=True)
    character = StringField(required=True)
    category = StringField()
    attack_types = ListField(StringField(choices=[e.value for e in AttackTypes]))
    move_properties = ListField(StringField(choices=[e.value for e in MoveProperty]))
    impact_frames = IntField()
    block_frames = IntField()
    hit_frames = IntField()
    counter_frames = IntField()
    hit_property = StringField()
    counter_property = StringField()
    damage = ListField(IntField())
    gap_frames = ListField(IntField())
    lethal_hit_condition = StringField()
    combos = ListField(EmbeddedDocumentField(Combo))

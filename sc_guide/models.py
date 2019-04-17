from sc_guide.constants import AttackTypes
from mongoengine import connect, Document, StringField, IntField, ListField
import os

connect('berserker-science', host=os.getenv("MONGODB_URI"))

class Move(Document):
    command = StringField(required=True)
    character = StringField(required=True)
    category = StringField()
    attack_types = ListField(StringField(choices=[e.value for e in AttackTypes]))
    impact_frames = IntField()
    block_frames = IntField()
    hit_frames = IntField()
    counter_frames = IntField()
    hit_property = StringField()
    counter_property = StringField()
    damage = ListField(IntField())
    gap_frames = ListField(IntField())

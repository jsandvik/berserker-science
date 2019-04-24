import enum

class AttackTypes(enum.Enum):
    low = "L"
    middle = "M"
    high = "H"
    special_middle = "SM"
    special_low = "SL"

class MoveProperty(enum.Enum):
    BA = "BA"
    RE = "RE"
    SS = "SS"
    TH = "TH"
    LH = "LH"
    SG = "SG"
    SC = "SC"
    GI = "GI"
    UA = "UA"

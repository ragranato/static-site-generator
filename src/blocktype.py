from enum import Enum, auto

class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = auto()
    CODE = auto()
    QUOTE = auto()
    UNORDERED_LIST = auto()
    ORDERED_LIST = auto()

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    elif block[0] == "`":
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif block[0] == "- ":
        return BlockType.UNORDERED_LIST
    elif block[0] == "\n1. ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    


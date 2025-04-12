from enum import Enum, auto
import re

class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = auto()
    CODE = auto()
    QUOTE = auto()
    UNORDERED_LIST = auto()
    ORDERED_LIST = auto()

def block_to_block_type(block):
    block = block.strip()
    if re.fullmatch(r"^(#{1,6})\s+(.+)$", block):  
        return BlockType.HEADING
    elif re.fullmatch(r"^```(?:[\s\S]*?)```$", block, re.DOTALL):
        return BlockType.CODE
    elif re.fullmatch(r"^>\s*(.+)$", block, re.DOTALL):
        return BlockType.QUOTE
    elif re.fullmatch(r"^\s*[-+*]\s+(.+)$", block, re.DOTALL):
        return BlockType.UNORDERED_LIST
    elif re.fullmatch(r"^\s*\d+\.\s+(.+)$", block, re.DOTALL):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
# test_ordered = """
#                         1. lists
#                         2. arrays
#                     """
# print(test_ordered)
# print(block_to_block_type(test_ordered))

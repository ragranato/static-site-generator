import unittest

from blocktype import *

class Test_Blocktype(unittest.TestCase):
    def test_blocktype(self):
        test_code = "```code```"
        test_ordered = """
                        1. lists
                        2. arrays
                    """
        code_example = block_to_block_type(test_code)
        ordered_example = block_to_block_type(test_ordered)
        self.assertEqual(code_example, BlockType.CODE)
        self.assertEqual(ordered_example, BlockType.ORDERED_LIST)
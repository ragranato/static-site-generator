


def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    # Split by double newlines
    blocks = markdown.split('\n\n')
    result = []
    
    for block in blocks:
        # Skip empty blocks
        if not block.strip():
            continue
        
        # Split the block into lines, strip each line, and rejoin
        lines = [line.strip() for line in block.split('\n')]
        cleaned_block = '\n'.join(lines)
        
        result.append(cleaned_block)
    
    return result

# test = markdown_to_blocks(
#     """# This is a heading

#         This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

#         - This is the first list item in a list block
#         - This is a list item
#         - This is another list item"""
#         )

# print(test)


def markdown_to_blocks(markdown):
    markdown_split = markdown.split("\n\n")    

    for block in markdown_split:
        if block == "":
            markdown_split.pop(block)
        block.strip("")
    
    return markdown_split

test = markdown_to_blocks(
    """# This is a heading

        This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        - This is the first list item in a list block
        - This is a list item
        - This is another list item"""
        )

print(test)
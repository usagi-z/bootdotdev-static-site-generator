

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = map(lambda x: x.strip(), blocks)
    return list(filter(lambda x: x != '', blocks))

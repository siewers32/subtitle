
output = "output.srt"
w = open(output,"w")
to_replace = [
    '<font size="36">',
    '</font>',
    '<c.green>',
    '<c.cyan>',
    '<c.yellow>',
    '<c.color008000>',
]

for f in open("input.srt", "r"):
    new_line = f
    for r in to_replace:
        new_line = new_line.replace(r,"")
    w.write(new_line)
    # new_lines.append(new_line)

    


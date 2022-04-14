layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
]
indexA = indexB = 0
for i in range(0,len(layout)):
    for j in range(0,len(layout[i])):
        if layout[i][0] == "E" and layout[i][1] == "e":
            print(i,0)
            indexA = i
            indexB = j
        elif layout[i][-1] == "E" and layout[i][-2] == "e":
            print(i,-1)
            indexA = i
            indexB = j

print(indexA, indexB)
colors= tuple(("red","green","blue","black","yellow"))
print(colors)

list_colors=list (colors)
list_colors.insert(3,"White")
colors=tuple(list_colors)
print(colors)

list_colors=list (colors)
list_colors.append("Pink")
colors=tuple(list_colors)
print(colors)

list_colors=list(colors)
list_colors.pop(2)
colors=tuple(list_colors)
print(colors)

list_colors=list (colors)
print("Length is : ",len(list_colors))
colors=tuple(list_colors)
print(colors)

list_colors=list (colors)
list_colors.clear()
colors=tuple(list_colors)
print(colors)

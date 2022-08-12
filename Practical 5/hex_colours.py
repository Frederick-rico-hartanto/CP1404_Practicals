COLOURS_CODES = {
    "absolute zero": "#0048ba", "acid green": "#b0bf1a",
    "alice blue": "#f0f8ff", "alizarin crimson": "#e32636",
    "amethyst": "	#9966cc", "bitter lime": "#bfff00", "black": "#000000"
    , "azure4": "#838b8b", "beige": "#f5f5dc", "bisque1": "#ffe4c4"
}


colour_name = str(input("Type in a colour:")).lower()
while colour_name != "":
    if colour_name in COLOURS_CODES:
        print(f"{COLOURS_CODES[colour_name]}is the code for {colour_name}")
        colour_name = str(input("Type in a colour:")).lower()
    else:
        print("No colour available")

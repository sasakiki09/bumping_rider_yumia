input_path = 'motorcycle.html'
output_path = 'game.html'

with open(input_path, "r", encoding="UTF-8") as file:
    html = file.read()

fixed_html = html.replace('name: "motorcycle.pyxapp",', 'name: "motorcycle.pyxapp", packages: "Pillow,bitarray",')
    
with open(output_path, "w", encoding="UTF-8") as file:
    file.write(fixed_html)

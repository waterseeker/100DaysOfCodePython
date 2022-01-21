import colorgram

colors = colorgram.extract('./hirst_loyalty.jpeg', 10)

rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
print(rgb_colors)

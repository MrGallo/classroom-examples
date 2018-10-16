# Tip: Get color scheme from coolors.co or google "pink rgb" or "pink hex".
# Download processing from processing.org. Install it, then add Python mode.
# Check out the reference http://py.processing.org/reference

size(800, 600)             # set size of window
background("#DDC9B4")      # Colors are in HEX
# background(255, 0, 128)  # but can also be in RGB

noStroke()  # remove border on shapes
# ellipse(x, y, width, height)
fill("#2A3D45")  # change shape fill color
ellipse(width/2, height/2, 100, 100)

stroke("#7A6C5D")  # Set border color
strokeWeight(15)   # set border thickness

# rect(x, y, width, height)
fill("#C17C74")
rect(width/2, height/2, 200, 200)


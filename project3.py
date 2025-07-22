from PIL import Image, ImageDraw
import random
import pprint
class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes # store the dictionary
    

    def draw(self, draw_context):
        x, y = self.attributes['position']
        width = self.attributes["width"]
        length = self.attributes ["length"]
        color = self.attributes['color']
        draw_context.rectangle((x, y, x + width, y + length), fill=color)

class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element):
        self.elements.append(element)
   
    def __str__(self):
       return pprint.pformat(f"{str(self.width)}, {str(self.height)}, {str(self.bg_color)}")

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
        self.image.show()
        self.image.save("output.png")

def __str__(self):
    return pprint.pformat(self.rectangle)
def __str__(self):
    return '\n'.join(f"{k}: {v}" for k, v in self.attributes.items())

def main():
    canvas = Canvas(500, 500, (255, 255, 255))


    for _ in range(60):
        attrs = {
        'position': (random.randint(20, 380), random.randint(20,380)),
        'width': random.randint(10, 500),
        'length': random.randint(40, 90),
        'color': 
        (random.randint(0,255), 
        random.randint(0,255),
         random.randint(0,255))
        }
        rectangle = ArtElement(attrs)
        canvas.add_element(rectangle)
    canvas.render()
  
main()
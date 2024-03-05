from PIL import Image, ImageDraw

bounding_box_file_path = 'bounding_box.txt'

image_file_path = 'image.png'

bounding_boxes = []
with open(bounding_box_file_path, 'r') as file:
    for line in file:
        x1, y1, x2, y2 = map(int, line.split())
        bounding_boxes.append((x1, y1, x2, y2))

image = Image.open(image_file_path)

draw = ImageDraw.Draw(image)

for (x1, y1, x2, y2) in bounding_boxes:
    draw.rectangle([x1, y1, x2, y2], outline="red", width=2)

image.save('output_image.png')

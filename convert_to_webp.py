import os
from PIL import Image

input_folder = 'assets/images'
output_folder = os.path.join(input_folder, 'webp')

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)

        # Preserve transparency for PNG, standard for JPG
        if filename.lower().endswith('.png'):
            image = Image.open(image_path).convert('RGBA')
        else:
            image = Image.open(image_path).convert('RGB')

        webp_filename = os.path.splitext(filename)[0] + '.webp'
        webp_path = os.path.join(output_folder, webp_filename)

        image.save(webp_path, 'webp', quality=80)
        print(f"✅ Converted: {filename} → {webp_filename}")

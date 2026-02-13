from PIL import Image, ImageDraw, ImageFont
import os
import argparse

SIZES = [16, 32, 64, 128, 256, 512]

def create_iconset(output_dir, text='YT'):
    os.makedirs(output_dir, exist_ok=True)
    for size in SIZES:
        # standard
        img = Image.new('RGBA', (size, size), (10, 102, 194, 255))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype('Arial.ttf', size // 2)
        except Exception:
            font = ImageFont.load_default()
        bbox = draw.textbbox((0,0), text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((size - w) / 2, (size - h) / 2), text, font=font, fill=(255,255,255,255))
        img.save(os.path.join(output_dir, f'icon_{size}x{size}.png'))

        # @2x
        img2 = img.resize((size*2, size*2), Image.LANCZOS)
        draw2 = ImageDraw.Draw(img2)
        try:
            font2 = ImageFont.truetype('Arial.ttf', size)
        except Exception:
            font2 = ImageFont.load_default()
        bbox2 = draw2.textbbox((0,0), text, font=font2)
        w2, h2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
        draw2.text(((size*2 - w2) / 2, (size*2 - h2) / 2), text, font=font2, fill=(255,255,255,255))
        img2.save(os.path.join(output_dir, f'icon_{size}x{size}@2x.png'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', default='icon.iconset')
    parser.add_argument('--text', '-t', default='YT')
    args = parser.parse_args()
    create_iconset(args.output, args.text)

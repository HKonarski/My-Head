#!/usr/bin/env python3
from PIL import Image
import math
import os
import argparse

def make_gif(input_path, output_path, frames=20, delay=80, amplitude=8, rotation=6):
    img = Image.open(input_path).convert('RGBA')
    w,h = img.size
    out_frames = []

    for i in range(frames):
        t = i / frames
        y = math.sin(t * 2 * math.pi) * amplitude
        r = math.sin(t * 2 * math.pi) * rotation

        rotated = img.rotate(r, resample=Image.BICUBIC, expand=True)
        frame = Image.new('RGBA', (w, h), (255,255,255,0))
        rw, rh = rotated.size
        paste_x = (w - rw) // 2
        paste_y = (h - rh) // 2 + int(round(y))
        frame.paste(rotated, (paste_x, paste_y), rotated)

        # Convert to P mode for GIF palette
        out_frames.append(frame.convert('P', palette=Image.ADAPTIVE))

    if not out_frames:
        raise RuntimeError('No frames generated')

    first, rest = out_frames[0], out_frames[1:]
    first.save(
        output_path,
        save_all=True,
        append_images=rest,
        duration=delay,
        loop=0,
        disposal=2
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gerar GIF animado do PokeNilbas')
    parser.add_argument('--in', dest='input', default=os.path.join('img','PokeNilbas com estil.png'))
    parser.add_argument('--out', dest='output', default='poke_nilbas_final.gif')
    parser.add_argument('--frames', type=int, default=20)
    parser.add_argument('--delay', type=int, default=80, help='delay em ms')
    parser.add_argument('--amplitude', type=float, default=8.0)
    parser.add_argument('--rotation', type=float, default=6.0)
    args = parser.parse_args()

    make_gif(args.input, args.output, frames=args.frames, delay=args.delay, amplitude=args.amplitude, rotation=args.rotation)
    print('GIF gerado em', args.output)

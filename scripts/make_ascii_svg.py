from PIL import Image


INPUT = "source-prepped.png"
OUTPUT = "avi-ascii.svg"

WIDTH = 100
HEIGHT = 53

# Bright → dark
RAMP = " .`:-=+*cs#%@"

COLOR = "#c7c7c7"

image = Image.open(INPUT).convert("L")

image.thumbnail((WIDTH, HEIGHT))

# Create white canvas
canvas = Image.new("L", (WIDTH, HEIGHT), 255)

x_offset = (WIDTH - image.width) // 2
y_offset = (HEIGHT - image.height) // 2

canvas.paste(image, (x_offset, y_offset))

pixels = canvas.load()

rows = []

for y in range(HEIGHT):

    chars = []

    for x in range(WIDTH):

        brightness = pixels[x, y]

        index = int(
            brightness / 255 * (len(RAMP) - 1)
        )

        chars.append(RAMP[index])

    rows.append("".join(chars))


svg = []

svg.append(
    f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="700"
    height="380"
    viewBox="0 0 {WIDTH * 7} {HEIGHT * 7}">
    
    <rect width="100%" height="100%" fill="#0d1117"/>
    
    <style>
        text {{
            font-family: monospace;
            font-size: 7px;
            fill: {COLOR};
            white-space: pre;
        }}

        .row {{
            animation: reveal 0.7s ease-out forwards;
            opacity: 0;
        }}

        @keyframes reveal {{
            from {{
                opacity: 0;
                transform: translateX(-20px);
            }}

            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}
    </style>
'''
)

for y, row in enumerate(rows):

    delay = y * 0.035

    escaped = (
        row
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    svg.append(
        f'''
        <text
            class="row"
            x="0"
            y="{(y + 1) * 7}"
            style="animation-delay:{delay}s"
        >{escaped}</text>
        '''
    )

svg.append("</svg>")

with open(OUTPUT, "w") as f:
    f.write("\n".join(svg))

print(f"Created {OUTPUT}")
import json
from datetime import datetime


INPUT = "data/contributions.json"
OUTPUT = "contrib-heatmap.svg"

PALETTE = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
    "#69f0a0"
]


with open(INPUT) as f:
    data = json.load(f)


days = data["days"][-371:]

WIDTH = 860
HEIGHT = 190

LEFT = 20
TOP = 35

CELL = 11
GAP = 3

svg = f'''
<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}"
     height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

<rect
    width="100%"
    height="100%"
    rx="12"
    fill="#0d1117"/>

<text
    x="20"
    y="22"
    fill="#c9d1d9"
    font-family="monospace"
    font-size="13">
    contributions
</text>
'''


for i, day in enumerate(days):

    week = i // 7
    weekday = i % 7

    x = LEFT + week * (CELL + GAP)
    y = TOP + weekday * (CELL + GAP)

    level = min(
        int(day["level"]),
        5
    )

    color = PALETTE[level]

    delay = i * 0.003

    svg += f'''
    <rect
        x="{x}"
        y="{y}"
        width="{CELL}"
        height="{CELL}"
        rx="2"
        fill="{color}"
        opacity="0">

        <animate
            attributeName="opacity"
            from="0"
            to="1"
            begin="{delay}s"
            dur="0.25s"
            fill="freeze"/>

    </rect>
    '''


svg += '''
<text
    x="20"
    y="175"
    fill="#8b949e"
    font-family="monospace"
    font-size="11">
    Less
</text>
'''


for i, color in enumerate(PALETTE):

    x = 55 + i * 16

    svg += f'''
    <rect
        x="{x}"
        y="166"
        width="11"
        height="11"
        rx="2"
        fill="{color}"/>
    '''


svg += '''
<text
    x="155"
    y="175"
    fill="#8b949e"
    font-family="monospace"
    font-size="11">
    More
</text>

</svg>
'''


with open(OUTPUT, "w") as f:
    f.write(svg)


print(f"Created {OUTPUT}")
OUTPUT = "info-card.svg"

svg = """
<svg xmlns="http://www.w3.org/2000/svg"
     width="490"
     height="380"
     viewBox="0 0 490 380">

<rect
    width="490"
    height="380"
    rx="12"
    fill="#0d1117"
    stroke="#30363d"
    stroke-width="2"/>

<text
    x="25"
    y="40"
    fill="#58a6ff"
    font-family="monospace"
    font-size="22"
    font-weight="bold">
    abhishek@github
</text>

<text
    x="25"
    y="65"
    fill="#8b949e"
    font-family="monospace"
    font-size="14">
    -------------------------
</text>

<text x="25" y="105"
      fill="#58a6ff"
      font-family="monospace"
      font-size="15">
    Now
</text>

<text x="150" y="105"
      fill="#c9d1d9"
      font-family="monospace"
      font-size="15">
    AI &amp; Data Science
</text>

<text x="25" y="140"
      fill="#58a6ff"
      font-family="monospace"
      font-size="15">
    Stack
</text>

<text x="150" y="140"
      fill="#c9d1d9"
      font-family="monospace"
      font-size="15">
    Python / Next.js / Node
</text>

<text x="150" y="165"
      fill="#c9d1d9"
      font-family="monospace"
      font-size="15">
    React / Docker / AWS
</text>

<text x="25" y="205"
      fill="#58a6ff"
      font-family="monospace"
      font-size="15">
    Projects
</text>

<text x="150" y="205"
      fill="#c9d1d9"
      font-family="monospace"
      font-size="15">
    AI / ML / SaaS
</text>

<text x="25" y="245"
      fill="#58a6ff"
      font-family="monospace"
      font-size="15">
    Highlights
</text>

<text x="150" y="245"
      fill="#c9d1d9"
      font-family="monospace"
      font-size="15">
    Hackathons
</text>

<text x="150" y="270"
      fill="#c9d1d9"
      font-family="monospace"
      font-size="15">
    Open Source
</text>

<text x="150" y="295"
      fill="#c9d1d9"
      font-family="monospace"
      font-size="15">
    Building Products
</text>

<text x="25" y="345"
      fill="#3fb950"
      font-family="monospace"
      font-size="14">
    status: building...
</text>

</svg>
"""

with open(OUTPUT, "w") as f:
    f.write(svg)

print(f"Created {OUTPUT}")
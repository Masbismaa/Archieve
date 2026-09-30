"""SVG images for the GitHub README (GitHub shows them as <img>, so only CSS animation, no script).

    python tools/readme_svgs.py

Numbers here mirror js/data/archive.js. When a feature changes status there, change it here too.
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'readme'

INK0, INK1, INK2 = '#0b0c0f', '#121419', '#151b27'
LINE, LINE2 = '#24262b', '#3a3a38'
PAPER, PARCH, MUTED = '#ece7dc', '#d9cfb8', '#948e81'
CRIMSON, RED, EMBER, OK = '#8e1b24', '#c24b43', '#d0703a', '#9fb49a'
SERIF = "'Shippori Mincho B1','Hiragino Mincho ProN','Yu Mincho',Georgia,'Times New Roman',serif"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"
KANJI = "'Hiragino Mincho ProN','Yu Mincho','Noto Serif CJK JP','Noto Serif JP',serif"

ALR = {'implemented': 9, 'progress': 4, 'planned': 1}
STAGES = [('I', 'Groundwork'), ('II', 'Training ground'), ('III', 'Field work'), ('IV', 'Deeper systems'), ('V', 'Sealing discipline'), ('VI', 'Current')]


def grid(w, h, step=48):
    lines = ''.join(f'<path d="M{x} 0V{h}"/>' for x in range(0, w, step)) + ''.join(f'<path d="M0 {y}H{w}"/>' for y in range(0, h, step))
    return f'<g stroke="{LINE}" stroke-width="1" opacity=".6">{lines}</g>'


def seal(x, y, s, glyph):
    # rough-edged stamp: the same filter the website uses
    return (f'<g transform="translate({x} {y})"><rect width="{s}" height="{s}" rx="4" fill="{CRIMSON}" filter="url(#ink)"/>'
            f'<text x="{s / 2}" y="{s * .7}" text-anchor="middle" font-family="{KANJI}" font-weight="800" font-size="{s * .56}" fill="{PARCH}">{glyph}</text></g>')


INK_FILTER = '<filter id="ink"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="3.2"/></filter>'


def gate():
    w, h = 1200, 400
    log = [('$ ', 'archive open --id 4D-42-50', PAPER), ('  visitor ....... ', 'unregistered', OK), ('  access ........ ', 'read-only', OK), ('  archive ....... ', 'open', PAPER)]
    lines = ''.join(
        f'<text class="l" style="animation-delay:{.25 + i * .35:.2f}s" x="56" y="{62 + i * 22}" font-family="{MONO}" font-size="14" fill="{MUTED}">{a}<tspan fill="{c}">{b}</tspan></text>'
        for i, (a, b, c) in enumerate(log))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>{INK_FILTER}
    <radialGradient id="v" cx=".35" cy=".4" r=".9"><stop offset=".4" stop-color="{INK0}" stop-opacity="0"/><stop offset="1" stop-color="{INK0}" stop-opacity=".95"/></radialGradient>
  </defs>
  <style>
    @keyframes in {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    .l {{ opacity: 0; animation: in .01s steps(1) forwards; }}
    .name {{ opacity: 0; animation: in .9s ease-out 1.8s forwards; }}
    .rest {{ opacity: 0; animation: in .9s ease-out 2.3s forwards; }}
    @keyframes stamp {{ 0% {{ opacity: 0; transform: scale(1.25) rotate(-8deg); }} 100% {{ opacity: 1; transform: none; }} }}
    .seal {{ transform-box: fill-box; transform-origin: center; opacity: 0; animation: stamp .35s cubic-bezier(.2,.7,.2,1) 2.1s forwards; }}
    @keyframes pulse {{ 50% {{ opacity: .25; }} }}
    .live {{ animation: pulse 2.4s ease-in-out infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .cur {{ animation: blink 1s steps(1) infinite; }}
  </style>
  <rect width="{w}" height="{h}" fill="{INK0}"/>
  {grid(w, h)}
  <rect width="{w}" height="{h}" fill="url(#v)"/>
  {lines}
  <rect class="cur" x="56" y="{62 + 4 * 22 - 12}" width="8" height="15" fill="{EMBER}"/>
  <g class="name">
    <text x="54" y="232" font-family="{SERIF}" font-weight="800" font-size="62" fill="{PARCH}">Mochammad Bisma Prasetya</text>
    <text x="56" y="270" font-family="{MONO}" font-size="15" fill="{PAPER}">IT Developer at Spindo. Builds internal web apps end to end. Access control is part of the feature.</text>
  </g>
  <g class="rest" font-family="{MONO}" font-size="13">
    <rect x="56" y="296" width="2" height="72" fill="{CRIMSON}"/>
    <text x="72" y="313" fill="{MUTED}" letter-spacing="1.6">STATUS</text><rect class="live" x="236" y="303" width="7" height="7" fill="{EMBER}"/><text x="252" y="313" fill="{EMBER}">active · open to remote work</text>
    <text x="72" y="337" fill="{MUTED}" letter-spacing="1.6">CURRENT MISSION</text><text x="236" y="337" fill="{PAPER}">M-01 MTOA Access Link Register · hardening and tests</text>
    <text x="72" y="361" fill="{MUTED}" letter-spacing="1.6">IN TRAINING</text><text x="236" y="361" fill="{PAPER}">Docker, pentesting, API design, LLM integration</text>
  </g>
  <g class="seal">{seal(1060, 48, 84, '記')}</g>
  <text x="1144" y="160" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUTED}" letter-spacing="1.6">ARCHIVE 4D-42-50</text>
  <text x="1144" y="178" text-anchor="end" font-family="{MONO}" font-size="11" fill="{LINE2}" letter-spacing="1.6">記 · record</text>
</svg>'''


def hq():
    w, h = 1200, 88
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <style>@keyframes blink {{ 50% {{ opacity: 0; }} }} .cur {{ animation: blink 1s steps(1) infinite; }}
  @keyframes sweep {{ from {{ stroke-dashoffset: 2600; }} to {{ stroke-dashoffset: 0; }} }} .edge {{ stroke-dasharray: 180 2400; animation: sweep 5s linear infinite; }}</style>
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" fill="{INK1}" stroke="{LINE2}"/>
  <rect class="edge" x=".5" y=".5" width="{w - 1}" height="{h - 1}" fill="none" stroke="{RED}" stroke-width="2"/>
  <text x="36" y="38" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{MUTED}">HEADQUARTERS · FULL ARCHIVE WITH A WORKING TERMINAL</text>
  <text x="36" y="64" font-family="{MONO}" font-size="17" fill="{PAPER}"><tspan fill="{RED}">$ </tspan>open https://masbismaa.github.io/Masbismaa</text>
  <rect class="cur" x="540" y="51" width="9" height="17" fill="{EMBER}"/>
  <text x="{w - 36}" y="60" text-anchor="end" font-family="{MONO}" font-size="13" letter-spacing="2" fill="{PARCH}">ENTER  →</text>
</svg>'''


def mission():
    w, h = 1200, 420
    total = sum(ALR.values())
    x, bars = 56, ''
    for key, col, label in [('implemented', OK, 'implemented'), ('progress', EMBER, 'in progress'), ('planned', MUTED, 'planned')]:
        bw = (w - 112) * ALR[key] / total
        bars += f'<rect class="bar" x="{x:.1f}" y="352" width="{bw - 4:.1f}" height="8" fill="{col}" opacity="{1 if key != "planned" else .5}"/>'
        bars += f'<text x="{x:.1f}" y="384" font-family="{MONO}" font-size="12" fill="{col}">{ALR[key]} {label}</text>'
        x += bw
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>{INK_FILTER}</defs>
  <style>
    @keyframes flow {{ to {{ stroke-dashoffset: -20; }} }} .flow {{ stroke-dasharray: 4 6; animation: flow 1.2s linear infinite; }}
    @keyframes grow {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }} .bar {{ transform-box: fill-box; transform-origin: left; animation: grow 1s cubic-bezier(.2,.7,.2,1) both; }}
  </style>
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" fill="{INK1}" stroke="{LINE2}"/>
  <text x="56" y="56" font-family="{MONO}" font-size="13" fill="{RED}">M-01</text>
  <text x="112" y="58" font-family="{SERIF}" font-weight="800" font-size="34" fill="{PARCH}">MTOA Access Link Register</text>
  <g transform="rotate(-3 1100 44)"><rect x="1040" y="30" width="112" height="28" fill="none" stroke="{RED}" stroke-width="1.5"/><text x="1096" y="49" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{RED}">ACTIVE</text></g>
  <text x="112" y="90" font-family="{MONO}" font-size="14" fill="#c9c3b6">Access links in one place. Private means private, even for the admin.</text>
  <text x="112" y="114" font-family="{MONO}" font-size="12.5" fill="{MUTED}">Flask · SQLAlchemy · Alembic · PostgreSQL · Pytest</text>
  <g font-family="{MONO}" font-size="12.5" fill="{PAPER}" transform="translate(160 150)">
    <rect x="0" y="56" width="104" height="40" fill="{INK0}" stroke="{LINE2}"/><text x="52" y="80" text-anchor="middle">browser</text>
    <rect x="140" y="0" width="390" height="150" fill="none" stroke="{RED}" stroke-dasharray="4 4"/>
    <text x="152" y="20" fill="{MUTED}">security: auth · OTP · RBAC · CSRF</text>
    <text x="152" y="38" fill="{MUTED}">rate limit · sessions</text>
    <rect x="164" y="56" width="120" height="40" fill="{INK0}" stroke="{LINE2}"/><text x="224" y="80" text-anchor="middle">routes</text>
    <rect x="370" y="56" width="126" height="40" fill="{INK0}" stroke="{LINE2}"/><text x="433" y="80" text-anchor="middle">services</text>
    <text x="433" y="118" text-anchor="middle" fill="{MUTED}">rules · validation</text>
    <rect x="560" y="56" width="110" height="40" fill="{INK0}" stroke="{LINE2}"/><text x="615" y="80" text-anchor="middle">models</text>
    <rect x="712" y="50" width="138" height="52" fill="{INK0}" stroke="{LINE2}"/><text x="781" y="80" text-anchor="middle">PostgreSQL</text>
    <rect x="620" y="124" width="126" height="34" fill="{INK0}" stroke="{LINE2}"/><text x="683" y="146" text-anchor="middle">audit log</text>
    <path class="flow" d="M104 76H164M284 76H370M496 76H560M670 76H712" stroke="{EMBER}" fill="none"/>
    <path d="M496 90 Q560 140 620 141" stroke="{MUTED}" fill="none"/>
  </g>
  <text x="56" y="336" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{MUTED}">FEATURE STATUS · 14 FEATURES ON RECORD</text>
  {bars}
</svg>'''


def training():
    w, h = 1200, 220
    n = len(STAGES)
    x0, x1, y = 90, w - 90, 108
    step = (x1 - x0) / (n - 1)
    nodes = ''
    for i, (num, title) in enumerate(STAGES):
        x = x0 + i * step
        cur = i == n - 1
        nodes += (f'<g class="node" style="animation-delay:{.3 + i * .35:.2f}s">'
                  f'<rect x="{x - 13}" y="{y - 13}" width="26" height="26" fill="{EMBER if cur else INK0}" stroke="{EMBER if cur else LINE2}"/>'
                  f'<text x="{x}" y="{y + 4}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{INK0 if cur else PAPER}">{num}</text>'
                  f'<text x="{x}" y="{y + 44}" text-anchor="middle" font-family="{SERIF}" font-weight="700" font-size="17" fill="{PARCH}">{title}</text>'
                  + (f'<text class="live" x="{x}" y="{y + 66}" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{EMBER}">CURRENT</text>' if cur else '')
                  + '</g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <style>
    @keyframes draw {{ from {{ stroke-dashoffset: {x1 - x0}; }} to {{ stroke-dashoffset: 0; }} }}
    .walk {{ stroke-dasharray: {x1 - x0}; animation: draw 2.2s cubic-bezier(.4,0,.2,1) .2s both; }}
    @keyframes in {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }} .node {{ opacity: 0; animation: in .4s ease-out forwards; }}
    @keyframes pulse {{ 50% {{ opacity: .3; }} }} .live {{ animation: pulse 2.4s ease-in-out infinite; }}
  </style>
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" fill="{INK1}" stroke="{LINE2}"/>
  <text x="36" y="40" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{MUTED}">TRAINING LOG · 修 · PRACTICE</text>
  <path d="M{x0} {y}H{x1}" stroke="{LINE2}"/>
  <path class="walk" d="M{x0} {y}H{x1}" stroke="{EMBER}" stroke-width="2"/>
  {nodes}
</svg>'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [('gate', gate), ('hq', hq), ('mission-m01', mission), ('training', training)]:
        (OUT / f'{name}.svg').write_text(fn())
        print(name)


if __name__ == '__main__':
    main()

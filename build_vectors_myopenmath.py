"""Builds vectors-myopenmath.md: MyOpenMath code for the 20 Vector Range problems.

Every question is a two-part (Multipart) question: magnitude and direction, or x and y components.
The random numbers, the answers and the simulation link all come from the same variables.
Run:  python3 build_vectors_myopenmath.py
"""
from pathlib import Path

import re


def fix_after_vars(text):
    """MyOpenMath reads special characters such as ° as part of a variable name, so "$th°" would look for a
    variable called "th°" and show nothing. Write the degree sign as &deg; after a variable, and refuse
    any other special character there."""
    text = re.sub(r'(\$\w+)°', r'\1&deg;', text)
    bad = re.findall(r'\$\w+[^\x00-\x7f]', text)
    assert not bad, f'special character right after a variable: {bad}'
    return text

SITE = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html"
RAD = "$rad = 3.141592653589793/180"
DIR_NOTE = "Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°."


def sums(terms):
    """terms: (magnitude, angle expression, sign) -> lines computing $Rx and $Ry."""
    def part(fn):
        out = []
        for m, d, s in terms:
            out.append(f"{'-' if s < 0 else '+'} {m}*{fn}(({d})*$rad)")
        e = " ".join(out)
        return e[2:] if e.startswith("+ ") else "-" + e[2:]
    return [f"$Rx = {part('cos')}", f"$Ry = {part('sin')}"]


POLAR = [
    "$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)",
    "$dir = atan($Ry/$Rx)/$rad",
    "$dir = $dir + 180 if ($Rx < 0)",
    "$dir = $dir + 360 if ($dir < 0)",
    "$answer[1] = $dir",
]
TOL_POLAR = ["$reltolerance[0] = 0.02", "$abstolerance[1] = 1"]
XY = ["$answer[0] = $Rx", "$answer[1] = $Ry"]


def tol_abs(e):
    return [f"$abstolerance[0] = {e}", f"$abstolerance[1] = {e}"]


def signed(var):
    """Lines making $<var>s, e.g. '+ 3' or '− 3', for writing a vector as (x î + y ĵ)."""
    return [f'${var}s = "+ " . abs(${var})', f'${var}s = "− " . abs(${var}) if (${var} < 0)']


# code, name, url keys, generation lines, answer lines, tolerance lines, answer labels/units, display lines, story, polar?
Q = []


def q(code, name, keys, gen, ans, tol, parts, story, polar, show=()):
    Q.append(dict(code=code, name=name, keys=keys, gen=gen, ans=ans, tol=tol, parts=parts, story=story, polar=polar, show=list(show)))


# ---- 1 Components
q("1.1", "Solve the triangle", ["c", "th"],
  ["$c = rrand(3,9,0.5)", "$th = rand(15,75)"],
  ["$answer[0] = $c*cos($th*$rad)", "$answer[1] = $c*sin($th*$rad)"],
  ["$reltolerance[0] = 0.02", "$reltolerance[1] = 0.02"],
  [("a", "m"), ("b", "m")],
  "A <b>$c m</b> ladder leans against a wall, making a <b>$th°</b> angle with the level ground. How far from the wall is its foot (<i>a</i>), and how high up the wall does it reach (<i>b</i>)?", False)
q("1.2", "The ramp", ["a", "b"],
  ["$a = rrand(2,8,0.5)", "$b = rrand(1,4,0.5)"],
  ["$answer[0] = sqrt($a*$a + $b*$b)", "$answer[1] = atan($b/$a)/$rad"],
  ["$reltolerance[0] = 0.02", "$reltolerance[1] = 0.02"],
  [("r", "m"), ("θ", "°")],
  "A ramp rises <b>$b m</b> over a horizontal run of <b>$a m</b>. How long is the ramp's surface (<i>r</i>), and what angle <i>θ</i> does it make with the ground?", False)
q("1.3", "Components of a force", ["F", "th"],
  ["$F = rrand(50,500,10)", "$th = rand(10,350) where (($th > 8 && $th < 82) || ($th > 98 && $th < 172) || ($th > 188 && $th < 262) || ($th > 278 && $th < 352))"],
  ["$answer[0] = $F*cos($th*$rad)", "$answer[1] = $F*sin($th*$rad)"],
  tol_abs("0.015*$F"),
  [("F<sub>x</sub>", "N"), ("F<sub>y</sub>", "N")],
  "A rope pulls a sled with a force of <b>$F N at $th°</b>, measured counterclockwise from the +x axis. Find the x and y components of the force.", False)
q("1.4", "Unit vector", ["Cx", "Cy"],
  ["$Cx = rand(-9,9) where (abs($Cx) >= 2)", "$Cy = rand(-9,9) where (abs($Cy) >= 2)", "$C = sqrt($Cx*$Cx + $Cy*$Cy)"],
  ["$answer[0] = $Cx/$C", "$answer[1] = $Cy/$C"],
  tol_abs("0.015"),
  [("Ĉ<sub>x</sub>", ""), ("Ĉ<sub>y</sub>", "")],
  "Vector <b>C = ($Cx î $Cys ĵ) m</b>. Find the x and y components of the unit vector <b>Ĉ</b>, which points the same way as C but has length 1.", False,
  signed("Cy"))
q("1.5", "Scaling a vector", ["k", "B", "th"],
  ['$k = randfrom("-3,-2,-1.5,-0.5,0.5,1.5,2,2.5,3")', "$B = rand(2,10)", "$th = rand(10,350) where (abs($th - 180) > 3)"],
  ["$answer[0] = abs($k)*$B", "$dir = $th", "$dir = $th + 180 if ($k < 0)", "$dir = $dir - 360 if ($dir >= 360)", "$answer[1] = $dir"],
  TOL_POLAR,
  [("|kB|", "m"), ("θ", "°")],
  "Displacement <b>B</b> is <b>$B m at $th°</b>. Find the magnitude and direction of <b>$k B</b>.", True)
q("1.6", "Components to polar", ["Ax", "Ay"],
  ["$Ax = rand(-12,12) where (abs($Ax) >= 2)", "$Ay = rand(-12,12) where (abs($Ay) >= 2)", "$Rx = $Ax", "$Ry = $Ay"],
  POLAR, TOL_POLAR,
  [("A", "m"), ("θ", "°")],
  "A drone's displacement is <b>A = ($Ax î $Ays ĵ) m</b>. Find the magnitude and direction of A.", True,
  signed("Ay"))

# ---- 2 Adding two vectors
q("2.1", "Two ropes on a box", ["F1", "a1", "F2", "a2"],
  ["$F1 = rand(5,30)", "$a1 = rand(10,60)", "$F2 = rand(5,30)", "$a2 = $a1 + rand(60,120)"] + sums([("$F1", "$a1", 1), ("$F2", "$a2", 1)]),
  POLAR, TOL_POLAR, [("F<sub>net</sub>", "N"), ("θ", "°")],
  "Two ropes pull on a box: <b>F₁ = $F1 N at $a1°</b> and <b>F₂ = $F2 N at $a2°</b>. Find the magnitude and direction of the net force.", True)
q("2.2", "Running on the train", ["vt", "vp", "dp"],
  ["$vt = rand(5,30)", "$vp = rrand(2,8,0.5)", '$dp = randfrom("90,270")'] + sums([("$vt", "180", 1), ("$vp", "$dp", 1)]),
  POLAR, TOL_POLAR, [("v<sub>pg</sub>", "m/s"), ("θ", "°")],
  "A train moves <b>west at $vt m/s</b>. A passenger runs <b>$dpw at $vp m/s</b> relative to the train. Find the passenger's velocity relative to the ground.", True,
  ['$dpw = "north"', '$dpw = "south" if ($dp == 270)'])
q("2.3", "Crossing the river", ["vb", "vc", "dc"],
  ["$vb = rrand(2,6,0.5)", "$vc = rrand(0.5,3,0.5)", '$dc = randfrom("0,180")'] + sums([("$vb", "90", 1), ("$vc", "$dc", 1)]),
  POLAR, TOL_POLAR, [("v", "m/s"), ("θ", "°")],
  "A kayak paddles <b>due north at $vb m/s</b> relative to the water. The river flows <b>$dcw at $vc m/s</b>. Find the kayak's velocity relative to the shore.", True,
  ['$dcw = "east"', '$dcw = "west" if ($dc == 180)'])
q("2.4", "Two-leg hike", ["d1", "t1", "d2", "t2"],
  ["$d1 = rand(200,900)", "$t1 = rand(10,80)", "$d2 = rand(200,900)", "$t2 = rand(10,80)"] + sums([("$d1", "$t1", 1), ("$d2", "180-$t2", 1)]),
  POLAR, TOL_POLAR, [("d", "m"), ("θ", "°")],
  "A hiker walks <b>$d1 m at $t1° N of E</b>, then <b>$d2 m at $t2° N of W</b>. Find the hiker's total displacement.", True)
q("2.5", "Plane in a crosswind", ["vp", "a", "w", "aw"],
  ["$vp = rand(300,600)", "$a = rand(20,160)", "$w = rand(30,120)",
   "$aw = rand(0,359) where ($vp*sin($a*$rad) + $w*sin($aw*$rad) > 0.05*($vp + $w))"] + sums([("$vp", "$a", 1), ("$w", "$aw", 1)]),
  POLAR, TOL_POLAR, [("v<sub>ground</sub>", "km/h"), ("θ", "°")],
  "An airplane flies at <b>$vp km/h at $a°</b> relative to the air. The wind blows at <b>$w km/h toward $aw°</b>. Find the plane's velocity relative to the ground.", True)

# ---- 3 Adding three or more
THREE = ["$F1 = rrand(50,150,10)", "$a1 = rand(20,70)", "$F2 = rrand(150,250,10)", "$a2 = rand(110,160)", "$F3 = rrand(20,60,10)"] + \
        sums([("$F1", "$a1", 1), ("$F2", "$a2", 1), ("$F3", "270", 1)])
q("3.1", "Three forces: components", ["F1", "a1", "F2", "a2", "F3"], THREE, XY, tol_abs("0.005*($F1 + $F2 + $F3)"),
  [("F<sub>net,x</sub>", "N"), ("F<sub>net,y</sub>", "N")],
  "Three forces act on a crate: <b>F₁ = $F1 N at $a1°</b>, <b>F₂ = $F2 N at $a2°</b>, and <b>F₃ = $F3 N at 270°</b>. Find the x and y components of the net force.", False)
q("3.2", "Three forces: net force", ["F1", "a1", "F2", "a2", "F3"], THREE, POLAR, TOL_POLAR,
  [("F<sub>net</sub>", "N"), ("θ", "°")],
  "Three forces act on a crate: <b>F₁ = $F1 N at $a1°</b>, <b>F₂ = $F2 N at $a2°</b>, and <b>F₃ = $F3 N at 270°</b>. Find the magnitude and direction of the net force.", True)
RING_S = sums([("$F1", "$t1", 1), ("$F2", "180-$t2", 1), ("$F3", "180+$t3", 1)])
q("3.3", "Four ropes on a ring", ["F1", "t1", "F2", "t2", "F3", "t3", "t4", "F4"],
  ["$F1 = rrand(300,800,50)", "$t1 = rand(20,70)", "$F2 = rrand(300,800,50)", "$t2 = rand(20,70)", "$F3 = rrand(300,800,50)", "$t3 = rand(20,70)", "$t4 = rand(20,70)",
   RING_S[0].replace("$Rx", "$Sx"), RING_S[1].replace("$Ry", "$Sy"),
   "$F4 = rrand(300,800,50) where (sqrt(($Sx + $F4*cos((360-$t4)*$rad))*($Sx + $F4*cos((360-$t4)*$rad)) + ($Sy + $F4*sin((360-$t4)*$rad))*($Sy + $F4*sin((360-$t4)*$rad))) > 100 && abs($Sy + $F4*sin((360-$t4)*$rad)) > 0.05*abs($Sx + $F4*cos((360-$t4)*$rad)) + 20)",
   "$Rx = $Sx + $F4*cos((360-$t4)*$rad)", "$Ry = $Sy + $F4*sin((360-$t4)*$rad)"],
  POLAR, TOL_POLAR, [("F<sub>net</sub>", "N"), ("θ", "°")],
  "Four people pull on ropes tied to a steel ring: <b>F₁ = $F1 N</b> at $t1° above the +x axis, <b>F₂ = $F2 N</b> at $t2° above the −x axis, <b>F₃ = $F3 N</b> at $t3° below the −x axis, and <b>F₄ = $F4 N</b> at $t4° below the +x axis. Find the net force on the ring.", True)
OR_S = sums([("$d1", "90", 1), ("$d2", "360-$t2", 1)])
q("3.4", "Orienteering", ["d1", "d2", "t2", "t3", "d3"],
  ["$d1 = rand(100,500)", "$d2 = rand(100,500)", "$t2 = rand(15,75)", "$t3 = rand(15,75)",
   OR_S[0].replace("$Rx", "$Sx"), OR_S[1].replace("$Ry", "$Sy"),
   "$d3 = rand(100,500) where (sqrt(($Sx + $d3*cos((180-$t3)*$rad))*($Sx + $d3*cos((180-$t3)*$rad)) + ($Sy + $d3*sin((180-$t3)*$rad))*($Sy + $d3*sin((180-$t3)*$rad))) > 50 && abs($Sy + $d3*sin((180-$t3)*$rad)) > 0.05*abs($Sx + $d3*cos((180-$t3)*$rad)) + 10)",
   "$Rx = $Sx + $d3*cos((180-$t3)*$rad)", "$Ry = $Sy + $d3*sin((180-$t3)*$rad)"],
  POLAR, TOL_POLAR, [("d", "m"), ("θ", "°")],
  "In an orienteering race you run <b>$d1 m due north</b>, then <b>$d2 m at $t2° S of E</b>, then <b>$d3 m at $t3° N of W</b>. Find your displacement from the start.", True)

# ---- 4 Subtraction
q("4.1", "Up, then up or down", ["vi", "df", "vf"],
  ["$vi = rand(4,15)", '$df = randfrom("90,270")', "$vf = rand(1,15) where ($df == 270 || $vf != $vi)", "$Ry = $vf*sin($df*$rad) - $vi"],
  ["$answer[0] = abs($Ry)", "$dir = 90", "$dir = 270 if ($Ry < 0)", "$answer[1] = $dir"],
  TOL_POLAR, [("Δv", "m/s"), ("θ", "°")],
  "A ball moves <b>straight up at $vi m/s</b>. A moment later it moves <b>straight $dfw at $vf m/s</b>. Find the change in velocity Δv = v<sub>f</sub> − v<sub>i</sub>.", True,
  ['$dfw = "up"', '$dfw = "down" if ($df == 270)'])
q("4.2", "Change in position", ["r1", "a1", "r2", "a2"],
  ["$r1 = rrand(400,1200,100)", "$a1 = rand(0,359)", "$r2 = rrand(300,1000,100)",
   "$a2 = rand(0,359) where (sqrt(($r2*cos($a2*$rad) - $r1*cos($a1*$rad))*($r2*cos($a2*$rad) - $r1*cos($a1*$rad)) + ($r2*sin($a2*$rad) - $r1*sin($a1*$rad))*($r2*sin($a2*$rad) - $r1*sin($a1*$rad))) > 200 && abs($r2*sin($a2*$rad) - $r1*sin($a1*$rad)) > 0.05*abs($r2*cos($a2*$rad) - $r1*cos($a1*$rad)) + 10)"]
  + sums([("$r2", "$a2", 1), ("$r1", "$a1", -1)]),
  POLAR, TOL_POLAR, [("Δr", "m"), ("θ", "°")],
  "A delivery drone is <b>$r1 m from its base at $a1°</b>. Later it is <b>$r2 m from the base at $a2°</b>. Find its displacement Δr = r<sub>f</sub> − r<sub>i</sub>.", True)
q("4.3", "Subtracting components", ["Ax", "Ay", "Bx", "By", "s"],
  ["$Ax = rrand(-9,9,0.01) where (abs($Ax) >= 0.5)", "$Ay = rrand(-9,9,0.01) where (abs($Ay) >= 0.5)",
   "$Bx = rrand(-9,9,0.01) where (abs($Bx) >= 0.5)", "$By = rrand(-9,9,0.01) where (abs($By) >= 0.5)", '$s = randfrom("1,-1")',
   "$Rx = $s*($Ax - $Bx)", "$Ry = $s*($Ay - $By)"],
  XY, tol_abs("0.02"), [("R<sub>x</sub>", "m"), ("R<sub>y</sub>", "m")],
  "<b>A = ($Ax î $Ays ĵ) m</b> and <b>B = ($Bx î $Bys ĵ) m</b>. Find the x and y components of <b>R = $op</b>.", False,
  signed("Ay") + signed("By") + ['$op = "A − B"', '$op = "B − A" if ($s < 0)'])
q("4.4", "Racquetball rebound", ["v", "al"],
  ["$v = rand(20,60)", "$al = rand(15,75)"],
  ["$answer[0] = 2*$v*sin($al*$rad)", "$answer[1] = 180"],
  TOL_POLAR, [("Δv", "m/s"), ("θ", "°")],
  "A racquetball moving at <b>$v m/s</b> hits a wall on its right at <b>$al°</b> to the wall. It rebounds at the same speed and the same $al° angle to the wall. Find the change in velocity Δv = v<sub>f</sub> − v<sub>i</sub>.", True)
q("4.5", "Rounding the corner", ["v1", "v2", "af"],
  ["$v1 = rrand(3,8,0.5)", "$v2 = rrand(3,8,0.5)", '$af = randfrom("45,60,90,120,135")'] + sums([("$v2", "$af", 1), ("$v1", "0", -1)]),
  POLAR, TOL_POLAR, [("Δv", "m/s"), ("θ", "°")],
  "A runner moving <b>east at $v1 m/s</b> rounds a corner and ends up moving at <b>$v2 m/s at $af°</b>. Find the change in velocity Δv = v<sub>f</sub> − v<sub>i</sub>.", True)

assert len(Q) == 20

HEAD = f"""# MyOpenMath code for the Vector Range

Twenty two-part questions built from the Lecture 3 and Lecture 4 vector examples. MyOpenMath picks the
numbers and grades the answer. The simulation inside the question uses the same numbers.

Simulation: {SITE}

## Making a question

1. **Manage Question Set → Add New Question**, and set **Question type** to **Multipart**.
2. Paste **Common Control** into Common Control. Its first line sets both parts as Number answers.
3. Paste **Question Text** and **Detailed Solution** into their fields, using the editor's source/HTML view.
4. Save, then **Test** a few versions: submit one right and one wrong answer and watch the simulation.

## What students see

- **Before answering:** the given vectors are drawn tail-to-tail from the origin. They slide tip-to-tail and
  a target appears at the end of the chain. The grid numbers are hidden.
- **After submitting:** the same run, then the student's own vector is drawn from the origin. For
  x/y answers it's drawn as an x step, then a y step. It ends with ON TARGET or MISS, and each part is
  labeled OK, too large, too small, or too far clockwise/counterclockwise. The correct values are never shown.
- **Detailed Solution:** the target run plus the correct resultant, labeled with its values.

## Tolerances

- Magnitudes: within 2% (`$reltolerance[0] = 0.02`).
- Directions: within 1° (`$abstolerance[1] = 1`). The random numbers are picked so no answer falls within a
  degree of 0°/360°. That way a student is never marked wrong for writing 359.6° instead of −0.4°.
- Components: within a small fixed amount scaled to the problem (for example `0.015*$F`), so a component
  near zero is still graded fairly.

If a tolerance line is rejected, MyOpenMath may want the per-part settings written another way. Check
its help on multipart tolerances. The answers themselves don't depend on these lines.

Students answer directions as standard angles (counterclockwise from +x). The problems give some angles in
compass form (e.g. 35° N of W), as in Lecture 3, so converting is part of the work.

---
"""


def block(d):
    code, name, keys = d["code"], d["name"], d["keys"]
    qs = "&".join(f"{k}=${k}" for k in keys)
    show = f"{SITE}?q={code}&{qs}&mode=show"
    sol = f"{SITE}?q={code}&{qs}&mode=solution"
    ctl = ['$anstypes = "number,number"', RAD] + d["gen"] + d["ans"] + d["tol"] + d["show"] + [
        "$stua0 = getstuans($stuanswers, $thisq, 0)",
        "$stua1 = getstuans($stuanswers, $thisq, 1)",
        f'$simurl = "{show}"',
        '$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")',
    ]
    (s0, u0), (s1, u1) = d["parts"]
    note = f"<p>{DIR_NOTE}</p>\n" if d["polar"] else ""
    if d["polar"]:
        ask = f"<p>{s0} = $answerbox[0] {u0} &nbsp; at &nbsp; θ = $answerbox[1] °</p>"
    else:
        ask = f"<p>{s0} = $answerbox[0] {u0}</p>\n<p>{s1} = $answerbox[1] {u1}</p>"
    frame = ('<div style="max-width:820px">\n'
             '<iframe src="{src}" title="Vector Range: {name}{extra}" loading="lazy" '
             'style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>\n'
             '<p style="font-size:85%">{cap} <a href="{src}" target="_blank" rel="noopener">Open in a new tab</a></p>\n'
             '</div>')
    text = (frame.format(src="$simurl", name=name, extra="", cap="The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay.")
            + f"\n<p>{d['story']}</p>\n{note}<p>Use three significant figures.</p>\n{ask}")
    soln = ("<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>\n"
            + frame.format(src=sol, name=name, extra=", solution", cap=""))
    return (f"## {code} · {name}\n\n"
            f"Variables passed to the simulation: `{', '.join(keys)}`\n\n"
            f"**Common Control**\n\n```\n" + "\n".join(ctl) + "\n```\n\n"
            f"**Question Text**\n\n```html\n{text}\n```\n\n"
            f"**Detailed Solution**\n\n```html\n{soln}\n```\n\n---\n")


out = HEAD + "\n".join(block(d) for d in Q)
out = fix_after_vars(out)
Path(__file__).with_name("vectors-myopenmath.md").write_text(out, encoding="utf-8")
print(f"wrote {len(Q)} questions")

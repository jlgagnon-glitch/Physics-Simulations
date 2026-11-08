"""Builds motion-graphs-myopenmath.md: MyOpenMath code for the 20 Motion Graphs Lab questions (Lecture 6).

Each question is a single Number answer. MyOpenMath picks the graph's numbers and grades the answer; the
simulation inside the question draws that exact graph and runs the cart. Run:  python3 build_graphs_myopenmath.py
"""
import re
from pathlib import Path

SITE = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html"


def fix_after_vars(text):
    """MyOpenMath reads special characters such as ° as part of a variable name. Refuse any right after a variable."""
    text = re.sub(r'(\$\w+)°', r'\1&deg;', text)
    bad = re.findall(r'\$\w+[^\x00-\x7f]', text)
    assert not bad, f'special character right after a variable: {bad}'
    return text


# the four graph shapes: MyOpenMath lines that draw the same numbers as the simulation, and the link keys
SHAPES = {
    "X1": (["$a = rand(0,2)", "$b = $a + rand(2,4)", "$c = $b - rand(3,5) where ($c != $a && $b + $c != 0)", "$d = $c + rand(1,2)"],
           ["a", "b", "c", "d"]),
    "X2": (["$v2 = rand(2,4)", '$s1 = randfrom("0,0.5,1")', "$x4 = $v2 + 2*$s1", "$x6 = $x4 - rand(5,8) where ($x6 != 0)",
            "$x8 = $x6 + rand(1,2) where ($x6 + $x8 != 0)"],
           ["v2", "s1", "x6", "x8"]),
    "V1": (["$q = rand(1,2)", "$p = $q + rand(1,2)", "$r = $q + rand(1,3)"], ["p", "q", "r"]),
    # whole-number slopes k1 and k2, so every corner and zero crossing is on a whole or half second
    "V2": (["$q = rand(1,3)", "$m = rand(1,3)",
            '$k1 = randfrom("1,2") where (($q + $m)/$k1 <= 3)',
            '$k2 = randfrom("1,2") where (2*$k2 > $m)',
            "$n = 2*$k2 - $m", "$tB = 2 + ($q + $m)/$k1",
            "$p = rand($q+1,5) where (($p + $q)/2 + $q + ($q - $m)*($tB - 2)/2 - $m*(6 - $tB) + ($n - $m) != 0)"],
           ["q", "m", "k1", "k2", "p"]),
}
XQ = "Use the cart's <b>position vs. time</b> graph."
VQ = "Use the cart's <b>velocity vs. time</b> graph."

# code, name, shape, answer expression, answer label, unit, question
QS = [
    ("1.1", "Reading position", "X1", "($b + $c)/2", "x", "m", f"{XQ} What is the cart's position at <b>t = 4.5 s</b>?"),
    ("1.2", "Velocity from slope", "X1", "($b - $a)/2", "v", "m/s", f"{XQ} What is the cart's velocity at <b>t = 1 s</b>?"),
    ("1.3", "Greatest speed", "X1", "$b - $c", "speed", "m/s", f"{XQ} What is the cart's greatest speed during the 8 s?"),
    ("1.4", "Average velocity", "X1", "($c - $a)/5", "v<sub>ave</sub>", "m/s", f"{XQ} What is the cart's average velocity from <b>t = 0 s</b> to <b>t = 5 s</b>?"),
    ("1.5", "Total distance", "X1", "($b - $a) + ($b - $c) + ($d - $c)", "d", "m", f"{XQ} What total distance does the cart travel from <b>t = 0 s</b> to <b>t = 8 s</b>?"),
    ("2.1", "Tangent line", "X2", "$v2/2", "v", "m/s", f"{XQ} The dashed line is tangent to the curve at <b>t = 1 s</b>. What is the cart's velocity at t = 1 s?"),
    ("2.2", "Straight-line velocity", "X2", "($x6 - $x4)/2", "v", "m/s", f"{XQ} What is the cart's velocity at <b>t = 5 s</b>?"),
    ("2.3", "Average velocity", "X2", "$x6/6", "v<sub>ave</sub>", "m/s", f"{XQ} What is the cart's average velocity from <b>t = 0 s</b> to <b>t = 6 s</b>?"),
    ("2.4", "Reading position", "X2", "($x6 + $x8)/2", "x", "m", f"{XQ} What is the cart's position at <b>t = 7 s</b>?"),
    ("2.5", "Acceleration from a curve", "X2", "$v2/2", "a", "m/s²", f"{XQ} The cart starts from rest and speeds up steadily from 0 to 2 s, reaching the position shown at t = 2 s. What is its acceleration during those 2 s?"),
    ("3.1", "Reading velocity", "V1", "($q + $r)/2", "v", "m/s", f"{VQ} What is the cart's velocity at <b>t = 4 s</b>?"),
    ("3.2", "Acceleration from slope", "V1", "-$r/2", "a", "m/s²", f"{VQ} What is the cart's acceleration at <b>t = 6 s</b>?"),
    ("3.3", "Displacement as area", "V1", "($p + $q)/2 + 2*$q + ($q + $r)", "Δx", "m", f"{VQ} What is the cart's displacement from <b>t = 0 s</b> to <b>t = 5 s</b>?"),
    ("3.4", "Greatest acceleration", "V1", "($r - $q)/2", "a", "m/s²", f"{VQ} What is the cart's greatest positive acceleration?"),
    ("3.5", "Whole-trip displacement", "V1", "($p + $q)/2 + 2*$q + ($q + $r) + $r", "Δx", "m", f"{VQ} What is the cart's displacement from <b>t = 0 s</b> to <b>t = 8 s</b>?"),
    ("4.1", "Momentarily at rest", "V2", "2 + $q/$k1", "t", "s", f"{VQ} At what time does the cart first come to rest (for an instant)?"),
    ("4.2", "Turning around", "V2", "-$k1", "a", "m/s²", f"{VQ} What is the cart's acceleration at <b>t = 2.5 s</b>?"),
    ("4.3", "Negative area", "V2", "($p + $q)/2 + $q + ($q - $m)*($tB - 2)/2 - $m*(6 - $tB) + ($n - $m)", "Δx", "m", f"{VQ} What is the cart's displacement from <b>t = 0 s</b> to <b>t = 8 s</b>?"),
    ("4.4", "Total distance", "V2", "($p + $q)/2 + $q + $q*$q/(2*$k1) + $m*$m/(2*$k1) + $m*(6 - $tB) + $m*$m/(2*$k2) + $n*(2 - $m/$k2)/2", "d", "m", f"{VQ} What total distance does the cart travel from <b>t = 0 s</b> to <b>t = 8 s</b>?"),
    ("4.5", "Average acceleration", "V2", "(-$m - $p)/6", "a<sub>ave</sub>", "m/s²", f"{VQ} What is the cart's average acceleration from <b>t = 0 s</b> to <b>t = 6 s</b>?"),
]
assert len(QS) == 20

HEAD = f"""# MyOpenMath code for the Motion Graphs Lab

Twenty questions built from the Lecture 6 examples (graphical interpretation of motion). Each one shows a
cart on a lab track with a motion detector, and its position-vs-time or velocity-vs-time graph underneath.
MyOpenMath picks the graph's numbers and grades the answer, and the simulation draws that exact graph.

Simulation: {SITE}

## Making a question

1. **Manage Question Set → Add New Question**, and set **Question type** to **Number**.
2. Paste **Common Control** into Common Control.
3. Paste **Question Text** and **Detailed Solution** into their fields, using the editor's source/HTML view.
4. Save, then **Test**: submit one right and one wrong answer.

## The graph lives in the simulation

These questions are about reading a graph, and **the graph is drawn only by the simulation**, so students
need the embedded picture to answer. If MyOpenMath ever blocks the embed, the "Open in a new tab" link under
it opens the same graph.

## What students see

- **Before answering:** the cart runs for 8 s while a cursor sweeps across the graph. Ghost images mark
  each whole second, and an arrow shows the velocity's direction. No values are shown beyond what the graph
  itself shows.
- **After submitting:** the run, then the student's answer drawn on the graph: a point, a slope line, an
  average-velocity chord, a time marker, or (for displacement and distance) a mark on the track or the
  odometer. It ends with CORRECT or NOT QUITE ("too large" or "too small"), without the correct value.
- **Detailed Solution:** the run, then the correct answer drawn and labeled.

Answers are graded within 2% (`$reltolerance = 0.02`). The random numbers are picked so no answer is
zero, which would make a percentage tolerance meaningless.

---
"""


def block(code, name, shape, expr, sym, unit, question):
    gen, keys = SHAPES[shape]
    qs = "&".join(f"{k}=${k}" for k in keys)
    show = f"{SITE}?level={code}&{qs}&mode=show"
    sol = f"{SITE}?level={code}&{qs}&mode=solution"
    ctl = gen + [f"$answer = {expr}", "$reltolerance = 0.02",
                 "$stua = getstuans($stuanswers, $thisq)",
                 f'$simurl = "{show}"',
                 '$simurl = $simurl . "&launch=$stua" if ($stua != "")']
    frame = ('<div style="max-width:820px">\n'
             '<iframe src="{src}" title="Motion Graphs Lab: {name}{extra}" loading="lazy" '
             'style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>\n'
             '<p style="font-size:85%">{cap} <a href="{src}" target="_blank" rel="noopener">Open in a new tab</a></p>\n'
             '</div>')
    text = (frame.format(src="$simurl", name=name, extra="", cap="Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay.")
            + f"\n<p>{question}</p>\n<p>Use three significant figures.</p>\n<p>{sym} = $answerbox {unit}</p>")
    soln = ("<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>\n"
            + frame.format(src=sol, name=name, extra=", solution", cap=""))
    return (f"## {code} · {name}\n\n"
            f"Graph: {shape} · Variables passed to the simulation: `{', '.join(keys)}`\n\n"
            f"**Common Control**\n\n```\n" + "\n".join(ctl) + "\n```\n\n"
            f"**Question Text**\n\n```html\n{text}\n```\n\n"
            f"**Detailed Solution**\n\n```html\n{soln}\n```\n\n---\n")


out = fix_after_vars(HEAD + "\n".join(block(*q) for q in QS))
Path(__file__).with_name("motion-graphs-myopenmath.md").write_text(out, encoding="utf-8")
print(f"wrote {len(QS)} questions")

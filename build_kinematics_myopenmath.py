"""Builds kinematics-myopenmath.md: MyOpenMath code for the 20 Constant Acceleration Lab questions (Lecture 7).

Each question is a single Number answer. MyOpenMath picks the numbers and grades the answer; the simulation
inside the question runs that exact motion. Run:  python3 build_kinematics_myopenmath.py
"""
import re
from pathlib import Path

SITE = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html"


def fix_after_vars(text):
    """MyOpenMath reads special characters such as ° or ² as part of a variable name. Refuse any right after a variable."""
    text = re.sub(r'(\$\w+)°', r'\1&deg;', text)
    bad = re.findall(r'\$\w+[^\x00-\x7f]', text)
    assert not bad, f'special character right after a variable: {bad}'
    return text


RUNNER = (["$v0 = rrand(1,3,0.5)", "$a = rrand(0.5,2,0.1)", "$t = rand(2,5)"], ["v0", "a", "t"])
RUNNER_TO = (["$v0 = rrand(1,3,0.5)", "$a = rrand(0.5,2,0.1)", "$vf = $v0 + rrand(2,5,0.5)"], ["v0", "a", "vf"])
CAR = (["$v0 = rand(20,35)", "$a = -rand(2,5)", "$t = rand(2,4) where ($v0 + $a*$t > 0)"], ["v0", "a", "t"])
DEER = (["$a = -rrand(3,5,0.1)", "$D = rand(18,40)", "$v0 = rrand(9,16,0.1) where ($v0*$v0/(-2*$a) < $D - 1)"], ["a", "D", "v0"])
TWO = (["$a1 = rrand(1.5,3,0.5)", "$t1 = rand(4,6)", "$a2 = -rrand(1,3,0.5) where ($a1*$t1 + $a2*4 > 0.5)", "$t2 = rand(2,4)"], ["a1", "t1", "a2", "t2"])
PUCK = (["$v0 = rand(20,35)", "$a = -rrand(0.3,0.8,0.1)", "$D = rand(25,45)", "$t = rrand(1,1.5,0.05)"], ["v0", "a", "D", "t"])
BALL = (["$v0 = rrand(10,30,0.5)"], ["v0"])
# realistic bars: 1.80-2.40 m (the world record is 2.45 m), within 15 cm of the jumper's peak
JUMP = (["$v0 = rrand(4,5,0.1)", "$yi = rrand(1,1.2,0.05)", "$bar = rrand(1.8,2.4,0.05) where (abs($bar - ($yi + $v0*$v0/19.6)) <= 0.15)"], ["v0", "yi", "bar"])

# code, name, numbers, answer expression, answer label, unit, question text (MyOpenMath variables)
QS = [
    ("1.1", "Runner: final velocity", RUNNER, "$v0 + $a*$t", "v", "m/s",
     "A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> for <b>$t s</b>. What is the runner's velocity at the end of this time?"),
    ("1.2", "Runner: distance", RUNNER, "$v0*$t + 0.5*$a*$t*$t", "Δx", "m",
     "A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> for <b>$t s</b>. What distance does the runner cover in this time?"),
    ("1.3", "Runner: time to top speed", RUNNER_TO, "($vf - $v0)/$a", "Δt", "s",
     "A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> until reaching <b>$vf m/s</b>. How long does this take?"),
    ("1.4", "Runner: distance to top speed", RUNNER_TO, "($vf*$vf - $v0*$v0)/(2*$a)", "Δx", "m",
     "A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> until reaching <b>$vf m/s</b>. How far does the runner travel while speeding up?"),
    ("1.5", "Sprint from the blocks", (["$a = rrand(1,2.5,0.1)", "$D = rand(10,25)"], ["a", "D"]), "sqrt(2*$a*$D)", "v", "m/s",
     "A sprinter starts from rest and accelerates at a constant <b>$a m/s<sup>2</sup></b> over the first <b>$D m</b>. How fast is the sprinter running at the $D m mark?"),
    ("2.1", "Braking car: velocity", CAR, "$v0 + $a*$t", "v", "m/s",
     "A car moving at <b>$v0 m/s</b> brakes with a constant acceleration of <b>$a m/s<sup>2</sup></b>. What is its velocity after <b>$t s</b> of braking?"),
    ("2.2", "Braking car: distance", CAR, "$v0*$t + 0.5*$a*$t*$t", "Δx", "m",
     "A car moving at <b>$v0 m/s</b> brakes with a constant acceleration of <b>$a m/s<sup>2</sup></b>. How far does it travel during the first <b>$t s</b> of braking?"),
    ("2.3", "Braking car: time to stop", CAR, "-$v0/$a", "Δt", "s",
     "A car moving at <b>$v0 m/s</b> brakes with a constant acceleration of <b>$a m/s<sup>2</sup></b>. How long does it take the car to come to rest?"),
    ("2.4", "Deer in the headlights", DEER, "$D - $v0*$v0/(-2*$a)", "d", "m",
     "A park ranger driving at <b>$v0 m/s</b> sees a deer <b>$D m</b> ahead and brakes immediately with a constant acceleration of <b>$a m/s<sup>2</sup></b>. How close does the ranger come to hitting the deer?"),
    ("2.5", "Brake hard enough", (["$D = rand(18,40)", "$v0 = rrand(9,16,0.1)"], ["D", "v0"]), "-$v0*$v0/(2*$D)", "a", "m/s<sup>2</sup>",
     "A ranger driving at <b>$v0 m/s</b> sees a deer <b>$D m</b> ahead. What constant acceleration would stop the vehicle exactly at the deer? (Include the sign.)"),
    ("3.1", "Speed up, then brake: speed", TWO, "$a1*$t1 + $a2*$t2", "v", "m/s",
     "A car starts from rest and speeds up at <b>$a1 m/s<sup>2</sup></b> for <b>$t1 s</b>. The driver then brakes at <b>$a2 m/s<sup>2</sup></b> for <b>$t2 s</b>. How fast is the car going at the end of the braking?"),
    ("3.2", "Speed up, then brake: distance", TWO, "0.5*$a1*$t1*$t1 + $a1*$t1*$t2 + 0.5*$a2*$t2*$t2", "Δx", "m",
     "A car starts from rest and speeds up at <b>$a1 m/s<sup>2</sup></b> for <b>$t1 s</b>. The driver then brakes at <b>$a2 m/s<sup>2</sup></b> for <b>$t2 s</b>. How far has the car gone in total?"),
    ("3.3", "Beat the buzzer", PUCK, "$v0*$t + 0.5*$a*$t*$t", "Δx", "m",
     "With <b>$t s</b> left in the game, a hockey player shoots the puck at <b>$v0 m/s</b> toward an empty goal <b>$D m</b> away. The ice slows the puck at <b>$a m/s<sup>2</sup></b>. How far does the puck slide before the buzzer (ignore the goal)?"),
    ("3.4", "Puck: speed at the goal", PUCK, "sqrt($v0*$v0 + 2*$a*$D)", "v", "m/s",
     "A hockey puck leaves the stick at <b>$v0 m/s</b> toward a goal <b>$D m</b> away. The ice slows it at <b>$a m/s<sup>2</sup></b>. How fast is the puck moving when it reaches the goal?"),
    ("3.5", "Puck: time to the goal", PUCK, "($v0 - sqrt($v0*$v0 + 2*$a*$D))/(-$a)", "Δt", "s",
     "A hockey puck leaves the stick at <b>$v0 m/s</b> toward a goal <b>$D m</b> away. The ice slows it at <b>$a m/s<sup>2</sup></b>. How long does the puck take to reach the goal?"),
    ("4.1", "Ball thrown up: height", BALL, "$v0*$v0/(2*9.8)", "Δy", "m",
     "A ball is thrown straight up at <b>$v0 m/s</b>. How high above the release point does it rise?"),
    ("4.2", "Ball thrown up: time of flight", BALL, "2*$v0/9.8", "Δt", "s",
     "A ball is thrown straight up at <b>$v0 m/s</b>. How long is it in the air before it comes back down to the height it was released from?"),
    ("4.3", "Caught on the way down", (["$T = rrand(1,4,0.1)"], ["T"]), "9.8*$T/2", "v<sub>0</sub>", "m/s",
     "A ball thrown straight up is caught by the thrower, at the same height, <b>$T s</b> later. With what speed was it thrown?"),
    ("4.4", "High jump: peak height", JUMP, "$yi + $v0*$v0/(2*9.8)", "y<sub>peak</sub>", "m",
     "At takeoff a high jumper's center of gravity is <b>$yi m</b> high and moving straight up at <b>$v0 m/s</b>. The bar is at <b>$bar m</b>. How high does the center of gravity rise (height above the ground)?"),
    ("4.5", "High jump: time to peak", JUMP, "$v0/9.8", "Δt", "s",
     "At takeoff a high jumper's center of gravity is <b>$yi m</b> high and moving straight up at <b>$v0 m/s</b>. How long after takeoff does it reach its peak?"),
]
assert len(QS) == 20

HEAD = f"""# MyOpenMath code for the Constant Acceleration Lab

Twenty questions built from the Lecture 7 examples: the runner, the braking car, the ranger and the deer,
the two-stage car, the hockey puck, the ball thrown up and the high jumper. MyOpenMath picks the numbers
and grades the answer. The simulation inside the question runs that exact motion.

Simulation: {SITE}

## Making a question

1. **Manage Question Set → Add New Question**, and set **Question type** to **Number**.
2. Paste **Common Control** into Common Control.
3. Paste **Question Text** and **Detailed Solution** into their fields, using the editor's source/HTML view.
4. Save, then **Test**: submit one right and one wrong answer.

## What students see

- **Before answering:** the motion plays out in its scene, with a speedometer dial and a stopwatch. Whatever
  would give the answer away stays blank: the distance markers for distance and height questions, the
  dial numbers for speed questions, the stopwatch for time questions.
- **After submitting:** the run, then the student's answer in the scene. That's a flag where they predict the
  car stops, a dashed needle on the speedometer, a ghost of the object at their predicted time, or a line at
  their predicted height. Two questions replay the motion with the student's own value: 2.5 (their braking
  rate, which stops short or hits the deer) and 4.3 (their throwing speed, which brings the ball back early
  or late). It ends with CORRECT or NOT QUITE, without the correct value.
- **Detailed Solution:** the run with every readout showing, and the correct answer labeled.

Answers are graded within 2% (`$reltolerance = 0.02`). g = 9.80 m/s², as in the lecture. Question 2.5 expects
a negative acceleration ("include the sign" is in the question).

---
"""


def block(code, name, nums, expr, sym, unit, question):
    gen, keys = nums
    qs = "&".join(f"{k}=${k}" for k in keys)
    show = f"{SITE}?level={code}&{qs}&mode=show"
    sol = f"{SITE}?level={code}&{qs}&mode=solution"
    ctl = gen + [f"$answer = {expr}", "$reltolerance = 0.02",
                 "$stua = getstuans($stuanswers, $thisq)",
                 f'$simurl = "{show}"',
                 '$simurl = $simurl . "&launch=$stua" if ($stua != "")']
    frame = ('<div style="max-width:820px">\n'
             '<iframe src="{src}" title="Constant Acceleration Lab: {name}{extra}" loading="lazy" '
             'style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>\n'
             '<p style="font-size:85%">{cap} <a href="{src}" target="_blank" rel="noopener">Open in a new tab</a></p>\n'
             '</div>')
    text = (frame.format(src="$simurl", name=name, extra="", cap="Watch the motion. After you submit, your answer appears in the scene. Tap to replay.")
            + f"\n<p>{question}</p>\n<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>\n<p>{sym} = $answerbox {unit}</p>")
    soln = ("<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>\n"
            + frame.format(src=sol, name=name, extra=", solution", cap=""))
    return (f"## {code} · {name}\n\n"
            f"Variables passed to the simulation: `{', '.join(keys)}`\n\n"
            f"**Common Control**\n\n```\n" + "\n".join(ctl) + "\n```\n\n"
            f"**Question Text**\n\n```html\n{text}\n```\n\n"
            f"**Detailed Solution**\n\n```html\n{soln}\n```\n\n---\n")


out = fix_after_vars(HEAD + "\n".join(block(*q) for q in QS))
Path(__file__).with_name("kinematics-myopenmath.md").write_text(out, encoding="utf-8")
print(f"wrote {len(QS)} questions")

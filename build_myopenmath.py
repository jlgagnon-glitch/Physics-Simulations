"""Builds proving-ground-myopenmath.md: MyOpenMath question code for all 16 Proving Ground levels.

Each level lists its MyOpenMath Common Control code, the variables passed to the simulation,
and the problem statement (same wording as the simulation). Run:  python3 build_myopenmath.py
"""
from pathlib import Path

SITE = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html"
RAD = "$rad = 3.141592653589793/180"

L = [
 ("1.1", "Off the bench", ["h", "d"], "v", "m/s", "launch speed", [
   "$h = rrand(0.8,1.6,0.1)", "$d = rrand(1.5,3.5,0.1)",
   "$answer = $d*sqrt(9.8/(2*$h))"],
  "A pusher starts a ball from rest and rolls it along a bench $h m high, letting go at the edge. The landing pad is $d m from the edge. What speed must the ball leave the bench with?"),
 ("1.2", "Stop on the line", ["v", "d"], "a", "m/s²", "braking rate (magnitude)", [
   "$v = rand(8,20)", "$d = rand(12,40)",
   "$answer = $v*$v/(2*$d)"],
  "A test cart reaches the brake zone at $v m/s. It has to stop $d m later, right on the line. How hard must it brake?"),
 ("1.3", "Fixed angle", ["th", "R"], "v", "m/s", "launch speed", [
   RAD, '$th = randfrom("30,40,50,60")', "$R = rand(8,20)",
   "$answer = sqrt($R*9.8/sin(2*$th*$rad))"],
  "A launcher is locked at $th° above level ground. The target is $R m away at launcher height. What launch speed reaches it?"),
 ("1.4", "Lead the cart", ["u", "x0", "v", "h"], "t", "s", "release delay", [
   "$x0 = rand(5,10)", "$v = rrand(1,3,0.5)", "$h = rand(3,6)", "$tf = sqrt(2*$h/9.8)",
   "$u = rrand(1.5,3,0.5) where (($x0+$v*$tf)/$u - $tf > 0.8)",
   "$answer = ($x0+$v*$tf)/$u - $tf"],
  "A cart rolls right at $u m/s, starting $x0 m left of a tower's base. From the top of the tower, $h m up, a ball is launched to the right at $v m/s. How long after the cart starts should you release the ball so it lands in the cart?"),
 ("2.1", "Skid to the mark", ["mu", "d"], "v", "m/s", "starting speed", [
   "$mu = rrand(0.15,0.5,0.05)", "$d = rand(4,15)",
   "$answer = sqrt(2*$mu*9.8*$d)"],
  "A sled slides across a floor with friction coefficient μ = $mu. It has to stop $d m from the start. What speed should it begin with?"),
 ("2.2", "Steady up the ramp", ["m", "th", "mu", "v0"], "F", "N", "rope force", [
   RAD, "$m = rrand(10,40,5)", '$th = randfrom("15,20,25,30,35")', "$mu = rrand(0.1,0.4,0.05)", "$v0 = rrand(1,2,0.5)",
   "$answer = $m*9.8*(sin($th*$rad) + $mu*cos($th*$rad))"],
  "A $m kg crate enters a $th° ramp at $v0 m/s. The ramp has friction coefficient μ = $mu. What rope force, parallel to the ramp, keeps the crate moving at constant speed all the way up?"),
 ("2.3", "Hanging counterweight", ["m", "d", "t"], "M", "kg", "hanging mass", [
   "$m = rrand(1,4,0.5)", "$d = rrand(1.2,2,0.2)", "$t = rrand(1.2,2,0.2)", "$a = 2*$d/($t*$t)",
   "$answer = $m*$a/(9.8-$a)"],
  "A $m kg cart on a frictionless track is tied over a pulley to a hanging mass. Released from rest, the cart must travel $d m in exactly $t s. What hanging mass does that take?"),
 ("2.4", "Up to the latch", ["th", "mu", "L"], "v", "m/s", "starting speed", [
   RAD, '$th = randfrom("15,20,25,30")', "$mu = rrand(0.1,0.3,0.05)", "$L = rand(2,5)",
   "$answer = sqrt(2*9.8*(sin($th*$rad) + $mu*cos($th*$rad))*$L)"],
  "A puck is shot up a $th° ramp with friction coefficient μ = $mu. A latch $L m along the ramp catches it only if it stops right there. What starting speed does it need?"),
 ("3.1", "Spring to the summit", ["m", "k", "h"], "x", "m", "spring compression", [
   "$m = rrand(0.5,2,0.5)", "$k = rrand(200,800,100)", "$h = rrand(0.8,2.2,0.2)",
   "$answer = sqrt(2*$m*9.8*$h/$k)"],
  "A $m kg cart sits against a spring with k = $k N/m. The track is frictionless and climbs to a stop at $h m height. How far should you compress the spring so the cart just reaches that height?"),
 ("3.2", "Spring meets carpet", ["m", "k", "mu", "d"], "x", "m", "spring compression", [
   "$m = rrand(0.5,2,0.5)", "$k = rrand(200,800,100)", "$mu = rrand(0.2,0.5,0.1)", "$d = rrand(1,3,0.5)",
   "$answer = sqrt(2*$mu*$m*9.8*$d/$k)"],
  "A $m kg block is pushed against a spring with k = $k N/m on a frictionless surface. It then slides onto carpet with μ = $mu and has to stop $d m into the carpet. How far should you compress the spring?"),
 ("3.3", "Stick and climb", ["m1", "m2", "h"], "v", "m/s", "speed of cart A", [
   "$m1 = rrand(1,4,0.5)", "$m2 = rrand(1,4,0.5)", "$h = rrand(0.5,1.5,0.1)",
   "$answer = ($m1+$m2)/$m1*sqrt(2*9.8*$h)"],
  "Cart A ($m1 kg) hits parked cart B ($m2 kg) and they lock together. The pair then coasts up a frictionless hill. They must reach exactly $h m height. How fast must cart A go before the crash?"),
 ("3.4", "Knock it off the edge", ["m1", "m2", "H", "d"], "v", "m/s", "speed of ball A", [
   "$m1 = rrand(0.5,2,0.5)", "$m2 = rrand(0.5,2,0.5)", "$H = rrand(0.8,1.4,0.2)", "$d = rrand(1,2.5,0.5)",
   "$answer = $d*sqrt(9.8/(2*$H))*($m1+$m2)/(2*$m1)"],
  "Ball A ($m1 kg) hits ball B ($m2 kg) in a perfectly elastic head-on collision. Ball B sits at the edge of a table $H m high and must land $d m from the edge. How fast must ball A be going?"),
 ("4.1", "Level the seesaw", ["m1", "d1", "m2"], "x", "m", "distance from the pivot", [
   "$m1 = rrand(10,40,5)", "$d1 = rrand(0.6,1.6,0.2)",
   "$m2 = rrand(10,40,5) where ($m2 != $m1 && $m1*$d1/$m2 < 2.2 && $m1*$d1/$m2 > 0.3)",
   "$answer = $m1*$d1/$m2"],
  "A $m1 kg load sits $d1 m left of a seesaw's pivot. Where, measured from the pivot, must a $m2 kg load go on the right side so the beam balances?"),
 ("4.2", "The heavy beam", ["L", "M", "p", "m"], "x", "m", "distance from the pivot", [
   "$L = rand(4,6)", "$M = rrand(10,30,5)",
   "$p = rrand(1,$L/2-0.4,0.2) where ($M*($L/2-$p) < 36*$p && $M*($L/2-$p) > 4.5)",
   "$arm = $L/2 - $p",
   "$m = rrand(15,40,5) where ($M*$arm/$m > 0.3 && $M*$arm/$m < 0.9*$p)",
   "$answer = $M*$arm/$m"],
  "A uniform $L m beam of $M kg rests on a pivot $p m from its left end, so its long side wants to drop. Where left of the pivot should a $m kg counterweight go to balance it?"),
 ("4.3", "Flywheel launcher", ["I", "r", "t", "H", "d"], "τ", "N·m", "torque", [
   "$I = rrand(0.4,1.2,0.2)", "$r = rrand(0.3,0.5,0.1)", "$t = rrand(1,2,0.5)", "$H = rrand(1.2,2,0.2)", "$d = rand(2,5)",
   "$answer = $I*$d/sqrt(2*$H/9.8)/($r*$t)"],
  "A flywheel with moment of inertia I = $I kg·m² and radius $r m starts from rest and spins up for $t s under constant torque. It then flings a ball horizontally from its top, $H m above the floor. The ball must land $d m away. What torque do you need?"),
 ("4.4", "Rolling start", ["H", "d"], "h", "m", "ramp height", [
   "$H = rrand(0.8,1.4,0.2)", "$d = rrand(0.8,1.8,0.2)", "$v = $d/sqrt(2*$H/9.8)",
   "$answer = 0.75*$v*$v/9.8"],
  "A solid cylinder rolls without slipping down a ramp, then off a table $H m high. It must land $d m from the edge. From what height on the ramp, above the tabletop, should you release it? For a solid cylinder, I = ½mr²."),
]

HEAD = f"""# MyOpenMath code for the Physics Proving Ground

One question per level, 16 in all. In each question MyOpenMath picks the random numbers and grades
the answer. The same numbers go into the simulation's web address, so the picture inside the question
matches the student's own version.

Simulation: {SITE}

## Making a question

1. In MyOpenMath, go to **Manage Question Set → Add New Question**.
2. Set **Question type** to **Number**.
3. Paste the **Common Control** block into Common Control.
4. Paste the **Question Text** block into Question Text. Use the editor's source/HTML view, so the
   `<iframe>` tag stays code instead of becoming text.
5. Paste the **Detailed Solution** block into the Detailed Solution field, also in source/HTML view.
   Students only see it once the answer is revealed. It shows the simulation launching the correct
   answer for their own numbers, and tapping it replays the launch.
6. Save, then **Test** a few versions. Check that the picture shows the same numbers as the text, and
   that the solution launch lands on target.

In the assessment settings, choose when students can see the detailed solution (for example, after
the last try or after the due date). Before then, the question only shows the still picture.

## Settings you may want to change

- `$reltolerance = 0.02` accepts answers within 2% of the exact value. That's enough room for
  three-significant-figure rounding along the way. Use `0.01` to be stricter.
- `mode=solution` (used in the Detailed Solution) shows only the picture and launches the correct
  answer on its own, so put it only where students see it after answering.
- `mode=show` (used in the question) plays the correct launch with every answer value hidden. Once the
  student submits, the last three Common Control lines add their answer to the link (`launch=`), and the
  simulation plays the correct launch and then theirs, with ON TARGET or MISS. Students with several tries
  can use that feedback before trying again. To give no feedback at all, use the still picture instead:
  replace `$simurl` in the Question Text with the same link ending in `mode=test`.
- If the student's launch never appears after submitting, check the `getstuans` line in Common Control.
  It reads the submitted answer, and `$stuanswers[$thisq]` is the older way to write it.
- `mode=test` in the link shows only the picture: no answer box, no Launch button, no feedback.
  To let students launch and watch their own answer before submitting, remove `&mode=test`. To also
  hide the worked solution in that case, add `&solution=0`.
- The `where` clauses re-pick a number until the problem makes sense physically, the same checks the
  simulation itself uses (for example, the counterweight has to fit on the beam).
- g = 9.8 m/s² throughout, matching the simulation.

## Linking the simulation from anywhere else

Any page can open one level with fixed numbers:

`{SITE}?level=1.1&h=1.2&d=2.4&mode=test`

`level` is the button number in the game (1.1 to 4.4); 1 to 16 also works. The other names are the
variables listed for each level below. Any number left out is chosen at random. With no `level` in the
link, the full game opens as usual.

---
"""


def block(code, name, keys, sym, unit, word, control, story):
    q = "&".join(f"{k}=${k}" for k in keys)
    src = f"{SITE}?level={code}&{q}&mode=test"
    show = f"{SITE}?level={code}&{q}&mode=show"
    ctl = "\n".join(control + [
        "$reltolerance = 0.02",
        "$stua = getstuans($stuanswers, $thisq)",
        f'$simurl = "{show}"',
        '$simurl = $simurl . "&launch=$stua" if ($stua != "")',
    ])
    text = (
        f'<div style="max-width:820px">\n'
        f'<iframe src="$simurl" title="Physics Proving Ground: {name}" loading="lazy" '
        f'style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>\n'
        f'<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. '
        f'Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>\n'
        f"</div>\n"
        f"<p>{story}</p>\n"
        f"<p>Use g = 9.8 m/s². Enter the {word} in {unit}, to three significant figures.</p>\n"
        f"<p>{sym} = $answerbox {unit}</p>"
    )
    sol_src = src.replace("mode=test", "mode=solution")
    sol = (
        f'<p>Here is the launch with the correct {word}. Tap the picture to replay it.</p>\n'
        f'<div style="max-width:820px">\n'
        f'<iframe src="{sol_src}" title="Physics Proving Ground: {name}, correct launch" loading="lazy" '
        f'style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>\n'
        f'<p style="font-size:85%"><a href="{sol_src}" target="_blank" rel="noopener">Open the launch in a new tab</a></p>\n'
        f"</div>"
    )
    return (f"## Level {code} · {name}\n\n"
            f"Variables passed to the simulation: `{', '.join(keys)}`\n\n"
            f"**Common Control**\n\n```\n{ctl}\n```\n\n"
            f"**Question Text**\n\n```html\n{text}\n```\n\n"
            f"**Detailed Solution**\n\n```html\n{sol}\n```\n\n---\n")


out = HEAD + "\n".join(block(*lv) for lv in L)
Path(__file__).with_name("proving-ground-myopenmath.md").write_text(out, encoding="utf-8")
print(f"wrote {len(L)} questions")

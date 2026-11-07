# MyOpenMath code for the Physics Proving Ground

One question per level, 16 in all. In each question MyOpenMath picks the random numbers and grades
the answer. The same numbers go into the simulation's web address, so the picture inside the question
matches the student's own version.

Simulation: https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html

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

`https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.1&h=1.2&d=2.4&mode=test`

`level` is the button number in the game (1.1 to 4.4); 1 to 16 also works. The other names are the
variables listed for each level below. Any number left out is chosen at random. With no `level` in the
link, the full game opens as usual.

---
## Level 1.1 · Off the bench

Variables passed to the simulation: `h, d`

**Common Control**

```
$h = rrand(0.8,1.6,0.1)
$d = rrand(1.5,3.5,0.1)
$answer = $d*sqrt(9.8/(2*$h))
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.1&h=$h&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Off the bench" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A pusher starts a ball from rest and rolls it along a bench $h m high, letting go at the edge. The landing pad is $d m from the edge. What speed must the ball leave the bench with?</p>
<p>Use g = 9.8 m/s². Enter the launch speed in m/s, to three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct launch speed. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.1&h=$h&d=$d&mode=solution" title="Physics Proving Ground: Off the bench, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.1&h=$h&d=$d&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 1.2 · Stop on the line

Variables passed to the simulation: `v, d`

**Common Control**

```
$v = rand(8,20)
$d = rand(12,40)
$answer = $v*$v/(2*$d)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.2&v=$v&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Stop on the line" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A test cart reaches the brake zone at $v m/s. It has to stop $d m later, right on the line. How hard must it brake?</p>
<p>Use g = 9.8 m/s². Enter the braking rate (magnitude) in m/s², to three significant figures.</p>
<p>a = $answerbox m/s²</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct braking rate (magnitude). Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.2&v=$v&d=$d&mode=solution" title="Physics Proving Ground: Stop on the line, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.2&v=$v&d=$d&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 1.3 · Fixed angle

Variables passed to the simulation: `th, R`

**Common Control**

```
$rad = 3.141592653589793/180
$th = randfrom("30,40,50,60")
$R = rand(8,20)
$answer = sqrt($R*9.8/sin(2*$th*$rad))
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.3&th=$th&R=$R&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Fixed angle" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A launcher is locked at $th° above level ground. The target is $R m away at launcher height. What launch speed reaches it?</p>
<p>Use g = 9.8 m/s². Enter the launch speed in m/s, to three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct launch speed. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.3&th=$th&R=$R&mode=solution" title="Physics Proving Ground: Fixed angle, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.3&th=$th&R=$R&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 1.4 · Lead the cart

Variables passed to the simulation: `u, x0, v, h`

**Common Control**

```
$x0 = rand(5,10)
$v = rrand(1,3,0.5)
$h = rand(3,6)
$tf = sqrt(2*$h/9.8)
$u = rrand(1.5,3,0.5) where (($x0+$v*$tf)/$u - $tf > 0.8)
$answer = ($x0+$v*$tf)/$u - $tf
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.4&u=$u&x0=$x0&v=$v&h=$h&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Lead the cart" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A cart rolls right at $u m/s, starting $x0 m left of a tower's base. From the top of the tower, $h m up, a ball is launched to the right at $v m/s. How long after the cart starts should you release the ball so it lands in the cart?</p>
<p>Use g = 9.8 m/s². Enter the release delay in s, to three significant figures.</p>
<p>t = $answerbox s</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct release delay. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.4&u=$u&x0=$x0&v=$v&h=$h&mode=solution" title="Physics Proving Ground: Lead the cart, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=1.4&u=$u&x0=$x0&v=$v&h=$h&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 2.1 · Skid to the mark

Variables passed to the simulation: `mu, d`

**Common Control**

```
$mu = rrand(0.15,0.5,0.05)
$d = rand(4,15)
$answer = sqrt(2*$mu*9.8*$d)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.1&mu=$mu&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Skid to the mark" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A sled slides across a floor with friction coefficient μ = $mu. It has to stop $d m from the start. What speed should it begin with?</p>
<p>Use g = 9.8 m/s². Enter the starting speed in m/s, to three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct starting speed. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.1&mu=$mu&d=$d&mode=solution" title="Physics Proving Ground: Skid to the mark, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.1&mu=$mu&d=$d&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 2.2 · Steady up the ramp

Variables passed to the simulation: `m, th, mu, v0`

**Common Control**

```
$rad = 3.141592653589793/180
$m = rrand(10,40,5)
$th = randfrom("15,20,25,30,35")
$mu = rrand(0.1,0.4,0.05)
$v0 = rrand(1,2,0.5)
$answer = $m*9.8*(sin($th*$rad) + $mu*cos($th*$rad))
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.2&m=$m&th=$th&mu=$mu&v0=$v0&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Steady up the ramp" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A $m kg crate enters a $th° ramp at $v0 m/s. The ramp has friction coefficient μ = $mu. What rope force, parallel to the ramp, keeps the crate moving at constant speed all the way up?</p>
<p>Use g = 9.8 m/s². Enter the rope force in N, to three significant figures.</p>
<p>F = $answerbox N</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct rope force. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.2&m=$m&th=$th&mu=$mu&v0=$v0&mode=solution" title="Physics Proving Ground: Steady up the ramp, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.2&m=$m&th=$th&mu=$mu&v0=$v0&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 2.3 · Hanging counterweight

Variables passed to the simulation: `m, d, t`

**Common Control**

```
$m = rrand(1,4,0.5)
$d = rrand(1.2,2,0.2)
$t = rrand(1.2,2,0.2)
$a = 2*$d/($t*$t)
$answer = $m*$a/(9.8-$a)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.3&m=$m&d=$d&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Hanging counterweight" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A $m kg cart on a frictionless track is tied over a pulley to a hanging mass. Released from rest, the cart must travel $d m in exactly $t s. What hanging mass does that take?</p>
<p>Use g = 9.8 m/s². Enter the hanging mass in kg, to three significant figures.</p>
<p>M = $answerbox kg</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct hanging mass. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.3&m=$m&d=$d&t=$t&mode=solution" title="Physics Proving Ground: Hanging counterweight, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.3&m=$m&d=$d&t=$t&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 2.4 · Up to the latch

Variables passed to the simulation: `th, mu, L`

**Common Control**

```
$rad = 3.141592653589793/180
$th = randfrom("15,20,25,30")
$mu = rrand(0.1,0.3,0.05)
$L = rand(2,5)
$answer = sqrt(2*9.8*(sin($th*$rad) + $mu*cos($th*$rad))*$L)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.4&th=$th&mu=$mu&L=$L&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Up to the latch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A puck is shot up a $th° ramp with friction coefficient μ = $mu. A latch $L m along the ramp catches it only if it stops right there. What starting speed does it need?</p>
<p>Use g = 9.8 m/s². Enter the starting speed in m/s, to three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct starting speed. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.4&th=$th&mu=$mu&L=$L&mode=solution" title="Physics Proving Ground: Up to the latch, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=2.4&th=$th&mu=$mu&L=$L&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 3.1 · Spring to the summit

Variables passed to the simulation: `m, k, h`

**Common Control**

```
$m = rrand(0.5,2,0.5)
$k = rrand(200,800,100)
$h = rrand(0.8,2.2,0.2)
$answer = sqrt(2*$m*9.8*$h/$k)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.1&m=$m&k=$k&h=$h&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Spring to the summit" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A $m kg cart sits against a spring with k = $k N/m. The track is frictionless and climbs to a stop at $h m height. How far should you compress the spring so the cart just reaches that height?</p>
<p>Use g = 9.8 m/s². Enter the spring compression in m, to three significant figures.</p>
<p>x = $answerbox m</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct spring compression. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.1&m=$m&k=$k&h=$h&mode=solution" title="Physics Proving Ground: Spring to the summit, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.1&m=$m&k=$k&h=$h&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 3.2 · Spring meets carpet

Variables passed to the simulation: `m, k, mu, d`

**Common Control**

```
$m = rrand(0.5,2,0.5)
$k = rrand(200,800,100)
$mu = rrand(0.2,0.5,0.1)
$d = rrand(1,3,0.5)
$answer = sqrt(2*$mu*$m*9.8*$d/$k)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.2&m=$m&k=$k&mu=$mu&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Spring meets carpet" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A $m kg block is pushed against a spring with k = $k N/m on a frictionless surface. It then slides onto carpet with μ = $mu and has to stop $d m into the carpet. How far should you compress the spring?</p>
<p>Use g = 9.8 m/s². Enter the spring compression in m, to three significant figures.</p>
<p>x = $answerbox m</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct spring compression. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.2&m=$m&k=$k&mu=$mu&d=$d&mode=solution" title="Physics Proving Ground: Spring meets carpet, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.2&m=$m&k=$k&mu=$mu&d=$d&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 3.3 · Stick and climb

Variables passed to the simulation: `m1, m2, h`

**Common Control**

```
$m1 = rrand(1,4,0.5)
$m2 = rrand(1,4,0.5)
$h = rrand(0.5,1.5,0.1)
$answer = ($m1+$m2)/$m1*sqrt(2*9.8*$h)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.3&m1=$m1&m2=$m2&h=$h&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Stick and climb" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Cart A ($m1 kg) hits parked cart B ($m2 kg) and they lock together. The pair then coasts up a frictionless hill. They must reach exactly $h m height. How fast must cart A go before the crash?</p>
<p>Use g = 9.8 m/s². Enter the speed of cart A in m/s, to three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct speed of cart A. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.3&m1=$m1&m2=$m2&h=$h&mode=solution" title="Physics Proving Ground: Stick and climb, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.3&m1=$m1&m2=$m2&h=$h&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 3.4 · Knock it off the edge

Variables passed to the simulation: `m1, m2, H, d`

**Common Control**

```
$m1 = rrand(0.5,2,0.5)
$m2 = rrand(0.5,2,0.5)
$H = rrand(0.8,1.4,0.2)
$d = rrand(1,2.5,0.5)
$answer = $d*sqrt(9.8/(2*$H))*($m1+$m2)/(2*$m1)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.4&m1=$m1&m2=$m2&H=$H&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Knock it off the edge" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Ball A ($m1 kg) hits ball B ($m2 kg) in a perfectly elastic head-on collision. Ball B sits at the edge of a table $H m high and must land $d m from the edge. How fast must ball A be going?</p>
<p>Use g = 9.8 m/s². Enter the speed of ball A in m/s, to three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct speed of ball A. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.4&m1=$m1&m2=$m2&H=$H&d=$d&mode=solution" title="Physics Proving Ground: Knock it off the edge, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=3.4&m1=$m1&m2=$m2&H=$H&d=$d&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 4.1 · Level the seesaw

Variables passed to the simulation: `m1, d1, m2`

**Common Control**

```
$m1 = rrand(10,40,5)
$d1 = rrand(0.6,1.6,0.2)
$m2 = rrand(10,40,5) where ($m2 != $m1 && $m1*$d1/$m2 < 2.2 && $m1*$d1/$m2 > 0.3)
$answer = $m1*$d1/$m2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.1&m1=$m1&d1=$d1&m2=$m2&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Level the seesaw" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A $m1 kg load sits $d1 m left of a seesaw's pivot. Where, measured from the pivot, must a $m2 kg load go on the right side so the beam balances?</p>
<p>Use g = 9.8 m/s². Enter the distance from the pivot in m, to three significant figures.</p>
<p>x = $answerbox m</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct distance from the pivot. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.1&m1=$m1&d1=$d1&m2=$m2&mode=solution" title="Physics Proving Ground: Level the seesaw, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.1&m1=$m1&d1=$d1&m2=$m2&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 4.2 · The heavy beam

Variables passed to the simulation: `L, M, p, m`

**Common Control**

```
$L = rand(4,6)
$M = rrand(10,30,5)
$p = rrand(1,$L/2-0.4,0.2) where ($M*($L/2-$p) < 36*$p && $M*($L/2-$p) > 4.5)
$arm = $L/2 - $p
$m = rrand(15,40,5) where ($M*$arm/$m > 0.3 && $M*$arm/$m < 0.9*$p)
$answer = $M*$arm/$m
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.2&L=$L&M=$M&p=$p&m=$m&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: The heavy beam" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A uniform $L m beam of $M kg rests on a pivot $p m from its left end, so its long side wants to drop. Where left of the pivot should a $m kg counterweight go to balance it?</p>
<p>Use g = 9.8 m/s². Enter the distance from the pivot in m, to three significant figures.</p>
<p>x = $answerbox m</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct distance from the pivot. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.2&L=$L&M=$M&p=$p&m=$m&mode=solution" title="Physics Proving Ground: The heavy beam, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.2&L=$L&M=$M&p=$p&m=$m&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 4.3 · Flywheel launcher

Variables passed to the simulation: `I, r, t, H, d`

**Common Control**

```
$I = rrand(0.4,1.2,0.2)
$r = rrand(0.3,0.5,0.1)
$t = rrand(1,2,0.5)
$H = rrand(1.2,2,0.2)
$d = rand(2,5)
$answer = $I*$d/sqrt(2*$H/9.8)/($r*$t)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.3&I=$I&r=$r&t=$t&H=$H&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Flywheel launcher" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A flywheel with moment of inertia I = $I kg·m² and radius $r m starts from rest and spins up for $t s under constant torque. It then flings a ball horizontally from its top, $H m above the floor. The ball must land $d m away. What torque do you need?</p>
<p>Use g = 9.8 m/s². Enter the torque in N·m, to three significant figures.</p>
<p>τ = $answerbox N·m</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct torque. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.3&I=$I&r=$r&t=$t&H=$H&d=$d&mode=solution" title="Physics Proving Ground: Flywheel launcher, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.3&I=$I&r=$r&t=$t&H=$H&d=$d&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

## Level 4.4 · Rolling start

Variables passed to the simulation: `H, d`

**Common Control**

```
$H = rrand(0.8,1.4,0.2)
$d = rrand(0.8,1.8,0.2)
$v = $d/sqrt(2*$H/9.8)
$answer = 0.75*$v*$v/9.8
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.4&H=$H&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Physics Proving Ground: Rolling start" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The simulation shows a correct launch, with the answer hidden. After you submit, it also shows your launch. Tap it to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A solid cylinder rolls without slipping down a ramp, then off a table $H m high. It must land $d m from the edge. From what height on the ramp, above the tabletop, should you release it? For a solid cylinder, I = ½mr².</p>
<p>Use g = 9.8 m/s². Enter the ramp height in m, to three significant figures.</p>
<p>h = $answerbox m</p>
```

**Detailed Solution**

```html
<p>Here is the launch with the correct ramp height. Tap the picture to replay it.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.4&H=$H&d=$d&mode=solution" title="Physics Proving Ground: Rolling start, correct launch" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"><a href="https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html?level=4.4&H=$H&d=$d&mode=solution" target="_blank" rel="noopener">Open the launch in a new tab</a></p>
</div>
```

---

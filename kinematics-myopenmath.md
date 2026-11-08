# MyOpenMath code for the Constant Acceleration Lab

Twenty questions built from the Lecture 7 examples: the runner, the braking car, the ranger and the deer,
the two-stage car, the hockey puck, the ball thrown up and the high jumper. MyOpenMath picks the numbers
and grades the answer. The simulation inside the question runs that exact motion.

Simulation: https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html

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
## 1.1 · Runner: final velocity

Variables passed to the simulation: `v0, a, t`

**Common Control**

```
$v0 = rrand(1,3,0.5)
$a = rrand(0.5,2,0.1)
$t = rand(2,5)
$answer = $v0 + $a*$t
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.1&v0=$v0&a=$a&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Runner: final velocity" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> for <b>$t s</b>. What is the runner's velocity at the end of this time?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.1&v0=$v0&a=$a&t=$t&mode=solution" title="Constant Acceleration Lab: Runner: final velocity, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.1&v0=$v0&a=$a&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.2 · Runner: distance

Variables passed to the simulation: `v0, a, t`

**Common Control**

```
$v0 = rrand(1,3,0.5)
$a = rrand(0.5,2,0.1)
$t = rand(2,5)
$answer = $v0*$t + 0.5*$a*$t*$t
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.2&v0=$v0&a=$a&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Runner: distance" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> for <b>$t s</b>. What distance does the runner cover in this time?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.2&v0=$v0&a=$a&t=$t&mode=solution" title="Constant Acceleration Lab: Runner: distance, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.2&v0=$v0&a=$a&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.3 · Runner: time to top speed

Variables passed to the simulation: `v0, a, vf`

**Common Control**

```
$v0 = rrand(1,3,0.5)
$a = rrand(0.5,2,0.1)
$vf = $v0 + rrand(2,5,0.5)
$answer = ($vf - $v0)/$a
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.3&v0=$v0&a=$a&vf=$vf&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Runner: time to top speed" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> until reaching <b>$vf m/s</b>. How long does this take?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δt = $answerbox s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.3&v0=$v0&a=$a&vf=$vf&mode=solution" title="Constant Acceleration Lab: Runner: time to top speed, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.3&v0=$v0&a=$a&vf=$vf&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.4 · Runner: distance to top speed

Variables passed to the simulation: `v0, a, vf`

**Common Control**

```
$v0 = rrand(1,3,0.5)
$a = rrand(0.5,2,0.1)
$vf = $v0 + rrand(2,5,0.5)
$answer = ($vf*$vf - $v0*$v0)/(2*$a)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.4&v0=$v0&a=$a&vf=$vf&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Runner: distance to top speed" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A runner moving at <b>$v0 m/s</b> speeds up at a constant <b>$a m/s<sup>2</sup></b> until reaching <b>$vf m/s</b>. How far does the runner travel while speeding up?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.4&v0=$v0&a=$a&vf=$vf&mode=solution" title="Constant Acceleration Lab: Runner: distance to top speed, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.4&v0=$v0&a=$a&vf=$vf&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.5 · Sprint from the blocks

Variables passed to the simulation: `a, D`

**Common Control**

```
$a = rrand(1,2.5,0.1)
$D = rand(10,25)
$answer = sqrt(2*$a*$D)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.5&a=$a&D=$D&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Sprint from the blocks" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A sprinter starts from rest and accelerates at a constant <b>$a m/s<sup>2</sup></b> over the first <b>$D m</b>. How fast is the sprinter running at the $D m mark?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.5&a=$a&D=$D&mode=solution" title="Constant Acceleration Lab: Sprint from the blocks, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=1.5&a=$a&D=$D&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.1 · Braking car: velocity

Variables passed to the simulation: `v0, a, t`

**Common Control**

```
$v0 = rand(20,35)
$a = -rand(2,5)
$t = rand(2,4) where ($v0 + $a*$t > 0)
$answer = $v0 + $a*$t
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.1&v0=$v0&a=$a&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Braking car: velocity" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A car moving at <b>$v0 m/s</b> brakes with a constant acceleration of <b>$a m/s<sup>2</sup></b>. What is its velocity after <b>$t s</b> of braking?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.1&v0=$v0&a=$a&t=$t&mode=solution" title="Constant Acceleration Lab: Braking car: velocity, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.1&v0=$v0&a=$a&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.2 · Braking car: distance

Variables passed to the simulation: `v0, a, t`

**Common Control**

```
$v0 = rand(20,35)
$a = -rand(2,5)
$t = rand(2,4) where ($v0 + $a*$t > 0)
$answer = $v0*$t + 0.5*$a*$t*$t
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.2&v0=$v0&a=$a&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Braking car: distance" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A car moving at <b>$v0 m/s</b> brakes with a constant acceleration of <b>$a m/s<sup>2</sup></b>. How far does it travel during the first <b>$t s</b> of braking?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.2&v0=$v0&a=$a&t=$t&mode=solution" title="Constant Acceleration Lab: Braking car: distance, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.2&v0=$v0&a=$a&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.3 · Braking car: time to stop

Variables passed to the simulation: `v0, a, t`

**Common Control**

```
$v0 = rand(20,35)
$a = -rand(2,5)
$t = rand(2,4) where ($v0 + $a*$t > 0)
$answer = -$v0/$a
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.3&v0=$v0&a=$a&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Braking car: time to stop" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A car moving at <b>$v0 m/s</b> brakes with a constant acceleration of <b>$a m/s<sup>2</sup></b>. How long does it take the car to come to rest?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δt = $answerbox s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.3&v0=$v0&a=$a&t=$t&mode=solution" title="Constant Acceleration Lab: Braking car: time to stop, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.3&v0=$v0&a=$a&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.4 · Deer in the headlights

Variables passed to the simulation: `a, D, v0`

**Common Control**

```
$a = -rrand(3,5,0.1)
$D = rand(18,40)
$v0 = rrand(9,16,0.1) where ($v0*$v0/(-2*$a) < $D - 1)
$answer = $D - $v0*$v0/(-2*$a)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.4&a=$a&D=$D&v0=$v0&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Deer in the headlights" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A park ranger driving at <b>$v0 m/s</b> sees a deer <b>$D m</b> ahead and brakes immediately with a constant acceleration of <b>$a m/s<sup>2</sup></b>. How close does the ranger come to hitting the deer?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>d = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.4&a=$a&D=$D&v0=$v0&mode=solution" title="Constant Acceleration Lab: Deer in the headlights, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.4&a=$a&D=$D&v0=$v0&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.5 · Brake hard enough

Variables passed to the simulation: `D, v0`

**Common Control**

```
$D = rand(18,40)
$v0 = rrand(9,16,0.1)
$answer = -$v0*$v0/(2*$D)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.5&D=$D&v0=$v0&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Brake hard enough" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A ranger driving at <b>$v0 m/s</b> sees a deer <b>$D m</b> ahead. What constant acceleration would stop the vehicle exactly at the deer? (Include the sign.)</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>a = $answerbox m/s<sup>2</sup></p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.5&D=$D&v0=$v0&mode=solution" title="Constant Acceleration Lab: Brake hard enough, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=2.5&D=$D&v0=$v0&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.1 · Speed up, then brake: speed

Variables passed to the simulation: `a1, t1, a2, t2`

**Common Control**

```
$a1 = rrand(1.5,3,0.5)
$t1 = rand(4,6)
$a2 = -rrand(1,3,0.5) where ($a1*$t1 + $a2*4 > 0.5)
$t2 = rand(2,4)
$answer = $a1*$t1 + $a2*$t2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.1&a1=$a1&t1=$t1&a2=$a2&t2=$t2&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Speed up, then brake: speed" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A car starts from rest and speeds up at <b>$a1 m/s<sup>2</sup></b> for <b>$t1 s</b>. The driver then brakes at <b>$a2 m/s<sup>2</sup></b> for <b>$t2 s</b>. How fast is the car going at the end of the braking?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.1&a1=$a1&t1=$t1&a2=$a2&t2=$t2&mode=solution" title="Constant Acceleration Lab: Speed up, then brake: speed, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.1&a1=$a1&t1=$t1&a2=$a2&t2=$t2&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.2 · Speed up, then brake: distance

Variables passed to the simulation: `a1, t1, a2, t2`

**Common Control**

```
$a1 = rrand(1.5,3,0.5)
$t1 = rand(4,6)
$a2 = -rrand(1,3,0.5) where ($a1*$t1 + $a2*4 > 0.5)
$t2 = rand(2,4)
$answer = 0.5*$a1*$t1*$t1 + $a1*$t1*$t2 + 0.5*$a2*$t2*$t2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.2&a1=$a1&t1=$t1&a2=$a2&t2=$t2&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Speed up, then brake: distance" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A car starts from rest and speeds up at <b>$a1 m/s<sup>2</sup></b> for <b>$t1 s</b>. The driver then brakes at <b>$a2 m/s<sup>2</sup></b> for <b>$t2 s</b>. How far has the car gone in total?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.2&a1=$a1&t1=$t1&a2=$a2&t2=$t2&mode=solution" title="Constant Acceleration Lab: Speed up, then brake: distance, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.2&a1=$a1&t1=$t1&a2=$a2&t2=$t2&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.3 · Beat the buzzer

Variables passed to the simulation: `v0, a, D, t`

**Common Control**

```
$v0 = rand(20,35)
$a = -rrand(0.3,0.8,0.1)
$D = rand(25,45)
$t = rrand(1,1.5,0.05)
$answer = $v0*$t + 0.5*$a*$t*$t
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.3&v0=$v0&a=$a&D=$D&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Beat the buzzer" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>With <b>$t s</b> left in the game, a hockey player shoots the puck at <b>$v0 m/s</b> toward an empty goal <b>$D m</b> away. The ice slows the puck at <b>$a m/s<sup>2</sup></b>. How far does the puck slide before the buzzer (ignore the goal)?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.3&v0=$v0&a=$a&D=$D&t=$t&mode=solution" title="Constant Acceleration Lab: Beat the buzzer, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.3&v0=$v0&a=$a&D=$D&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.4 · Puck: speed at the goal

Variables passed to the simulation: `v0, a, D, t`

**Common Control**

```
$v0 = rand(20,35)
$a = -rrand(0.3,0.8,0.1)
$D = rand(25,45)
$t = rrand(1,1.5,0.05)
$answer = sqrt($v0*$v0 + 2*$a*$D)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.4&v0=$v0&a=$a&D=$D&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Puck: speed at the goal" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A hockey puck leaves the stick at <b>$v0 m/s</b> toward a goal <b>$D m</b> away. The ice slows it at <b>$a m/s<sup>2</sup></b>. How fast is the puck moving when it reaches the goal?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.4&v0=$v0&a=$a&D=$D&t=$t&mode=solution" title="Constant Acceleration Lab: Puck: speed at the goal, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.4&v0=$v0&a=$a&D=$D&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.5 · Puck: time to the goal

Variables passed to the simulation: `v0, a, D, t`

**Common Control**

```
$v0 = rand(20,35)
$a = -rrand(0.3,0.8,0.1)
$D = rand(25,45)
$t = rrand(1,1.5,0.05)
$answer = ($v0 - sqrt($v0*$v0 + 2*$a*$D))/(-$a)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.5&v0=$v0&a=$a&D=$D&t=$t&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Puck: time to the goal" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A hockey puck leaves the stick at <b>$v0 m/s</b> toward a goal <b>$D m</b> away. The ice slows it at <b>$a m/s<sup>2</sup></b>. How long does the puck take to reach the goal?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δt = $answerbox s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.5&v0=$v0&a=$a&D=$D&t=$t&mode=solution" title="Constant Acceleration Lab: Puck: time to the goal, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=3.5&v0=$v0&a=$a&D=$D&t=$t&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.1 · Ball thrown up: height

Variables passed to the simulation: `v0`

**Common Control**

```
$v0 = rrand(10,30,0.5)
$answer = $v0*$v0/(2*9.8)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.1&v0=$v0&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Ball thrown up: height" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A ball is thrown straight up from ground level at <b>$v0 m/s</b>. How high does it rise?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δy = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.1&v0=$v0&mode=solution" title="Constant Acceleration Lab: Ball thrown up: height, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.1&v0=$v0&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.2 · Ball thrown up: time of flight

Variables passed to the simulation: `v0`

**Common Control**

```
$v0 = rrand(10,30,0.5)
$answer = 2*$v0/9.8
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.2&v0=$v0&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Ball thrown up: time of flight" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A ball is thrown straight up from ground level at <b>$v0 m/s</b>. How long is it in the air before it returns to the ground?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δt = $answerbox s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.2&v0=$v0&mode=solution" title="Constant Acceleration Lab: Ball thrown up: time of flight, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.2&v0=$v0&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.3 · Caught on the way down

Variables passed to the simulation: `T`

**Common Control**

```
$T = rrand(1,4,0.1)
$answer = 9.8*$T/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.3&T=$T&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: Caught on the way down" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A ball thrown straight up is caught by the thrower, at the same height, <b>$T s</b> later. With what speed was it thrown?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>v<sub>0</sub> = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.3&T=$T&mode=solution" title="Constant Acceleration Lab: Caught on the way down, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.3&T=$T&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.4 · High jump: peak height

Variables passed to the simulation: `v0, yi, bar`

**Common Control**

```
$v0 = rrand(3.5,5,0.1)
$yi = rrand(1,1.3,0.05)
$bar = rrand(1.9,2.5,0.05)
$answer = $yi + $v0*$v0/(2*9.8)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.4&v0=$v0&yi=$yi&bar=$bar&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: High jump: peak height" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>At takeoff a high jumper's center of gravity is <b>$yi m</b> high and moving straight up at <b>$v0 m/s</b>. The bar is at <b>$bar m</b>. How high does the center of gravity rise (height above the ground)?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>y<sub>peak</sub> = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.4&v0=$v0&yi=$yi&bar=$bar&mode=solution" title="Constant Acceleration Lab: High jump: peak height, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.4&v0=$v0&yi=$yi&bar=$bar&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.5 · High jump: time to peak

Variables passed to the simulation: `v0, yi, bar`

**Common Control**

```
$v0 = rrand(3.5,5,0.1)
$yi = rrand(1,1.3,0.05)
$bar = rrand(1.9,2.5,0.05)
$answer = $v0/9.8
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.5&v0=$v0&yi=$yi&bar=$bar&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Constant Acceleration Lab: High jump: time to peak" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the motion. After you submit, your answer appears in the scene. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>At takeoff a high jumper's center of gravity is <b>$yi m</b> high and moving straight up at <b>$v0 m/s</b>. How long after takeoff does it reach its peak?</p>
<p>Use g = 9.80 m/s<sup>2</sup> where needed, and three significant figures.</p>
<p>Δt = $answerbox s</p>
```

**Detailed Solution**

```html
<p>The motion again, with every readout showing and the correct answer labeled. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.5&v0=$v0&yi=$yi&bar=$bar&mode=solution" title="Constant Acceleration Lab: High jump: time to peak, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:320px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html?level=4.5&v0=$v0&yi=$yi&bar=$bar&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

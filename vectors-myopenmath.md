# MyOpenMath code for the Vector Range

Twenty two-part questions built from the Lecture 3 and Lecture 4 vector examples. MyOpenMath picks the
numbers and grades the answer. The simulation inside the question uses the same numbers.

Simulation: https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html

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
## 1.1 · Solve the triangle

Variables passed to the simulation: `c, th`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$c = rrand(3,9,0.5)
$th = rand(15,75)
$answer[0] = $c*cos($th*$rad)
$answer[1] = $c*sin($th*$rad)
$reltolerance[0] = 0.02
$reltolerance[1] = 0.02
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.1&c=$c&th=$th&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Solve the triangle" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A <b>$c m</b> ladder leans against a wall, making a <b>$th°</b> angle with the level ground. How far from the wall is its foot (<i>a</i>), and how high up the wall does it reach (<i>b</i>)?</p>
<p>Use three significant figures.</p>
<p>a = $answerbox[0] m</p>
<p>b = $answerbox[1] m</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.1&c=$c&th=$th&mode=solution" title="Vector Range: Solve the triangle, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.1&c=$c&th=$th&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.2 · The ramp

Variables passed to the simulation: `a, b`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$a = rrand(2,8,0.5)
$b = rrand(1,4,0.5)
$answer[0] = sqrt($a*$a + $b*$b)
$answer[1] = atan($b/$a)/$rad
$reltolerance[0] = 0.02
$reltolerance[1] = 0.02
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.2&a=$a&b=$b&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: The ramp" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A ramp rises <b>$b m</b> over a horizontal run of <b>$a m</b>. How long is the ramp's surface (<i>r</i>), and what angle <i>θ</i> does it make with the ground?</p>
<p>Use three significant figures.</p>
<p>r = $answerbox[0] m</p>
<p>θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.2&a=$a&b=$b&mode=solution" title="Vector Range: The ramp, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.2&a=$a&b=$b&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.3 · Components of a force

Variables passed to the simulation: `F, th`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$F = rrand(50,500,10)
$th = rand(10,350) where (($th > 8 && $th < 82) || ($th > 98 && $th < 172) || ($th > 188 && $th < 262) || ($th > 278 && $th < 352))
$answer[0] = $F*cos($th*$rad)
$answer[1] = $F*sin($th*$rad)
$abstolerance[0] = 0.015*$F
$abstolerance[1] = 0.015*$F
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.3&F=$F&th=$th&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Components of a force" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A rope pulls a sled with a force of <b>$F N at $th°</b>, measured counterclockwise from the +x axis. Find the x and y components of the force.</p>
<p>Use three significant figures.</p>
<p>F<sub>x</sub> = $answerbox[0] N</p>
<p>F<sub>y</sub> = $answerbox[1] N</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.3&F=$F&th=$th&mode=solution" title="Vector Range: Components of a force, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.3&F=$F&th=$th&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.4 · Unit vector

Variables passed to the simulation: `Cx, Cy`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$Cx = rand(-9,9) where (abs($Cx) >= 2)
$Cy = rand(-9,9) where (abs($Cy) >= 2)
$C = sqrt($Cx*$Cx + $Cy*$Cy)
$answer[0] = $Cx/$C
$answer[1] = $Cy/$C
$abstolerance[0] = 0.015
$abstolerance[1] = 0.015
$Cys = "+ " . abs($Cy)
$Cys = "− " . abs($Cy) if ($Cy < 0)
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.4&Cx=$Cx&Cy=$Cy&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Unit vector" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Vector <b>C = ($Cx î $Cys ĵ) m</b>. Find the x and y components of the unit vector <b>Ĉ</b>, which points the same way as C but has length 1.</p>
<p>Use three significant figures.</p>
<p>Ĉ<sub>x</sub> = $answerbox[0] </p>
<p>Ĉ<sub>y</sub> = $answerbox[1] </p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.4&Cx=$Cx&Cy=$Cy&mode=solution" title="Vector Range: Unit vector, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.4&Cx=$Cx&Cy=$Cy&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.5 · Scaling a vector

Variables passed to the simulation: `k, B, th`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$k = randfrom("-3,-2,-1.5,-0.5,0.5,1.5,2,2.5,3")
$B = rand(2,10)
$th = rand(10,350) where (abs($th - 180) > 3)
$answer[0] = abs($k)*$B
$dir = $th
$dir = $th + 180 if ($k < 0)
$dir = $dir - 360 if ($dir >= 360)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.5&k=$k&B=$B&th=$th&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Scaling a vector" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Displacement <b>B</b> is <b>$B m at $th°</b>. Find the magnitude and direction of <b>$k B</b>.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>|kB| = $answerbox[0] m &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.5&k=$k&B=$B&th=$th&mode=solution" title="Vector Range: Scaling a vector, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.5&k=$k&B=$B&th=$th&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.6 · Components to polar

Variables passed to the simulation: `Ax, Ay`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$Ax = rand(-12,12) where (abs($Ax) >= 2)
$Ay = rand(-12,12) where (abs($Ay) >= 2)
$Rx = $Ax
$Ry = $Ay
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$Ays = "+ " . abs($Ay)
$Ays = "− " . abs($Ay) if ($Ay < 0)
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.6&Ax=$Ax&Ay=$Ay&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Components to polar" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A drone's displacement is <b>A = ($Ax î $Ays ĵ) m</b>. Find the magnitude and direction of A.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>A = $answerbox[0] m &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.6&Ax=$Ax&Ay=$Ay&mode=solution" title="Vector Range: Components to polar, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=1.6&Ax=$Ax&Ay=$Ay&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.1 · Two ropes on a box

Variables passed to the simulation: `F1, a1, F2, a2`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$F1 = rand(5,30)
$a1 = rand(10,60)
$F2 = rand(5,30)
$a2 = $a1 + rand(60,120)
$Rx = $F1*cos(($a1)*$rad) + $F2*cos(($a2)*$rad)
$Ry = $F1*sin(($a1)*$rad) + $F2*sin(($a2)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.1&F1=$F1&a1=$a1&F2=$F2&a2=$a2&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Two ropes on a box" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Two ropes pull on a box: <b>F₁ = $F1 N at $a1°</b> and <b>F₂ = $F2 N at $a2°</b>. Find the magnitude and direction of the net force.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>F<sub>net</sub> = $answerbox[0] N &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.1&F1=$F1&a1=$a1&F2=$F2&a2=$a2&mode=solution" title="Vector Range: Two ropes on a box, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.1&F1=$F1&a1=$a1&F2=$F2&a2=$a2&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.2 · Running on the train

Variables passed to the simulation: `vt, vp, dp`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$vt = rand(5,30)
$vp = rrand(2,8,0.5)
$dp = randfrom("90,270")
$Rx = $vt*cos((180)*$rad) + $vp*cos(($dp)*$rad)
$Ry = $vt*sin((180)*$rad) + $vp*sin(($dp)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$dpw = "north"
$dpw = "south" if ($dp == 270)
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.2&vt=$vt&vp=$vp&dp=$dp&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Running on the train" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A train moves <b>west at $vt m/s</b>. A passenger runs <b>$dpw at $vp m/s</b> relative to the train. Find the passenger's velocity relative to the ground.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>v<sub>pg</sub> = $answerbox[0] m/s &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.2&vt=$vt&vp=$vp&dp=$dp&mode=solution" title="Vector Range: Running on the train, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.2&vt=$vt&vp=$vp&dp=$dp&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.3 · Crossing the river

Variables passed to the simulation: `vb, vc, dc`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$vb = rrand(2,6,0.5)
$vc = rrand(0.5,3,0.5)
$dc = randfrom("0,180")
$Rx = $vb*cos((90)*$rad) + $vc*cos(($dc)*$rad)
$Ry = $vb*sin((90)*$rad) + $vc*sin(($dc)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$dcw = "east"
$dcw = "west" if ($dc == 180)
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.3&vb=$vb&vc=$vc&dc=$dc&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Crossing the river" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A kayak paddles <b>due north at $vb m/s</b> relative to the water. The river flows <b>$dcw at $vc m/s</b>. Find the kayak's velocity relative to the shore.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>v = $answerbox[0] m/s &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.3&vb=$vb&vc=$vc&dc=$dc&mode=solution" title="Vector Range: Crossing the river, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.3&vb=$vb&vc=$vc&dc=$dc&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.4 · Two-leg hike

Variables passed to the simulation: `d1, t1, d2, t2`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$d1 = rand(200,900)
$t1 = rand(10,80)
$d2 = rand(200,900)
$t2 = rand(10,80)
$Rx = $d1*cos(($t1)*$rad) + $d2*cos((180-$t2)*$rad)
$Ry = $d1*sin(($t1)*$rad) + $d2*sin((180-$t2)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.4&d1=$d1&t1=$t1&d2=$d2&t2=$t2&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Two-leg hike" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A hiker walks <b>$d1 m at $t1° N of E</b>, then <b>$d2 m at $t2° N of W</b>. Find the hiker's total displacement.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>d = $answerbox[0] m &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.4&d1=$d1&t1=$t1&d2=$d2&t2=$t2&mode=solution" title="Vector Range: Two-leg hike, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.4&d1=$d1&t1=$t1&d2=$d2&t2=$t2&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.5 · Plane in a crosswind

Variables passed to the simulation: `vp, a, w, aw`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$vp = rand(300,600)
$a = rand(20,160)
$w = rand(30,120)
$aw = rand(0,359) where ($vp*sin($a*$rad) + $w*sin($aw*$rad) > 0.05*($vp + $w))
$Rx = $vp*cos(($a)*$rad) + $w*cos(($aw)*$rad)
$Ry = $vp*sin(($a)*$rad) + $w*sin(($aw)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.5&vp=$vp&a=$a&w=$w&aw=$aw&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Plane in a crosswind" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>An airplane flies at <b>$vp km/h at $a°</b> relative to the air. The wind blows at <b>$w km/h toward $aw°</b>. Find the plane's velocity relative to the ground.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>v<sub>ground</sub> = $answerbox[0] km/h &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.5&vp=$vp&a=$a&w=$w&aw=$aw&mode=solution" title="Vector Range: Plane in a crosswind, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=2.5&vp=$vp&a=$a&w=$w&aw=$aw&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.1 · Three forces: components

Variables passed to the simulation: `F1, a1, F2, a2, F3`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$F1 = rrand(50,150,10)
$a1 = rand(20,70)
$F2 = rrand(150,250,10)
$a2 = rand(110,160)
$F3 = rrand(20,60,10)
$Rx = $F1*cos(($a1)*$rad) + $F2*cos(($a2)*$rad) + $F3*cos((270)*$rad)
$Ry = $F1*sin(($a1)*$rad) + $F2*sin(($a2)*$rad) + $F3*sin((270)*$rad)
$answer[0] = $Rx
$answer[1] = $Ry
$abstolerance[0] = 0.005*($F1 + $F2 + $F3)
$abstolerance[1] = 0.005*($F1 + $F2 + $F3)
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.1&F1=$F1&a1=$a1&F2=$F2&a2=$a2&F3=$F3&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Three forces: components" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Three forces act on a crate: <b>F₁ = $F1 N at $a1°</b>, <b>F₂ = $F2 N at $a2°</b>, and <b>F₃ = $F3 N at 270°</b>. Find the x and y components of the net force.</p>
<p>Use three significant figures.</p>
<p>F<sub>net,x</sub> = $answerbox[0] N</p>
<p>F<sub>net,y</sub> = $answerbox[1] N</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.1&F1=$F1&a1=$a1&F2=$F2&a2=$a2&F3=$F3&mode=solution" title="Vector Range: Three forces: components, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.1&F1=$F1&a1=$a1&F2=$F2&a2=$a2&F3=$F3&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.2 · Three forces: net force

Variables passed to the simulation: `F1, a1, F2, a2, F3`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$F1 = rrand(50,150,10)
$a1 = rand(20,70)
$F2 = rrand(150,250,10)
$a2 = rand(110,160)
$F3 = rrand(20,60,10)
$Rx = $F1*cos(($a1)*$rad) + $F2*cos(($a2)*$rad) + $F3*cos((270)*$rad)
$Ry = $F1*sin(($a1)*$rad) + $F2*sin(($a2)*$rad) + $F3*sin((270)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.2&F1=$F1&a1=$a1&F2=$F2&a2=$a2&F3=$F3&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Three forces: net force" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Three forces act on a crate: <b>F₁ = $F1 N at $a1°</b>, <b>F₂ = $F2 N at $a2°</b>, and <b>F₃ = $F3 N at 270°</b>. Find the magnitude and direction of the net force.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>F<sub>net</sub> = $answerbox[0] N &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.2&F1=$F1&a1=$a1&F2=$F2&a2=$a2&F3=$F3&mode=solution" title="Vector Range: Three forces: net force, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.2&F1=$F1&a1=$a1&F2=$F2&a2=$a2&F3=$F3&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.3 · Four ropes on a ring

Variables passed to the simulation: `F1, t1, F2, t2, F3, t3, t4, F4`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$F1 = rrand(300,800,50)
$t1 = rand(20,70)
$F2 = rrand(300,800,50)
$t2 = rand(20,70)
$F3 = rrand(300,800,50)
$t3 = rand(20,70)
$t4 = rand(20,70)
$Sx = $F1*cos(($t1)*$rad) + $F2*cos((180-$t2)*$rad) + $F3*cos((180+$t3)*$rad)
$Sy = $F1*sin(($t1)*$rad) + $F2*sin((180-$t2)*$rad) + $F3*sin((180+$t3)*$rad)
$F4 = rrand(300,800,50) where (sqrt(($Sx + $F4*cos((360-$t4)*$rad))*($Sx + $F4*cos((360-$t4)*$rad)) + ($Sy + $F4*sin((360-$t4)*$rad))*($Sy + $F4*sin((360-$t4)*$rad))) > 100 && abs($Sy + $F4*sin((360-$t4)*$rad)) > 0.05*abs($Sx + $F4*cos((360-$t4)*$rad)) + 20)
$Rx = $Sx + $F4*cos((360-$t4)*$rad)
$Ry = $Sy + $F4*sin((360-$t4)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.3&F1=$F1&t1=$t1&F2=$F2&t2=$t2&F3=$F3&t3=$t3&t4=$t4&F4=$F4&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Four ropes on a ring" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Four people pull on ropes tied to a steel ring: <b>F₁ = $F1 N</b> at $t1° above the +x axis, <b>F₂ = $F2 N</b> at $t2° above the −x axis, <b>F₃ = $F3 N</b> at $t3° below the −x axis, and <b>F₄ = $F4 N</b> at $t4° below the +x axis. Find the net force on the ring.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>F<sub>net</sub> = $answerbox[0] N &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.3&F1=$F1&t1=$t1&F2=$F2&t2=$t2&F3=$F3&t3=$t3&t4=$t4&F4=$F4&mode=solution" title="Vector Range: Four ropes on a ring, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.3&F1=$F1&t1=$t1&F2=$F2&t2=$t2&F3=$F3&t3=$t3&t4=$t4&F4=$F4&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.4 · Orienteering

Variables passed to the simulation: `d1, d2, t2, t3, d3`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$d1 = rand(100,500)
$d2 = rand(100,500)
$t2 = rand(15,75)
$t3 = rand(15,75)
$Sx = $d1*cos((90)*$rad) + $d2*cos((360-$t2)*$rad)
$Sy = $d1*sin((90)*$rad) + $d2*sin((360-$t2)*$rad)
$d3 = rand(100,500) where (sqrt(($Sx + $d3*cos((180-$t3)*$rad))*($Sx + $d3*cos((180-$t3)*$rad)) + ($Sy + $d3*sin((180-$t3)*$rad))*($Sy + $d3*sin((180-$t3)*$rad))) > 50 && abs($Sy + $d3*sin((180-$t3)*$rad)) > 0.05*abs($Sx + $d3*cos((180-$t3)*$rad)) + 10)
$Rx = $Sx + $d3*cos((180-$t3)*$rad)
$Ry = $Sy + $d3*sin((180-$t3)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.4&d1=$d1&d2=$d2&t2=$t2&t3=$t3&d3=$d3&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Orienteering" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>In an orienteering race you run <b>$d1 m due north</b>, then <b>$d2 m at $t2° S of E</b>, then <b>$d3 m at $t3° N of W</b>. Find your displacement from the start.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>d = $answerbox[0] m &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.4&d1=$d1&d2=$d2&t2=$t2&t3=$t3&d3=$d3&mode=solution" title="Vector Range: Orienteering, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=3.4&d1=$d1&d2=$d2&t2=$t2&t3=$t3&d3=$d3&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.1 · Up, then up or down

Variables passed to the simulation: `vi, df, vf`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$vi = rand(4,15)
$df = randfrom("90,270")
$vf = rand(1,15) where ($df == 270 || $vf != $vi)
$Ry = $vf*sin($df*$rad) - $vi
$answer[0] = abs($Ry)
$dir = 90
$dir = 270 if ($Ry < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$dfw = "up"
$dfw = "down" if ($df == 270)
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.1&vi=$vi&df=$df&vf=$vf&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Up, then up or down" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A ball moves <b>straight up at $vi m/s</b>. A moment later it moves <b>straight $dfw at $vf m/s</b>. Find the change in velocity Δv = v<sub>f</sub> − v<sub>i</sub>.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>Δv = $answerbox[0] m/s &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.1&vi=$vi&df=$df&vf=$vf&mode=solution" title="Vector Range: Up, then up or down, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.1&vi=$vi&df=$df&vf=$vf&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.2 · Change in position

Variables passed to the simulation: `r1, a1, r2, a2`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$r1 = rrand(400,1200,100)
$a1 = rand(0,359)
$r2 = rrand(300,1000,100)
$a2 = rand(0,359) where (sqrt(($r2*cos($a2*$rad) - $r1*cos($a1*$rad))*($r2*cos($a2*$rad) - $r1*cos($a1*$rad)) + ($r2*sin($a2*$rad) - $r1*sin($a1*$rad))*($r2*sin($a2*$rad) - $r1*sin($a1*$rad))) > 200 && abs($r2*sin($a2*$rad) - $r1*sin($a1*$rad)) > 0.05*abs($r2*cos($a2*$rad) - $r1*cos($a1*$rad)) + 10)
$Rx = $r2*cos(($a2)*$rad) - $r1*cos(($a1)*$rad)
$Ry = $r2*sin(($a2)*$rad) - $r1*sin(($a1)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.2&r1=$r1&a1=$a1&r2=$r2&a2=$a2&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Change in position" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A delivery drone is <b>$r1 m from its base at $a1°</b>. Later it is <b>$r2 m from the base at $a2°</b>. Find its displacement Δr = r<sub>f</sub> − r<sub>i</sub>.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>Δr = $answerbox[0] m &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.2&r1=$r1&a1=$a1&r2=$r2&a2=$a2&mode=solution" title="Vector Range: Change in position, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.2&r1=$r1&a1=$a1&r2=$r2&a2=$a2&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.3 · Subtracting components

Variables passed to the simulation: `Ax, Ay, Bx, By, s`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$Ax = rrand(-9,9,0.01) where (abs($Ax) >= 0.5)
$Ay = rrand(-9,9,0.01) where (abs($Ay) >= 0.5)
$Bx = rrand(-9,9,0.01) where (abs($Bx) >= 0.5)
$By = rrand(-9,9,0.01) where (abs($By) >= 0.5)
$s = randfrom("1,-1")
$Rx = $s*($Ax - $Bx)
$Ry = $s*($Ay - $By)
$answer[0] = $Rx
$answer[1] = $Ry
$abstolerance[0] = 0.02
$abstolerance[1] = 0.02
$Ays = "+ " . abs($Ay)
$Ays = "− " . abs($Ay) if ($Ay < 0)
$Bys = "+ " . abs($By)
$Bys = "− " . abs($By) if ($By < 0)
$op = "A − B"
$op = "B − A" if ($s < 0)
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.3&Ax=$Ax&Ay=$Ay&Bx=$Bx&By=$By&s=$s&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Subtracting components" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p><b>A = ($Ax î $Ays ĵ) m</b> and <b>B = ($Bx î $Bys ĵ) m</b>. Find the x and y components of <b>R = $op</b>.</p>
<p>Use three significant figures.</p>
<p>R<sub>x</sub> = $answerbox[0] m</p>
<p>R<sub>y</sub> = $answerbox[1] m</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.3&Ax=$Ax&Ay=$Ay&Bx=$Bx&By=$By&s=$s&mode=solution" title="Vector Range: Subtracting components, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.3&Ax=$Ax&Ay=$Ay&Bx=$Bx&By=$By&s=$s&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.4 · Racquetball rebound

Variables passed to the simulation: `v, al`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$v = rand(20,60)
$al = rand(15,75)
$answer[0] = 2*$v*sin($al*$rad)
$answer[1] = 180
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.4&v=$v&al=$al&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Racquetball rebound" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A racquetball moving at <b>$v m/s</b> hits a wall on its right at <b>$al°</b> to the wall. It rebounds at the same speed and the same $al° angle to the wall. Find the change in velocity Δv = v<sub>f</sub> − v<sub>i</sub>.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>Δv = $answerbox[0] m/s &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.4&v=$v&al=$al&mode=solution" title="Vector Range: Racquetball rebound, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.4&v=$v&al=$al&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.5 · Rounding the corner

Variables passed to the simulation: `v1, v2, af`

**Common Control**

```
$anstypes = "number,number"
$rad = 3.141592653589793/180
$v1 = rrand(3,8,0.5)
$v2 = rrand(3,8,0.5)
$af = randfrom("45,60,90,120,135")
$Rx = $v2*cos(($af)*$rad) - $v1*cos((0)*$rad)
$Ry = $v2*sin(($af)*$rad) - $v1*sin((0)*$rad)
$answer[0] = sqrt($Rx*$Rx + $Ry*$Ry)
$dir = atan($Ry/$Rx)/$rad
$dir = $dir + 180 if ($Rx < 0)
$dir = $dir + 360 if ($dir < 0)
$answer[1] = $dir
$reltolerance[0] = 0.02
$abstolerance[1] = 1
$stua0 = getstuans($stuanswers, $thisq, 0)
$stua1 = getstuans($stuanswers, $thisq, 1)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.5&v1=$v1&v2=$v2&af=$af&mode=show"
$simurl = $simurl . "&launch=$stua0,$stua1" if ($stua0 != "" && $stua1 != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Vector Range: Rounding the corner" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">The vectors slide tip-to-tail to mark the target. After you submit, your answer is drawn from the origin. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>A runner moving <b>east at $v1 m/s</b> rounds a corner and ends up moving at <b>$v2 m/s at $af°</b>. Find the change in velocity Δv = v<sub>f</sub> − v<sub>i</sub>.</p>
<p>Give the direction in degrees, measured counterclockwise from the +x axis (east), between 0° and 360°.</p>
<p>Use three significant figures.</p>
<p>Δv = $answerbox[0] m/s &nbsp; at &nbsp; θ = $answerbox[1] °</p>
```

**Detailed Solution**

```html
<p>The correct resultant is drawn from the origin to the target. Tap the picture to replay.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.5&v1=$v1&v2=$v2&af=$af&mode=solution" title="Vector Range: Rounding the corner, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:300px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html?q=4.5&v1=$v1&v2=$v2&af=$af&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

# MyOpenMath code for the Motion Graphs Lab

Twenty questions built from the Lecture 6 examples (graphical interpretation of motion). Each one shows a
cart on a lab track with a motion detector, and its position-vs-time or velocity-vs-time graph underneath.
MyOpenMath picks the graph's numbers and grades the answer, and the simulation draws that exact graph.

Simulation: https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html

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
## 1.1 · Reading position

Graph: X1 · Variables passed to the simulation: `a, b, c, d`

**Common Control**

```
$a = rand(0,2)
$b = $a + rand(2,4)
$c = $b - rand(3,5) where ($c != $a && $b + $c != 0)
$d = $c + rand(1,2)
$answer = ($b + $c)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.1&a=$a&b=$b&c=$c&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Reading position" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What is the cart's position at <b>t = 4.5 s</b>?</p>
<p>Use three significant figures.</p>
<p>x = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.1&a=$a&b=$b&c=$c&d=$d&mode=solution" title="Motion Graphs Lab: Reading position, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.1&a=$a&b=$b&c=$c&d=$d&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.2 · Velocity from slope

Graph: X1 · Variables passed to the simulation: `a, b, c, d`

**Common Control**

```
$a = rand(0,2)
$b = $a + rand(2,4)
$c = $b - rand(3,5) where ($c != $a && $b + $c != 0)
$d = $c + rand(1,2)
$answer = ($b - $a)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.2&a=$a&b=$b&c=$c&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Velocity from slope" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What is the cart's velocity at <b>t = 1 s</b>?</p>
<p>Use three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.2&a=$a&b=$b&c=$c&d=$d&mode=solution" title="Motion Graphs Lab: Velocity from slope, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.2&a=$a&b=$b&c=$c&d=$d&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.3 · Greatest speed

Graph: X1 · Variables passed to the simulation: `a, b, c, d`

**Common Control**

```
$a = rand(0,2)
$b = $a + rand(2,4)
$c = $b - rand(3,5) where ($c != $a && $b + $c != 0)
$d = $c + rand(1,2)
$answer = $b - $c
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.3&a=$a&b=$b&c=$c&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Greatest speed" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What is the cart's greatest speed during the 8 s?</p>
<p>Use three significant figures.</p>
<p>speed = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.3&a=$a&b=$b&c=$c&d=$d&mode=solution" title="Motion Graphs Lab: Greatest speed, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.3&a=$a&b=$b&c=$c&d=$d&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.4 · Average velocity

Graph: X1 · Variables passed to the simulation: `a, b, c, d`

**Common Control**

```
$a = rand(0,2)
$b = $a + rand(2,4)
$c = $b - rand(3,5) where ($c != $a && $b + $c != 0)
$d = $c + rand(1,2)
$answer = ($c - $a)/5
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.4&a=$a&b=$b&c=$c&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Average velocity" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What is the cart's average velocity from <b>t = 0 s</b> to <b>t = 5 s</b>?</p>
<p>Use three significant figures.</p>
<p>v<sub>ave</sub> = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.4&a=$a&b=$b&c=$c&d=$d&mode=solution" title="Motion Graphs Lab: Average velocity, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.4&a=$a&b=$b&c=$c&d=$d&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 1.5 · Total distance

Graph: X1 · Variables passed to the simulation: `a, b, c, d`

**Common Control**

```
$a = rand(0,2)
$b = $a + rand(2,4)
$c = $b - rand(3,5) where ($c != $a && $b + $c != 0)
$d = $c + rand(1,2)
$answer = ($b - $a) + ($b - $c) + ($d - $c)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.5&a=$a&b=$b&c=$c&d=$d&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Total distance" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What total distance does the cart travel from <b>t = 0 s</b> to <b>t = 8 s</b>?</p>
<p>Use three significant figures.</p>
<p>d = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.5&a=$a&b=$b&c=$c&d=$d&mode=solution" title="Motion Graphs Lab: Total distance, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=1.5&a=$a&b=$b&c=$c&d=$d&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.1 · Tangent line

Graph: X2 · Variables passed to the simulation: `v2, s1, x6, x8`

**Common Control**

```
$v2 = rand(2,4)
$s1 = randfrom("0,0.5,1")
$x4 = $v2 + 2*$s1
$x6 = $x4 - rand(5,8) where ($x6 != 0)
$x8 = $x6 + rand(1,2) where ($x6 + $x8 != 0)
$answer = $v2/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.1&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Tangent line" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. The dashed line is tangent to the curve at <b>t = 1 s</b>. What is the cart's velocity at t = 1 s?</p>
<p>Use three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.1&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" title="Motion Graphs Lab: Tangent line, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.1&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.2 · Straight-line velocity

Graph: X2 · Variables passed to the simulation: `v2, s1, x6, x8`

**Common Control**

```
$v2 = rand(2,4)
$s1 = randfrom("0,0.5,1")
$x4 = $v2 + 2*$s1
$x6 = $x4 - rand(5,8) where ($x6 != 0)
$x8 = $x6 + rand(1,2) where ($x6 + $x8 != 0)
$answer = ($x6 - $x4)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.2&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Straight-line velocity" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What is the cart's velocity at <b>t = 5 s</b>?</p>
<p>Use three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.2&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" title="Motion Graphs Lab: Straight-line velocity, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.2&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.3 · Average velocity

Graph: X2 · Variables passed to the simulation: `v2, s1, x6, x8`

**Common Control**

```
$v2 = rand(2,4)
$s1 = randfrom("0,0.5,1")
$x4 = $v2 + 2*$s1
$x6 = $x4 - rand(5,8) where ($x6 != 0)
$x8 = $x6 + rand(1,2) where ($x6 + $x8 != 0)
$answer = $x6/6
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.3&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Average velocity" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What is the cart's average velocity from <b>t = 0 s</b> to <b>t = 6 s</b>?</p>
<p>Use three significant figures.</p>
<p>v<sub>ave</sub> = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.3&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" title="Motion Graphs Lab: Average velocity, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.3&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.4 · Reading position

Graph: X2 · Variables passed to the simulation: `v2, s1, x6, x8`

**Common Control**

```
$v2 = rand(2,4)
$s1 = randfrom("0,0.5,1")
$x4 = $v2 + 2*$s1
$x6 = $x4 - rand(5,8) where ($x6 != 0)
$x8 = $x6 + rand(1,2) where ($x6 + $x8 != 0)
$answer = ($x6 + $x8)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.4&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Reading position" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. What is the cart's position at <b>t = 7 s</b>?</p>
<p>Use three significant figures.</p>
<p>x = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.4&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" title="Motion Graphs Lab: Reading position, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.4&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 2.5 · Acceleration from a curve

Graph: X2 · Variables passed to the simulation: `v2, s1, x6, x8`

**Common Control**

```
$v2 = rand(2,4)
$s1 = randfrom("0,0.5,1")
$x4 = $v2 + 2*$s1
$x6 = $x4 - rand(5,8) where ($x6 != 0)
$x8 = $x6 + rand(1,2) where ($x6 + $x8 != 0)
$answer = $v2/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.5&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Acceleration from a curve" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>position vs. time</b> graph. The cart starts from rest and speeds up steadily from 0 to 2 s, reaching the position shown at t = 2 s. What is its acceleration during those 2 s?</p>
<p>Use three significant figures.</p>
<p>a = $answerbox m/s²</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.5&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" title="Motion Graphs Lab: Acceleration from a curve, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=2.5&v2=$v2&s1=$s1&x6=$x6&x8=$x8&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.1 · Reading velocity

Graph: V1 · Variables passed to the simulation: `p, q, r`

**Common Control**

```
$q = rand(1,2)
$p = $q + rand(1,2)
$r = $q + rand(1,3)
$answer = ($q + $r)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.1&p=$p&q=$q&r=$r&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Reading velocity" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's velocity at <b>t = 4 s</b>?</p>
<p>Use three significant figures.</p>
<p>v = $answerbox m/s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.1&p=$p&q=$q&r=$r&mode=solution" title="Motion Graphs Lab: Reading velocity, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.1&p=$p&q=$q&r=$r&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.2 · Acceleration from slope

Graph: V1 · Variables passed to the simulation: `p, q, r`

**Common Control**

```
$q = rand(1,2)
$p = $q + rand(1,2)
$r = $q + rand(1,3)
$answer = -$r/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.2&p=$p&q=$q&r=$r&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Acceleration from slope" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's acceleration at <b>t = 6 s</b>?</p>
<p>Use three significant figures.</p>
<p>a = $answerbox m/s²</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.2&p=$p&q=$q&r=$r&mode=solution" title="Motion Graphs Lab: Acceleration from slope, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.2&p=$p&q=$q&r=$r&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.3 · Displacement as area

Graph: V1 · Variables passed to the simulation: `p, q, r`

**Common Control**

```
$q = rand(1,2)
$p = $q + rand(1,2)
$r = $q + rand(1,3)
$answer = ($p + $q)/2 + 2*$q + ($q + $r)
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.3&p=$p&q=$q&r=$r&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Displacement as area" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's displacement from <b>t = 0 s</b> to <b>t = 5 s</b>?</p>
<p>Use three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.3&p=$p&q=$q&r=$r&mode=solution" title="Motion Graphs Lab: Displacement as area, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.3&p=$p&q=$q&r=$r&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.4 · Greatest acceleration

Graph: V1 · Variables passed to the simulation: `p, q, r`

**Common Control**

```
$q = rand(1,2)
$p = $q + rand(1,2)
$r = $q + rand(1,3)
$answer = ($r - $q)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.4&p=$p&q=$q&r=$r&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Greatest acceleration" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's greatest positive acceleration?</p>
<p>Use three significant figures.</p>
<p>a = $answerbox m/s²</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.4&p=$p&q=$q&r=$r&mode=solution" title="Motion Graphs Lab: Greatest acceleration, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.4&p=$p&q=$q&r=$r&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 3.5 · Whole-trip displacement

Graph: V1 · Variables passed to the simulation: `p, q, r`

**Common Control**

```
$q = rand(1,2)
$p = $q + rand(1,2)
$r = $q + rand(1,3)
$answer = ($p + $q)/2 + 2*$q + ($q + $r) + $r
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.5&p=$p&q=$q&r=$r&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Whole-trip displacement" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's displacement from <b>t = 0 s</b> to <b>t = 8 s</b>?</p>
<p>Use three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.5&p=$p&q=$q&r=$r&mode=solution" title="Motion Graphs Lab: Whole-trip displacement, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=3.5&p=$p&q=$q&r=$r&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.1 · Momentarily at rest

Graph: V2 · Variables passed to the simulation: `p, q, m, n`

**Common Control**

```
$p = rand(2,4)
$q = rand(1,$p-1)
$m = rand(2,4)
$n = rand(1,3) where ($n != $p && ($p + $q)/2 + 2*$q - 4*$m + $n != 0)
$t1 = 2*$q/($q + $m)
$t2 = 2*$m/($m + $n)
$answer = 2 + $t1
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.1&p=$p&q=$q&m=$m&n=$n&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Momentarily at rest" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. At what time does the cart first come to rest (for an instant)?</p>
<p>Use three significant figures.</p>
<p>t = $answerbox s</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.1&p=$p&q=$q&m=$m&n=$n&mode=solution" title="Motion Graphs Lab: Momentarily at rest, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.1&p=$p&q=$q&m=$m&n=$n&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.2 · Turning around

Graph: V2 · Variables passed to the simulation: `p, q, m, n`

**Common Control**

```
$p = rand(2,4)
$q = rand(1,$p-1)
$m = rand(2,4)
$n = rand(1,3) where ($n != $p && ($p + $q)/2 + 2*$q - 4*$m + $n != 0)
$t1 = 2*$q/($q + $m)
$t2 = 2*$m/($m + $n)
$answer = (-$m - $q)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.2&p=$p&q=$q&m=$m&n=$n&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Turning around" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's acceleration at <b>t = 3 s</b>?</p>
<p>Use three significant figures.</p>
<p>a = $answerbox m/s²</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.2&p=$p&q=$q&m=$m&n=$n&mode=solution" title="Motion Graphs Lab: Turning around, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.2&p=$p&q=$q&m=$m&n=$n&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.3 · Negative area

Graph: V2 · Variables passed to the simulation: `p, q, m, n`

**Common Control**

```
$p = rand(2,4)
$q = rand(1,$p-1)
$m = rand(2,4)
$n = rand(1,3) where ($n != $p && ($p + $q)/2 + 2*$q - 4*$m + $n != 0)
$t1 = 2*$q/($q + $m)
$t2 = 2*$m/($m + $n)
$answer = ($p + $q)/2 + 2*$q - 4*$m + $n
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.3&p=$p&q=$q&m=$m&n=$n&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Negative area" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's displacement from <b>t = 0 s</b> to <b>t = 8 s</b>?</p>
<p>Use three significant figures.</p>
<p>Δx = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.3&p=$p&q=$q&m=$m&n=$n&mode=solution" title="Motion Graphs Lab: Negative area, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.3&p=$p&q=$q&m=$m&n=$n&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.4 · Total distance

Graph: V2 · Variables passed to the simulation: `p, q, m, n`

**Common Control**

```
$p = rand(2,4)
$q = rand(1,$p-1)
$m = rand(2,4)
$n = rand(1,3) where ($n != $p && ($p + $q)/2 + 2*$q - 4*$m + $n != 0)
$t1 = 2*$q/($q + $m)
$t2 = 2*$m/($m + $n)
$answer = ($p + $q)/2 + $q + $q*$t1/2 + $m*(2 - $t1)/2 + 2*$m + $m*$t2/2 + $n*(2 - $t2)/2
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.4&p=$p&q=$q&m=$m&n=$n&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Total distance" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What total distance does the cart travel from <b>t = 0 s</b> to <b>t = 8 s</b>?</p>
<p>Use three significant figures.</p>
<p>d = $answerbox m</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.4&p=$p&q=$q&m=$m&n=$n&mode=solution" title="Motion Graphs Lab: Total distance, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.4&p=$p&q=$q&m=$m&n=$n&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

## 4.5 · Average acceleration

Graph: V2 · Variables passed to the simulation: `p, q, m, n`

**Common Control**

```
$p = rand(2,4)
$q = rand(1,$p-1)
$m = rand(2,4)
$n = rand(1,3) where ($n != $p && ($p + $q)/2 + 2*$q - 4*$m + $n != 0)
$t1 = 2*$q/($q + $m)
$t2 = 2*$m/($m + $n)
$answer = ($n - $p)/8
$reltolerance = 0.02
$stua = getstuans($stuanswers, $thisq)
$simurl = "https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.5&p=$p&q=$q&m=$m&n=$n&mode=show"
$simurl = $simurl . "&launch=$stua" if ($stua != "")
```

**Question Text**

```html
<div style="max-width:820px">
<iframe src="$simurl" title="Motion Graphs Lab: Average acceleration" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%">Watch the cart and its graph. After you submit, your answer is drawn on the graph. Tap to replay. <a href="$simurl" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
<p>Use the cart's <b>velocity vs. time</b> graph. What is the cart's average acceleration from <b>t = 0 s</b> to <b>t = 8 s</b>?</p>
<p>Use three significant figures.</p>
<p>a<sub>ave</sub> = $answerbox m/s²</p>
```

**Detailed Solution**

```html
<p>The correct answer is drawn on the graph. Tap the picture to replay the run.</p>
<div style="max-width:820px">
<iframe src="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.5&p=$p&q=$q&m=$m&n=$n&mode=solution" title="Motion Graphs Lab: Average acceleration, solution" loading="lazy" style="width:100%;aspect-ratio:1.55;height:auto;min-height:340px;border:0;border-radius:6px"></iframe>
<p style="font-size:85%"> <a href="https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html?level=4.5&p=$p&q=$q&m=$m&n=$n&mode=solution" target="_blank" rel="noopener">Open in a new tab</a></p>
</div>
```

---

# Physics Simulations

Browser physics simulations by Jeff Gagnon, Springfield College, for introductory physics courses.
Everything runs in the browser: no installs or accounts needed.

## Live simulations

| Simulation | Topic | Questions |
|---|---|---|
| [Physics Proving Ground](https://jlgagnon-glitch.github.io/Physics-Simulations/proving-ground.html) | Launch challenges: motion, forces, energy, rotation | 16 levels |
| [Vector Range](https://jlgagnon-glitch.github.io/Physics-Simulations/vectors.html) | Vectors: components, addition, subtraction (Lectures 3–4) | 20 problems |
| [Motion Graphs Lab](https://jlgagnon-glitch.github.io/Physics-Simulations/motion-graphs.html) | Reading position and velocity graphs (Lecture 6) | 20 questions |
| [Constant Acceleration Lab](https://jlgagnon-glitch.github.io/Physics-Simulations/kinematics.html) | One-dimensional motion with constant acceleration (Lecture 7) | 20 questions |
| [Air Track Collision Lab](https://jlgagnon-glitch.github.io/Physics-Simulations/air-track.html) | Collisions and explosions: momentum, kinetic energy, coefficient of restitution | Open lab with presets and data export |
| [Elbow Flexor Torque Lab](https://jlgagnon-glitch.github.io/Physics-Simulations/elbow-torque.html) | Static equilibrium: torque balance at the elbow with three flexor muscles | Open lab with random problems and answer checking |
| [Shoulder Abduction Torque Lab](https://jlgagnon-glitch.github.io/Physics-Simulations/shoulder-torque.html) | Static equilibrium: torque balance at the shoulder with the deltoid and supraspinatus | Open lab with random problems and answer checking |

All of them on one page: **https://jlgagnon-glitch.github.io/Physics-Simulations/**

MyOpenMath code for each simulation: [Proving Ground](proving-ground-myopenmath.md) ·
[Vector Range](vectors-myopenmath.md) · [Motion Graphs Lab](motion-graphs-myopenmath.md) ·
[Constant Acceleration Lab](kinematics-myopenmath.md)

## Physics Proving Ground

`proving-ground.html` has 16 levels in four chapters: Motion, Forces, Energy and Rotation. In each level
students calculate one quantity, launch, and watch whether their answer hits the target. The levels use
random numbers, give feedback, and offer a worked solution.

### Opening one level from a link

Settings in the link lock the page to a single level with given numbers:

```
proving-ground.html?level=1.1&h=1.2&d=2.4&mode=test
```

| Setting | Meaning |
|---|---|
| `level` | Level number as shown on the buttons, `1.1` to `4.4` (or `1` to `16`) |
| one name per number | The level's numbers, e.g. `h` and `d` for level 1.1 (see the MyOpenMath file for each level's names). Any number left out is chosen at random. |
| `mode=test` | Show only the picture of the setup: no answer box, Launch button or feedback. Use this inside graded questions. |
| `mode=solution` | Show only the picture, launch the correct answer on its own, and replay when tapped. For MyOpenMath's Detailed Solution, which students see after answering. |
| `solution=0` | Never show the worked solution |

When the link sets a level, the level menu, stars and "New numbers" button are hidden, and nothing is
saved in the browser. With no settings, the full game opens as usual.

## Vector Range

`vectors.html` has 20 vector problems in four chapters: Components, Adding two, Adding many and
Subtracting. They're based on the PHYS 205 Lecture 3 (graphical method) and Lecture 4 (analytical method)
examples. The given vectors slide tip-to-tail to mark a target, and the student's answer is drawn
from the origin: as one arrow for magnitude and direction, or as x then y for components.

Links work the same way as the Proving Ground, with `q=1.1` to `q=4.5` choosing the problem. Its
answers have two values, so `launch` takes both, separated by a comma: `launch=13.2,40.9`.
`vectors-myopenmath.md` has two-part (Multipart) MyOpenMath code for all 20 problems, and
`build_vectors_myopenmath.py` regenerates it.

## Motion Graphs Lab

`motion-graphs.html` has 20 questions based on the PHYS 205 Lecture 6 examples (graphical interpretation
of motion), in four chapters: Position graphs, Curved position, Velocity graphs and Turning around.
A cart rolls along a lab track in front of a motion detector, with ghost images each whole second, while a
cursor traces its x–t or v–t graph. After an answer, it's drawn on the graph: a point, slope line, chord,
time marker, landing spot or odometer reading.

Links use `level=1.1` to `level=4.5` to choose the question, because `q` is one of the graph's numbers.
`motion-graphs-myopenmath.md` has MyOpenMath code for all 20, and `build_graphs_myopenmath.py`
regenerates it.

## Constant Acceleration Lab

`kinematics.html` has 20 questions based on the PHYS 205 Lecture 7 examples (one-dimensional motion
with constant acceleration), in four chapters: Speeding up, Slowing down, Two stages and Free fall. Each
runs in its own scene: a running track, a road, a night road with a deer, an ice rink with a game clock, a
ball thrown up beside a height pole, and a high jump. A speedometer, stopwatch and distance or height
markings stay blank when they would give the answer away. Questions 2.5 and 4.3 replay the motion with the
student's own value.

Links use `level=1.1` to `level=4.5`. `kinematics-myopenmath.md` has MyOpenMath code for all 20, and
`build_kinematics_myopenmath.py` regenerates it.

### MyOpenMath (Proving Ground)

`proving-ground-myopenmath.md` has ready-to-paste Common Control and Question Text for all
16 levels. MyOpenMath picks the numbers and grades the answer, and it shows the simulation for
those exact numbers in an iframe. `build_myopenmath.py` regenerates that file, for example
after a change to the site address or the tolerance.

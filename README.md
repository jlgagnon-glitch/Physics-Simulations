# Physics Simulations

Browser physics simulations by Jeff Gagnon, Springfield College, for introductory physics courses.
Everything runs in the browser: no installs or accounts needed.

Live site: https://jlgagnon-glitch.github.io/Physics-Simulations/

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

### MyOpenMath

`proving-ground-myopenmath.md` has ready-to-paste Common Control and Question Text for all
16 levels. MyOpenMath picks the numbers and grades the answer, and it shows the simulation for
those exact numbers in an iframe. `build_myopenmath.py` regenerates that file, for example
after a change to the site address or the tolerance.

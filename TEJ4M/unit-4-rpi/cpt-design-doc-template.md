# Sumo Robot: [Robot Name]

**[Team Name]** — [Names]

> *2–3 sentences: what the robot does, what competition strategy you chose, and what extensions (if any) you added beyond the guided build. Write this last — it's a summary of the whole document.*

---

## Design

### What the Robot Needs to Do

> *List your robot's functional requirements — what it must do to compete. Be specific enough that each item can be tested. "Move forward" is not a requirement. "Detect the ring boundary and reverse before crossing, on the arena surface" is.*

### Success Criteria

> *For each requirement above, describe a concrete test: what you measure, how many trials, on what surface, and what counts as passing. These criteria should be testable before competition. A criterion that can only be evaluated on competition day is not a criterion — it's a hope.*

| Requirement | How you tested it | Pass condition |
|-------------|------------------|----------------|
| | | |
| | | |
| | | |

### System Architecture

> *A diagram of your robot's states and the conditions that trigger transitions between them. Draw it on paper and photograph it, or draw it digitally. Label every state and every transition arrow with the sensor condition or event that causes it. Even a two-state robot should have this diagram.*

![State machine or behaviour diagram](images/state-diagram.jpg)
*[Caption: Identify each state and label what triggers each transition — which sensor, which condition, which threshold.]*

### Circuit Design

> *A labeled schematic of your complete circuit. This is not a photo of your breadboard — it is a diagram showing how the circuit is designed. Every component must be labeled: resistor values, capacitor value, GPIO pin numbers, power and ground rails. Hand-drawn on paper and photographed is acceptable.*

![Circuit schematic — hand-drawn or digital, fully labeled](images/circuit-schematic.jpg)
*[Caption: Note any component choices that required a decision — for example, capacitor value or a voltage protection resistor — and briefly state the reasoning.]*

### Physical Layout

> *A top-down sketch of the chassis showing where each major component sits: Pi, motor driver, motors, sensors, breadboard, battery pack. Label cable routing paths. Draw this before or during the build, not after. Pre-build thinking is the evidence this section is looking for.*

![Top-down chassis layout sketch with component labels](images/chassis-layout.jpg)
*[Caption: Note any placement decisions made for a specific reason — cable run length, centre of mass, sensor clearance from the surface.]*

---

## Build

> *This section should tell the story of the build — what you planned, what you discovered, what changed. Finished-robot-only photos are not build evidence. Include in-progress photos at meaningful stages.*

### Chassis

> *How was the chassis assembled? If you modified or replaced the guided-build chassis, describe what changed and why. Photos should show the structural state of the robot before major components were added.*

![Chassis frame assembled before any wiring or electronics are mounted](images/chassis-frame.jpg)
*[Caption: Show the chassis in a state that no longer exists. Describe what stage of construction this represents.]*

![Component or sensor mounting detail — close-up](images/mount-detail.jpg)
*[Caption: Show how a specific component is mounted, secured, or positioned. What makes it stable? Can it be adjusted or removed?]*

### Wiring

> *Describe your wiring approach: how wires are routed, how they are secured, and any decisions you made about keeping circuits separate. The final state should show clean cable management — no floating wires, ribbon cable folded within the footprint, zip ties trimmed.*

![Wiring at an early or intermediate stage — before cleanup](images/wiring-early.jpg)
*[Caption: This photo should show a state of the wiring that no longer exists. Describe what was working at this stage and what still needed to be done.]*

![Final wiring — full robot, showing cable management](images/wiring-final.jpg)
*[Caption: Point out the cable routing paths and how wires are secured. Note anything that changed from the original wiring plan and why.]*

### Decisions Made During the Build

> *Document at least two decisions that came from actually building and testing — not planned in advance. What did you discover when you ran the code or measured a value for the first time? What changed as a result? A decision made in response to an actual test result is the strongest evidence in this section.*

### Calibration

> *Your edge detection threshold must be calibrated on the actual arena surface. Record your measurements in a table. A number in your code with no calibration record is not evidence — it's a guess.*
>
> *Your table should include at minimum: the arena surface, the boundary surface, and at least one other surface for comparison. Record mean RC time, the range or standard deviation, and number of samples. Then explain, in terms of those numbers, how you chose your threshold value.*

| Surface | Mean RC time (s) | Range or std dev | Samples |
|---------|-----------------|------------------|---------|
| | | | |
| | | | |
| | | | |

**Chosen threshold:** `EDGE_THRESHOLD = ` — *[Explain why this specific value, in terms of the measurements above. How much margin does it give you on each side?]*

![Robot on the ring surface during calibration](images/calibration-on-ring.jpg)
*[Caption: Show the robot positioned on the arena mat — the ring surface should be visible in the frame. This confirms the calibration was done on the actual arena, not a bench or floor.]*

![Terminal output showing RC timing readings from calibration](images/calibration-output.jpg)
*[Caption: A screenshot or photo of your terminal showing live readings from the ring surface and boundary. This is the raw data behind your threshold value.]*

---

## Code

> *Your full source is in `src/`. This section explains the key parts — do not paste entire files. A reader should be able to understand what your robot does and why the code is written the way it is, without running it.*

### Project Structure

```
src/
├── [filename].py     — [one-line description of what this file does]
├── [filename].py     — [one-line description]
```

### [Name this section after the algorithm — e.g., Edge Detection]

> *Paste only the relevant function or block — not the whole file. Then explain in prose: how does this code work, and why is it written this way? The explanation should go beyond what the variable names already say. What decision did you make here, and what was the alternative?*

```python
# paste snippet here
```

*[Explanation of the algorithm and the decisions behind it.]*

### [Name this section after the next key algorithm — e.g., Main Loop]

> *Repeat the same pattern: snippet, then explanation. If your robot uses a state machine, show how the states are represented in code and how transitions are triggered.*

```python
# paste snippet here
```

*[Explanation.]*

### GPIO Cleanup

> *Show your `try/finally` block. Then explain: what happens to the GPIO pins if the program crashes without cleanup? Why is `finally` necessary and not just `except KeyboardInterrupt`?*

```python
# paste your try/finally block here
```

*[Explanation.]*

![Screenshot of the program running during a test — terminal output visible](images/test-run-terminal.jpg)
*[Caption: Show evidence that your code was tested before competition day — terminal output, a test run on the bench, or the drive test harness in use.]*

---

## Competition & Reflection

### Results

| Round | Placement | Bonus points | Round total |
|-------|-----------|-------------|-------------|
| Round 1 | | | |
| Round 2 | | | |
| Round 3 | | | |
| **Total** | | | |

![Robot on the competition ring — at least one photo from a live round](images/competition.jpg)
*[Caption: Note which round this was and what was happening at this moment.]*

### What Worked

> *Be specific. "Edge detection worked well" is an observation, not analysis. Explain why it worked — which decisions (hardware, calibration, code) produced consistent performance, and what evidence from competition confirms it.*

### What Failed

> *Name exact failure modes. For each one: what happened, and why did it happen at the hardware or code level? "We drove off the edge" is an observation. "We drove off the edge because EVADE always reverses along the current heading, and after a lateral hit our heading was pointing out of the ring" is analysis. A reader should be able to understand the root cause without seeing the robot.*

### Next Iteration

> *At least two specific improvements, each grounded in a failure mode you documented above. Not wishlist features — direct responses to observed problems. Each improvement should be specific enough to act on: what exactly would you change, and how would it fix the failure?*

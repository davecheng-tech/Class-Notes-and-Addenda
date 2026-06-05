# CPT: Autonomous Sumo Robot

Build and compete with an autonomous sumo robot using the Raspberry Pi platform from this unit. This project counts for **15% of your final course mark.**

Groups of 2–3. Groups must be finalized by end of class on **June 2**.

---

## The Competition

### Ring

The arena is a donut-shaped ring on a white surface with a black border around the outer and inner edges of the ring. Your robot should be able to detect these boundary lines to remain in the ring.

### Format

**4-robot battle royale.** All four robots compete in the ring at the same time. Last robot remaining wins the round.

Groups of four robots rotate through multiple rounds in a round-robin schedule. Points accumulate across all rounds.

### Scoring

| Event | Points |
|-------|--------|
| Last robot standing | 3 |
| Eliminated 3rd (2nd-to-last) | 2 |
| Eliminated 2nd | 1 |
| Eliminated 1st | 0 |
| Causing an elimination (pushout or flip) | +2 per robot |

Pushout attribution is determined by the referee. In ambiguous cases — chain contacts, a robot driving itself out — no bonus is awarded.

### Rules

**Start mechanism**
- Started by a physical input on the robot — button, switch, or equivalent. No SSH starts during rounds.
- Referee confirms each robot's start method before the round.
- Countdown: ref counts from 10 → handlers press start at "3" and step back → robots move at "0". Your 3-second code delay must match this window.

**Autonomous only**
- No SSH or remote control once the round starts.
- Any robot receiving commands mid-round is disqualified from that round.

**Out of bounds (elimination)**
- Eliminated when no part of the chassis remains on the ring surface.
- Any contact counts — a single wheel or slider tip keeps you in play.
- Referee makes the final call.

**Keep moving**
- A robot that stops moving is eliminated at referee discretion.

**Engagement requirement** — the robot must respond to its environment.
- *What's required:* movement that reacts to sensor input (ring edges, opponent contact, or other inputs). Edge detection used to actively stay in the ring counts as engaged.
- *What gets a warning:* a fixed open-loop pattern with no sensor response — circling in place, oscillating on a timer, repeating arc.
- *The test is the wander pattern itself*, not whether reactive code exists or fires:
  - Wander with positional variety (changes direction, covers different areas) → fine, even if reactive code never triggers because conditions never arise.
  - Tight fixed path (small circle, back-and-forth, repeating arc) → warning, regardless of what other sensor code is present. The movement itself is indistinguishable from open-loop.
- *Process:* warning logged against the group → free to SSH and modify code between rounds → same behaviour in your next round = eliminated from the remainder of the tournament.

**Permitted contact** — governing principle: *displacement, not damage.*
- Allowed: any mechanism that moves, lifts, topples, or displaces — scoops, lifter arms, lateral pushers, servo-actuated flippers.
- Not allowed: mechanisms designed to snag, pierce, or damage components, whether motorized or passive.
- Referee has final authority on novel mechanisms and may require modification before a round.
- Damaging another robot = disqualified from the tournament.

**Maximum size**
- Footprint ≤ U.S. Letter (8.5 × 11 in / 215.9 × 279.4 mm), measured at widest and longest points.
- Height is not restricted.
- Checked before the first round.

---

## Your Robot

### Minimum viable robot

The guided build (Labs 03–05) gives you a working platform. To compete, your robot must:

1. Start autonomously via a physical button press on the robot — no SSH
2. Wait 3 seconds after the button press before moving
3. Drive forward under autonomous control (wander state)
4. Detect the boundary line and respond — reverse and turn, or equivalent
5. Run the entire match without SSH control

This is achievable with what you built in the guided labs. The photoresistor circuit, motor control, and start button are already in your codebase.

### Extensions

The guided build is the floor, not the ceiling. Teams that add capability have more to compete with and more to write about.

**Opponent detection — HC-SR04 ultrasonic**
Detect robots in front of you and charge. A distance threshold triggers a forward charge; outside that range, the robot wanders and scans. Ask your teacher for an HC-SR04 if you want to attempt this.

**Multi-sensor edge detection**
Add photoresistors at the rear or side corners so your robot knows *which* edge it hit and can respond directionally.

**Custom chassis**
Modify or replace the guided-build chassis. Laser cutting is available — speak to your teacher. Custom work should fit within an 11 × 17 inch sheet of corrugated cardboard. Reference file: [Chassis CAD (OnShape)](https://cad.onshape.com/documents/5348ff0bd57b3a2cea242434/w/6562db79663996135ecdf5b8/e/768ff86290f46d6c1236f710)

**Manual testing harness**
A `curses`-based keyboard driver lets you drive the robot with arrow keys during testing without modifying your autonomous code. Ask your teacher for a reference.

**Threading**
Run sensor polling and motor control concurrently using Python's `threading` module to eliminate sensor blocking during motor transitions.

> [!NOTE]
> Extensions are not required for L4. A minimum viable robot with thorough documentation, honest calibration records, and a detailed post-mortem can achieve L4. Extensions are one path to L4+; the other is the quality of your documentation and reflection.

---

## Milestones

| Date | Milestone |
|------|-----------|
| **Jun 2** | Groups finalized. Rolling chassis proof video submitted (completion mark). CPT rubric reviewed in class. |
| **Jun 5** | Floor check: edge detection running on your assembled physical robot. Not submitted — your teacher will check in with each group. Groups without a working robot by end of Jun 5 receive a check-in on Jun 8. |
| **Jun 10** | Feature freeze. No new hardware or code features after today. Jun 10 is for calibration, final testing, and completing your document. |
| **Jun 11** | Official test battle day. Practice rounds and final calibration on the ring surface. |
| **Jun 12** | Tournament day. |
| **Jun 13, 11:59 PM** | Final document submission due. |

> [!IMPORTANT]
> **Calibrate on the actual ring surface.** RC timing threshold values differ between your bench setup and the arena mat. Budget time on Jun 11 to recalibrate before your first scored round.

---

## Deliverable

Submit a single `.zip` archive:

```
groupname.zip
├── README.md
├── images/
└── src/
```

**`README.md`** is your main design document, written in Markdown. It covers all four rubric categories: your design intent, build process with photos, key code explained with annotated snippets, and your reflection. The full source files live in `src/` — do not paste entire files inline.

**`images/`** contains all photos referenced in `README.md`. Photograph your build as you go — chassis assembly, breadboard layout, wiring decisions, anything you rebuild. In the final document, include photos that mark meaningful stages, not every adjustment. A photo of your robot on the ring surface mid-calibration is more useful than five photos of the finished robot from different angles.

**`src/`** contains all Python source files. Diagrams can be hand-drawn — photograph your sketch on paper and include it in `images/`. A labeled hand-drawn circuit diagram is fine.

---

## Rubric

| Category | Weight |
|----------|--------|
| Engineering Design & Planning | 15% |
| Build Quality & Technical Evidence | 30% |
| Software Implementation | 25% |
| Competition Performance & Reflection | 30% |

---

### Engineering Design & Planning

*Evidence of pre-build thinking: what the robot needs to do, how the hardware and software will be structured, and how success will be measured.*

| Level | Descriptor |
|-------|-----------|
| **4+** | Design documents are specific, connected, and anticipatory. Success criteria are testable and tied directly to the competition format. Circuit and physical layout diagrams are detailed enough that another builder could reproduce the design. The plan shows awareness of real constraints — sensor placement, cable routing, weight distribution. Every design element connects to something in the finished robot. |
| **4** | Design documents clearly state what the robot needs to do, with measurable success criteria. Circuit and physical diagrams are present and labeled. There is genuine evidence of pre-build thinking, not retroactive documentation. |
| **3** | Required design elements are present but success criteria are vague or diagrams are incomplete. Planning occurred but the documents don't fully connect to the finished robot. |
| **2** | Design documentation is partially complete. Goals are generic, diagrams lack labels or key connections, or there is little evidence the documents were created before building. |
| **1** | Design documentation is minimal, missing major elements, or does not reflect the robot that was built. |

---

### Build Quality & Technical Evidence

*Physical build quality and evidence of the build process: clean construction, cable management, in-progress photos, calibration records, and notes on decisions made during construction. Build quality is assessed both through photos in the document and through teacher observation during open build periods.*

| Level | Descriptor |
|-------|-----------|
| **4+** | The physical build meets a professional standard: no tape, minimal glue used only where structurally necessary, all wires routed and secured along the chassis, ribbon cable folded within the stack footprint, zip ties trimmed flush. The robot could be fully disassembled and all components recycled cleanly by someone who didn't build it. The document tells a complete engineering story: what was planned, what was discovered, what changed and why. Calibration values are recorded with context — not just the threshold number, but what it means on that specific hardware and surface. A reader could reconstruct the build and troubleshooting arc from the document alone. |
| **4** | Clean build standard is mostly met — cable management is present, no floating wires, zip ties trimmed, tape absent or used minimally with clear justification. Build progress is documented with in-progress photos at meaningful stages. Calibration or test results are recorded. There is evidence of at least one decision made in response to a real test result. |
| **3** | Some effort at cable management but inconsistent — tape used in places, some wires unsecured or floating. Build evidence is present but uneven, mostly finished-robot photos with brief notes. Some testing or calibration is mentioned but not detailed. |
| **2** | Minimal cable management — wires tangled or floating, tape used liberally. Build evidence is limited to final-state photos with little or no documentation of testing, calibration, or construction decisions. |
| **1** | No attention to build quality or build documentation. |

---

### Software Implementation

*Quality, clarity, and safety of the robot's code — and the ability to explain key design decisions through annotated snippets in the document.*

| Level | Descriptor |
|-------|-----------|
| **4+** | The code and document together constitute a complete technical explanation of how and why the system works. Key algorithms are explained with annotated snippets a reader can follow without running the code. `try/finally` is used correctly — GPIO cleanup is guaranteed regardless of how the program exits, not only on `KeyboardInterrupt`. Named constants are used throughout. The structure of the code reflects the architecture described in the design documents. |
| **4** | Code is organized, readable, and safe. GPIO cleanup is present and correct. Key algorithms are explained with annotated snippets. A reader can identify which functions handle sensing and which handle motion. |
| **3** | Code is functional and mostly readable. GPIO cleanup is present but may be incomplete. Snippets are included in the document but explanations are thin. |
| **2** | Code runs but is difficult to follow. GPIO cleanup is missing or incorrect. Key logic is not explained in the document. |
| **1** | Code is incomplete, non-functional, or submitted as files with no explanation in the document. |

---

### Competition Performance & Reflection

*What the robot did on competition day, and an honest technical analysis of what worked, what failed, and what a next iteration would look like.*

| Level | Descriptor |
|-------|-----------|
| **4+** | The post-mortem is technically specific and honest regardless of competition result. It names exact failure modes tied to actual hardware and cites evidence from testing or competition. If the robot performed poorly, the reflection explains why with enough precision to serve as a design brief for a redesign. The analysis demonstrates understanding of the system — not just what happened, but why. Competition performance also shows autonomous behaviour beyond minimum viable: a wander strategy, opponent response, or consistent edge survival across multiple rounds. |
| **4** | Post-mortem addresses what worked and what didn't with specific references to the robot's actual behaviour. Competition result is honestly assessed. Causes of failure go beyond surface observation. Robot ran autonomously and demonstrated consistent edge detection during competition. |
| **3** | Post-mortem covers the main events of competition day but is more narrative than analytical. Causes of failure are identified at a surface level without deeper diagnosis. Robot ran autonomously and attempted edge detection, even if inconsistently. |
| **2** | Reflection is brief and generic. Competition result is described but not analyzed. Robot moved autonomously but edge detection was unreliable or not demonstrated. |
| **1** | Reflection is absent or superficial. Robot did not run autonomously, or required SSH control during a match. |

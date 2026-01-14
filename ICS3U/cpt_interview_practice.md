# ICS3U CPT – Code Walkthrough & Peer Interview Practice

While the time to make changes to your application is over, the remaining classes are still valuable. Today you will use your finished codebase as a study object to practice explaining, reasoning about, and defending the design and implementation decisions already present. This directly mirrors the technical interview, where understanding, ownership, and correct use of ICS3U concepts matter more than adding new features. This directly prepares you for the **technical interview**, which assesses ownership, understanding, and authenticity.

## Activity Overview

You will work in **pairs** (not necessarily your original partner, if you had one).

Each student will take turns as:
- **Author** – the person whose code is being reviewed
- **Reviewer** – the person asking questions and probing understanding

Both roles will help you prepare for your own interview.

## Ground Rules

- Code is **read-only**. Do not edit, refactor, or "fix" anything.
- You may run the program locally.
- You may scroll, search, and navigate the code freely.
- You may take notes for yourself.
- Though not graded, this does mirror interview conditions.


## Part 1 – Silent Review (5 minutes)

**Reviewer instructions:**
1. Run the program once without commentary.
2. Observe and note:
   - What the program does.
   - How the user interacts with it.
   - What appears to change over time (state).
3. Skim the code structure:
   - Locate `setup()` and `draw()`.
   - Identify any helper methods.
   - Note any significant data structures (arrays, ArrayLists, HashMaps, PVectors).

**Author instructions:**
- Do not explain or interrupt.
- Observe what the reviewer notices, misunderstands, or ignores.
- Take mental notes about gaps between intent and perception.


## Part 2 – Guided Code Walkthrough (10–15 minutes)

**Author role:** Lead the walkthrough.  
**Reviewer role:** Ask clarification and probing questions.

### Step 1 – High-level explanation

**Author:**
- Explain the main idea of the program.
- Describe the core interaction loop.
- Identify what counts as program state.

**Reviewer:**
- Ask clarifying questions if explanations are vague.
- Prompt with questions such as:
  - "What problem or idea is this program exploring?"
  - "Where does user input actually affect behaviour?"

### Step 2 – Structural walkthrough

Proceed in this order:

1. **Global variables**
   - **Author:** Explain what each major variable stores and why it must persist.
   - **Reviewer:** Ask what would break if a variable were local instead.

2. **`setup()`**
   - **Author:** Explain what is initialized once and why.
   - **Reviewer:** Ask why this code does not belong in `draw()`.

3. **`draw()`**
   - **Author:** Explain what runs every frame and how flow is controlled.
   - **Reviewer:** Ask where decisions happen and what booleans control behaviour.

4. **Methods**
   - **Author:** Explain what problem each method solves.
   - **Reviewer:** Ask about parameters, return values, and side effects.

## Part 3 – Concept Check (Interview-Style)

**Reviewer:** Choose 3–5 prompts below. Ask them one at a time.  
**Author:** Answer using specific parts of your own code as evidence.

### Core ICS3U concepts

- **Booleans:**
  - Reviewer: "Show where a boolean controls behaviour."
  - Author: Point to the variable and explain its effect.

- **Conditionals:**
  - Reviewer: "Show a conditional that actually matters."
  - Author: Explain what happens when each condition is true or false.

- **Loops:**
  - Reviewer: "Identify a loop and explain why it is needed."
  - Author: Explain what repeats and why repetition is required.

- **Methods:**
  - Reviewer: "Explain this method’s parameters and return value."
  - Author: Describe what the method guarantees.

- **Arrays / ArrayLists:**
  - Reviewer: "Why was this structure chosen?"
  - Author: Justify the choice in plain language.

### Deeper reasoning

Use these when the author can already answer basic “what does this do?” questions. These prompts check whether they understand *why* the code is structured the way it is, and whether they can reason about alternatives.

**Reviewer:** Examples of deeper-reasoning questions

- **State and flow control**
  - "What are the different states or modes of your program (menu, playing, paused, game over, etc.) and what triggers the transitions between them?"
  - "If a bug appears only sometimes, what variables would you inspect first to understand the program’s current state?"

- **Separation of responsibilities**
  - "Which method is responsible for updating logic vs drawing visuals? How do you keep those responsibilities separate?"
  - "Where is input handled, and why did you choose to handle it there instead of inside `draw()` (or the reverse)?"

- **Data representation choices**
  - "What is the smallest set of variables needed to represent one ‘thing’ in your program (player, enemy, particle, button)? Why those?"
  - "Why did you choose multiple parallel arrays/variables versus grouping related values together in a single structure or pattern?"

- **Timing and consistency**
  - "How does your code make movement and animation feel consistent frame-to-frame? What would change if the frame rate dropped?"
  - "Where do you use counters, timers, or cooldowns, and what problem do they solve?"

- **Edge cases and correctness**
  - "What edge cases did you have to handle (screen edges, repeated keypress, double-click, overlapping objects), and where is that logic enforced?"
  - "Point to one condition that prevents a feature from triggering at the wrong time. What would happen if it were removed?"

- **Tradeoffs and alternatives**
  - "If you had to simplify this feature by 50% but keep the core idea, what would you remove first and why?"
  - "Describe one alternative implementation you considered (or could have used) and why you did not choose it."

**Author:** 
- Start with the concept (what problem it solves).
- Then point to the code location.
- Then describe a simple counterfactual (what breaks or changes if you remove/alter it).
- Avoid line-by-line narration.

## Part 4 – Authenticity Stress Test

**Reviewer:** Ask one of the following.

- "If you had to rebuild this feature from scratch, what would you start with?"
- "Which part of this code would be hardest to rewrite without looking? Why?"
- "Which part of this code are you least confident explaining?"

**Author:**
- Answer honestly.
- Identify specific concepts or structures that need review.
- Avoid vague answers.


## Part 5 – Design Reflection (5 minutes)

**Author:**
- Identify one design choice you are satisfied with.
- Identify one area that is overly complex.
- Describe one refactor you would make if changes were allowed.

**Reviewer:**
- Ask follow-ups such as:
  - "Where is there repetition?"
  - "What is doing too much work?"
  - "What would you extract into a method?"


## What You Should Take Away From Today

By the end of this activity, you should know:

- Which parts of your code you can explain confidently
- Which concepts you need to review before your interview
- Whether your understanding is **structural** or **surface-level**

The interview does not reward complexity. Rather, it rewards:

- ownership
- clear reasoning
- correct terminology
- honest understanding

If you understand your own code, this activity should feel manageable.
If you don’t, today shows you *exactly* what to fix in your preparation.


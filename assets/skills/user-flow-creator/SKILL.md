---
name: user-flow-creator
description: Turns a product idea, feature brief or existing journey into clear user flows drawn as clean HTML pipeline diagrams (a labelled lozenge, a title, stages joined by connectors, optional return loops and decision branches), plus a step table and edge cases. It can show a current flow next to a proposed one to make the improvement obvious. Use this whenever someone asks for a user flow, a journey, a process or workflow diagram, "map the steps", "before vs after flow", an onboarding or checkout flow, or wants to visualise how a feature or system works, even if they don't say "user flow".
---

# User Flow Creator

You design user flows and present them as calm, readable pipeline diagrams in a single HTML file. Each diagram reads left to right like a sentence: a label, a title that states the outcome, and the stages in order. When it helps, you show the current way and the better way stacked, so the difference is obvious at a glance.

## Why this format

Most flow diagrams are tangled boxes and arrows that only their author can read. A pipeline that names each stage in plain words, with one title stating the result, can be understood in five seconds by a stakeholder and still be precise enough for a designer or engineer. The return path makes loops (sync, retry, review) visible instead of hidden.

## Workflow

1. **Pin down the flow.** Who is the user, what is their goal, where do they start, and what single end state counts as success? If something essential is missing, ask at most two questions; otherwise state your assumptions.
2. **Write the happy path** as 4–7 stages. Each stage is a short verb phrase from the user's or system's point of view ("Uploads the document", "AI suggests fields"). Merge or cut stages that don't change what the user knows or decides.
3. **Find the loops and branches.** Where does the flow repeat (sync, retry, review cycle)? Where does it split (error, abandonment, approval)? Every error branch must lead back into the flow or to a clear exit.
4. **Decide if a comparison helps.** If the request is about improving something, draw the current flow ("Traditional method") and the proposed one, with titles that name the outcome of each ("One-time styleguide → drift" vs "Continuous spec → audit → enforce").
5. **Build the HTML** from `assets/flow-template.html`. Copy the whole file, keep its CSS, and replace the example diagrams with yours. Use:
   - `.flow-diagram` with the modifier `flow-diagram--current` (muted) or `flow-diagram--proposed` (accent).
   - `.flow-label` → a `.lozenge` with the method name and a `.flow-title` with the outcome.
   - `.flow-pipeline` containing `.flow-stage` items separated by `.flow-connector` elements.
   - `.flow-return` with a `.flow-return-label` for loops back to an earlier stage.
   - `.flow-branch` under a stage for an alternative or error path.
5b. **Explain the comparison.** Under the diagrams, add a short "What changed" list: each step you removed, merged or automated, and why it can go. A reader should see the reason, not just a shorter line.
5c. **Cover the domain's risks.** Flows in money, health, identity or legal products must show the safeguards: identity checks, rate limits and lockouts, confirmation messages, and notifying the user after sensitive changes. Show them as stages or branches, not footnotes.
6. **Add the step table** below the diagrams: number, stage, actor, what they see, what they do, failure case.
7. **List edge cases and open questions** you didn't decide. Every flow gets its failure paths: what happens when a message never arrives, a link expires, the user gives up halfway, or the system is down.
8. **Check** the result: stage names match between diagram and table, no dead ends, each diagram has a title that states an outcome, and it reads well at 375 px (the template stacks stages vertically on small screens).

## Writing rules for stages

- 2–6 words, verb first or actor + verb ("Designer creates styleguide", "AI reads specs").
- Same grammatical shape across a pipeline.
- No jargon the audience wouldn't use.
- Titles are outcomes, written with arrows: "Brief → review → approved draft".

## Output

Save one self-contained HTML file (default name `user-flow.html`) with:
1. A heading and one-line context (user, goal, success state).
2. The pipeline diagram(s).
3. The step table.
4. Edge cases and open questions.

Then summarise in chat: the flow in one line, the number of stages, and the key change if you drew a comparison. Offer Mermaid or Figma-ready text if the user needs to edit it elsewhere.

## Consistency

- Step tables follow the same order as the diagrams (current first, then proposed).
- Numbers you assume (field counts, wait times) are marked as assumptions in the table, not stated as facts.

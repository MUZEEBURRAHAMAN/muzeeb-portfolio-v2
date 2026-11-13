---
name: antislop-content
description: Finds and removes the patterns that make writing sound AI-generated (filler openers, fake profundity, "not X but Y" contrasts, triplets, punchy one-liners, hedging, em-dash habits) and rewrites the text in plain, direct, human language. Use this whenever someone asks to edit, tighten, humanize or "de-AI" a draft, LinkedIn post, case study, email, landing page copy, README or essay, says their writing "sounds like ChatGPT", or asks you to write anything that will be published under their name.
---

# Antislop · Content

You edit writing so it sounds like a specific, thoughtful person wrote it, not a model. You keep the author's meaning and facts, and remove the habits readers now recognise as machine-made.

## Why this matters

Readers stop trusting text the moment they spot AI tells, even when the ideas are good. The patterns below are not wrong grammatically; they are wrong because they are predictable, vague, or perform insight instead of delivering it. Each fix makes the text more specific and easier to read.

## Workflow

0. **Make a fact ledger.** Before editing, list every fact in the draft: names, numbers, dates, versions, prices, features and claims. After rewriting, tick each one off. Nothing on the list may disappear, and nothing new may be added.
1. **Read the whole draft first.** Note the author's point, audience and voice (formal, casual, technical). Your rewrite must keep all three.
2. **Mark the tells.** Go through `references/patterns.md` and mark every instance. In review mode (when the user asks "what's wrong" or "check this"), show them with the category.
3. **Rewrite.** Fix each tell with the move listed for its category. The aim is fewer words, more specifics, and natural rhythm.
4. **Check the fact ledger.** Every fact on the list is still there, worded accurately; no new numbers or claims crept in.
4b. **Check facts didn't change.** Every number, name and claim in the original survives, unless it was itself filler.
5. **Score** the before and after (see Scoring) and show both.

## The core moves

- **Cut throat-clearing.** Delete openers that announce instead of say ("Here's the thing:", "Let's dive in", "It's worth noting that"). Start with the point.
- **State it directly.** Replace "It's not X, it's Y" with "It's Y". Replace "Not because A. Because B." with "Because B."
- **Name the specific thing.** Turn vague abstractions ("drive meaningful impact", "unlock value") into the concrete thing that happened.
- **Break the rhythm.** Vary sentence length. Two examples are often stronger than the reflexive three. Don't end every paragraph with a punchy one-liner.
- **Remove hedges and intensifiers.** "Very", "really", "truly", "arguably", "incredibly", "it's important to note".
- **Use active voice with a human subject.** "We shipped it in March", not "It was shipped in March". Avoid objects doing human things ("the data tells a story").
- **Drop em dashes.** Use a full stop, comma, colon or parentheses instead. Em dashes are one of the most recognised tells.
- **No rhetorical setups.** Don't ask a question and immediately answer it ("So what does this mean? It means…").

## Modes

- **Rewrite (default):** return the cleaned text, then a short list of the main changes.
- **Review:** return the original with each tell marked, e.g. `[filler: "Here's the thing:"]`, then the rewrite.
- **Write:** when asked to write new content, write it clean from the start and run the checklist before returning.

## Scoring

Rate the text 1–10 on each, before and after:
- **Directness**: statements, not announcements.
- **Specificity**: concrete nouns, numbers, names.
- **Rhythm**: varied sentence length, no formula.
- **Trust**: respects the reader, no hand-holding.
- **Density**: nothing cuttable left.

Below 35/50 needs another pass. Report: `Before 21/50 → After 42/50`.

## Output format

```
<rewritten text>

---
**Changes**
- Cut 3 filler openers ("Here's the thing", …)
- Replaced 2 "not X but Y" contrasts with direct statements
- Removed 5 em dashes
- …
**Score:** Before xx/50 → After xx/50
```

Keep the author's formatting (headings, lists, links). Don't add emojis, hashtags or headers they didn't have.

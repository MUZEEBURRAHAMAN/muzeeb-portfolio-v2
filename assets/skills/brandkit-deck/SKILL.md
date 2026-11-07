---
name: brandkit-deck
description: Builds a complete brand kit and a matching pitch deck from a logo and theme (or from a short brief if there's no logo yet): positioning, colour system with contrast checks, type pairing, logo usage rules, mockups, and a 10-slide investor or sales deck in the same visual language, delivered as self-contained HTML. Use this whenever someone uploads a logo or brand colours and wants a brand board, brand guidelines, a style guide, a pitch deck, investor deck, sales deck or "slides that match my brand", or is starting a new company, product or sub-brand and needs a first visual identity.
---

# Brand Kit & Pitch Deck

You turn a logo and theme, or a short brief, into two things that belong together: a one-page brand kit and a pitch deck built from it. The deck should look like it came from the same studio as the brand, because it did.

## Why this skill exists

Founders often get a logo and then build a deck in a default template, so the story and the brand never match. Starting from the brand system (colours with jobs, type with a scale, logo rules) and then building every slide from those tokens produces a deck that looks designed and stays consistent when someone edits it later.

## Inputs

- **With a logo:** read its colours (pick exact HEX values from the file when you can), shapes and type style. Respect them; extend the system, don't redesign the logo.
- **Without a logo:** build from the brief, and propose 3 wordmark-first logo directions as simple SVG.
- **Brief:** company, what it does, audience, 3 brand attributes, competitors, and the deck's purpose (investors, sales, partners). Fill gaps with plausible assumptions and mark them as assumptions.

## Workflow

1. **Positioning in one sentence:** "For [audience], [brand] is the [category] that [differentiator]." Every later decision should serve it.
2. **Colour system:** 1 primary, 1–2 secondary, 2 neutrals, 1 accent, max 6 total. Give each a HEX value and a job ("Primary: buttons and key numbers"). Check contrast mathematically: body text ≥ 4.5:1, large text ≥ 3:1. Show the ratio next to each text pairing.
3. **Typography:** one display face and one text face from freely licensed sources (Google Fonts), with fallback stacks and a scale (ratio ~1.25). No more than two families.
4. **Logo usage:** clear space, minimum size, single-colour and inverted versions, a 24 px favicon test, and 3 don'ts.
5. **Mockups:** website hero, business card and social avatar, using only the defined tokens.
6. **Pitch deck:** 10 slides in 16:9, built from the same tokens:
   1. Title (logo, one-line positioning)
   2. Problem (one sharp sentence, one supporting fact)
   3. Solution (what it does, in plain words)
   4. Product (screenshot or mockup with 3 callouts)
   5. How it works (3 steps)
   6. Market (size with source, or "assumption" if estimated)
   7. Business model
   8. Traction or proof (real numbers only; otherwise milestones)
   9. Team
   10. Ask / next step and contact
   Use one idea per slide, a headline that states the takeaway, and large type. Never invent traction, customers, logos or quotes; use clearly marked placeholders instead.
7. **Assemble** using `assets/brand-template.html`: it contains the brand-board layout and a slide system (`.slide` sections at 16:9 with print styles). Replace the example tokens and content with yours.

## Quality rules

- Every colour has a HEX value and a job; nothing decorative without a role.
- All text pairings pass WCAG AA; show the ratios.
- Max two type families and six colours.
- Only free or client-licensed fonts.
- No clichés (lightbulbs, gears, handshakes, rockets) without a deliberate twist.
- The logo works in one colour, inverted, and at 24 px.
- Every design decision has a one-sentence rationale.
- Placeholders for unknown facts are marked `[placeholder]`, never presented as real.

## Output

One self-contained HTML file (default `brand-kit.html`) with the brand board followed by the deck slides, plus a short text spec in chat: positioning, colour table (HEX, job, contrast), fonts with licence, logo rationale, 3 don'ts, and the list of placeholders the user needs to fill.

## Facts in the deck

Treat product specs (sensor rates, integrations, prices, timelines) the same as traction: if the brief didn't state it, mark it `[placeholder]`. Only the brief and cited sources count as facts.

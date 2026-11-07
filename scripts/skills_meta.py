# Content for the AI Skills list and the skill detail pages.
# Demos quote real outputs from the skill tests (claude-skills-workspace/iteration-1).
# `tested` is filled from the grading results by build.py when benchmark data exists.

UPDATED = 'Nov 2026'

def _m(t):  # mark a phrase the skill catches in the highlight demo
    return f'<mark>{t}</mark>'

SKILLS = [
  dict(
    slug='honest-review', icon='sk-honest', name='Honest Review', category='Review', tone='accent',
    tagline='A design review that tells you what is wrong, ranked by how much it hurts.',
    description='Reviews a screen, page, flow or Figma frame like a senior design lead who has no reason to be polite. You get a verdict first, then findings ranked Blocker to Nit, each with what it sees, why it matters and the fix.',
    level='Intermediate', saves='About 1 hour per review', version='1.0.0', updated=UPDATED,
    who='Designers who want blunt feedback before a crit, founders checking a page before launch, and developers who built UI without a designer.',
    uses=['Pressure-test a pricing page, landing page or onboarding before it ships',
          'Get a second opinion on a Figma frame when no senior designer is around',
          'Turn vague “something feels off” into a ranked list of fixes'],
    triggers=['Be brutally honest about this page', 'Roast my design', 'What is wrong with this screen?', 'Review this before I ship it'],
    demo=dict(type='text', title='From the test: a pricing page',
              text='Verdict: Rework before shipping. None of the buttons go anywhere, the plan details are almost unreadable, and a visitor can\'t tell what each plan costs per month.\n\n1. [Blocker] None of the buttons do anything\n   What I see: every button is an <a class="btn"> with no href.\n   Why it matters: the page can\'t convert a single visitor, and keyboard users can\'t reach the buttons.\n   What to do: point each plan at its signup URL with the plan pre-selected.\n\n2. [Blocker] Plan features are unreadable\n   What I see: #ccc on white at 11px, about 1.6:1 contrast.\n   What to do: 14–16px body text, features at #555 or darker (about 7:1).\n\n3. [Blocker] The prices have no unit or billing period\n   What to do: write "$9 per user / month" and say how billing works.',
              caption='Excerpt from the test output. The full review had 3 Blockers, 4 Majors and a short list of what to keep.')),
  dict(
    slug='ux-assistant', icon='sk-ux', name='UX Assistant', category='Audit', tone='accent',
    tagline='A UX and accessibility audit with the WCAG rule, the measured value and the code fix.',
    description='Audits a screen, component or flow against usability heuristics and WCAG 2.2 AA. It works through every state (empty, error, focus, loading, 375px, 200% zoom) and returns findings by severity, each tied to a rule, a measurement and a fix you can paste.',
    level='Intermediate', saves='2–3 hours per audit', version='1.0.0', updated=UPDATED,
    who='Product designers handing off to engineering, engineers fixing accessibility bugs, and teams preparing for an accessibility review.',
    uses=['Audit a form, checkout or settings page before release',
          'Find contrast, focus and labelling failures with exact ratios',
          'Get code fixes for each issue, not just a list of rule numbers'],
    triggers=['Audit this form for UX and accessibility', 'Is this screen WCAG compliant?', 'Check the UX of this flow', 'What would fail an accessibility review here?'],
    demo=dict(type='text', title='From the test: a sign-up form',
              text='Summary: Not ready to release. Blocker 7 · Major 7 · Minor 4 · Nit 1\n\n[Blocker] Inputs have no label (placeholders used as labels)\n  Rule: WCAG 2.2 · 1.3.1, 3.3.2, 4.1.2 · Checklist A-04\n  Evidence: no <label>, aria-label or aria-labelledby on any field.\n  Fix: <label for="email">Work email</label>\n       <input id="email" type="email" autocomplete="email" required>\n\n[Blocker] Submit button text is unreadable\n  Evidence: white on light green, 1.46:1 (needs 4.5:1).\n\n[Blocker] Submit locks itself\n  Evidence: one click disables the button for good. Nothing is sent and nothing tells the user what happened.',
              caption='Excerpt from the test output. Every finding names the element, the rule and the measured value.')),
  dict(
    slug='portfolio-review', icon='sk-portfolio', name='Portfolio Review', category='Review', tone='accent',
    tagline='Reads your case study the way a hiring manager does in 60 seconds, then tells you what to fix.',
    description='Reviews a design portfolio or case study for a specific role. You get the 60-second verdict a hiring manager would reach, a score, the fixes ranked by how much they change your chances, and example rewrites.',
    level='Beginner', saves='A week of waiting for feedback', version='1.0.0', updated=UPDATED,
    who='Designers applying for jobs, juniors building a first portfolio, and seniors moving into a new industry.',
    uses=['Check if a case study lands for the role you are applying to',
          'Find missing evidence: research, outcomes, decisions you rejected',
          'Get rewrites for a summary, headline or caption'],
    triggers=['Review my portfolio', 'Would a hiring manager shortlist this case study?', 'Tear apart my case study for senior roles', 'How can I make my portfolio stronger?'],
    demo=dict(type='text', title='From the test: my own Jobly case study',
              text='Target role: Senior product designer at B2B SaaS companies\n60-second verdict: Maybe. The ownership, judgement and honesty are senior-level, but this is a solo consumer project with no users, no research and no business context.\nScore: 22/35\n\nTop fixes\n1. Don\'t lead with Jobly for B2B roles. Reframe it around messy data, trust and AI guardrails.\n2. Add evidence: sample listings to back the "ghost jobs" claim, 5 usability sessions.\n3. Show what you considered and rejected: why 60 days, jobs with no date.\n4. Shift the balance from engineering to design.\n\nAlready strong: the TL;DR, the honest "No usage numbers yet", the audit that failed.',
              caption='I ran it on my own Jobly case study. It was right, and I am working through the list.')),
  dict(
    slug='antislop-content', icon='sk-antislop-copy', name='Antislop · Content', category='Writing', tone='warn',
    tagline='Strips the ChatGPT tells out of your writing and keeps every fact.',
    description='Rewrites posts, emails, docs and UI copy so they stop sounding machine-made. It cuts throat-clearing openers, fake depth, forced triplets and vague verbs, keeps every fact, scores the before and after, and lists each change.',
    level='Beginner', saves='15 minutes per post', version='1.0.0', updated=UPDATED,
    who='Anyone who drafts with AI: designers writing case studies, founders posting on LinkedIn, PMs writing specs.',
    uses=['Clean a LinkedIn post or newsletter before it goes out',
          'Edit a case study so it reads like a person wrote it',
          'Review UI copy for filler and vague verbs'],
    triggers=['Make this sound less like ChatGPT', 'Remove the AI slop from this', 'Edit this so it sounds human', 'Antislop this post'],
    demo=dict(type='highlight', title='Try it: what it catches',
              html=('<p class="sk-before"><b class="sk-tag">Before · 14/50</b>'
                    + _m("Here's the thing:") + ' shipping a design system is hard. ' + _m("It's not about components, it's about people.")
                    + ' We spent 6 months building ours at Omnis AI ' + _m('—') + ' and it cut UI inconsistencies by 40%. ' + _m('Let that sink in.') + ' '
                    + _m('The real unlock?') + ' ' + _m('Alignment, clarity, and trust.') + ' ' + _m('So what did we learn?') + ' That every team needs a source of truth. '
                    + _m("And that's okay.") + ' ' + _m("In today's fast-paced world") + ", it's " + _m('truly important') + ' to ' + _m('leverage') + ' your design system to '
                    + _m('drive meaningful impact') + '. ' + _m('Full stop.') + '</p>'
                    '<p class="sk-after"><b class="sk-tag">After · 41/50</b>Shipping a design system is hard, and most of the difficulty is people. We spent six months building ours at Omnis AI, and it cut UI inconsistencies by 40%.<br><br>'
                    "Most of those six months went into getting designers and engineers to agree on one source of truth and then use it every day. If your team doesn't have one yet, I'd start there.</p>"),
              caption='The real test input and output. Press the button to mark every pattern it removed. All the facts survive: six months, Omnis AI, 40%.')),
  dict(
    slug='antislop-ui', icon='sk-antislop-ui', name='Antislop · UI', category='Design', tone='warn',
    tagline='Finds the defaults that make a page look AI-generated and rebuilds it around the product.',
    description='Reviews a page or component for the tells of AI-generated UI: purple gradients, gradient text, emoji cards, glow buttons, fake stats, Inter everywhere. It scores how generic the page is, lists each tell with where it is, and rebuilds the page with tokens and a product-specific idea.',
    level='Intermediate', saves='Half a day of redesign', version='1.0.0', updated=UPDATED,
    who='Developers shipping AI-generated front ends, designers reviewing vibe-coded prototypes, and founders whose landing page looks like everyone else\'s.',
    uses=['Fix a landing page generated by an AI coding tool',
          'Remove fake social proof and placeholder metrics before launch',
          'Give a generic page one idea that belongs to the product'],
    triggers=['This page looks AI-generated, fix it', 'Make this UI less generic', 'Antislop this landing page', 'Why does my site look like every other SaaS?'],
    demo=dict(type='text', title='From the test: a generic SaaS landing page',
              text='Generic score: 10/10 (10 = indistinguishable from a template)\n\nThe only sentence that says what Flowly is sits in the footer.\n\nTells found\n1. Purple-to-blue gradient hero: .hero linear-gradient(135deg,#6366f1,#8b5cf6)\n2. Gradient text headline: background-clip:text, lavender on violet drops contrast\n3. 100vh fully centred hero pushes everything below the fold\n4. Buzzword copy: "Supercharge Your Workflow", "Unlock your potential with AI"\n5. "Get Started" glow button: an <a> with no href\n6. Card soup with emoji icons: 🚀 ✨ 🔒\n7. Fake proof: "Trusted by 10,000+ teams", "99.9% uptime · 10x faster"\n\nAfter the rebuild: 2/10. Headline "Know which round every client is on." with an example round tracker as the hero.',
              caption='Excerpt from the test output. The rebuilt page kept the product, cut the fake proof, and passed AA contrast.')),
  dict(
    slug='fact-checker', icon='sk-factcheck', name='Fact Checker', category='Research', tone='ok',
    tagline='Checks a document claim by claim, with a source for every verdict.',
    description='Upload a document or paste text. It pulls out every checkable claim, checks each against primary sources, and returns a verdict (correct, partly correct, incorrect, unsupported, can\'t verify) with the source and a corrected version. It never invents a link.',
    level='Beginner', saves='An hour of tab-hopping', version='1.0.0', updated=UPDATED,
    who='Writers, marketers and researchers checking facts before publishing, and anyone asking “is this actually true?”.',
    uses=['Check statistics and dates in a blog post or deck before it goes out',
          'Verify a viral claim or a screenshot someone sent you',
          'Find numbers used out of context, such as the wrong year or population'],
    triggers=['Fact-check this', 'Is this true?', 'Verify the numbers in this document', 'Check these claims before I publish'],
    demo=dict(type='text', title='From the test: five mixed claims',
              text='Summary: 5 claims checked · Correct 2 · Partly correct 1 · Incorrect 2\nOverall: Don\'t post it as written.\n\n1. "The Eiffel Tower was completed in 1889"            Correct\n2. "The Great Wall is visible from the Moon"           Incorrect: a long-running myth\n3. "WCAG 2.2 became a Recommendation in October 2023"  Correct: 5 Oct 2023\n4. "Adobe completed its acquisition of Figma"          Incorrect: the deal ended on 18 Dec 2023\n5. "Medicare pays for cancer navigation (G0023/G0024)" Partly correct: the codes cover any\n   serious high-risk illness, not only cancer\n\nEach row links to W3C, the Adobe newsroom or the Federal Register.',
              caption='Excerpt from the test output. When search was rate-limited, it fetched the primary sources directly instead of guessing.')),
  dict(
    slug='user-flow-creator', icon='sk-flow', name='User Flow Creator', category='Design', tone='accent',
    tagline='Turns a brief into clean pipeline flows, with the current and better way stacked.',
    description='Designs user flows and draws them as calm HTML pipelines: a label, a title that states the outcome, stages joined by connectors, return loops and error branches. It can stack the current flow over a proposed one, then adds a step table and open questions.',
    level='Beginner', saves='1–2 hours per flow', version='1.0.0', updated=UPDATED,
    who='Product designers mapping a feature, PMs explaining a process to stakeholders, and founders sketching how their product works.',
    uses=['Show a before and after flow in a design review',
          'Map onboarding, checkout or booking with every error path',
          'Explain how a system works in one diagram anyone can read'],
    triggers=['Create a user flow for this', 'Map the steps of this journey', 'Show the current flow vs a better one', 'Draw how this process works'],
    demo=dict(type='flows', title='Example output',
              flows=[
                dict(kind='current', label='Traditional method', title='One-time styleguide → drift',
                     stages=['Designer creates styleguide', 'AI reads it once', 'Guesses on gaps', 'Drifts each session', 'Inconsistent output']),
                dict(kind='proposed', label='LLM-readable method', title='Continuous spec → audit → enforce',
                     stages=['Spec DS local to repo', 'AI reads specs', 'Uses tokens', 'Mandated audit looks for drift', 'Consistent output'],
                     ret='update specs with regular source sync'),
                dict(kind='current', label='Current method', title='Long form → email back-and-forth → demo days later',
                     stages=['Clicks “Request a demo”', 'Fills 15-field form', 'Waits for sales reply', 'Trades emails about times', 'Attends generic demo'],
                     ret='no time works → propose again, wait again'),
                dict(kind='proposed', label='Proposed method', title='Short form → instant booking → demo confirmed in one visit',
                     stages=['Clicks “Book a demo”', ('Enters work email and role', 'Not a fit → self-guided tour'), ('Picks a live time slot', 'No slot fits → request a callback'),
                             'Gets instant confirmation', 'Attends tailored demo'],
                     ret='reschedule from the confirmation link'),
              ],
              caption='The first pair is the reference style. The second pair is the skill’s own output from the test brief, with error branches under two stages.')),
  dict(
    slug='brandkit-deck', icon='sk-brand', name='Brand Kit & Pitch Deck', category='Brand', tone='ok',
    tagline='Give it a logo and a theme. Get a brand kit and a 10-slide deck that match.',
    description='Builds a brand kit from a logo and theme (or a short brief): positioning, a colour system with contrast ratios, a type pairing, logo rules and mockups. Then it builds a 10-slide investor or sales deck from the same tokens, as one HTML file. It never invents traction.',
    level='Intermediate', saves='2–3 days of brand work', version='1.0.0', updated=UPDATED,
    who='Founders starting a company, designers kicking off a brand project, and teams launching a sub-brand.',
    uses=['Turn a logo into brand guidelines and a matching deck',
          'Start a visual identity from a short brief, with 3 logo directions',
          'Rebuild a default-template deck in your own brand'],
    triggers=['Make a brand kit from this logo', 'Create a pitch deck that matches my brand', 'Build brand guidelines for my startup', 'I need a brand board and investor deck'],
    demo=dict(type='text', title='From the test: Tidewell, a water-sensor startup',
              text='Positioning: For municipal water utilities, Tidewell is the continuous water-quality monitoring network that turns every pipe junction into a calibrated, auditable reading.\n\nColour (6, each with a job and a contrast ratio)\n  Deep Tide      #0B3C49  headlines, buttons, logo    11.19:1 on Still Water\n  Clear Channel  #1F7A8C  links, chart lines           4.66:1\n  Signal         #F2B134  one emphasis per view        6.33:1 on Deep Tide\n  Ink            #102A33  body text                   14.03:1\n  Still Water    #F5F8F7  backgrounds\n  Slate          #4E6470  captions, sources            5.81:1\nType: Manrope (display) + Inter (text), both OFL\nLogo: 3 directions drawn as SVG; recommended "Level Ring"\nDeck: 10 slides in 16:9 built from the same tokens\n\nThe one outside fact (about 50,000 US water systems, EPA) is flagged for a citation.',
              caption='Summary of the test output. Nothing about the company was invented; unknowns stay as [placeholder].')),
]

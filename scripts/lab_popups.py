"""Lab popups, rendered by build.py as <dialog> elements on lab.html.

Each popup: id (also the #link that opens it), eyebrow, title, lede, sections [(eyebrow, headline or None, [blocks])],
links [(label, url)]. Blocks use the same types as case_studies.py.
"""

POPUPS = [
dict(
 id='claude-skills', eyebrow='Claude skills & automation',
 title='I turned the design reviews I repeat into reusable Claude skills.',
 lede='I kept giving AI the same context, frameworks and rules. So I packaged the processes I trust into skills that run inside Claude Code, and each session starts from them.',
 sections=[
  ('The problem', 'Good AI output depends on the workflow around it.', [
    ('p', 'Without a rule system, you repeat the same loop every session:'),
    ('flow', ['Explain context', 'Prompt', 'Token drift', 'Manual fix', 'Re-prompt', 'Review']),
  ]),
  ('How I build a skill', None, [
    ('rows', [('Spot the friction', 'I watch for a prompting loop I repeat more than three times across reviews and handoffs.'),
              ('Write the rules', 'I turn it into structured rules: W3C tokens, WCAG 2.2 checks, checklists and edge-case matrices, in Markdown and XML.'),
              ('Package it', 'I bundle the rules into a .skill file that Claude Code runs, so I never re-explain the context.')], None),
  ]),
  ('Skills I ship', None, [
    ('cards', [('Design System Architect', 'Turns interface screenshots into components, maps semantic tokens, checks state matrices and WCAG 2.2.'),
               ('AI UX Audit Assistant', 'Reviews screens and live products for usability, hierarchy, contrast and missing states.'),
               ('Honestly', 'Makes the model separate facts from assumptions and skip flattery.'),
               ('Honestly Review', 'A design-manager critique of type hierarchy, density and engineering feasibility.')]),
  ]),
  ('What changed', None, [
    ('panels', [('bad', 'Before', 'Raw chat', ['Repeat context and format rules each time', 'Context → prompt → correct → review']),
                ('good', 'After', 'Skill runtime', ['Start from codified rules', '.skill → context → output → my judgement'])]),
    ('callout', 'What I learned', 'When you write your design taste down as rules, the AI follows your craft instead of giving generic answers.'),
  ]),
 ],
 links=[('AI UX Audit Assistant on GitHub', 'https://github.com/MUZEEBURRAHAMAN/AI-UX-Audit-Assistant'), ('Read the AI UX Audit case study', 'projects/audit-engine.html')],
),
dict(
 id='omnis-design-system', eyebrow='Design system · Omnis AI',
 title='One token and component system across 7 legal-tech products.',
 lede='I built the Omnis Design System so seven products share one set of tokens, components and interaction patterns. UI inconsistencies dropped 40%, and new-feature design went from days to hours.',
 sections=[
  ('Results', None, [
    ('stats', [('7', 'Products', 'On one shared system'), ('40%', 'Fewer inconsistencies', 'Across product UIs'), ('Hours', 'Feature design', 'Down from days per screen')]),
  ]),
  ('Token architecture', 'Three tiers keep design decisions reusable.', [
    ('p', 'Hardcoded hex values and one-off margins cause brand drift. I structure tokens to the W3C Design Tokens (DTCG) format so they compile to CSS, iOS and Android.'),
    ('rows', [('Global primitives', 'Raw values: colour ramps, a modular type scale, grid multiples. Example: blue.600 = #0284c7.'),
              ('Semantic tokens', 'Intent that changes with the theme, like dark mode or high contrast. Example: color.action.primary = blue.600.'),
              ('Component tokens', 'Bindings that protect a component from global changes. Example: button.primary.bg = color.action.primary.')], None),
    ('flow', ['Figma Variables', 'Style Dictionary', 'CSS, Swift and Kotlin packages']),
  ]),
  ('Component standard', 'I design 7 states before handoff.', [
    ('flow', ['Default', 'Hover', 'Pressed', 'Focus-visible', 'Disabled', 'Error', 'Loading']),
    ('p', 'Each component also ships with keyboard behaviour and ARIA semantics. A component without its loading, error and focus states is not finished.'),
  ]),
 ],
 links=[('See the system in use: LitBox case study', 'projects/litbox.html')],
),
dict(
 id='mobile-apps', eyebrow='Mobile apps',
 title='Three small mobile products I’m building.',
 lede='Native apps for food preservation, healthier screen habits and better photo composition.',
 sections=[
  ('The apps', None, [
    ('iters', [('mid', 'In development', 'SafeSide', 'Helps people find, organize and manage preserved food, with clear product information and simple navigation.', None),
               ('mid', 'In development', 'Anchor', 'Helps people build healthier screen habits and spend more intentional time away from their devices, without adding pressure.', None),
               ('mid', 'In research', 'Photoly', 'A photography companion that suggests better angles and composition, with practical visual tips.', None)]),
  ]),
 ],
 links=[],
),
dict(
 id='web-apps', eyebrow='Web apps',
 title='Web products and experiments.',
 lede='Browser tools I build to test frontend architecture, real-time algorithms and visual tooling.',
 sections=[
  ('The tools', None, [
    ('iters', [('good', 'In production', 'Thumbly', 'An AI thumbnail tool that previews how YouTube thumbnails and titles look in mobile feeds, sidebars and dark or light mode before you publish. Built with Next.js and Canvas.', None),
               ('mid', 'Beta this month', 'UIRare', 'A directory of rare UI components and a Figma library of micro-animated patterns, spring transitions and tactile tokens.', None),
               ('mid', 'In beta testing', 'Cutcliply', 'An extension and web tool for creators: cut clips, extract audio, split video, grab high-res frames and make highlight clips.', None)]),
  ]),
  ('What I learned', None, [
    ('rows', [('Thumbly', 'How to score text hierarchy and focal contrast at thumbnail sizes down to 120 px.'),
              ('Cutcliply', 'How to crop, capture frames and trim video in the browser with WebCodecs and canvas.')], None),
  ]),
 ],
 links=[('Open Cutcliply', 'https://cutcliply.up.railway.app/')],
),
dict(
 id='avatarly', eyebrow='Figma plugins',
 title='Plugins that remove repetitive work from Figma.',
 lede='I build small Figma plugins for jobs I kept doing by hand. Avatarly fills a design with generated avatars, so placeholder people take one click.',
 sections=[
  ('The plugins', None, [
    ('cards', [('Avatarly', 'Generates avatars and fills them into your frames.'),
               ('Blobby', 'Generates editable organic SVG blobs for heroes and brand visuals.'),
               ('Token Audit Helper', 'Finds raw colours and font sizes in a frame and maps them to your design tokens.')]),
  ]),
 ],
 links=[('Blobby on Figma Community', 'https://www.figma.com/community/plugin/1672948027574838944/blobby-editable-blob-generator')],
),
dict(
 id='ai-workflow', eyebrow='AI in my design process',
 title='AI speeds up the work. I make the decisions.',
 lede='I use AI to synthesize research faster, find edge cases I’d miss and get to a working prototype sooner. Taste, empathy and trade-offs stay with me.',
 sections=[
  ('In numbers', None, [
    ('stats', [('10×', 'Context', 'Faster research ingestion'), ('3×', 'Prototypes', 'Faster validation'), ('100%', 'Decisions', 'Made by me')]),
  ]),
  ('Where AI helps, and where I decide', None, [
    ('table', ['Stage', 'AI does', 'I decide'], [
      ['Discover', 'Clusters interview notes, Mobbin patterns and Jira stories', 'The root problem and the problem statement'],
      ['Frame', 'Drafts 7-state component matrices and WCAG checklists', 'Scope, trade-offs and direction'],
      ['Pressure-test', 'Checks type hierarchy, cognitive load and contrast', 'Brand craft, tone and micro-interactions'],
      ['Prototype', 'Turns Figma tokens into working React or HTML', 'Gesture feel, perceived speed and handoff']]),
    ('callout', 'The rule I follow', 'I check every AI output against real production tokens before it reaches a design.'),
  ]),
 ],
 links=[('How I built Claude skills', '#claude-skills')],
),
]

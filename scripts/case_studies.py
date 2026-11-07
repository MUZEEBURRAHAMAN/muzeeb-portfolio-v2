"""Case study content, rendered by build.py into projects/<slug>.html.

Each section is (eyebrow, headline, [blocks]). Block types:
  ('p', text)                      muted paragraph        ('lead', text)   normal paragraph
  ('rows', [(title, a, b?)], (label_a, label_b))          numbered rows
  ('list', [items])                ('flow', [items])      ('quote', text)
  ('callout', label, text)         ('honest', title, text)
  ('panels', [(pill, pill_text, title, [items])])         2 or 3 side-by-side panels
  ('cards', [(title, text)])       ('stats', [(big, label, sub)])
  ('table', [headers], [[cells]])  ('tldr', [(pill, label, text)])
  ('iters', [(pill, pill_text, title, text, quote?)])
  ('fig', file, caption)           ('figs', [(file, caption)])   two images side by side
  ('cmp', before_file, after_file, before_label, after_label)   drag slider
  ('details', summary, [items])
  ('links', [(label, url)])        row of link buttons
A case can also carry links=[(label, url)], shown under its summary.
pill is one of: good, bad, mid. **text** renders bold. Images live in assets/img/cs/<slug>/.
"""

CASES = [
# ------------------------------------------------------------------ GOFULLY
dict(
 slug='gofully', name='GoFully', tags=['Chrome extension', 'Brand + product'], read=9,
 cover='assets/img/cover/gofully.webp',
 title='GoFully: redesigning a screenshot extension around one promise, nothing leaves your device.',
 lede='GoFully already did a lot: full-page capture, text reading, markup, redaction and PDF export, all offline. I redesigned the brand, the extension and the website so the tool is **calm to pick up and private by default**.',
 meta=[('Role', 'Product Designer, end-to-end redesign'), ('Product', 'Chrome extension · 5 browsers'), ('Scope', 'Brand, design system, extension UI, website'), ('Status', 'Designed · new site in development')],
 stats=[('41 pages', 'Brand guide', 'From positioning and voice to the 16 px app icon'), ('70+', 'Extension screens', 'Every state, in light and dark'), ('1 action', 'Per screen', 'One primary action in navy; everything else quiet')],
 tldr=[('The problem', 'The old extension and website listed every feature at once, so a capable offline screenshot tool felt busy and its main promise got lost.'),
       ('What I did', 'Redesigned the brand, extension and website end to end: a 41-page brand guide, 70+ screens in light and dark, and one primary action per screen.'),
       ('Where it stands', 'Designed, with the new website in development. No post-launch metrics yet, so this shows the design work, not results.')],
 sections=[
  ('Overview', 'GoFully worked well and looked like dozens of other screenshot tools.', [
    ('p', 'GoFully scrolls a page, waits for lazy images, handles sticky headers and stitches one clean image. It reads text in six languages, marks up and redacts, beautifies captures and exports PNG, JPG, WebP or PDF. There’s no account and no server: everything runs on the device.'),
    ('callout', 'The opening insight', 'On the old website, “100% on-device” was a small badge above a headline about features. The one thing that set GoFully apart was the quietest thing on the page.'),
  ]),
  ('The problem', 'The store page, website and popup each listed every feature at once.', [
    ('rows', [('A headline made of features', '“Full Page Screenshot Tool. One Extension. Every Job.” followed by WebAssembly OCR, 4K export and PDF in one sentence.'),
              ('A generic identity', 'A glossy camera icon, next to other screenshot extensions with camera icons.'),
              ('Busy visuals that hid the UI', 'Gradients, tilted devices and callouts; each surface in its own style.')], None),
    ('cmp', 'before-site-hero.webp', 'after-site-hero.webp', 'Before · old site', 'After · new site'),
    ('fig', 'before-store-entire.webp', 'Before: four store screenshots, four different layouts.'),
  ]),
  ('Direction', 'I built the direction on one promise: capture the whole page and keep it on your device.', [
    ('p', 'The audience is everyday sharers: developers, QA testers, writers, researchers and privacy teams. The problem in the brand guide’s three words: three tools, one leak.'),
    ('cards', [('Private', 'Everything runs on the device. No account, no upload, no tracking.'), ('Precise', 'Pixel-exact captures, checked seams, crops that keep the marks.'), ('Fast', 'One click or one shortcut from page to finished file.')]),
    ('fig', 'brand-positioning.webp', 'Positioning and moodboard from the 41-page brand guide.'),
  ]),
  ('Brand', 'From a glossy camera to a viewfinder drawn as a G.', [
    ('p', 'The new symbol still says “screenshot”, and it can only be GoFully. Chrome shows it at 16 px in the toolbar, so below 32 px the wordmark drops and the symbol stands alone.'),
    ('fig', 'r0-mark-a.webp', 'Logo anatomy: viewfinder frame, lens ring, shutter dot and tail, each with a job.'),
    ('table', ['Role', 'Pair', 'Contrast'], [
      ['Body text', 'Ink on White · #152333 / #FFFFFF', '15.9:1 Pass'], ['Primary button', 'White on Navy · #FFFFFF / #014073', '10.6:1 Pass'],
      ['Text on Sky fills', 'Navy on Sky · #014073 / #6AB0FF', '4.7:1 Pass'], ['Never for text', 'Sky on White · #6AB0FF / #FFFFFF', '2.3:1 Fail']]),
    ('p', 'Voice: a calm expert. “Screenshot saved. 4,200 px captured.” Never “Your amazing screenshot has been successfully saved!”'),
  ]),
  ('Design system', 'Soft corners, a 4 px grid and two quiet shadows.', [
    ('cards', [('Radius by role', '6 px inputs, 10 px buttons, 16 px cards, 24 px dialogs.'), ('Two navy shadows', 'Raised for cards, Overlay for menus and dialogs. Never pure black.'), ('One icon weight', '24 px grid, 1.75 px stroke, round caps and joins.')]),
    ('fig', 'ui-components.webp', 'Core components, each in default, hover, focus and disabled.'),
  ]),
  ('Extension', 'Each screen gets one primary action and a way out of errors.', [
    ('p', 'I followed a capture through every state it can reach, including the ones that go wrong: a page Chrome won’t allow, a capture that stopped halfway, a search with no results. Each explains what happened and offers the next step.'),
    ('figs', [('popup-default.webp', 'The popup lists each capture mode with its shortcut.'), ('popup-failed.webp', 'A failed capture says what to do next.')]),
    ('fig', 'ov-result-card.webp', 'After a capture, the result card offers copy, save, edit and pin, on top of any site.'),
  ]),
  ('Editor', 'Everything after the capture, in one quiet window.', [
    ('p', 'Crop, arrows, text, blur, auto-redact, Beautify and export. Auto-redact covers emails and card numbers before anything is shared.'),
    ('cmp', 'ed-default.webp', 'ed-dark.webp', 'Light', 'Dark'),
    ('fig', 'ed-redact.webp', 'Auto-redact results, before export.'),
  ]),
  ('Website', 'I replaced the feature list with one sentence.', [
    ('lead', 'Old: “Full Page Screenshot Tool. One Extension. Every Job.” New: **“Screenshot the whole page. Share it ready to go.”**'),
    ('p', 'The privacy promise moved from a badge into the first paragraph. I tried three hero layouts against a realistic long article, then storyboarded every feature demo.'),
    ('fig', 'landing-hero-options.webp', 'Three hero directions, each tested against the same long article.'),
  ]),
  ('Where it stands', 'What’s done and what comes next.', [
    ('tldr', [('good', 'Designed', 'The brand and 41-page guide, Design System v2, 70+ extension screens in light and dark, and the new website.'),
              ('mid', 'Building', 'The new site runs in development; the live site and store listing still show the old design.'),
              ('bad', 'Not yet', 'Post-launch metrics.')]),
    ('panels', [('mid', 'Next', 'v1.2 pushes privacy and precision', ['Redact page: cover emails, cards and API keys before capture.', 'Measure: sizes, padding and colours on hover.', 'Delayed capture for menus and tooltips.', 'QR codes and barcodes, read on device.'])]),
    ('lead', 'I kept every feature. The icon, popup, editor and website now share one look and one message.'),
  ]),
 ],
 faq=[('Why redesign if the features worked?', 'The product was strong; the way it presented itself hid that. Privacy, its real difference, was the quietest message.'),
      ('Is the redesign live?', 'Not yet. The new website is in development and the extension’s current release is v1.1.3.')],
),

# ------------------------------------------------------------------ JOBLY
dict(
 slug='jobly', name='Jobly', tags=['Chrome extension', '0 → 1', 'Design + code'], read=10,
 cover='assets/img/cover/jobly.webp',
 title='Jobly: fresh jobs from company career pages, with the real posting date on every card.',
 lede='Job boards bury new openings under listings that closed months ago. I designed and built Jobly, a free Chrome extension, website and resume studio that reads the hiring systems of **2,000+ employers** and shows only jobs posted in the last 60 days.',
 meta=[('Role', 'Product designer & builder, solo'), ('Timeline', 'Sep – Nov 2026'), ('Platforms', 'Chrome extension, website, Jobly Studio'), ('Stack', 'React, Astro, Python, Cloudflare Pages')],
 stats=[('2,000+', 'Employers', 'Read from their own public job boards'), ('60 days', 'Freshness rule', 'Anything older is dropped'), ('0', 'Accounts', 'No server, no login, no tracking')],
 tldr=[('The problem', 'Job seekers lose hours to listings that closed months ago. Big boards mix fresh roles with stale ones, hide the posting date and route applications through their own forms.'),
       ('What I did', 'Designed and built Jobly end to end: an extension that shows fresh jobs with their real date, a product website, and Jobly Studio for tailored resumes. Everything runs in the browser.'),
       ('Where it stands', 'The website and Studio are live, with job data refreshed every 4 hours. Version 1.1 of the extension is packaged for the Chrome Web Store. No usage numbers yet.')],
 links=[('Visit the Jobly website', 'https://jobly-88t.pages.dev'), ('Open Jobly Studio', 'https://jobly-studio.pages.dev'), ('Source on GitHub', 'https://github.com/MUZEEBURRAHAMAN/Jobly')],
 sections=[
  ('Overview', 'One promise: every job shows when it was posted.', [
    ('p', 'Jobly reads the public job feeds employers embed on their careers pages (Greenhouse, Ashby, Lever, Workday and nine more) plus three remote boards. A scheduled job publishes the result as static files, and the extension, website and Studio filter it in your browser.'),
    ('rows', [('Find jobs', 'Product design, frontend, product, AI/ML and fullstack roles, plus more families, with filters for location, level, salary and date posted.'),
              ('Track applications', 'A board for Saved, Applied, Interviewing, Offer and Closed, with notes, reminders and interview prep.'),
              ('Apply faster', 'Resume profiles, cover letters and autofill that you review. Jobly never presses Submit.')], None),
    ('fig', 'store-1.webp', 'Fresh jobs, discovered automatically: listings come straight from employers’ hiring systems.'),
  ]),
  ('The problem', 'Job search turns into a pile of stale tabs.', [
    ('rows', [('Old listings stay up', 'Ghost jobs sit on boards for months, so you apply to roles nobody is hiring for.'),
              ('Dates are hidden or vague', '“30+ days ago” tells you nothing, and a repost looks brand new.'),
              ('Applications take a detour', 'Boards keep you inside their own forms and messaging instead of the employer’s page.'),
              ('Your search becomes their data', 'Accounts, tracking and promoted listings come with the free tools.')], None),
    ('callout', 'The goal', 'Show only fresh roles, with a date you can trust, and send people straight to the employer.'),
  ]),
  ('Principles', 'Five rules I set before designing a screen.', [
    ('rows', [('A date is a fact', 'Jobly reads the date from the employer’s own listing. If a source has none, the card shows none and the date filter leaves it out.'),
              ('Nothing older than 60 days', 'Old listings never appear, so ghost jobs stay out.'),
              ('Apply on the employer’s site', 'Every Apply button opens the company’s own application page.'),
              ('No account', 'Preferences, saved jobs and alerts live on your device. There is nothing to sign up for.'),
              ('No made-up proof', 'Jobly had no users yet, so the site shows product facts instead of invented reviews or quotes.')], None),
  ]),
  ('Architecture', 'No server, by design.', [
    ('flow', ['2,000+ employer job feeds', 'GitHub Actions, every 4 hours', 'Static files on Cloudflare Pages', 'Extension · Website · Studio']),
    ('p', 'Every client downloads the same public files and filters, matches and sorts them in the browser. A query reads only the categories and age buckets it needs: tech roles from the last week come to about **0.7 MB** compressed, even at 200,000 jobs.'),
    ('table', ['Source', 'How Jobly reads it'], [
      ['Greenhouse, Ashby, Lever', 'Public job-board APIs, with real publish dates'],
      ['SmartRecruiters, Workable, Recruitee and 5 more', 'Public feeds employers embed on careers pages'],
      ['Workday, Amazon Jobs', 'Public careers search'],
      ['We Work Remotely, Himalayas, Arbeitnow', 'RSS and public APIs, labelled “via” the board']]),
  ]),
  ('The extension', 'Filters people already know, and alerts that don’t spam.', [
    ('figs', [('store-2.webp', 'Filters for location, experience, salary, remote and date posted.'), ('store-4.webp', 'Pick your roles once; the feed personalizes without an account.')]),
    ('rows', [('Grouped alerts', 'Jobly checks every 60 to 90 minutes and sends one grouped notification, not a flood.'),
              ('Saved jobs that stay', 'A saved job keeps a copy on your device, so it stays on your list after the company takes it down.'),
              ('A tracker that fills itself', 'After you open a job, Jobly asks “Did you apply?” and moves it on the board.')], None),
    ('cmp', 'dashboard-jobs-light.webp', 'dashboard-jobs-dark.webp', 'Light', 'Dark'),
  ]),
  ('The website', 'A product site that only says what’s true.', [
    ('p', 'I studied the page set of the GoFully site and the interactions of wrangle.ai, then planned 27 pages: how dates work, a live list of companies, guides, and honest comparison pages with sources and a “checked on” date.'),
    ('fig', 'store-3.webp', 'The headline I chose: “Find jobs posted this week, not last year.”'),
    ('fig', 'landing-wireframe.webp', 'The landing page wireframe, section by section, before visual design.'),
  ]),
  ('Jobly Studio', 'A resume tool that can’t make things up.', [
    ('p', 'Studio writes a tailored resume and cover letter for each job from one profile, and tracks every application. It runs fully in the browser and works offline.'),
    ('callout', 'The fact check', 'Every line the AI writes must cite facts from your profile. Code removes a bullet that cites nothing, and flags any number that isn’t in the facts it cites.'),
    ('table', ['AI option', 'Cost', 'Where your profile goes'], [
      ['Claude, by hand (default)', 'Your Claude plan', 'You paste a prompt into claude.ai and paste the answer back'],
      ['Anthropic API', 'Your API key', 'Straight from the browser to Anthropic'],
      ['OpenAI-compatible', 'Your key, or free locally', 'OpenAI, OpenRouter, or Ollama on your own computer']]),
  ]),
  ('Quality', 'I audited Jobly before launch, and it failed.', [
    ('p', 'On 16 October I ran a QA and security audit with Playwright, axe-core and dependency checks against a local copy. The verdict: not ready for the Chrome Web Store.'),
    ('stats', [('46', 'Findings', '6 of them blockers'), ('1 day', 'To fix', 'Re-verified in a real browser'), ('0', 'axe issues', 'In both light and dark themes')]),
    ('p', 'The fixes went further than patches. I moved every preference, saved job and alert onto the device, then removed the server entirely in favour of static files. With no server, there is nothing to attack and nothing to keep running.'),
  ]),
  ('Looking back', 'What Jobly taught me.', [
    ('rows', [('Freshness is a data problem first', 'No layout can fix a stale listing. The 60-day rule and real dates had to live in the data pipeline.'),
              ('Privacy you can see is a feature', '“No account” is something people notice on the first screen, not a line in a policy.'),
              ('Audit before you publish', 'Testing my own product like an attacker found problems no design review would.')], None),
  ]),
 ],
 faq=[('How is Jobly different from LinkedIn or Indeed?', 'Jobly reads postings from company career pages, shows the real posting date and hides anything older than two months. It has no promoted jobs, no account and no messaging. LinkedIn and Indeed list far more jobs and offer things Jobly doesn’t, like Easy Apply.'),
      ('How much does it cost?', 'Nothing. Jobly is free.'),
      ('Why build it without a server?', 'Static files cost nothing to host, can’t leak user data and keep working when traffic spikes.')],
),

# ------------------------------------------------------------------ ASSISTANTLY
dict(
 slug='assistantly', name='Assistantly', tags=['AI tooling', 'Design QA'], read=12,
 cover='assets/img/cover/assistantly.webp',
 title='Design QA took me a day per release. So I built Assistantly, which takes minutes.',
 lede='Assistantly opens a web app the way a person would, clicks through its menus and pop-ups, and lists each design problem it finds with **the exact code fix**. It costs about $0.30 a screen.',
 meta=[('Role', 'Solo product designer & builder'), ('Duration', 'Jun – Jul 2026 · Omnis AI'), ('Owned', 'Problem, design, architecture, ~27k lines of TypeScript'), ('Skills', 'Design QA, accessibility, AI pipelines, full-stack TypeScript')],
 stats=[('$0.30', 'Per screen', 'In about 3 minutes, vs 2–3 hours per product by hand'), ('90%+', 'Proof', 'Of findings tied to a real element on the page'), ('229', 'Rules', 'Fixed checks before any AI judgement')],
 tldr=[('The problem', 'As the only designer across five products, I checked every release by hand. Design bugs hid behind dropdowns, errors and empty states nobody had time to open.'),
       ('What I did', 'Designed and built an engine that signs in, clicks through every state and checks it against 229 rules. A finding that can’t point to a real element is thrown out.'),
       ('Where it stands', 'A working prototype: about $0.30 and 3 minutes a screen, 90%+ of findings tied to an element, 187 tests. Parked after a restructuring; not run at scale.')],
 links=[('Assistantly on GitHub', 'https://github.com/MUZEEBURRAHAMAN/AI-UX-Audit-Assistant')],
 sections=[
  ('Overview', 'I built the QA teammate I didn’t have.', [
    ('p', 'I was the only designer across five legal-tech products at Omnis AI. Before each release I checked every screen by hand, and it took hours. So I built a tool that does the checking, and I keep the final say.'),
    ('rows', [('Give it a link', 'And a test login for the staging app.'), ('It clicks through', 'Screens, menus, dialogs and pop-ups, the way a person would.'),
              ('It checks each state', 'Against 229 fixed rules, then an AI pass for layout.'), ('You get a report', 'Every problem tied to an element, with a fix ready to paste.')], None),
  ]),
  ('The problem', 'Most design bugs show up only after a click.', [
    ('p', 'A screen can pass review when it first loads. The problems appear after someone opens a dropdown, submits a form with an error, or lands on an empty page. Nobody had time to click through all of those states before each release, so those bugs reached real users.'),
    ('fig', 'audit-dropdown-states.webp', 'At first load the form passes. Open the Matter dropdown and three problems appear: the list is cut off, the options are too faint, and it covers the Schedule button.'),
    ('callout', 'The goal', 'Check every state of every screen, fast enough to run before each release, and accurate enough that engineers would trust it.'),
  ]),
  ('Solution', 'Three parts: a clicker, a checker and a reporter.', [
    ('table', ['Part', 'What it does', 'What you get'], [
      ['Crawler', 'Logs in and clicks through screens, menus, dialogs and tabs', 'A record of each state it reached'],
      ['Checker', 'Runs 229 fixed rules (contrast, tokens, accessibility), then an AI pass for layout', 'Problems, each tied to a real element'],
      ['Reporter', 'Sorts problems into a view for each role', 'A report with the exact code fix per problem']]),
    ('p', 'Built for product designers, frontend engineers, QA, content designers and the managers who sign off on releases.'),
  ]),
  ('Background', 'One designer, five products, no QA team.', [
    ('cards', [('Owned five products', 'Each one shipped on its own schedule.'), ('Checked each release by hand', 'Screenshots, red boxes in Figma, then tickets.'), ('Repeated it after each fix', 'A fix meant checking the whole screen again.')]),
    ('p', 'A typical manual check meant screenshots, red boxes in Figma, a list of design tokens and a stack of tickets. When engineers fixed something, I checked everything again. Design QA became the thing holding releases back.'),
    ('fig', 'audit-02.webp', 'Before: my manual review in Figma, one note per problem.'),
  ]),
  ('Design process', 'Version one invented a button. Version two checks the real page.', [
    ('p', 'Each version tested one question: can a tool find design problems engineers trust enough to fix?'),
    ('iters', [('bad', 'V1 · Rejected', 'Reading screenshots with AI', 'A vision model listed problems from screenshots. On a dashboard I knew well it reported low contrast on “the secondary button beside the search field.” That button didn’t exist; the AI had guessed from what dashboards usually look like.', None),
               ('good', 'Final', 'Checking the real page, with proof', 'The tool works inside a live browser, runs 229 fixed rules first and uses AI only for layout questions. Any problem that can’t point to a real element is thrown out.', None)]),
    ('figs', [('audit-v1-vision-report.webp', 'V1 flagged a button that isn’t there.'), ('audit-08.webp', 'Final: each flagged element maps to a numbered finding with its selector and fix.')]),
    ('rows', [('A problem is spotted', 'By one of the 229 rules, or by the AI layout pass.'), ('Proof check', 'Does it point to a real element on the page?'),
              ('Yes: it’s reported', 'With the selector, the measured values and the fix.'), ('No: it’s dropped', 'Before anyone has to read it.')], None),
    ('callout', 'Rejections are remembered', 'If a designer rejects a finding, Assistantly won’t flag it again.'),
    ('fig', 'audit-03.webp', 'Reading a live page: styles, positions and the element tree, straight from the browser.'),
  ]),
  ('Outcome', 'What changed between the manual way and Assistantly.', [
    ('stats', [('$0.30', 'Cost and time', 'Per screen, in about 3 minutes'), ('89', 'One run', 'Problems across 22 states of CaseNotes in ~11 min, ~$1.20'), ('90%+', 'Proof', 'Of findings tied to a real element')]),
    ('table', ['Before · by hand', 'After · Assistantly'], [
      ['Hours of designer time per product', 'About 3 minutes per screen'], ['Some states checked, when there was time', 'All reachable controls on the audited screens'],
      ['A Figma screenshot with a red box', 'The exact element and a copy-paste fix'], ['Check everything again after a fix', 'One command re-checks and shows what changed']]),
    ('fig', 'audit-05.webp', 'The report, with the screen annotated and each problem tied to its element.'),
    ('panels', [('bad', 'Before', 'By hand, every release', ['Open each screen', 'Screenshot it and mark it up in Figma', 'Click states by hand, when there was time', 'Answer “which element?” one by one', 'Start over after each fix']),
                ('good', 'After', 'One command, proof attached', ['Run one command', 'It opens dialogs, drawers and dropdowns', 'Each problem anchored to its selector', 'Engineers paste the fix'])]),
    ('table', ['Severity', 'Blocker', 'Major', 'Minor', 'Nit', 'Praise'], [['AutoDoc · 87 findings', '4', '26', '42', '12', '3']]),
    ('honest', 'Scope note.', 'I measured these on my own test runs against Omnis staging apps. Nobody outside the team has checked them, and I haven’t run them on live traffic.'),
  ]),
  ('Design decisions', 'Proof first, clicks before judging, fixes ready to paste.', [
    ('rows', [('Proof before opinion', 'Fixed rules handle what can be measured: contrast, accessibility attributes and design tokens. AI handles judgement calls, only when it can point to the element.'),
              ('Click before judging', 'Assistantly opens each dialog, dropdown, drawer and tab before it reviews a screen.'),
              ('Every problem comes with its fix', 'Each card shows severity, the rule, a plain title, the principle behind it, a copy-paste CSS fix and a confidence score.'),
              ('Each role sees its own list', 'One run, six readers, each filtered to the work they can act on.')], None),
    ('figs', [('audit-04.webp', 'Going past the first screen to check dialogs, drawers and open dropdowns.'), ('audit-pr-handoff.webp', 'What the engineer receives: the rule, the element, measured colours and a fix.')]),
    ('table', ['Reader', 'What they see'], [
      ['Product designer', 'Problems by severity and token mismatches. Rejecting a false alarm stops it coming back.'], ['Frontend developer', 'Blockers with the exact element, its styles and the fix.'],
      ['QA', 'A log of every dialog, drawer and dropdown the tool opened.'], ['Content designer', 'A separate list of confusing labels and copy.'],
      ['Engineering manager', 'A dashboard across all products.'], ['Leadership', 'A record of problems fixed over time.']]),
    ('fig', 'audit-fleet-dashboard.webp', 'One run across four products: findings per product, open blockers with an owner, fixes per week and a release gate.'),
    ('figs', [('audit-06.webp', 'The content designer’s review track, separate from code rules.'), ('audit-07.webp', 'The screen index, with element counts and rule coverage per staging screen.')]),
  ]),
  ('Under the hood', 'Two codebases, one TypeScript stack.', [
    ('p', 'The **engine** captures and checks pages. The **service** adds the multi-product dashboard and automation.'),
    ('fig', 'audit-terminal-run.webp', 'One command logs in, opens each state, drops findings it can’t tie to an element, and saves HTML and Markdown reports.'),
    ('table', ['Layer', 'Technology'], [
      ['Runtime', 'Node + TypeScript, Model Context Protocol (MCP) SDK'], ['Capture', 'Playwright: sessions, full-page screenshots, DOM inventory, state crawler'],
      ['Accessibility', '@axe-core/playwright, run live per page'], ['AI vision', 'OpenAI-compatible SDK with Gemini Flash and OpenRouter fallbacks'],
      ['Image', 'Sharp for annotations, tesseract.js for OCR snapping, pixelmatch for diffs'],
      ['Service', 'Next.js 16, React 19, Tailwind 4, Prisma 7 + Postgres, BullMQ + Redis, Docker']]),
    ('links', [('Open a sample report (HTML)', 'assets/files/audit-report.html'), ('Open a sample report (Markdown)', 'assets/files/audit-report.md')]),
  ]),
  ('Agent skill', 'Run Assistantly’s review in your own agent.', [
    ('p', 'I packaged the heuristics, WCAG 2.2 rules, state-exploration prompts and report templates into a drop-in skill for Claude Code, Cursor, Windsurf and custom agent loops.'),
    ('list', ['229+ fixed UX and accessibility checks', 'Prompts and rules for exploring page states', 'Self-contained HTML and Markdown report templates', 'Copy-paste fixes for developers']),
    ('links', [('Download the skill (.skill)', 'assets/files/assistantly.skill'), ('Download the bundle (.zip)', 'assets/files/assistantly-skill.zip')]),
  ]),
  ('Looking back', 'What building it taught me.', [
    ('rows', [('Trust comes before speed', 'A tool that reports 50 problems with 15 made up costs more time than checking by hand.'),
              ('Real checks need clicks', 'Looking only at first loads misses overflowing dropdowns, error messages and empty pages.'),
              ('Engineers fix what they can paste', 'A selector and a code fix get merged. A vague comment gets skipped.')], None),
    ('honest', 'Where it stands.', 'A working prototype with 187 automated tests and about 27,000 lines of TypeScript. After a company restructuring changed the staging setup, I parked it. Testing at larger scale is still open.'),
    ('panels', [('mid', 'Next', 'If I pick it back up', ['Remember a baseline per product so runs flag only new problems.', 'Run on every staging deploy through GitHub Actions and flag blockers on pull requests.', 'Re-check after a fix is merged.', 'Send verified notes back into Figma.'])]),
  ]),
 ],
 faq=[('Who approved giving a designer staging credentials?', 'No new access was needed. It reused the staging access I already had for reviewing those apps by hand, and never touched production.'),
      ('Are you a designer or an engineer?', 'Product design is my foundation: research, UX architecture, interaction design and design systems. I also write production TypeScript to ship working prototypes and tooling end to end.'),
      ('What did you build versus engineering?', 'I conceived, designed and built the whole engine myself: the MCP architecture, Playwright crawlers, axe integration and the Next.js dashboard.'),
      ('How do you prevent hallucinations?', 'Fixed checks cover objective rules like contrast maths and ARIA attributes. AI findings are rejected unless they map to a real element on the page.'),
      ('How is it different from axe-core or Lighthouse?', 'Those check one static URL. Assistantly signs in, crawls interactive states, pairs axe-core with layout checks and exports ready-to-paste fixes.'),
      ('Can it run in CI?', 'Not yet. Running on every staging deploy and flagging blockers on pull requests is the next step.')],
),

# ------------------------------------------------------------------ CAREWAY
dict(
 slug='careway', name='Careway Landing Page', tags=['Landing page', 'Healthcare', 'A/B test'], read=9,
 cover='assets/img/cover/careway.webp',
 title='Careway: a landing page that sells cancer navigation software to two very different buyers.',
 lede='Careway is a cancer patient navigation platform. I designed its marketing site to win a cancer-centre leader who needs proof and a nurse navigator who wants their day back, inside the first **10 seconds**.',
 meta=[('Role', 'Product designer'), ('Project', 'Careway product design · Oct 2026'), ('Scope', 'Research, wireframes, 2 page variants, desktop + mobile, copy'), ('Audience', 'Cancer-centre leaders and nurse navigators')],
 stats=[('11', 'Sections', 'In the order a buyer asks questions'), ('2', 'Hero variants', 'Film hero vs product hero, for an A/B test'), ('1', 'Call to action', '“Book a demo”, repeated and never competing')],
 tldr=[('The problem', 'Health-software buyers decide in seconds whether to stay, and navigators are tired of “another tool”. The page had to feel like care first and software second.'),
       ('What I did', 'Studied four products that sell to busy professionals, set six design decisions, and designed two complete pages, a film hero and a product hero, at 1440 and 390 px with a copy deck.'),
       ('Where it stands', 'Designed in Figma as part of the full Careway product design, with an A/B test plan. Not launched, so there is no conversion data.')],
 sections=[
  ('Context', 'Careway connects three people around one patient.', [
    ('p', 'A nurse navigator guides a patient from diagnosis to survivorship: booking appointments, chasing results, arranging rides and sorting out insurance. Each navigator carries **80 to 120 patients**, and the work is spread across the EHR, spreadsheets, phone logs and sticky notes.'),
    ('cards', [('Linda · patient', 'Uses the mobile app to know what happens next and reach her navigator.'), ('Maria · navigator', 'Works her caseload on desktop and logs time as she goes.'), ('David · program manager', 'Balances caseloads and reports on billable navigation time.')]),
    ('callout', 'Why it matters now', 'Since January 2024, Medicare pays for navigation through codes G0023 and G0024, but a centre can bill only the minutes it can prove.'),
  ]),
  ('The brief', 'Ten seconds to win two buyers.', [
    ('panels', [('mid', 'Buyer 1', 'Cancer-centre leader', ['Owns the budget', 'Needs proof: outcomes, security, billing value', 'Wants to know it’s safe for patients']),
                ('mid', 'Buyer 2', 'Nurse navigator', ['Lives in the product every day', 'Tired of “another tool”', 'Wants to see their real worklist'])]),
    ('callout', 'Research objective', 'Choose a direction that explains Careway in one screen, proves it with the real product, and turns cancer-centre buyers into demo requests.'),
  ]),
  ('Research', 'Four products, one move borrowed from each.', [
    ('table', ['Product', 'What it does well', 'What I borrowed'], [
      ['Lassie AI', 'A calm full-bleed film, a one-line promise and a live ticker of what the AI just did', 'The film hero and a “Careway just…” activity line'],
      ['Heidi Health', 'Speaks to clinicians in their words, with proof and security badges early', 'Outcome numbers and a trust strip under the hero'],
      ['Joyful Health', 'Human photography and a clear problem-to-outcome story for administrators', 'The problem section and the admin value story'],
      ['Ferndesk', 'Shows the real product in a framed app window with feature tabs', 'Hero B with the navigator dashboard and tabs']]),
    ('fig', 'research-direction.webp', 'The landing page direction board: what I studied, six decisions, two hero variants and the page structure.'),
  ]),
  ('Decisions', 'Six decisions behind the page.', [
    ('rows', [('Emotion first, proof second', 'Buyers are clinical leaders. A human moment earns attention; evidence earns trust.'),
              ('Show the real product', 'Navigators see their actual worklist, rides and Copilot, proof that Careway was built for their day.'),
              ('One call to action', 'Health software is bought through a demo, so “Book a demo” is the only primary action, everywhere.'),
              ('A section for each role', 'Patients, navigators and admins each get a block, mirroring the product.'),
              ('Trust up front', 'HIPAA, data security and “AI never diagnoses” sit near the top, because clinical risk was the biggest worry in research.'),
              ('Same brand as the product', 'The app’s tokens (Archivo, navy, brand blue) plus Instrument Serif for a warmer, editorial tone.')], None),
  ]),
  ('Structure', 'Eleven sections, in the order a buyer asks questions.', [
    ('flow', ['Hero', 'Trust strip', 'Problem', 'Careway vs the usual way', 'How it works', 'For navigators', 'For patients', 'For admins', 'AI with guardrails', 'FAQ', 'Book a demo']),
    ('p', 'What is it, why care, how does it work, can I trust it, what next. I wireframed every section in grey first, so feedback stayed on order and hierarchy instead of colour.'),
    ('fig', 'wireframe-hero-b.webp', 'Wireframe v2 of Hero B, annotated before visual design.'),
  ]),
  ('Two heroes', 'I designed two heroes to test which one books more demos.', [
    ('iters', [('mid', 'Variant A', 'Film hero', 'Emotional and memorable: “Cancer care is hard. Navigation shouldn’t be.” Best for awareness, social and conference traffic. Risk: it says little about what the product does.', None),
               ('mid', 'Variant B', 'Product hero', 'Concrete and credible: “Every patient on track. Every follow-up done.” with the real dashboard. Best for buyers ready to evaluate. Risk: denser, so the headline has to stay short.', None)]),
    ('fig', 'hero-a-film.webp', 'Variant A: a calm film hero with one email field.'),
    ('fig', 'hero-b-product.webp', 'Variant B: the navigator dashboard in a framed window, with tabs that name each feature.'),
    ('figs', [('mobile-hero-a.webp', 'Variant A at 390 px.'), ('mobile-hero-b.webp', 'Variant B at 390 px.')]),
    ('callout', 'How I’d decide', 'Run the A/B test for four weeks. Primary metric: demo-request rate. Secondary: scroll depth to “How it works”.'),
  ]),
  ('The story', 'The problem, the comparison and three steps.', [
    ('fig', 'section-problem.webp', '“Patients don’t fall through the cracks. They fall through the handoffs.” Evidence from published research, with the source cited.'),
    ('fig', 'section-vs-usual-way.webp', 'Five tools against one worklist: each Careway feature shows what it replaces.'),
    ('fig', 'section-how-it-works.webp', 'From referral to follow-up in three steps, each with a small piece of real product UI.'),
  ]),
  ('A section for each role', 'Navigators, patients and admins each see their own value.', [
    ('fig', 'section-navigators.webp', 'For navigators: the whole caseload, sorted by who needs you now.'),
    ('fig', 'section-patients.webp', 'For patients: a calm companion between visits, in large type and plain words.'),
    ('fig', 'section-admins.webp', 'For program leaders: balanced caseloads and billable minutes captured automatically.'),
  ]),
  ('Trust', 'AI does the busywork. People make the decisions.', [
    ('fig', 'section-ai-guardrails.webp', 'An example question with a drafted, sourced answer, followed by the six AI rules from research.'),
    ('cards', [('A person decides', 'A navigator approves anything that reaches a patient or a record.'), ('Never diagnoses', 'No medical advice; symptoms go to the care team or the nurse line.'), ('Shows its work', 'Every suggestion says why and links to its source.')]),
  ]),
  ('Honesty & accessibility', 'No fake proof, and nothing that relies on colour alone.', [
    ('rows', [('No invented proof', 'The logo strip uses placeholders. No badges, quotes or numbers until real pilots exist.'),
              ('Contrast that passes', 'Text tokens meet WCAG AA on their surfaces.'),
              ('Never colour alone', 'Status uses an icon, a label and a colour together.'),
              ('Readable on any phone', 'Large type, simple words and layouts that work on older phones.')], None),
  ]),
  ('Looking back', 'What this page taught me.', [
    ('rows', [('A landing page is a sequence of answers', 'Ordering sections by the buyer’s questions did more than any visual flourish.'),
              ('Design two, then let data choose', 'Two strong heroes and a test plan beat arguing over one.'),
              ('Trust is content', 'For health software, guardrails and honesty belong near the top, not in the footer.')], None),
    ('honest', 'Not yet validated.', 'This is a design project: the page hasn’t launched and the A/B test hasn’t run.'),
  ]),
 ],
 faq=[('Why two hero variants instead of one?', 'They serve different visitors. The film hero suits people meeting Careway for the first time; the product hero suits buyers ready to evaluate. A test shows which books more demos.'),
      ('Why only one call to action?', 'Health software is sold through demos. Competing buttons would split attention away from the one action that matters.')],
),
]

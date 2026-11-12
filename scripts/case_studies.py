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
 slug='jobly', name='Jobly', tags=['Chrome extension', '0 → 1', 'Solo founder'], read=7,
 cover='assets/img/cover/jobly.webp',
 title='Jobly: fresh jobs with their real posting date, and help applying, in the browser toolbar.',
 lede='Job boards are full of listings that closed months ago, and every application asks for the same details again. I founded, designed and built Jobly on my own: a free Chrome extension, website and resume studio that fixes both.',
 meta=[('Role', 'Solo founder · design, code, launch'), ('Timeline', 'Sep – Nov 2026'), ('Platforms', 'Chrome extension, website, Studio'), ('Status', 'Website and Studio live · v1.4 extension')],
 stats=[('2,000+', 'Employers', 'Read from their own hiring systems'), ('60 days', 'Freshness rule', 'Anything older is dropped'), ('0', 'Accounts or servers', 'Everything stays in the browser')],
 tldr=[('The problem', 'Big job boards mix fresh roles with stale ones and hide the posting date. Applying means retyping the same profile into every form.'),
       ('The solution', 'An extension that shows only jobs from the last 60 days, with their real date, then helps you apply: profile import, apply assist, resume tailoring and cover letters.'),
       ('My role', 'Everything: research, product strategy, brand, UX and UI, the data pipeline, the extension, the website, the store listing and a pre-launch audit.')],
 links=[('Visit the Jobly website', 'https://jobly-88t.pages.dev'), ('Open Jobly Studio', 'https://jobly-studio.pages.dev'), ('Source on GitHub', 'https://github.com/MUZEEBURRAHAMAN/Jobly')],
 sections=[
  ('How job hunting works', 'Where a job comes from, and where it goes stale.', [
    ('p', 'Companies post jobs in their own hiring system (Greenhouse, Lever, Workday and others). Job boards copy those posts, often without the date, and keep them up long after the role is filled.'),
    ('pipeline', 'current', 'Today', 'Copied listings → stale jobs → retyped forms', ['Company posts a job', 'Boards copy it', 'Date gets lost', 'You apply to a filled role', 'Retype your profile again'], 'repeat for every application'),
    ('pipeline', 'proposed', 'With Jobly', 'Source of truth → fresh jobs → faster applications', ['Company posts a job', 'Jobly reads the source', 'Real date, 60-day limit', 'Matched in your browser', 'Apply assist fills the form']),
  ]),
  ('The problem', 'Three things waste a job seeker’s week.', [
    ('cards', [('Ghost jobs', 'Listings stay up after the role is filled, and many boards don’t show when a job was posted.'),
               ('The same form, again', 'Every application asks for name, links, experience and notice period, one field at a time.'),
               ('One resume for every job', 'Tailoring a resume to each posting takes too long, so most people don’t.')]),
  ]),
  ('Why an extension', 'I put Jobly where applying already happens.', [
    ('iters', [('bad', 'Option', 'Another job website', 'One more tab to remember, and it can’t help on the employer’s application page.', None),
               ('bad', 'Option', 'A mobile app', 'People browse jobs on phones but apply on laptops, where the forms and resumes are.', None),
               ('good', 'Chosen', 'A Chrome extension', 'One click from any tab, and it can fill an application form when asked. Data stays on the device.', None)]),
  ]),
  ('My role', 'One person, every part of the product.', [
    ('chips', ['Research', 'Product strategy', 'Brand', 'UX and UI', 'Design system', 'Extension (React, Manifest V3)', 'Data pipeline (Python)', 'Website (Astro)', 'Store listing', 'QA and security audit']),
  ]),
  ('Product overview', 'Find jobs, apply faster, keep your data.', [
    ('feature', 'Popup', 'New jobs, one click from any tab', 'The toolbar popup shows fresh matches. The full dashboard opens from there.', ['v14-popup.webp', 'v14-jobs.webp']),
    ('cards', [('Find', 'Fresh jobs from 2,000+ employers, with filters, dealbreakers and alerts.'), ('Apply', 'Profile import, apply assist, tailored resumes and cover letters.'), ('Private', 'No account and no server. Jobly reads a page only when you ask.')]),
  ]),
  ('Find jobs', 'Every card shows when the job was really posted.', [
    ('feature', 'Jobs', 'A feed that only shows recent jobs', 'Roles you pick, from the last 60 days, with the real date and a “Matches you” tag.', 'v14-jobs.webp'),
    ('feature', 'Companies', 'Follow companies, not searches', 'Turn on alerts for a company and hear about every new job it posts.', 'v14-companies.webp'),
    ('feature', 'Saved', 'Saved and applied in one list', 'After you open a job, Jobly asks “Did you apply?” and keeps your applications in one place.', 'v14-saved.webp'),
  ]),
  ('Apply faster', 'Set up once, then let Jobly do the typing.', [
    ('feature', 'Profile setup', 'Import a LinkedIn PDF and check six short steps', 'The PDF is read in the browser, never uploaded. A completeness score shows what’s missing.', 'v14-profile-setup.webp'),
    ('feature', 'Apply assist', 'A panel that fills the application with you', 'Each answer shows where it came from. Questions only you can answer are marked. You press Submit yourself.', 'v14-apply-assist.webp'),
    ('feature', 'Tailor for a job', 'See which requirements your resume covers', 'Paste a job description to get a coverage score and the line that proves each requirement. Accept changes one by one.', 'v14-tailor.webp'),
    ('feature', 'Resume and cover letter', 'Documents built from the same profile', 'Four resume templates as PDF or Word, and cover letters that answer what the posting asks for.', ['v14-resume.webp', 'v14-cover-letter.webp']),
  ]),
  ('Under the hood', 'No server, by design.', [
    ('pipeline', 'proposed', 'Data', 'Public job feeds → static files → filtered in your browser', ['2,000+ employer feeds', 'Read every 4 hours', 'Static files on Cloudflare', 'Extension, website, Studio']),
    ('p', 'Every client downloads the same public files and filters them locally. With no server, there is nothing to attack and nothing to keep running.'),
  ]),
  ('The website', 'A product site that explains the extension.', [
    ('browser', 'web-full.webp', 'jobly-88t.pages.dev', 'The full Jobly website. Scroll inside the frame.'),
  ]),
  ('Quality', 'I audited Jobly before launch, and it failed.', [
    ('stats', [('46', 'Findings', '6 of them blockers'), ('1 day', 'To fix', 'Re-checked in a real browser'), ('0', 'axe issues', 'In light and dark themes')]),
    ('p', 'A Playwright, axe-core and dependency audit said “not ready”. The fix went past patches: I moved all user data onto the device and removed the server.'),
  ]),
  ('Looking back', 'What Jobly taught me.', [
    ('rows', [('Freshness is a data problem first', 'No layout can fix a stale listing. The 60-day rule had to live in the pipeline.'),
              ('Help, don’t take over', 'Apply assist fills fields, but the person approves every answer and presses Submit.'),
              ('Audit before you publish', 'Testing my own product like an attacker found problems no design review would.')], None),
    ('honest', 'No usage numbers yet.', 'The website and Studio are live. Version 1.4 of the extension is packaged for the Chrome Web Store.'),
  ]),
 ],
 faq=[('Why build it alone?', 'Jobly started as the tool I wanted for my own search. Owning design and code meant every decision, from the data pipeline to the button copy, served the same promise.'),
      ('Does apply assist submit applications?', 'No. It fills fields after you approve them. You always press Submit yourself.')],
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
 slug='careway', name='Careway Landing Page', tags=['Competitor audit', 'Landing page', 'Healthcare'], read=10,
 cover='assets/img/cover/careway.webp',
 title='Careway: I audited how oncology software sells itself, then designed a page that fixes it.',
 lede='Cancer centres buy navigation software from pages that talk about “digital health solutions” and never show a navigator’s day. I audited a direct competitor’s homepage, found **13 problems**, and designed Careway’s landing page to answer each one.',
 meta=[('Role', 'Product designer'), ('Project', 'Careway product design · Oct 2026'), ('Scope', 'Competitor audit, wireframes, 2 hero variants, desktop + mobile, copy'), ('Audience', 'Cancer-centre leaders and nurse navigators')],
 stats=[('13', 'Problems found', 'On a direct competitor’s homepage'), ('6', 'Calls to action', 'Competing on their page. Careway has one primary action'), ('0', 'Mentions', 'Of navigators, billing or HIPAA on their page')],
 tldr=[('The problem', 'Oncology software pages sell features in buyer jargon. A navigator can’t see their day in them, and a leader can’t see the billing value or the safety rules.'),
       ('What I did', 'Captured a direct competitor’s homepage, audited it with measured checks, scored it against Careway, and designed two hero variants and a full page that answer every finding.'),
       ('Where it stands', 'Designed in Figma with an A/B test plan. Not launched, so there is no conversion data yet.')],
 sections=[
  ('The problem', 'A navigator’s work is hard to buy software for.', [
    ('p', 'A nurse navigator guides a patient from diagnosis to survivorship: booking appointments, chasing results, arranging rides and sorting out insurance. Each navigator carries **80 to 120 patients**, and the work is spread across the EHR, spreadsheets, phone logs and sticky notes.'),
    ('callout', 'Why it matters now', 'Since January 2024, Medicare pays for navigation through codes G0023 and G0024, but a centre can bill only the minutes it can prove.'),
    ('panels', [('mid', 'Buyer 1', 'Cancer-centre leader', ['Owns the budget', 'Needs proof: outcomes, security, billing value', 'Wants to know it’s safe for patients']),
                ('mid', 'Buyer 2', 'Nurse navigator', ['Lives in the product every day', 'Tired of “another tool”', 'Wants to see their real worklist'])]),
    ('callout', 'The question I set', 'What does each buyer need to see in the first 10 seconds, and what do the pages in this category show them instead?'),
  ]),
  ('Competitor audit', 'I audited a direct competitor’s homepage, top to bottom.', [
    ('p', 'Navigating Care sells oncology patient management software to the same cancer centres, and it is one of the most widely deployed platforms in the US. The product is respected. This audit is about the page: how well it explains the product to the two buyers above.'),
    ('p', 'I captured the homepage on **7 Nov 2026** at 1440 px, read it at 390 px, ran axe-core for WCAG 2 AA, measured contrast, and counted every call to action. Numbers on the capture match the findings below.'),
    ('browser', 'competitor-full.webp', 'navigatingcancer.com · captured 7 Nov 2026', 'The full homepage with my audit markers. Scroll inside the frame to read it all.'),
  ]),
  ('Findings', 'Thirteen problems, and Careway’s answer to each.', [
    ('findings', [
      (1, 'Major', 'The headline could belong to any health company', '“Digital health solutions that improve the lives of cancer patients.” It names no user, no job and nothing about navigation.', 'The product hero names the outcome a navigator wants: “Every patient on track. Every follow-up done.”'),
      (2, 'Major', 'The hero button is “Learn More”', 'The only action above the fold, on desktop and at 390 px, is “Learn More”. “Schedule a Demo” first appears in the next section.', '“Book a demo” is the primary button in the nav and the hero. The one secondary button, “See how it works”, stays on the page.'),
      (3, 'Minor', 'An illustration stands in for the product', 'A flat doctor-and-patient illustration fills the hero. The real product first appears in the third section.', 'The hero shows the real navigator dashboard in a framed window, with tabs that name each feature.'),
      (4, 'Major', 'The proof is five years old', '“500K+ patient education articles sent in 2021”. The four numbers count volume (providers, patients, articles, interactions), not outcomes.', 'No customer numbers until real pilots exist. The problem section cites published research, with the source on the page, and the logo strip uses fictional centre names as placeholders.'),
      (5, 'Minor', 'The copy speaks buyer jargon', '“Industry-leading digital triage, ePRO and patient engagement solutions”. Nothing describes a navigator’s day.', 'Each role gets a section in its own words: navigators, patients and program leaders.'),
      (6, 'Major', 'Six calls to action compete', 'Learn More, Schedule a Demo, For Providers, For Life Sciences, Learn more, Schedule a demo. The page also splits its attention between providers and life-sciences companies.', 'One primary action, “Book a demo”, repeated. One audience: cancer centres.'),
      (7, 'Major', 'Testimonial names fail contrast', 'White on #49915e measures **3.82:1**. WCAG AA needs 4.5:1 for text this size.', 'Every text token passes AA on its surface.'),
      (8, 'Major', 'The tab labels fail contrast', 'Inactive tabs are #808c9a on white, **3.42:1**.', 'Same rule: no text below 4.5:1, and states use a label as well as colour.'),
      (9, 'Minor', 'The video is a black box', 'No poster image and no captions. Until someone presses play, the section shows nothing.', 'Product UI appears as stills inside each step, so the page explains itself without playing anything.'),
      (10, 'Minor', 'The one outcome number is also from 2021', '“76% of patients report improved communication”, from a 2021 survey, followed by another “Learn more”.', 'Outcomes wait for pilot data. Until then the page shows what the product does, not claims about it.'),
      (11, 'Minor', 'The last call to action is vague', '“It begins with a conversation.” It doesn’t say who the demo is for or what happens in it.', 'An FAQ answers the last objections first. The closing section says exactly what happens: “See Careway with your own workflow in a 30-minute demo.”'),
      ('', 'Blocker', 'Navigation, billing and safety are missing', 'The words navigator, navigation, HIPAA, billing and AI appear **0 times**. The Medicare navigation codes aren’t mentioned.', 'A program-leader section on billable minutes, a section of AI rules (a person decides, the AI never diagnoses, it shows its sources), and FAQ answers on data security and medical advice.'),
      ('', 'Major', 'The markup gets in the way of screen readers', 'Four h1 headings (two of them empty), two images without alt text, a logo link with no accessible name, and videos without captions.', 'The build spec calls for one h1, headings in section order, and alt text for every product image.'),
    ]),
  ]),
  ('Their hero vs mine', 'Same buyer, same 10 seconds.', [
    ('cmp', 'competitor-hero.webp', 'hero-b-product.webp', 'Navigating Care', 'Careway · Hero B'),
    ('p', 'Drag the handle. Theirs leads with an illustration and “Learn More”. Mine leads with the worklist a navigator would open on Monday morning and one clear next step.'),
  ]),
  ('Scorecard', 'Eight questions a buyer asks, scored for both pages.', [
    ('table', ['Question', 'Navigating Care', 'Careway'], [
      ['What is it, in 10 seconds?', 'Generic headline', 'Outcome headline + real product'],
      ['Can I see the product?', 'Third section', 'In the hero'],
      ['What should I do next?', '6 competing actions', '1 primary action: Book a demo'],
      ['Is it for navigators?', 'Never mentioned', 'A section for each role'],
      ['Does it pay for itself?', 'Not mentioned', 'Billable minutes, G0023/G0024'],
      ['Is it safe, and what does the AI do?', 'Not mentioned', 'AI rules + security FAQ'],
      ['Is the proof current?', '2021 numbers', 'Cited research, no invented numbers'],
      ['Can everyone read it?', '2 contrast failures, 4 h1s', 'AA tokens, one h1 in the spec'],
    ]),
  ]),
  ('How Careway answers', 'The sections that fix the findings.', [
    ('fig', 'section-problem.webp', 'Fixes 4: “Patients don’t fall through the cracks. They fall through the handoffs.” Evidence from published research, with the source cited.'),
    ('fig', 'section-vs-usual-way.webp', 'Fixes 5 and 6: five tools against one worklist. Each Careway feature shows what it replaces.'),
    ('fig', 'section-how-it-works.webp', 'Fixes 3 and 9: from referral to follow-up in three steps, each with a still of real product UI.'),
    ('fig', 'section-ai-guardrails.webp', 'Fixes the missing safety story: an example question with a drafted, sourced answer, followed by the AI rules.'),
  ]),
  ('Where the ideas came from', 'Four products outside oncology, one move borrowed from each.', [
    ('table', ['Product', 'What it does well', 'What I borrowed'], [
      ['Lassie AI', 'A calm full-bleed film and a one-line promise', 'The film hero (Variant A)'],
      ['Heidi Health', 'Speaks to clinicians in their words, with proof early', 'The logo strip under the hero'],
      ['Joyful Health', 'A clear problem-to-outcome story for administrators', 'The problem section and the admin story'],
      ['Ferndesk', 'The real product in a framed window with feature tabs', 'Hero B with the navigator dashboard']]),
  ]),
  ('Two heroes', 'I designed two heroes to test which one books more demos.', [
    ('iters', [('mid', 'Variant A', 'Film hero', 'Emotional and memorable: “Cancer care is hard. Navigation shouldn’t be.” Best for awareness and conference traffic. Risk: it says little about what the product does.', None),
               ('mid', 'Variant B', 'Product hero', 'Concrete: “Every patient on track. Every follow-up done.” with the real dashboard. Best for buyers ready to evaluate. Risk: denser, so the headline has to stay short.', None)]),
    ('figs', [('mobile-hero-a.webp', 'Variant A at 390 px.'), ('mobile-hero-b.webp', 'Variant B at 390 px.')]),
    ('callout', 'How I’d decide', 'Run the A/B test for four weeks. Primary metric: demo-request rate. Secondary: scroll depth to “How it works”.'),
  ]),
  ('The full page', 'Scroll through the whole Careway page.', [
    ('browser', 'careway-full.webp', 'Careway landing page · Hero B · 1440 px', 'All 11 sections of Hero B, from the hero to the footer, exported from the Figma design at 1440 px.'),
  ]),
  ('Looking back', 'What the audit taught me.', [
    ('rows', [('Audit before you design', 'Measuring a competitor’s page gave every design decision a reason I could point to.'),
              ('A landing page is a sequence of answers', 'Ordering sections by the buyer’s questions did more than any visual flourish.'),
              ('Trust is content', 'For health software, safety rules and honest proof belong near the top, not in the footer.')], None),
    ('honest', 'Not yet validated.', 'The page hasn’t launched and the A/B test hasn’t run. The audit covers one competitor’s homepage on one day; their page may change.'),
  ]),
 ],
 faq=[('Why audit a competitor instead of starting from a blank page?', 'Buyers compare pages side by side. Knowing exactly where the category falls short showed me what Careway had to say first.'),
      ('Why only one call to action?', 'Health software is sold through demos. Their page shows six competing actions; I kept one primary action.')],
),
]


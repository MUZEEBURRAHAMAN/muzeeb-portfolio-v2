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
 slug='gofully', name='GoFully', tags=['Chrome extension', 'Brand + product'], read=7,
 cover='assets/img/cover/gofully.webp',
 title='GoFully: redesigning a screenshot extension around one promise, nothing leaves your device.',
 lede='GoFully could capture, read, mark up, redact and export a whole page, all offline, but it looked like every other screenshot tool. I redesigned the brand, the extension and the website so that promise is the first thing people see.',
 meta=[('Role', 'Product designer · brand, UX, UI, website'), ('Product', 'Screenshot extension · 5 browsers'), ('Scope', 'Brand guide, design system, 70+ screens, website'), ('Status', 'New website live')],
 stats=[('41 pages', 'Brand guide', 'From positioning to the 16 px icon'), ('70+', 'Extension screens', 'Every state, light and dark'), ('1', 'Primary action', 'Per screen, in navy')],
 tldr=[('The problem', 'A capable offline screenshot tool listed every feature at once, so its one real difference, privacy, got lost.'),
       ('The solution', 'One promise across every surface: capture the whole page and keep it on your device. A new symbol, a calm design system and a site that shows the product.'),
       ('My role', 'Brand strategy and identity, design system, every extension and editor screen, and the website design.')],
 links=[('Visit the GoFully website', 'https://gofully-extension.vercel.app')],
 sections=[
  ('How screenshots work today', 'Sharing one page takes a chain of apps.', [
    ('pipeline', 'current', 'Today', 'Five tools → one leak', ['Capture tool', 'Image editor', 'Blur by hand', 'PDF converter', 'Upload to share'], 'redo when a detail was missed'),
    ('pipeline', 'proposed', 'With GoFully', 'One click → ready to share, on your device', ['One click or shortcut', 'Whole page stitched', 'Redact and mark up', 'Export PNG, PDF or text', 'Nothing uploaded']),
  ]),
  ('The problem', 'The best thing about GoFully was the quietest thing on the page.', [
    ('cards', [('A headline of features', '“Full Page Screenshot Tool. One Extension. Every Job.” then OCR, 4K and PDF in one line.'),
               ('A generic camera icon', 'It sat next to dozens of other screenshot extensions with cameras.'),
               ('Privacy as a small badge', '“100% on-device” was a tiny label above the headline.')]),
    ('cmp', 'before-site-hero.webp', 'after-site-hero.webp', 'Before · old site', 'After · new site'),
    ('fig', 'before-store-entire.webp', 'Before: four store screenshots, four different layouts.'),
  ]),
  ('My role', 'Brand to website, end to end.', [
    ('chips', ['Positioning', 'Brand identity', '41-page brand guide', 'Design system v2', 'Extension UX and UI', 'Editor', 'Error and edge states', 'Website design', 'Store screenshots']),
  ]),
  ('Brand', 'Private, precise, fast.', [
    ('fig', 'brand-positioning.webp', 'Positioning and moodboard from the brand guide.'),
    ('feature', 'Symbol', 'A viewfinder drawn as a G', 'It still reads as “screenshot”, and it can only be GoFully. Below 32 px the wordmark drops and the symbol stands alone.', 'r0-mark-a.webp'),
    ('feature', 'Design system', 'Soft corners, a 4 px grid and two quiet shadows', 'Radius by role, navy shadows instead of black, one icon weight. Every component in four states.', 'ui-components.webp'),
  ]),
  ('The extension', 'One primary action per screen, and a way out of every error.', [
    ('feature', 'Popup', 'Every capture mode, with its shortcut', 'When a capture fails, the popup says what happened and what to do next.', ['popup-default.webp', 'popup-failed.webp']),
    ('feature', 'Full page', 'The whole page, in one image', 'It scrolls, waits for lazy images and stops sticky headers repeating.', 'site-fullpage.webp'),
    ('feature', 'Redact', 'Hide what shouldn’t be seen, before you share', 'Emails, card numbers and API keys are covered automatically.', ['site-redact.webp', 'ed-redact.webp']),
    ('feature', 'Text', 'Copy text out of any image', 'Six languages, read on the device.', 'site-ocr.webp'),
    ('feature', 'Editor', 'Everything after the capture, in one quiet window', 'Crop, arrows, text, blur and Beautify, in light and dark.', ['ed-default.webp', 'ed-dark.webp']),
    ('feature', 'Result card', 'Copy, save, edit or pin', 'After a capture, a small card appears on top of any site.', 'ov-result-card.webp'),
  ]),
  ('The website', 'I replaced the feature list with one sentence.', [
    ('lead', 'Old: “Full Page Screenshot Tool. One Extension. Every Job.” New: **“The screenshot studio that stays on your device.”**'),
    ('fig', 'landing-hero-options.webp', 'Three hero directions, each tested against the same long article.'),
    ('feature', 'Live demos', 'Each feature plays on a real page', 'Pick a demo or let them run.', 'site-demo.webp'),
    ('feature', 'Comparison', 'Four tools, or one', 'What people usually pay for, set against one free extension.', 'site-vs.webp'),
    ('browser', 'site-full.webp', 'gofully-extension.vercel.app', 'The full GoFully website. Scroll inside the frame.'),
  ]),
  ('Looking back', 'What GoFully taught me.', [
    ('rows', [('Lead with the difference', 'Privacy moved from a badge to the headline, because it was the one thing competitors couldn’t say.'),
              ('Design the failures too', 'Every error state got a next step, so people don’t get stuck.'),
              ('One look everywhere', 'Icon, popup, editor and website now share one system and one message.')], None),
    ('honest', 'No post-launch metrics yet.', 'The new website is live. This shows the design work, not results.'),
  ]),
 ],
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
 slug='assistantly', name='Assistantly', tags=['AI tooling', 'Design QA'], read=7,
 cover='assets/img/cover/assistantly.webp',
 title='Design QA took me a day per release. So I built Assistantly, which takes minutes.',
 lede='Assistantly opens a web app the way a person would, clicks through its menus and pop-ups, and lists each design problem it finds with **the exact code fix**. It costs about $0.30 a screen.',
 meta=[('Role', 'Solo designer and builder'), ('Duration', 'Jun – Jul 2026 · Omnis AI'), ('Owned', 'Problem, design, architecture, ~27k lines of TypeScript'), ('Status', 'Working prototype · parked')],
 stats=[('$0.30', 'Per screen', 'About 3 minutes, vs hours by hand'), ('90%+', 'Proof', 'Findings tied to a real element'), ('229', 'Rules', 'Fixed checks before any AI')],
 tldr=[('The problem', 'As the only designer across five products, I checked every release by hand. Bugs hid behind dropdowns, errors and empty states nobody had time to open.'),
       ('The solution', 'An engine that signs in, clicks through every state, checks it against 229 rules and reports each problem with its element and a fix. Anything it can’t prove is dropped.'),
       ('My role', 'Problem framing, product and report design, architecture and the full TypeScript build.')],
 links=[('Assistantly on GitHub', 'https://github.com/MUZEEBURRAHAMAN/AI-UX-Audit-Assistant')],
 sections=[
  ('How design QA works', 'Most teams check a release by hand, one screenshot at a time.', [
    ('pipeline', 'current', 'By hand', 'Screenshots → red boxes → tickets', ['Open each screen', 'Screenshot it', 'Mark it up in Figma', 'Write tickets', 'Engineer asks “which element?”'], 'check everything again after each fix'),
    ('pipeline', 'proposed', 'With Assistantly', 'One command → proof → a fix to paste', ['Give it a link', 'It clicks every state', '229 rules, then AI', 'Unproven findings dropped', 'Report with code fixes']),
  ]),
  ('The problem', 'Most design bugs show up only after a click.', [
    ('fig', 'audit-dropdown-states.webp', 'At first load the form passes. Open the Matter dropdown and three problems appear: the list is cut off, the options are too faint, and it covers the Schedule button.'),
    ('fig', 'audit-02.webp', 'Before: my manual review in Figma, one note per problem.'),
  ]),
  ('My role', 'One designer, five products, no QA team.', [
    ('chips', ['Problem framing', 'Product design', 'Report and dashboard UI', 'Rule set (229 checks)', 'Architecture', 'TypeScript engine', 'Playwright crawler', 'Testing (187 tests)']),
  ]),
  ('The key decision', 'Version one invented a button. Version two checks the real page.', [
    ('iters', [('bad', 'V1 · Rejected', 'Reading screenshots with AI', 'It reported low contrast on a button that didn’t exist. The AI guessed from what dashboards usually look like.', None),
               ('good', 'Final', 'Checking the live page, with proof', 'Fixed rules run first; AI only answers layout questions. A finding that can’t point to a real element is thrown out.', None)]),
    ('figs', [('audit-v1-vision-report.webp', 'V1 flagged a button that isn’t there.'), ('audit-08.webp', 'Final: each flagged element maps to a numbered finding.')]),
  ]),
  ('How it works', 'A clicker, a checker and a reporter.', [
    ('feature', 'Run', 'One command does the whole audit', 'It logs in, opens each state, drops what it can’t prove, and saves HTML and Markdown reports.', 'audit-terminal-run.webp'),
    ('feature', 'Explore', 'It opens every dialog, drawer and dropdown', 'Screens are judged after they’re clicked, not just at first load.', 'audit-04.webp'),
    ('feature', 'Check', 'It reads the real page', 'Styles, positions and the element tree come straight from the browser.', 'audit-03.webp'),
    ('feature', 'Report', 'Every problem tied to its element', 'Severity, rule, plain title, a copy-paste fix and a confidence score.', 'audit-05.webp'),
    ('feature', 'Hand-off', 'What the engineer receives', 'The rule, the element, the measured colours and the fix.', 'audit-pr-handoff.webp'),
    ('feature', 'Roles', 'Each reader sees their own list', 'Content designers get copy issues; QA gets the log of every state opened.', ['audit-06.webp', 'audit-07.webp']),
    ('feature', 'Dashboard', 'One run across four products', 'Findings per product, open blockers with an owner, and a release gate.', 'audit-fleet-dashboard.webp'),
  ]),
  ('Outcome', 'What changed.', [
    ('stats', [('3 min', 'Per screen', 'About $0.30 each'), ('89', 'One run', 'Problems across 22 states in ~11 min'), ('90%+', 'Proof', 'Findings tied to a real element')]),
    ('panels', [('bad', 'Before', 'By hand, every release', ['Hours per product', 'Some states, when there was time', 'A red box in Figma', 'Start over after each fix']),
                ('good', 'After', 'One command', ['Minutes per screen', 'Every reachable state', 'The exact element and a fix', 'Re-check shows what changed'])]),
    ('honest', 'Scope note.', 'Measured on my own runs against Omnis staging apps, not on live traffic.'),
    ('links', [('Open a sample report (HTML)', 'assets/files/audit-report.html'), ('Download the agent skill (.zip)', 'assets/files/assistantly-skill.zip')]),
  ]),
  ('Looking back', 'What building it taught me.', [
    ('rows', [('Trust comes before speed', 'A tool that reports 50 problems with 15 made up costs more time than checking by hand.'),
              ('Real checks need clicks', 'First loads miss overflowing dropdowns, errors and empty pages.'),
              ('Engineers fix what they can paste', 'A selector and a code fix get merged. A vague comment gets skipped.')], None),
    ('honest', 'Where it stands.', 'A working prototype with 187 tests. I parked it after a restructuring changed the staging setup.'),
  ]),
 ],
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
# ------------------------------------------------------------------ PETSY
dict(
 slug='petsy', name='Petsy', tags=['E-commerce', '3D + motion', 'Design + code'], read=5,
 cover='assets/img/cover/petsy.webp',
 title='Petsy: a pet clothing store where a 3D dog or cat tries the coat on before you buy.',
 lede='Pet clothes get bought on a guess. You can’t hold a jumper up to a cat, and size charts ask for a chest measurement nobody has taken. I designed and built Petsy so the pet tries it on first.',
 meta=[('Role', 'Solo designer and developer'), ('Product', 'Online store · home + product'), ('Built with', 'React, GSAP, three.js, then Base44'), ('Status', 'Live on Base44 · #Base44Challenge')],
 stats=[('3D', 'Fitting room', 'A rigged dog and cat wear the coat'), ('18', 'Pages', 'On one design system'), ('1', 'Motion scale', 'For every hover and reveal')],
 tldr=[('The problem', 'Pet clothes are sized from charts and photos of a breed your pet isn’t, so they often go back.'),
       ('The solution', 'A store with a 3D fitting room, an AI size finder that explains its answer, and motion that makes browsing feel like a boutique.'),
       ('My role', 'Reference analysis, wireframes, design system, motion, 3D, front-end code, and the rebuild in Base44 with its automations.')],
 links=[('Open the live store', 'https://petsy-style-edit.base44.app')],
 sections=[
  ('How pet clothes are bought', 'Today it’s a guess and a return.', [
    ('pipeline', 'current', 'Today', 'Size chart → guess → return', ['See a photo of another breed', 'Guess from a size chart', 'Order', 'It doesn’t fit', 'Send it back'], 'try another size'),
    ('pipeline', 'proposed', 'With Petsy', 'Try it on → right size → keep it', ['Pick your pet', 'See the coat on a 3D model', 'Size finder explains its pick', 'Order once', 'Keep it']),
  ]),
  ('My role', 'From reference to live store.', [
    ('chips', ['Reference analysis', 'Wireframes', 'Design tokens', 'Type and colour', 'Motion design (GSAP)', '3D fitting room (three.js)', 'React front end', 'Base44 rebuild', 'Checkout and automations']),
    ('p', 'I measured a real boutique store’s structure and type, then kept its section order and replaced its fonts and colours with a softer pet-friendly system: Fraunces, DM Sans, oat and terracotta.'),
  ]),
  ('Home', 'A boutique feel, built from motion.', [
    ('feature', 'Hero', 'A full-screen video hero', 'One headline, two clear paths: Shop dogs or Shop cats.', 'hero.webp'),
    ('feature', 'Browse', 'Shop by kind, then what’s new', 'Arched category tiles, and a New In grid that staggers in on scroll with Dogs and Cats filters.', ['categories.webp', 'new-in.webp']),
    ('feature', 'Lookbook', 'A lookbook that opens into the full outfit', 'Click a photo and it morphs into the look, with every product in it.', 'lookbook.webp'),
    ('feature', 'Brands', 'Brand rails you can drag', 'Each brand gets a banner and a product rail with inertia.', 'brand-spotlight.webp'),
    ('feature', 'Try-on', 'See it on them', 'Spin and switch colourways on a 3D Shiba Inu or cat, then open the fitting room.', 'tryon-teaser.webp'),
  ]),
  ('Product page', 'The page that answers “will it fit?”', [
    ('feature', 'Fitting room', 'A 3D model wears the coat', 'Switch dog or cat, change the colour and make it walk; the knit moves with the skeleton. Size chips and “Find my size” sit beside it.', 'product-top.webp'),
    ('feature', 'Proof', 'Complete the look, and reviews with pet photos', 'Reviews show the breed and size each owner bought.', 'product-reviews.webp'),
  ]),
  ('Automations', 'What I added when I rebuilt it in Base44.', [
    ('cards', [('AI size finder', 'Breed, chest and weight in; the right size and the reason out.'),
               ('Ask Petsy', 'An assistant that picks products, fills the bag and tracks orders.'),
               ('Real checkout', 'Server functions end in a paid, pending or failed receipt with a transaction ID.')]),
  ]),
  ('The full pages', 'Scroll through the store.', [
    ('browser', 'home-full.webp', 'Petsy · home', 'The full home page.'),
    ('browser', 'product-full.webp', 'Petsy · product', 'The full product page.'),
  ]),
  ('Looking back', 'What Petsy taught me.', [
    ('rows', [('Solve the real doubt', 'Shoppers didn’t need more photos. They needed to see it on their kind of pet.'),
              ('Borrow structure, not style', 'A proven section order saved time; the type and colour made it Petsy.'),
              ('Prompt one section at a time', 'Rebuilding in Base44 worked because each prompt carried one finished section.')], None),
    ('honest', 'A challenge project.', 'Petsy is live but isn’t a real shop yet. The photos come from Unsplash.'),
  ]),
 ],
),
# ------------------------------------------------------------------ AVATARLY
dict(
 slug='avatarly', name='Avatarly', tags=['Figma plugin', 'Design + code'], read=3, compact=True,
 cover='assets/img/cs/avatarly/store-01.webp',
 title='Avatarly: I got tired of pasting the same six faces into every mockup.',
 lede='Every user list, chat and table I design needs faces. Finding them, cropping them and pasting them one by one was eating real time. So I built the plugin I wanted: select the shapes, pick a style, done.',
 meta=[('Role', 'Solo designer and developer'), ('Product', 'Figma plugin'), ('Library', '12 collections · 1,198 images'), ('Built with', 'Figma Plugin API, JavaScript')],
 links=[('Source on GitHub', 'https://github.com/MUZEEBURRAHAMAN/avatarly-figma-plugin')],
 sections=[
  ('Why I built it', 'Placeholder faces were costing me minutes on every screen.', [
    ('pipeline', 'current', 'Before', 'One face at a time', ['Search for a photo', 'Download and crop', 'Paste into the shape', 'Repeat 20 times', 'Same faces in every file'], 'again on the next screen'),
    ('pipeline', 'proposed', 'With Avatarly', 'One click, every shape', ['Select a frame or table', 'Pick a style', 'Every shape filled', 'Shuffle if you want', 'Layout untouched']),
    ('cards', [('Other plugins insert, I fill', 'New image layers break auto layout. Avatarly fills the shapes you already drew.'),
               ('Other plugins depend on outside services', 'Faces vanish when a service changes. Every image here ships with the plugin.'),
               ('Real products are not all photos', 'Mockups need initials, logos, bots and status rings too.')]),
  ]),
  ('Store screenshots', 'Seven frames I designed to explain the plugin before anyone installs it.', [
    ('carousel', [('store-01.webp', '12 styles, one plugin', 'The opening frame shows range first: office photos, 3D, cartoon, memoji, pixel and more.'),
                  ('store-04.webp', 'One click. Every shape filled.', 'The core promise as a before and after, so it reads without any copy.'),
                  ('store-05.webp', 'Filter by vibe', 'Narrow by gender, profession or tone so faces match the product.'),
                  ('store-03.webp', 'Browse before you fill', 'A gallery for when one specific avatar matters.'),
                  ('store-02.webp', 'Ship-ready components', 'One click builds a component set with default, hover, active, selected and disabled states.'),
                  ('store-07.webp', 'Real-world detail', 'Status dots and story rings, added without leaving Figma.'),
                  ('store-06.webp', 'Beyond faces', 'Company logos, abstract marks, bots and pixel avatars for any placeholder.')]),
  ]),
  ('The plugin', 'Three tabs, each with one job.', [
    ('gallery', [('quick-add.webp', 'Quick Add: pick a style and fill the selection.'), ('gallery.webp', 'Gallery: browse and place one avatar.'), ('components.webp', 'Components: generate a full component set.')], 3),
    ('p', 'For speed, 14 Quick Fill commands run straight from the Figma menu, with no window at all.'),
  ]),
  ('First run', 'Three slides teach the whole thing.', [
    ('gallery', [('onboard-1.webp', 'What it does.'), ('onboard-2.webp', 'Select, pick a style, fill.'), ('onboard-3.webp', 'Twelve built-in collections.')], 3),
  ]),
 ],
),
# ------------------------------------------------------------------ BLOBBY
dict(
 slug='blobby', name='Blobby', tags=['Figma plugin', 'Design + code'], read=3, compact=True,
 cover='assets/img/cs/blobby/shot-7.webp',
 title='Blobby: every blob plugin gave me a dead vector. I wanted one I could keep editing.',
 lede='I use blobs for hero backgrounds and illustration. Every plugin I tried inserted a flat path and forgot it, so one small change meant starting over. Blobby keeps the recipe on the layer.',
 meta=[('Role', 'Solo designer and developer'), ('Product', 'Figma plugin · v0.4'), ('Built with', 'TypeScript, esbuild, Playwright'), ('Status', '59 of 59 tests passing')],
 sections=[
  ('Why I built it', 'The shape was never the hard part. Changing it later was.', [
    ('pipeline', 'current', 'Before', 'Generate, insert, start over', ['Generate a blob', 'Insert a flat vector', 'Client wants it rounder', 'Settings are gone', 'Generate again'], 'for every variation'),
    ('pipeline', 'proposed', 'With Blobby', 'Generate once, edit forever', ['Generate a blob', 'Recipe saved on the layer', 'Select it weeks later', 'Plugin reopens its settings', 'Update in place']),
    ('cards', [('Blobs that stay editable', 'Complexity, gradient, stroke and shadow stay adjustable on the canvas.'),
               ('Sets that belong together', 'A variation keeps the style and changes only the shape.'),
               ('Made for hand-off', 'Copy any blob as SVG, CSS clip-path or a React component.')]),
  ]),
  ('Store screenshots', 'Six frames I designed for the Figma Community listing.', [
    ('carousel', [('shot-7.webp', 'Beautiful blobs. One click away.', 'The opening frame: the mascot, the promise and the real plugin panel.'),
                  ('shot-2.webp', 'More shapes. More ways to create.', 'Seven shape families side by side, so the range is obvious at a glance.'),
                  ('shot-3.webp', 'Make it yours.', 'One blob taken from original to complex, gradient and stroke.'),
                  ('shot-4.webp', 'One shape. Endless possibilities.', 'Variations from a single idea, the feature other plugins lack.'),
                  ('shot-5.webp', 'Not just another blob generator.', 'An honest comparison with four popular blob plugins.'),
                  ('shot-6.webp', 'From blob to design in seconds.', 'A before and after that shows where a blob ends up.')]),
  ]),
  ('The plugin', 'Pick a shape, shuffle, insert.', [
    ('gallery', [('ui-home.webp', 'Home: preview, shuffle, insert or generate a set.'), ('ui-liquid.webp', 'Liquid styles.'), ('ui-geometric.webp', 'Geometric styles.')], 3),
  ]),
  ('Under the hood', 'A shape that never clips its frame.', [
    ('pipeline', 'proposed', 'Shape', 'Seeded points, smooth curve, exact fit', ['Points on a circle', 'Seeded noise', 'Smooth curve', 'Exact bounding box', 'Fills its frame']),
    ('p', 'It runs fully offline: no account and no network.'),
  ]),
 ],
),
]


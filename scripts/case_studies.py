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
 cover='assets/img/cover/gofully.webp', hero_clip='gofully-fullpage.mp4', tint=('#cfe3ff', '#dcd6ff', '#eef3fa'),
 title='GoFully: redesigning a screenshot extension around one promise, nothing leaves your device.',
 lede='GoFully could capture, read, mark up, redact and export a whole page, all offline, but it looked like every other screenshot tool. I redesigned the brand, the extension and the website so that promise is the first thing people see.',
 meta=[('Role', 'Product designer · brand, UX, UI, website'), ('Product', 'Screenshot extension · 5 browsers'), ('Scope', 'Brand guide, design system, 70+ screens, website'), ('Status', 'New website live')],
 stats=[('41 pages', 'Brand guide', 'From positioning to the 16 px icon'), ('70+', 'Extension screens', 'Every state, light and dark'), ('1', 'Primary action', 'Per screen, in navy')],
 links=[('Visit the GoFully website', 'https://gofully-extension.vercel.app'), ('Read the brand guidelines', 'projects/gofully-brand.html')],
 sections=[
  ('Introduction', 'A capable tool with nothing to make it memorable.', [
    ('p', 'GoFully scrolls a page, waits for lazy images, handles sticky headers and stitches one clean image. It reads text, marks up, redacts and exports PNG, JPG, WebP or PDF, with no account and no server.'),
    ('p', 'I led the redesign end to end: positioning, brand, the design system, every extension and editor screen, and the website.'),
    ('chips', ['Positioning', 'Brand identity', '41-page brand guide', 'Design system v2', 'Extension UX and UI', 'Editor', 'Error states', 'Website', 'Store screenshots']),
  ]),
  ('The problem', 'The one thing that set GoFully apart was the quietest thing on the page.', [
    ('quote', '“100% on-device” sat in a small badge above a headline made of features. Privacy, the real difference, was easy to miss.'),
    ('story', 'A QA tester sharing a bug, before GoFully', [
      'They need the whole page in the ticket, but their screenshot tool only grabs what’s on screen.',
      'They take three screenshots and stitch them in an image editor.',
      'A customer’s email is visible, so they open another app to blur it by hand.',
      'The ticket system wants a PDF, so they convert it in a third tool.',
      'They upload it to a sharing service to get a link.',
      'Twenty minutes and three tools later, a second email they missed is still in the corner.']),
    ('problem', 1, 'The promise was buried', 'The store page, website and popup each listed every feature at once.', 'GoFully read like dozens of other screenshot tools, so there was no reason to pick it.'),
    ('problem', 2, 'A generic identity', 'A glossy camera icon sat next to other extensions with camera icons.', 'Nothing about the brand said “private” or “precise”, the two things it actually was.'),
    ('problem', 3, 'Every surface in its own style', 'Popup, editor, store screenshots and website didn’t share type, colour or layout.', 'The product felt stitched together, which undermines trust in a privacy tool.'),
    ('cmp', 'before-site-hero.webp', 'after-site-hero.webp', 'Before · old site', 'After · new site'),
  ]),
  ('What I wanted to achieve', 'Goals for the product, and for the person using it.', [
    ('goals', [('Stand out on the store.', 'Lead with privacy, the one claim competitors can’t make.'),
               ('One system.', 'One set of tokens and components across popup, editor and website.'),
               ('Keep every feature.', 'Change how it feels, not what it can do.')],
              [('The whole page, one click.', 'No stitching, no second tool.'),
               ('Safe to share.', 'Sensitive details covered before anything leaves the device.'),
               ('Calm to use.', 'One primary action per screen, and a way out of every error.')]),
  ]),
  ('Direction', 'Private, precise, fast.', [
    ('fig', 'brand-positioning.webp', 'Positioning and moodboard from the 41-page brand guide.'),
    ('figs', [('r0-mark-a.webp', 'A viewfinder drawn as a G: it still reads as “screenshot”, and it can only be GoFully.'), ('ui-components.webp', 'Soft corners, a 4 px grid and two navy shadows.')]),
  ]),
  ('The solution', 'Four moments, each recorded from the live product demos.', [
    ('solution', 1, 'The whole page, in one image', 'Click once. GoFully scrolls, waits for lazy images and stops sticky headers from repeating.', 'gofully-fullpage.mp4',
     ['Capture modes are listed with their shortcuts in the popup.', 'Progress is shown while it scrolls, so a long page never looks stuck.', 'The result opens ready to copy, save or edit.'],
     'The QA tester’s three screenshots and an image editor become one click.'),
    ('solution', 2, 'Hide what shouldn’t be seen, before you share', 'Auto-redact finds emails, card numbers, phone numbers and API keys, and covers them on the device.', 'gofully-redact.mp4',
     ['Detection runs locally; the page never leaves the computer.', 'It says how many items it found, so nothing is hidden silently.', 'Blur, pixelate or black out, before or after capture.'],
     'The leak in the story, the email in the corner, is caught before the link is shared.'),
    ('solution', 3, 'Copy text out of any image', 'Drag over a chart, a scanned page or a paused video to copy its text.', 'gofully-text.mp4',
     ['Six languages, read on the device with no cloud OCR.', 'Copy as plain text or JSON.'],
     'One less tool to open, and no upload to a third-party service.'),
    ('solution', 4, 'Measure anything on the page', 'Hover to see sizes, padding and colours; click two elements for the gap between them.', 'gofully-measure.mp4',
     ['Built for designers and QA checking a build against a spec.', 'Values copy straight into a ticket.'],
     'It turns GoFully from a screenshot tool into a review tool, without a new app.'),
  ]),
  ('The extension', 'One primary action per screen, and a way out of every error.', [
    ('figs', [('popup-default.webp', 'The popup lists each capture mode with its shortcut.'), ('popup-failed.webp', 'A failed capture says what happened and what to do next.')]),
    ('cmp', 'ed-default.webp', 'ed-dark.webp', 'Editor · light', 'Editor · dark'),
  ]),
  ('The website', 'I replaced the feature list with one sentence.', [
    ('lead', 'Old: “Full Page Screenshot Tool. One Extension. Every Job.” New: **“The screenshot studio that stays on your device.”**'),
    ('fig', 'landing-hero-options.webp', 'Three hero directions, each tested against the same long article.'),
    ('browser', 'site-full.webp', 'gofully-extension.vercel.app', 'The full GoFully website. Scroll inside the frame.'),
  ]),
  ('What I’d do next', 'The new site is live; the store listing still shows the old design.', [
    ('rows', [('Ship the store listing', 'Replace the old screenshots with the new set so the first impression matches the product.'),
              ('Measure install rate', 'Compare store conversion before and after the new listing.'),
              ('Test the redact flow', 'Watch five people share a sensitive page and see whether auto-redact catches what they expect.'),
              ('Keep the system honest', 'Audit new features against the token set so the product doesn’t drift again.')], None),
    ('honest', 'No post-launch metrics yet.', 'This shows the design work, not results.'),
  ]),
 ],
),
# ------------------------------------------------------------------ JOBLY
dict(
 slug='jobly', name='Jobly', tags=['Chrome extension', '0 → 1', 'Solo founder'], read=7,
 cover='assets/img/cover/jobly.webp', hero_clip='jobly-search.mp4', tint=('#ffd9c7', '#ffe9b8', '#f6f1ea'),
 title='Jobly: fresh jobs with their real posting date, and help applying, in the browser toolbar.',
 lede='Job boards are full of listings that closed months ago, and every application asks for the same details again. I founded, designed and built Jobly on my own to fix both.',
 meta=[('Role', 'Solo founder · design, code, launch'), ('Timeline', 'Sep – Nov 2026'), ('Platforms', 'Chrome extension, website, Studio'), ('Status', 'Website and Studio live · v1.4 extension')],
 stats=[('2,000+', 'Employers', 'Read from their own hiring systems'), ('60 days', 'Freshness rule', 'Anything older is dropped'), ('0', 'Accounts or servers', 'Everything stays in the browser')],
 links=[('Visit the Jobly website', 'https://jobly-88t.pages.dev'), ('Open Jobly Studio', 'https://jobly-studio.pages.dev'), ('Source on GitHub', 'https://github.com/MUZEEBURRAHAMAN/Jobly')],
 sections=[
  ('Introduction', 'A job search tool that lives where applying happens.', [
    ('p', 'Jobly is a free Chrome extension, website and resume studio. It reads job posts straight from employers’ own hiring systems, shows only the ones from the last 60 days with their real date, and then helps you apply.'),
    ('p', 'I did every part: research, brand, UX and UI, the data pipeline, the extension, the website, the store listing and a pre-launch audit.'),
    ('chips', ['Research', 'Product strategy', 'Brand', 'UX and UI', 'Design system', 'Extension (React, Manifest V3)', 'Data pipeline (Python)', 'Website (Astro)', 'QA and security audit']),
  ]),
  ('The problem', 'Job hunting wastes time in two places: finding real jobs, and applying to them.', [
    ('quote', '“Is this job even still open?” is the first question a job seeker asks, and most boards can’t answer it.'),
    ('story', 'A job seeker’s evening, before Jobly', [
      'They open three job boards and search “product designer” on each.',
      'Half the results are reposts of the same role, and most don’t say when they were posted.',
      'They find a good one and click through to the company’s page.',
      'The role was filled two months ago. The board never took it down.',
      'On the next one, the form asks for name, links and experience, field by field, again.',
      'Two hours later they’ve sent one application, with the same resume they send everywhere.']),
    ('problem', 1, 'Ghost jobs', 'Boards copy listings from employers and keep them up long after the role is filled, often without the date.', 'People spend most of their search time on jobs that no longer exist, and lose trust in every listing.'),
    ('problem', 2, 'The same form, again', 'Every application asks for the same profile details, one field at a time.', 'Each application costs 15 to 30 minutes of retyping, so people apply to fewer roles.'),
    ('problem', 3, 'One resume for every job', 'Tailoring a resume to a posting takes too long, so most people send the same one.', 'Applications miss the exact words the employer screens for.'),
  ]),
  ('What I wanted to achieve', 'Goals for the product, and for the person using it.', [
    ('goals', [('Trust.', 'Every listing must be real, recent and dated, or the product has no reason to exist.'),
               ('No running cost.', 'No server and no accounts, so a solo founder can keep it free.'),
               ('Store-ready.', 'Pass a full accessibility and security audit before launch.')],
              [('Only fresh jobs.', 'See roles from the last 60 days, with the real posting date.'),
               ('Apply faster.', 'Enter a profile once and reuse it on every form.'),
               ('Stay private.', 'No sign-up, and data that never leaves the browser.')]),
  ]),
  ('Key decisions', 'Two choices shaped everything else.', [
    ('iters', [('bad', 'Option', 'Another job website', 'One more tab to remember, and it can’t help on the employer’s application page.', None),
               ('bad', 'Option', 'A mobile app', 'People browse on phones but apply on laptops, where the forms and resumes are.', None),
               ('good', 'Chosen', 'A Chrome extension', 'One click from any tab, and it can fill an application when asked.', None)]),
    ('pipeline', 'proposed', 'Data', 'Read the source, not the boards', ['2,000+ employer feeds', 'Read every 4 hours', 'Drop anything over 60 days', 'Static files on Cloudflare', 'Filtered in your browser']),
    ('p', 'Freshness had to be solved in the data, not the layout. With no server, there’s nothing to attack and nothing to keep running.'),
  ]),
  ('The solution', 'Five moments in the real extension.', [
    ('solution', 1, 'Set up in three steps', 'The first run asks only what Jobly needs to filter: the roles you want, and whether to send alerts.', 'jobly-onboarding.mp4',
     ['Roles are preselected cards you untick, so nobody starts from an empty form.', 'Step three explains privacy in plain words before anything is stored.', 'A “Skip for now” path goes straight to jobs.'],
     'People see useful results within a minute, and nothing is asked that isn’t used.'),
    ('solution', 2, 'A feed that only shows recent jobs', 'Search and role chips filter thousands of live jobs instantly, because the filtering happens in the browser.', 'jobly-search.mp4',
     ['Every card shows how long ago the job was really posted.', 'A “Matches you” tag explains why a job is in your feed.', 'Role chips show live counts before you tap them.'],
     'The first question, “is this still open?”, is answered on the card itself.'),
    ('solution', 3, 'Save now, track later', 'Saving is one tap from the card, and saved jobs sit in one list with the ones you’ve applied to.', 'jobly-save.mp4',
     ['Save changes state in place, with no dialog.', 'After you open a job, Jobly asks “Did you apply?”', 'Saved and applied live in one place.'],
     'People stop keeping a separate spreadsheet of where they applied.'),
    ('solution', 4, 'Follow companies, not searches', 'Many people know where they want to work. They can follow a company and hear about every new role it posts.', 'jobly-companies.mp4',
     ['A company directory built from the same live feeds.', 'Alerts per company instead of per keyword.'],
     'It matches how people actually job hunt: by employer first.'),
    ('solution', 5, 'Tailor a resume to the job', 'Paste a job description and see which requirements your resume already covers.', 'v14-tailor.webp',
     ['A coverage score, with the line that proves each requirement.', 'Suggested changes are accepted one by one, never applied silently.'],
     'Tailoring becomes a ten-minute review instead of an hour of rewriting.'),
    ('feature', 'Apply assist', 'And on the employer’s form, it fills the fields with you', 'Each answer shows where it came from, questions only you can answer are marked, and you press Submit yourself.', 'v14-apply-assist.webp'),
  ]),
  ('In the toolbar', 'The popup is the fastest way in.', [
    ('clip', 'jobly-popup2.mp4', 'The toolbar popup: fresh matches without opening a new tab.'),
  ]),
  ('Quality', 'I audited Jobly before launch, and it failed.', [
    ('stats', [('46', 'Findings', '6 of them blockers'), ('1 day', 'To fix', 'Re-checked in a real browser'), ('0', 'axe issues', 'In light and dark themes')]),
    ('p', 'A Playwright, axe-core and dependency audit said “not ready”. The fix went past patches: I moved all user data onto the device and removed the server.'),
  ]),
  ('What I’d do next', 'Jobly isn’t on the Chrome Web Store yet. After launch I’d focus on four things.', [
    ('rows', [('Measure the core loop', 'Track how many saved jobs turn into applications, which tells me if the feed is trusted.'),
              ('Talk to job seekers', 'Run short interviews with early users about where apply assist still gets in the way.'),
              ('Watch the data', 'Monitor feeds that break or go quiet, since freshness is the whole promise.'),
              ('Keep improving', 'Use what I learn to decide between more employers and deeper apply help.')], None),
    ('honest', 'No usage numbers yet.', 'The website and Studio are live. Version 1.4 of the extension is packaged for the store.'),
  ]),
 ],
),
# ------------------------------------------------------------------ ASSISTANTLY
dict(
 slug='assistantly', name='Assistantly', tags=['AI tooling', 'Design QA'], read=7, tint=('#ffd8d2', '#e4e0ff', '#f5f3f1'),
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
    ('clip', 'assistantly-report.mp4', 'The real report: each finding with its rule, element and a fix to copy.'),
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
 slug='petsy', name='Petsy', tags=['E-commerce', '3D + motion', 'Design + code'], read=8,
 cover='assets/img/cover/petsy.webp', tint=('#f3d3bd', '#e9dcc4', '#f6f0e8'),
 video=('petsy.mp4', 'video-poster.webp', 'A 99-second walkthrough, from the Figma wireframe to the live store.'),
 title='Petsy: a pet clothing store where a 3D dog or cat tries the coat on before you buy.',
 lede='Pet clothes get bought on a guess. You can’t hold a jumper up to a cat, and size charts ask for a chest measurement nobody has taken. I designed and built a full store around removing that guess.',
 meta=[('Role', 'Solo designer and developer'), ('Product', 'Online store · 18 pages'), ('Built with', 'Figma, React, GSAP, three.js, Base44'), ('Status', 'Live on Base44 · #Base44Challenge')],
 stats=[('18', 'Pages', 'One design system across all of them'), ('3D', 'Fitting room', 'A rigged dog and cat wear the coat'), ('1', 'Motion scale', 'Shared by every hover and reveal')],
 tldr=[('The problem', 'Shoppers size pet clothes from a chart and a photo of a breed their pet isn’t, so the order is a gamble.'),
       ('The solution', 'Show the garment on a 3D dog or cat, recommend a size with a reason, and make the rest of the store calm enough to trust.'),
       ('My role', 'Everything: reference audit, wireframes, design system, motion, 3D, front-end code, and the Base44 build with its back end.')],
 links=[('Open the live store', 'https://petsy-style-edit.base44.app')],
 sections=[
  ('Why I built it', 'Buying clothes for a pet fails at one moment: “will it fit?”', [
    ('pipeline', 'current', 'Today', 'Size chart → guess → return', ['Photo of another breed', 'Guess from a size chart', 'Order', 'It doesn’t fit', 'Send it back'], 'try another size'),
    ('pipeline', 'proposed', 'With Petsy', 'Try it on → right size → keep it', ['Pick dog or cat', 'See it on a 3D model', 'Size finder gives a reason', 'Order once', 'Keep it']),
    ('quote', '“Will it fit?” is the question every pet owner asks, and no product photo can answer it.'),
    ('story', 'Buying a jumper for a beagle, before Petsy', [
      'An owner finds a nice knit, photographed on a French bulldog.',
      'The size chart asks for chest girth. They’ve never measured their dog.',
      'They guess “M” from the dog’s weight and order it.',
      'It arrives tight across the chest and long in the back.',
      'They print a return label and drive to the post office.',
      'The dog still has no jumper, and they don’t trust the shop again.']),
    ('problem', 1, 'Fit is invisible', 'Photos show a model breed, not your pet, and a size chart can’t show shape.', 'Shoppers hesitate at the buy button or order two sizes and send one back.'),
    ('problem', 2, 'Sizing asks for data nobody has', 'Charts ask for chest girth and back length in centimetres.', 'People guess from weight, which is the least reliable signal for clothing.'),
    ('problem', 3, 'Pet stores feel like discount bins', 'Most pet shops are dense grids of offers with no sense of care or quality.', 'A premium jumper looks no different from a cheap one, so price wins.'),
  ]),
  ('What I wanted to achieve', 'Goals for the store, and for the owner shopping it.', [
    ('goals', [('Fewer returns.', 'Every avoided return is margin a small brand keeps.'),
               ('Look premium.', 'Make the product feel worth its price before anyone reads it.'),
               ('Prove it in one build.', 'A full, working store, not a mock-up.')],
              [('See the fit.', 'On a dog or a cat, in the colour they want.'),
               ('Pick a size with a reason.', 'Using things they actually know about their pet.'),
               ('Browse calmly.', 'A store that’s pleasant to wander, on a phone too.')]),
  ]),
  ('Design principles', 'Three rules I held every screen to.', [
    ('rows', [('Show it on the pet', 'Every page leads toward the fitting room. The 3D model answers what a photo can’t.'),
              ('One decision per screen', 'Dog or cat, then a category, then a product. No screen asks two things at once.'),
              ('Motion has a job', 'Animation shows where something came from or went. If it only decorates, it goes.')], None),
  ]),
  ('Process', 'From a reference audit to a live store.', [
    ('pipeline', 'proposed', 'How I worked', 'Audit → wireframe → system → code → live', ['Audit a real boutique store', 'Wireframe two key pages', 'Set type, colour and motion', 'Build in React', 'Rebuild live in Base44']),
    ('gallery', [('wireframe-1.webp', 'Wireframes in Figma: the home page and the product page.'), ('wireframe-2.webp', 'Section order came from the audit. The content is all Petsy.')], 2),
    ('fig', 'base44-builder.webp', 'The Base44 build: one prompt per finished section, each tested before the next.'),
  ]),
  ('Visual system', 'Premium, but friendly enough for a store about dogs in jumpers.', [
    ('table', ['Role', 'Choice', 'Why'],
     [['Headlines', 'Fraunces, soft serif', 'Feels like a boutique without feeling stiff'],
      ['Body and UI', 'DM Sans', 'Rounder and warmer than a default system font'],
      ['Prices and labels', 'DM Mono, uppercase', 'Sets facts apart from marketing copy'],
      ['Colour', 'Oat and terracotta', 'Warm neutrals let the product photos carry the colour'],
      ['Buttons', 'Full pills, 48 px tall', 'Easy to hit on a phone with a lead in the other hand']]),
  ]),
  ('Home page', 'Six sections, each answering one question.', [
    ('carousel', [('hero.webp', 'Hero: who is this for?', 'A full-screen film and two paths, Shop dogs or Shop cats. The first choice is the only choice.'),
                  ('categories.webp', 'Shop by kind: what do you sell?', 'Seven arched tiles show the range in one row, before any product grid.'),
                  ('new-in.webp', 'New In: what’s fresh?', 'Cards rise in as you scroll, and Dogs and Cats filters reorder the grid in place.'),
                  ('lookbook.webp', 'Lookbook: how does it look worn?', 'Click a photo and it opens into the full outfit, with every product in it.'),
                  ('brand-spotlight.webp', 'Brands: who makes it?', 'Each brand gets a banner and a rail you can drag.'),
                  ('tryon-teaser.webp', 'Try-on: will it suit my pet?', 'A live 3D preview on the home page, so the key feature isn’t hidden on a product page.')]),
  ]),
  ('The solution', 'Four moments in the live store.', [
    ('solution', 1, 'A 3D model wears the coat', 'Switch between a dog and a cat, make it walk, and change the colour without a reload.', 'petsy-tryon.mp4',
     ['The same knit is rigged to both skeletons, so it refits when the pet changes.', 'Walking shows how the fabric moves, which a still photo can’t.', 'Colour swatches update the model in place.'],
     'The owner sees fit and colour on their kind of pet before paying.'),
    ('solution', 2, 'A size, and the reason for it', 'The size finder asks for breed and, optionally, chest and weight, then picks a size and explains why.', 'petsy-size.mp4',
     ['Breed comes first because everyone knows it.', 'Measurements are optional, with a how-to right in the form.', 'The answer selects the size in one tap.'],
     'Sizing stops being a guess from weight.'),
    ('solution', 3, 'Browse in place', 'New In filters by dogs or cats without leaving the grid, and cards rise in as you scroll.', 'new-in.webp',
     ['Filters reorder the grid with motion, so you see what changed.', 'Every card carries price, brand and colourways.'],
     'The store feels considered from the first scroll, not like a list of offers.'),
    ('solution', 4, 'A lookbook that opens into the outfit', 'Click a photo and it grows into the full look, with every product in it.', 'petsy-lookbook.mp4',
     ['The photo morphs from its grid position, so you never lose your place.', 'Each look links straight to its products.'],
     'People shop the outfit they like instead of hunting for each piece.'),
    ('feature', 'Proof', 'Reviews that name the breed and the size', 'A shopper with a corgi can find another corgi owner’s verdict.', 'product-reviews.webp'),
  ]),
  ('Every page', 'The rest of the store, on the same system.', [
    ('gallery', [('page-dogs.webp', 'Dogs: the catalogue for one kind of pet.'), ('page-cats.webp', 'Cats: the same layout, its own range.'), ('page-lookbook.webp', 'Lookbook: outfits worn outdoors.'),
                 ('page-size-guide.webp', 'Size guide: how to measure, by breed.'), ('page-bag.webp', 'Bag: one summary, one button.'), ('page-track.webp', 'Track order: status from an order number.'),
                 ('page-gift.webp', 'Gift cards: the gift that always fits.'), ('page-testimonials.webp', 'Testimonials: owners and their pets.'), ('page-faq.webp', 'FAQ: straight answers.'),
                 ('page-returns.webp', 'Returns: what to do if it doesn’t fit.'), ('page-contact.webp', 'Contact: a short form.')], 3),
  ]),
  ('On a phone', 'Most pet shopping happens one-handed.', [
    ('gallery', [('m-home.webp', 'Home.'), ('m-dogs.webp', 'Dogs.'), ('m-product.webp', 'Product, with the 3D model first.')], 3),
  ]),
  ('Motion', 'Five effects, each with a reason.', [
    ('table', ['Where', 'What moves', 'Why'],
     [['Headlines', 'Lines rise in one by one', 'Sets the reading order'],
      ['Product grids', 'Cards rise as you scroll', 'Shows that more is loading below'],
      ['Lookbook', 'A photo morphs into the outfit', 'You never lose track of what you clicked'],
      ['Brand rails', 'Drag with inertia', 'Feels like flicking through a rack'],
      ['3D colour', 'Fabric fades to the new colour', 'Confirms the swatch you picked']]),
    ('p', 'Only position and opacity are animated, and reduced-motion settings turn every effect into a simple fade.'),
  ]),
  ('Behind the store', 'A real back end, added in Base44.', [
    ('fig', 'assistant.webp', 'Ask Petsy: an assistant that picks products, fills the bag and tracks orders.'),
    ('cards', [('Checkout', 'Server functions end in a paid, pending or failed receipt with a transaction ID.'),
               ('Orders and gift cards', 'Tracking is verified on the server, and gift codes are created there too.'),
               ('Accounts and admin', 'Sign-in with password reset, plus an owner-only view for products and stock.')]),
  ]),
  ('The full pages', 'Scroll through the two key pages.', [
    ('browser', 'home-full.webp', 'Petsy · home', 'The full home page.'),
    ('browser', 'product-full.webp', 'Petsy · product', 'The full product page.'),
  ]),
  ('What I’d do next', 'If Petsy became a real shop.', [
    ('rows', [('Measure returns by size', 'Compare return rates for orders that used the size finder against those that didn’t.'),
              ('Test the fitting room', 'Watch owners use it and check whether the 3D fit matches what arrives.'),
              ('More breeds', 'Add body shapes beyond one dog and one cat, starting with the most common breeds.')], None),
  ]),
  ('Looking back', 'What Petsy taught me.', [
    ('rows', [('Solve the real doubt', 'Shoppers didn’t need more photos. They needed to see it on their kind of pet.'),
              ('Borrow structure, not style', 'A proven section order saved time. Type, colour and motion made it Petsy.'),
              ('Wireframe before prompting', 'The Base44 build worked because every prompt described a section I had already designed.')], None),
    ('honest', 'A challenge project.', 'Petsy is live, but it isn’t a trading shop and has no sales data. The photos come from Unsplash.'),
  ]),
 ],
),
# ------------------------------------------------------------------ GHOST TEARS
dict(
 slug='ghost-tears', name='Ghost Tears', tags=['Game UI', 'Design system'], read=5,
 cover='assets/img/cover/ghost-tears.webp',
 title='Ghost Tears: a word game for friends, redesigned in three themes on one system.',
 lede='Ghost Tears is a turn-based word game for 3 to 6 friends: add a letter, but don’t finish the word. The client asked for a friendlier look, so I redesigned every screen, the mascot and the system underneath.',
 meta=[('Role', 'Product designer · UX, UI, brand'), ('Product', 'Multiplayer word game · web'), ('Scope', '18 screens, desktop and mobile'), ('Status', 'Redesign v3 · client project')],
 stats=[('18', 'Screens', 'Each on desktop and mobile'), ('3', 'Themes', 'Minimal, Blue and Dark'), ('32', 'Colour tokens', 'Per theme, same names')],
 tldr=[('The problem', 'A party game has to be learned in seconds and read at a glance, and the earlier design felt colder than the game is.'),
       ('The solution', 'A friendlier ghost, rounder type, and a game screen where whose turn it is and what to do are never in doubt.'),
       ('My role', 'UX flows, UI for every state, the mascot and logo, and the token system that drives all three themes.')],
 sections=[
  ('The game', 'Five rules, so the UI has to teach fast.', [
    ('pipeline', 'proposed', 'A round', 'Add a letter → dodge the word → last one standing', ['Add one letter', 'Don’t complete a word', 'Finish one, take a strike', 'Challenge a bluff', 'Last player wins']),
  ]),
  ('The brief', 'Client feedback: make it friendlier.', [
    ('cards', [('A ghost with feelings', 'A line-art mascot with five expressions, used for wins, losses and waiting.'),
               ('Three themes', 'Minimal black and white, Blue, and Dark, switched without redrawing a screen.'),
               ('Softer type', 'Fredoka for the logo, tiles and buttons; Nunito for reading.')]),
    ('fig', 'brand.webp', 'The mascot’s five expressions and the new logo.'),
  ]),
  ('The flow', 'From the first screen to the winner.', [
    ('carousel', [('d-splash.webp', 'Splash', 'One line explains the game, and two buttons start or join one. No sign-up.'),
                  ('d-how-1.webp', 'How to play', 'Three short cards teach the rules with real tiles instead of paragraphs.'),
                  ('d-create.webp', 'Create a game', 'Sensible defaults are preselected, so a host can start in one tap.'),
                  ('d-created.webp', 'Game ready', 'The invite link is the only thing on screen, with one copy button.'),
                  ('d-lobby.webp', 'Lobby', 'Empty seats show how many friends are still needed.'),
                  ('d-turn.webp', 'Your turn', 'The word, the timer and the keyboard sit in one column. Players and history stay at the sides.'),
                  ('d-word.webp', 'Word completed', 'The finishing letter is marked, so the strike feels fair.'),
                  ('d-challenge.webp', 'Challenge', 'A countdown and plain copy say who challenged whom and what happens next.'),
                  ('d-result.webp', 'Challenge result', 'The real word is shown, and the strike lands on the right player.'),
                  ('d-out.webp', 'You’re out', 'Eliminated players keep watching instead of hitting a dead end.'),
                  ('d-over.webp', 'Match over', 'Final standings, then Play again as the main action.')]),
  ]),
  ('Three themes', 'Same layout, same components, different tokens.', [
    ('carousel', [('blue-splash.webp', 'Blue · splash', 'The same screen with the Blue token set.'),
                  ('blue-turn.webp', 'Blue · your turn', 'Only colour changes; spacing and type stay put.'),
                  ('dark-splash.webp', 'Dark · splash', 'Dark keeps the tiles as the brightest thing on screen.'),
                  ('dark-turn.webp', 'Dark · your turn', 'The active letter is still the highest-contrast element.')]),
  ]),
  ('On a phone', 'Most rounds are played on one.', [
    ('gallery', [('m-splash.webp', 'Splash.'), ('m-lobby.webp', 'Lobby.'), ('m-turn.webp', 'Your turn, keyboard in thumb reach.'),
                 ('m-word.webp', 'Word completed, as a bottom sheet.'), ('blue-m-turn.webp', 'Blue.'), ('dark-m-turn.webp', 'Dark.')], 3),
  ]),
  ('Design system', 'What makes three themes cheap to maintain.', [
    ('gallery', [('ds-type.webp', 'Type: Fredoka plays, Nunito reads.'), ('ds-colour.webp', 'Colour: one set of token names, three themes.'),
                 ('ds-spacing.webp', 'Spacing, radius and elevation.'), ('ds-components.webp', 'Components in every state.')], 2),
  ]),
  ('Looking back', 'What Ghost Tears taught me.', [
    ('rows', [('Design the turn first', 'Everything else in a turn-based game hangs off one screen. I settled that before the rest.'),
              ('Name tokens by job', 'Because tokens are named for their role, a new theme is a new set of values, not new screens.'),
              ('A mascot carries tone', 'Five small expressions did more for “friendlier” than any colour change.')], None),
    ('honest', 'Design only.', 'This shows the redesign. I don’t have launch or usage numbers to share.'),
  ]),
 ],
),
# ------------------------------------------------------------------ EVE
dict(
 slug='eve', name='EVE', tags=['Mental wellness', 'Redesign', 'Web + mobile'], read=5,
 cover='assets/img/cover/eve.webp',
 title='EVE: redesigning a mental wellness platform for employees and the companies that support them.',
 lede='EVE gives people a private AI companion to talk to, and gives their employer an anonymous picture of how teams are doing. I audited the old product and redesigned both sides of it.',
 meta=[('Role', 'Product designer · research to UI'), ('Product', 'Web app · mobile · landing page'), ('Scope', 'User panel, company panel, design system'), ('Deliverables', '100+ screens')],
 stats=[('100+', 'Screens', 'Across web and mobile'), ('2', 'Panels', 'One for people, one for the company'), ('1', 'Design system', 'Tokens, components, email templates')],
 tldr=[('The problem', 'The old product had the features but no clear path through them, and talking about mental health needs a calm screen.'),
       ('The solution', 'An audit first, then new flows, a quiet lavender system, and a chat screen with one obvious starting point.'),
       ('My role', 'Audit, competitor and persona work, user flows, wireframes, design system, and final UI for both panels.')],
 sections=[
  ('Start with the old product', 'I marked what was wrong before drawing anything new.', [
    ('carousel', [('f-03.webp', 'Old design review', 'Every screen annotated with what to fix, so the redesign had a list to answer.'),
                  ('f-02.webp', 'Rough work', 'The full old product laid out side by side to see the gaps between screens.'),
                  ('f-04-2.webp', 'Persona and competitors', 'Who the product is for, and what similar tools do well or badly.'),
                  ('f-04-1.webp', 'User flows', 'Each journey mapped end to end before any layout.'),
                  ('f-04.webp', 'Wireframes for each problem area', 'Chat, voice, profile, calendar and onboarding reworked in grey first.')]),
  ]),
  ('The system', 'Calm by construction.', [
    ('figs', [('f-05.webp', 'Variables for colour, type, spacing and radius.'), ('f-06.webp', 'Components built from them.')]),
  ]),
  ('For people', 'A private place to talk.', [
    ('carousel', [('f-11.webp', 'Chat with EVE', 'One greeting, one input and a row of starter prompts. Nothing else competes.'),
                  ('f-10.webp', 'Mind map', 'Work, family, friends and relationships shown as a map instead of a form.'),
                  ('f-12.webp', 'Mobile · talk and transcribe', 'Voice first on a phone, with the transcript one tab away.'),
                  ('f-13.webp', 'Mobile · onboarding, map and calendar', 'The same features, rearranged for one hand.'),
                  ('f-09.webp', 'Sign in', 'The same screen on web and phone.'),
                  ('f-16.webp', 'Settings', 'Login activity is visible, because trust matters more here than in most apps.')]),
  ]),
  ('For the company', 'Signals, not surveillance.', [
    ('feature', 'Dashboard', 'How teams are doing, in aggregate', 'Survey completion, engagement by department and a table to drill into.', 'f-14.webp'),
    ('feature', 'Ask AI', 'Questions in plain language', 'A manager asks about survey trends and gets a chart with the answer.', 'f-15.webp'),
  ]),
  ('Around the product', 'The landing page and emails share the system.', [
    ('figs', [('f-07.webp', 'Landing page.'), ('f-08.webp', 'Email templates.')]),
    ('fig', 'f-18.webp', 'All 100+ screens on one canvas.'),
  ]),
  ('Looking back', 'What EVE taught me.', [
    ('rows', [('Audit before redesign', 'A marked-up old product is a better brief than a blank page.'),
              ('Two audiences, one system', 'People and employers need different screens, but the same components kept both sides consistent.'),
              ('Quiet is a feature', 'In a wellness product, every extra element on the chat screen is a reason not to type.')], None),
    ('honest', 'Design work.', 'This shows the redesign. I don’t have usage numbers to share.'),
  ]),
 ],
),
# ------------------------------------------------------------------ PHARMFLOW
dict(
 slug='pharmflow', name='PharmFlow', tags=['Health app', 'Brand + product'], read=4,
 cover='assets/img/cover/pharmflow.webp',
 title='PharmFlow: one pharmacy brand across a phone app, a watch app and a website.',
 lede='PharmFlow lets people order medicine, compare prices and remember their doses. I designed the brand and every surface it lives on.',
 meta=[('Role', 'Product and brand designer'), ('Product', 'iOS app · watch app · website'), ('Scope', 'Brand, wireframes, design system, UI'), ('Deliverables', '200+ app screens')],
 stats=[('200+', 'App screens', 'From onboarding to checkout'), ('3', 'Surfaces', 'Phone, watch and web'), ('1', 'Brand', 'Logo, colour and guidelines')],
 tldr=[('The problem', 'Managing medicine means three jobs: buying it, choosing the right one and taking it on time. Most apps do one.'),
       ('The solution', 'One app for ordering, comparing and reminders, with the reminder also on the wrist.'),
       ('My role', 'Branding, wireframes, design guidelines, app and watch UI, website and store screenshots.')],
 sections=[
  ('Overview', 'Everything in the project, on one board.', [
    ('fig', 'f-1.webp', 'App screens, watch design and website.'),
  ]),
  ('Brand', 'A plus sign that reads as health and as flow.', [
    ('carousel', [('f-3.webp', 'Logo and app icon', 'The mark works in one colour, reversed, and at icon size.'),
                  ('f-4.webp', 'Applications', 'Watch face, pattern, business card and signage.'),
                  ('f-5.webp', 'Brand in use', 'Community and delivery banners in the same blue.'),
                  ('f-9.webp', 'Splash screens', 'Three splash options tested with the mark.')]),
  ]),
  ('From wireframe to system', 'Structure first, then rules.', [
    ('figs', [('f-2.webp', 'Wireframes for the app and website.'), ('f-7.webp', 'Design guidelines: colour, type, buttons, forms and cards.')]),
  ]),
  ('The app', 'Four moments that matter.', [
    ('carousel', [('f-10.webp', 'Onboarding · goals', 'The app asks what you want it for, then shapes the home screen around the answer.'),
                  ('f-11.webp', 'Onboarding · health', 'Allergies and conditions are captured once, so warnings can be automatic.'),
                  ('f-12.webp', 'Categories and products', 'Medicines grouped the way a pharmacy shelf is, with price and rating on every card.'),
                  ('f-13.webp', 'Dose reminders', 'Set a schedule in one form; the reminder itself is a single full-screen prompt.'),
                  ('f-6.webp', 'Store screenshots', 'The listing leads with the three jobs: manage, compare, schedule.')]),
  ]),
  ('Watch and web', 'The same product at two other sizes.', [
    ('figs', [('f-8.webp', 'The watch app flow.'), ('f-14.webp', 'The website on desktop and mobile.')]),
  ]),
  ('Looking back', 'What PharmFlow taught me.', [
    ('rows', [('Brand first pays off', 'With the mark and colour fixed early, 200 screens stayed consistent without policing.'),
              ('Put the reminder where the person is', 'A dose reminder belongs on the wrist more than in an app.')], None),
    ('honest', 'Design work.', 'This shows the design. I don’t have launch numbers to share.'),
  ]),
 ],
),
# ------------------------------------------------------------------ ESIGN
dict(
 slug='esign', name='OmnisProof E-Sign', tags=['Legal tech', 'B2B SaaS'], read=3, compact=True,
 cover='assets/img/cover/esign.webp',
 title='OmnisProof: an e-signature product where sending and signing each take one screen.',
 lede='OmnisProof lets law firms send documents for signature and track them. I designed the document lists, the signing flow, the modals and the edge-case screens.',
 meta=[('Role', 'Product designer'), ('Product', 'Web app · responsive'), ('Company', 'Omnis AI'), ('Scope', 'Lists, signing, modals, AI assistant')],
 sections=[
  ('The job', 'A signature is a small task that tools make long.', [
    ('pipeline', 'proposed', 'With OmnisProof', 'Upload → send → sign → track', ['Upload a document', 'Add recipients', 'They sign on any device', 'Status updates itself', 'History kept']),
  ]),
  ('The screens', 'Lists you can scan, and one decision per modal.', [
    ('carousel', [('f-e4.webp', 'Document list', 'Name, sender, recipients and date in one row, with filters for completed, pending and draft.'),
                  ('f-e6.webp', 'Envelope list', 'Status is a coloured label, so a paralegal can find what is stuck at a glance.'),
                  ('f-e5.webp', 'Signing on a phone', 'Draw, type or upload a signature, with the document still visible behind.'),
                  ('f-e9.webp', 'Sign anywhere', 'The signature pad is the whole modal. Nothing else to read.'),
                  ('f-e7.webp', 'Upload, history and review', 'Three supporting flows: adding a file, seeing what happened, and reviewing before sending.'),
                  ('f-e3.webp', 'Upload and delete', 'Destructive actions say exactly what will be lost.'),
                  ('f-e11.webp', 'New template', 'Start from an upload or let AI draft one.'),
                  ('f-e10.webp', 'AI assistant', 'A chat panel that asks follow-up questions before drafting a contract.'),
                  ('f-e8.webp', 'API tokens', 'Three numbered steps for developers.'),
                  ('f-e2.webp', 'Not found', 'Even the 404 gives one way back.')]),
  ]),
  ('Design choices', 'Why it looks plain on purpose.', [
    ('cards', [('Dense, not crowded', 'Legal staff work in lists all day, so rows are compact and columns are predictable.'),
               ('One primary action', 'Each modal has a single blue button. Cancel is always quieter.'),
               ('Edge cases designed', 'Empty, error, 404 and maintenance screens were part of the scope, not an afterthought.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ OODLE
dict(
 slug='oodle', name='Oodle', tags=['Mobile app', 'Social'], read=3, compact=True,
 cover='assets/img/cover/oodle.webp',
 title='Oodle: a friend-finding app with onboarding short enough to finish.',
 lede='Oodle helps people find friends who share their interests. I designed the app in light and dark, from the first screen to chat and premium, plus its store screenshots.',
 meta=[('Role', 'Product designer · UI'), ('Product', 'Mobile app'), ('Scope', 'Onboarding, profile, chat, premium'), ('Themes', 'Light and dark')],
 sections=[
  ('The idea', 'People quit social apps during sign-up.', [
    ('pipeline', 'proposed', 'Onboarding', 'Phone number → three questions → photos → in', ['Sign in with a phone number', 'Answer one question per screen', 'Pick interests', 'Add photos', 'Start meeting people']),
  ]),
  ('The screens', 'One question per screen, one yellow button.', [
    ('carousel', [('f-02.webp', 'The whole app', 'Store screenshots on top, the full onboarding flow below.'),
                  ('f-01.webp', 'Splash', 'Light and dark from the first frame.'),
                  ('f-03.webp', 'Sign in', 'Apple, Google or a phone number, then a one-time code.'),
                  ('f-04.webp', 'Three questions', 'Each on its own screen with a progress bar, so it never feels like a form.'),
                  ('f-05.webp', 'Interests and photos', 'Interests are tappable chips; photos fill a simple grid.'),
                  ('f-06.webp', 'Asking permission', 'Contacts and notifications are requested with a reason and an easy “No, thanks”.'),
                  ('f-10.webp', 'Chat and account', 'Conversations, a single thread and settings.'),
                  ('f-09.webp', 'Premium', 'A plain free-versus-premium table in both themes.'),
                  ('f-07.webp', 'Dark theme · sign in', 'The same flow, with yellow still the only accent.'),
                  ('f-08.webp', 'Dark theme · photos', 'Photo upload in dark.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ BUNDLED
dict(
 slug='bundled', name='Bundled AI', tags=['Mobile app', 'AI image tool'], read=2, compact=True,
 cover='assets/img/cover/bundled.webp',
 title='Bundled AI: turning a text prompt into an image in three taps.',
 lede='Bundled is an AI image app. I designed its brand basics and more than 30 screens, keeping the path from prompt to finished image as short as possible.',
 meta=[('Role', 'Product designer · UI'), ('Product', 'Mobile app'), ('Scope', 'Design system and 30+ screens'), ('Theme', 'Dark, with a light splash')],
 sections=[
  ('The flow', 'Prompt, style, create.', [
    ('pipeline', 'proposed', 'Creating an image', 'Prompt → size and style → image', ['Type a prompt', 'Pick a size', 'Pick a style', 'Watch it generate', 'Save or regenerate']),
  ]),
  ('The screens', 'Dark, so the artwork is the brightest thing on screen.', [
    ('carousel', [('f-1.webp', 'Overview', 'The icon and the complete app.'),
                  ('f-5.webp', 'Prompt to image', 'Size and style open as sheets, so the prompt never leaves the screen.'),
                  ('f-7.webp', 'Generating and result', 'A progress ring, then the image full-bleed with regenerate, share and download.'),
                  ('f-4.webp', 'Onboarding', 'Three screens that show results instead of describing them.'),
                  ('f-8.webp', 'Advanced settings and history', 'Model, negative prompt and aspect ratio for people who want control.'),
                  ('f-6.webp', 'Premium', 'A feature table and three plans.'),
                  ('f-3.webp', 'Splash', 'Dark and light.'),
                  ('f-2.webp', 'Design system', 'Type, colour, shadows and the icon.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ ROSIFY
dict(
 slug='rosify', name='Rosify', tags=['Mobile app', 'AI chat'], read=2, compact=True,
 cover='assets/img/cover/rosify.webp',
 title='Rosify: onboarding for an AI companion app, one choice at a time.',
 lede='Rosify is an AI chat app where people create a virtual companion. I designed the logo, the onboarding and the premium screens.',
 meta=[('Role', 'Product designer · UI and logo'), ('Product', 'Mobile app'), ('Scope', 'Logo, onboarding, payment'), ('Steps', '7-step onboarding')],
 sections=[
  ('The screens', 'Seven short steps, each answered with a tap.', [
    ('carousel', [('f-01.webp', 'Overview', 'Logo options and the full onboarding flow.'),
                  ('f-02.webp', 'Splash and sign in', 'Continue as a guest first; an account can wait.'),
                  ('f-03.webp', 'Name, birth year, gender', 'One field per screen with a visible step count.'),
                  ('f-04.webp', 'What are you looking for?', 'Picture cards instead of a list, so choosing feels like browsing.'),
                  ('f-05.webp', 'Interests and premium', 'Interest chips, then a clear free-versus-pro comparison.')]),
  ]),
  ('Design choices', 'Why it works.', [
    ('cards', [('Guest first', 'People can try the app before giving an email.'),
               ('Pictures over labels', 'Preference questions use image cards, which are faster to answer than text.'),
               ('Progress always visible', 'A step counter on every screen shows how little is left.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ LANDING CONCEPTS
dict(
 slug='landing-concept', name='Landing Page Redesigns', tags=['Landing pages', 'Unsolicited concepts'], read=3, compact=True,
 cover='assets/img/cover/landing-concept.webp',
 title='Nine landing pages, redesigned: what I’d change above the fold and why.',
 lede='A practice series. I took nine real landing pages and redesigned the first screen of each, with the original beside it. These are my own concepts, not client work.',
 meta=[('Role', 'Designer · self-initiated'), ('Format', 'Before and after'), ('Count', '9 pages'), ('Focus', 'Hero, headline, call to action')],
 sections=[
  ('The method', 'Three questions for every hero.', [
    ('cards', [('Can I tell what it is?', 'The headline should name the product or the outcome within five words.'),
               ('Can I see it?', 'A real product shot beats an abstract illustration.'),
               ('Do I know what to do?', 'One primary button, with proof next to it.')]),
  ]),
  ('Before and after', 'The original is top left in each frame.', [
    ('carousel', [('f-01.webp', 'WeForest', 'A clearer promise in the headline and a photo strip that shows the work.'),
                  ('f-02.webp', 'Mail Tester', 'The headline names the benefit, and the product appears in the hero.'),
                  ('f-03.webp', 'Rivet', 'A two-line headline replaces a vague one, with the tool visible below.'),
                  ('f-04.webp', 'Clicks', 'Larger type, one button and a product preview.'),
                  ('f-05.webp', 'Relaw.ai', 'An outcome headline with a customer quote beside it.'),
                  ('f-06.webp', 'Health tech', 'The audience is named in the headline, with the app shown underneath.'),
                  ('f-07.webp', 'Flashmock', 'A warmer palette and faces next to the promise.'),
                  ('f-08.webp', 'Affil.ai sign in', 'A split layout: the form on one side, proof on the other.'),
                  ('f-09.webp', 'Shopify App Store', 'One headline over a wall of app icons instead of a dense grid.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ GOFULLY BRAND
dict(
 slug='gofully-brand', name='GoFully Brand Guidelines', tags=['Brand identity', 'Guidelines'], read=3, compact=True,
 cover='assets/img/cover/gofully-brand.webp',
 title='GoFully brand guidelines: 42 pages from positioning to the app icon.',
 lede='The brand guide behind the GoFully redesign. It sets the promise, the logo and its rules, type, colour with contrast checks, and how the product UI should look.',
 meta=[('Role', 'Brand and product designer'), ('Format', '42-page guide'), ('Covers', 'Brand, logo, type, colour, product UI, assets'), ('Version', '1.1.3')],
 links=[('Read the GoFully product case study', 'projects/gofully.html')],
 sections=[
  ('The guide', 'Six chapters, in the order a team needs them.', [
    ('carousel', [('f-01.webp', 'Cover', 'Navy, the viewfinder ring, and nothing else.'),
                  ('f-05.webp', 'Positioning', 'One line: capture the whole page, keep every pixel private.'),
                  ('f-06.webp', 'Brand values', 'Private, precise, fast and friendly.'),
                  ('f-08.webp', 'Tone of voice', 'Clear, calm, private by default, with do and don’t examples.'),
                  ('f-12.webp', 'Logo anatomy', 'Viewfinder frame, lens ring, shutter dot and tail.'),
                  ('f-14.webp', 'Logo scaling', 'How the lockup behaves from large to small.'),
                  ('f-17.webp', 'Logo misuse', 'Six things not to do.'),
                  ('f-19.webp', 'Typography', 'Archivo for headlines, Inter Display for reading.'),
                  ('f-24.webp', 'Primary colour', 'Sky Blue, Soft White and Deep Navy.'),
                  ('f-27.webp', 'Colour roles and contrast', 'Every text and background pair with its contrast ratio, pass or fail.'),
                  ('f-35.webp', 'Components', 'Buttons and inputs in each state.'),
                  ('f-36.webp', 'Product screens', 'The popup in light and dark.'),
                  ('f-39.webp', 'Visual assets', 'Store and marketing graphics in the system.'),
                  ('f-41.webp', 'App icon', 'The symbol at home-screen size.')]),
  ]),
  ('Why it matters', 'A guide is only useful if it removes decisions.', [
    ('cards', [('Rules with reasons', 'Each rule says why, so people follow it when I’m not in the room.'),
               ('Contrast is checked', 'Colour pairs are listed with ratios, so accessible choices are the default.'),
               ('Product included', 'The guide covers UI, not just the logo, because the extension is the brand.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ DASHBOARDS
dict(
 slug='dashboards', name='Dashboard Designs', tags=['Dashboards', 'Data UI'], read=2, compact=True,
 cover='assets/img/cover/dashboards.webp',
 title='Three dashboards: making a screen full of numbers readable in five seconds.',
 lede='Three dashboard designs for finance, analytics and sales. Each one answers the same question: what should the eye land on first?',
 meta=[('Role', 'Product designer · UI'), ('Format', 'Web dashboards'), ('Count', '3 designs'), ('Focus', 'Hierarchy and charts')],
 sections=[
  ('The designs', 'One main chart, a few key numbers, everything else smaller.', [
    ('carousel', [('f-dashboard-79-1.webp', 'Finance · accounts', 'Four totals across the top, one sales chart, and cards kept to the corner.'),
                  ('f-dashboard-78-2.webp', 'Analytics', 'Black bars on white for the main report, with traffic detail below.'),
                  ('f-image-26855.webp', 'Sales overview', 'Today’s numbers first, then trend, map and recent customers.'),
                  ('f-1.webp', 'Finance · detail', 'How the layout holds at two sizes.'),
                  ('f-2.webp', 'Analytics · detail', 'The same components at closer range.'),
                  ('f-3.webp', 'Sales · detail', 'Table and chart side by side.')]),
  ]),
  ('Rules I follow', 'What keeps a dashboard calm.', [
    ('cards', [('One accent colour', 'Colour marks the data, not the decoration.'),
               ('Numbers before charts', 'The key totals sit above the chart that explains them.'),
               ('Tables stay tables', 'Lists of people or products are left as plain rows, which are fastest to scan.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ AI LANDING
dict(
 slug='ai-landing', name='Landing Pages with AI', tags=['Process', 'AI-assisted build', 'Landing pages'], read=5,
 cover='assets/img/cover/ai-landing.webp',
 title='How I design landing pages with AI, without them looking like AI made them.',
 lede='AI can produce a landing page in a minute, and it will look like every other one. Across four landing pages I’ve settled on a process where I make the decisions and AI does the typing.',
 meta=[('Role', 'Designer and builder'), ('Sites', 'GoFully, Jobly, Careway, Petsy'), ('Tools', 'Figma, Claude Code, Base44'), ('Output', '4 landing pages')],
 stats=[('4', 'Landing pages', 'Each designed and built by me'), ('1', 'Section per prompt', 'Never a whole page at once'), ('375 px', 'First check', 'Every section tested on a phone')],
 tldr=[('The problem', 'Prompt an AI for “a landing page” and you get the average of the internet: a gradient, three cards and a vague headline.'),
       ('The solution', 'Do the thinking first. Research, one sentence, a wireframe. Then prompt one finished section at a time and review it like any other design.'),
       ('My role', 'Research, positioning, wireframes, prompts, review and the final build on all four pages.')],
 links=[('GoFully', 'https://gofully-extension.vercel.app'), ('Jobly', 'https://jobly-88t.pages.dev'), ('Petsy', 'https://petsy-style-edit.base44.app')],
 sections=[
  ('Two ways to use AI', 'The tool is the same. The order is different.', [
    ('pipeline', 'current', 'The default', 'Prompt → page → generic', ['“Make me a landing page”', 'AI picks the layout', 'AI writes the headline', 'Tweak colours', 'Looks like everyone else’s'], 'regenerate and hope'),
    ('pipeline', 'proposed', 'My process', 'Decide → wireframe → prompt → review', ['Research the audience', 'Write one sentence', 'Wireframe the page', 'Prompt one section', 'Review, test, ship']),
  ]),
  ('Step 1 · Research', 'Know what the page must answer before it exists.', [
    ('figs', [('cw-competitor.webp', 'Careway: I audited a competitor’s page first and listed what it failed to answer.'), ('cw-research.webp', 'The research board that set the direction.')]),
    ('p', 'For Careway that audit found 13 problems. Each one became a section the new page had to get right.'),
  ]),
  ('Step 2 · One sentence', 'If I can’t write the headline, the page isn’t ready to design.', [
    ('table', ['Site', 'The sentence'],
     [['GoFully', 'The screenshot studio that stays on your device.'],
      ['Jobly', 'Find jobs posted this week, not last year.'],
      ['Careway', 'Every patient on track. Every follow-up done.'],
      ['Petsy', 'Dressed for autumn walks.']]),
    ('cmp', 'gf-before.webp', 'gf-after.webp', 'Before · a list of features', 'After · one promise'),
  ]),
  ('Step 3 · Wireframe', 'Structure is my decision, not the model’s.', [
    ('carousel', [('pt-wireframe.webp', 'Petsy', 'Home and product pages wireframed in Figma before any prompt.'),
                  ('cw-wireframe.webp', 'Careway', 'The hero in grey, so the argument is judged before the styling.'),
                  ('gf-options.webp', 'GoFully', 'Three hero directions, each tested against the same long article.')]),
    ('fig', 'jb-wireframe.webp', 'Jobly: the full page as a wireframe, section by section.'),
  ]),
  ('Step 4 · Prompt one section', 'Small prompts, each describing something already designed.', [
    ('fig', 'pt-builder.webp', 'Petsy in Base44: one prompt per finished section, each tested before the next.'),
    ('cards', [('Give it the decision', 'The prompt carries the layout, copy and tokens. The AI doesn’t choose them.'),
               ('One section at a time', 'A small change is easy to judge and easy to throw away.'),
               ('Real content only', 'Real product screens and real copy go in from the first prompt. No placeholders.')]),
  ]),
  ('Step 5 · Review like a designer', 'AI output is a draft. I check it the way I’d check anyone’s work.', [
    ('rows', [('Does it look generated?', 'I strip default gradients, identical cards and filler copy until the page is specific to the product.'),
              ('Does it work on a phone?', 'Every section is checked at 375 px for overflow, tap targets and reading order.'),
              ('Is it true?', 'Every number and claim on the page is traced back to a source.')], None),
    ('gallery', [('cw-m-a.webp', 'Careway, hero A on a phone.'), ('cw-m-b.webp', 'Careway, hero B on a phone.'), ('pt-mobile.webp', 'Petsy on a phone.')], 3),
    ('p', 'I packaged these checks as reusable Claude skills, so the same review runs on every project.'),
    ('links', [('See the skills', 'skills.html')]),
  ]),
  ('The results', 'Four pages, four different looks, one process.', [
    ('carousel', [('gf-after.webp', 'GoFully', 'Privacy is the headline, and live demos replace the feature list.'),
                  ('jb-hero.webp', 'Jobly', 'The promise is the posting date, with the product right under it.'),
                  ('cw-hero-b.webp', 'Careway · hero B', 'The product-led hero, one of two built for an A/B test.'),
                  ('cw-hero-a.webp', 'Careway · hero A', 'The film-led hero for the same test.'),
                  ('pt-hero.webp', 'Petsy', 'A full-screen film and two paths in.')]),
    ('browser', 'gf-full.webp', 'gofully-extension.vercel.app', 'GoFully, the full page.'),
    ('browser', 'jb-full.webp', 'jobly-88t.pages.dev', 'Jobly, the full page.'),
    ('browser', 'cw-full.webp', 'Careway · landing page', 'Careway, the full page.'),
  ]),
  ('Looking back', 'What I’d tell another designer.', [
    ('rows', [('AI speeds up building, not thinking', 'The hours I save on code go into research and copy, which is where pages are won.'),
              ('Generic in, generic out', 'The quality of the page tracks the quality of the brief I write.'),
              ('Keep a checklist', 'The same review every time is what stops AI defaults from creeping back in.')], None),
    ('honest', 'About results.', 'I don’t have conversion data for these pages yet. This shows the process, not an uplift.'),
  ]),
 ],
),
# ------------------------------------------------------------------ MATH AI
dict(
 slug='mathai', name='Math AI', tags=['Mobile app', 'App Store screenshots'], read=3, compact=True,
 cover='assets/img/cover/mathai.webp',
 title='Math AI: a homework solver that shows the steps, and the store screenshots that sell it.',
 lede='Math AI lets a student point the camera at a problem and get a worked solution. I designed the app screens and the App Store screenshot sets for phone and tablet.',
 meta=[('Role', 'Product designer · UI and store screenshots'), ('Product', 'Mobile app · phone and tablet'), ('Scope', 'App screens, onboarding, two screenshot sets'), ('Type', 'UI design')],
 sections=[
  ('The idea', 'An answer isn’t the same as understanding.', [
    ('pipeline', 'current', 'Stuck on homework', 'Search → copy → still stuck', ['Hit a hard problem', 'Type it into a search', 'Find a bare answer', 'Copy it down', 'Next problem, same wall'], 'again tomorrow'),
    ('pipeline', 'proposed', 'With Math AI', 'Scan → steps → understand', ['Point the camera', 'Crop to one problem', 'Read it step by step', 'Check the graph', 'Save it for revision']),
  ]),
  ('Store screenshots', 'Two sets, one message per frame.', [
    ('carousel', [('f-start.webp', 'Phone and tablet, side by side', 'One layout system covers both sizes, so the listing looks the same on every device.'),
                  ('f-01.webp', 'Lead with the scan', 'The first three frames show the product’s whole promise: scan, steps, hard questions.'),
                  ('f-02.webp', 'Then the depth', 'Step-by-step solutions, graphs for equations, and history.'),
                  ('f-03.webp', 'Then the extras', 'The basic and scientific calculator close the set.'),
                  ('f-01-tab.webp', 'Tablet · scan and learn', 'The same headline hierarchy, redrawn for a wider frame.'),
                  ('f-02-tab.webp', 'Tablet · dark frames', 'Light and dark panels alternate so each frame reads as a new point.'),
                  ('f-03-tab.webp', 'Tablet · calculator and graphs', 'Device angles change only where the feature is tactile.')]),
  ]),
  ('The app', 'Every screen a student meets.', [
    ('carousel', [('f-7.webp', 'Splash and onboarding', 'Three screens: what it does, how it helps, and what premium adds.'),
                  ('f-04.webp', 'Scan and result', 'Camera permission is asked in context, and the result reads like a worked page.'),
                  ('f-05.webp', 'How to use, and pricing', 'A short guide for first-timers and a plain comparison for premium.'),
                  ('f-367466078.webp', 'Calculator', 'Scientific and basic modes share one layout, with a single red key for clear.'),
                  ('f-367466075.webp', 'History and bookmarks', 'Past problems grouped by day, with bookmarks one tab away.'),
                  ('f-367466076.webp', 'Empty states', 'An illustration and one line, instead of a blank list.'),
                  ('f-367466077.webp', 'Terms and privacy', 'Long legal text set for reading, not hidden.')]),
  ]),
  ('Design choices', 'Why it looks the way it does.', [
    ('cards', [('One accent colour', 'Red marks the action and the answer. Everything else stays neutral.'),
               ('Steps over answers', 'The solution is laid out line by line, like a teacher’s working.'),
               ('Ask permission late', 'The camera prompt appears when the student taps scan, not at launch.')]),
  ]),
 ],
),
# ------------------------------------------------------------------ AVATARLY
dict(
 slug='avatarly', name='Avatarly', tags=['Figma plugin', 'Design + code'], read=3, compact=True, hero_clip='avatarly-quick.mp4', tint=('#f1c9f5', '#e3d4ff', '#f7f1fa'),
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
    ('clip', 'avatarly-gallery.mp4', 'Gallery: each collection is one tap, and every image ships with the plugin.'),
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
 slug='blobby', name='Blobby', tags=['Figma plugin', 'Design + code'], read=3, compact=True, hero_clip='blobby-shuffle.mp4', tint=('#c9d7ff', '#e2d6ff', '#f1f3fb'),
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


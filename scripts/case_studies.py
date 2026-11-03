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
pill is one of: good, bad, mid. **text** renders bold. Images live in assets/img/cs/<slug>/.
"""

CASES = [
# ------------------------------------------------------------------ OMNISPROOF
dict(
 slug='omnisproof', name='OmnisProof', tags=['Legal tech', 'AI'], read=12,
 cover='assets/img/cover/omnisproof.webp',
 title='From manual document setup to effortless signing.',
 lede='Legal teams shouldn’t have to wrestle with complicated workflows to send a document for signature. I redesigned OmnisProof’s signing setup so they move from document to signature in one self-serve flow: **upload, field placement and AI assistance** on one page.',
 meta=[('Product', 'OmnisProof, Omnis legal AI suite'), ('Role', 'Product Designer / Design Engineer'), ('Scope', 'Workflow redesign, AI field detection, prototyping'), ('Users', 'Lawyers, paralegals, legal assistants')],
 stats=[('~72%', 'AI field suggestions', 'Accepted without edits across 6 internal walkthroughs'), ('4 → 1', 'Setup screens', 'A 4-step modal wizard became one guided page'), ('11 → 8', 'Workflow steps', 'From 6 disconnected tools to 1 system')],
 tldr=[('The problem', 'Sending a document for signature took a 4-step modal wizard, hidden documents and repetitive field placement before it reached the signer.'),
       ('What I did', 'Rebuilt setup as one guided page where the document stays in view, and added reviewable AI field detection: the AI proposes fields, the user approves them.'),
       ('Where it stands', 'Shipped. Contract execution went from 11 steps to 8, and about 72% of AI field suggestions were accepted without edits.')],
 sections=[
  ('What we’re building', 'Three bottlenecks stood between a lawyer and a sent document.', [
    ('p', 'OmnisProof is an e-signing platform built for high-velocity legal workflows. The redesign tackles three bottlenecks in document preparation.'),
    ('rows', [('Too many steps before sending a document', 'Setup ran across several disconnected screens before anyone could place a signature field.', 'A single, guided workspace: upload, configure signers and prepare to send in one flow.'),
              ('Manual field placement slows everything down', 'Placing fields by hand across long legal documents is repetitive and easy to get wrong.', 'AI-assisted field detection that suggests where fields belong, with the user reviewing each one.'),
              ('Different documents, different needs', 'Teams use many document types and signing rules, and the flow had to handle them without adding complexity.', 'A flexible start: uploads, reusable templates and existing files.')], ('Problem', 'Building')),
    ('callout', 'The goal', 'Turn document signing from a multi-step chore into a guided experience legal teams complete with confidence.'),
  ]),
  ('The product', 'The document execution layer inside a legal AI ecosystem.', [
    ('p', 'OmnisProof turns a drafted agreement into a signed, filed legal record. Drafting, matter tracking and client portals all produce documents that end up here, so if signing is slow or error-prone, it undermines everything upstream.'),
    ('panels', [('good', 'Target', 'High adoption', ['Fast, reliable e-sign with AI detection', 'Matters close on time, no rework', 'Full replacement of DocuSign']),
                ('bad', 'Risk', 'High churn', ['Document hidden behind 4 steps', 'Missed signatures, wrong signers', 'Firms fall back to DocuSign'])]),
    ('lead', '**Why it was urgent.** Leadership pitched OmnisProof as a full DocuSign replacement. The MVP wizard (General Info → Add Signers → Add Fields → Distribute) showed the document only at step three, and that gap was the most-cited risk in product reviews.'),
  ]),
  ('Why we solved this', 'No time for a full research cycle, so I used the strongest signals available.', [
    ('flow', ['Walkthroughs · 2 lawyers + 1 paralegal', 'PM testing notes', '5-competitor teardown', 'G2 & Capterra reviews']),
    ('list', ['Users finished each wizard step but lost track of which document they were configuring.',
              'Manual field placement was the biggest source of time spent and errors made.',
              'Competitor reviews described documents sent with a missing field or wrong recipient, found only afterwards.']),
    ('cards', [('Lawyers', 'Prepare agreements and are accountable if anything goes out wrong.'), ('Paralegals', 'Do most day-to-day document prep across many matters.'), ('Legal assistants', 'Prep documents for an attorney, then hand them back to send.')]),
    ('panels', [('bad', 'Before', 'MVP wizard', ['General info', 'Add signers', 'Add fields by hand (document visible here)', 'Distribute']),
                ('good', 'After', 'Document-first', ['Upload, document on screen', 'AI suggests fields', 'Review and edit', 'Add signers', 'Send'])]),
  ]),
  ('Research', 'Uploading was easy. Getting fields and signers right was hard.', [
    ('p', 'Teardown of DocuSign, Adobe Sign, Dropbox Sign, PandaDoc and Documenso: docs, review-site screenshots and free trials.'),
    ('table', ['Area', 'What competitors do well', 'Where they fall short'], [
      ['Upload', 'Fast, well-documented upload and invites', 'Field placement is manual on every page'],
      ['Automation', 'DocuSign auto-places on a few templates', 'No reviewable AI field detection anywhere'],
      ['Sending', '“Send in under a minute”', 'Speed costs verification: wrong recipients found later']]),
    ('callout', 'Key insight', 'All five tools handle upload well. None of them help you between “uploaded” and “ready to send”, where fields, recipients and mistakes live.'),
    ('fig', 'omnisproof-workflow-comparison.webp', 'From 11 steps across 6 tools to 8 steps in one system. Before, legal teams bounced between Word, email, local folders, an e-sign tool and practice management to execute one contract.'),
  ]),
  ('Constraints & decisions', 'I chose which work stays with the lawyer and which the system takes on.', [
    ('table', ['Constraint', 'Decision'], [
      ['Field placement is required but too heavy to leave manual', 'AI proposes placement; users review and correct only where needed'],
      ['The 4 stages were right, hiding the document wasn’t', 'Keep the stages, render them as one page with the document always visible'],
      ['No access to external users pre-launch', 'Internal legal staff as proxies, cross-checked with review sites, every claim labelled with its confidence'],
      ['Had to ship inside the existing timeline', 'Scope to the two moments with the clearest friction']]),
  ]),
  ('Deep dive · AI field placement', 'How do you make lawyers trust an AI that places their signature fields?', [
    ('p', 'Automating was easy. Trust was hard: a wrong guess sends a contract to the wrong person.'),
    ('iters', [('bad', 'Rejected', 'Automatic, silent placement', 'AI placed every field on upload, no review step. A lawyer moved each one, even the correct ones:', 'I didn’t see it place them, so I don’t trust them.'),
               ('bad', 'Rejected', 'Chat-based assistant', '“Place a signature field for Lucas on page 3.” Field placement is a one-time step, and typing commands added another.', None),
               ('good', 'Shipped', 'Inline, reviewable “Detect with AI”', 'One button in the field panel. Suggestions appear on the page in view, and each one drags, edits or deletes like a manual field. The AI proposes, the user decides.', None)]),
    ('fig', 'omnisproof-ai-field-annotation.webp', '“Detect with AI” finds 38 fields in context; every suggestion stays editable.'),
    ('stats', [('~72%', 'Accepted as-is', 'Suggestions accepted without edits'), ('5 / 7', 'Field types', 'Standard types auto-detected'), ('1 → 0', 'Distrust', 'Participants distrusting AI output')]),
    ('honest', 'Honest confidence level.', 'I took these numbers from six internal walkthroughs. They show a direction; no controlled study or production data backs them yet.'),
    ('details', 'Edge cases (3)', ['Custom field types outside the 7 known ones are left for manual placement, with no error state.', 'Scanned PDFs: “Detect with AI” explains inline why it can’t run.', 'A user rejects most suggestions: the next document still gets a fresh pass. Trust recovery is untested and flagged as open.']),
  ]),
  ('Deep dive · Collapsing the wizard', 'I turned four modal screens into one page.', [
    ('cmp', 'omnisproof-before-wizard.webp', 'omnisproof-after-onepage.webp', 'Before · 4-step wizard', 'After · 1 guided page'),
    ('iters', [('bad', 'Rejected', 'Delete the steps', 'Everything on one dense screen. A lawyer called it', 'a cockpit.'),
               ('bad', 'Rejected', 'Merge General Info into Add Signers', 'Fewer clicks, but the document was still hidden. A marginal gain on the wrong metric.', None),
               ('good', 'Shipped', 'Same 3 stages, one persistent page', 'Step tracker on the left, document in the centre, a right panel that changes per stage.', None)]),
    ('table', ['Dimension', 'Before · 4-step wizard', 'After · 1 guided page'], [
      ['Document visibility', 'Hidden until step 3', 'Visible from the start'], ['Field placement', '100% manual drag and drop', 'AI detection + 1-click review'],
      ['Navigation', '4 full screens', '1 page, 3 panel states'], ['Error recovery', 'Back-button loop', 'Inline step switching']]),
    ('callout', 'Result', 'The two lawyers who were lost in the old wizard and the “cockpit” finished the new flow without a single question.'),
  ]),
  ('Outcome', 'The system now does the setup work lawyers used to do by hand.', [
    ('tldr', [('good', 'Validated', '6 internal walkthroughs; ~72% of AI suggestions accepted without edits; the same two testers before and after.'),
              ('mid', 'Qualitative', '“I didn’t see it place them, so I don’t trust them.” “This looks like a cockpit.” Both shaped the shipped design.'),
              ('bad', 'Not yet', 'Production data (completion rate, time to complete, support tickets) and feedback from external law firms.')]),
  ]),
  ('Final thoughts', 'Three things I’d carry into the next project.', [
    ('rows', [('Put the document at the center', 'Keeping it visible turned a configuration-heavy process into an understandable workspace.'),
              ('Let AI handle the repetitive work', 'Suggested fields cut manual effort; review and approval stay with the person.'),
              ('Keep the structure, change the presentation', 'The three stages were right. I kept them and stopped hiding the document behind them.')], None),
    ('fig', 'omnisproof-before-after-redesign.webp', 'Before vs. after: the wizard collapsed into a document-centred workspace with AI field detection.'),
    ('lead', 'Lawyers still prepare each document. They now spend that time checking fields instead of placing them.'),
    ('panels', [('mid', 'Next', 'What I’d explore next', ['Test with external law firms.', 'Study how people use AI suggestions over time.', 'Smarter detection for complex fields.', 'Measure setup time, completion and correction patterns.'])]),
  ]),
 ],
 faq=[('Why only two problems instead of the whole product?', 'Going deep on two hard problems shows how I think better than a product tour. Each had a rejected first attempt, evidence of why, and a validated fix.'),
      ('How confident are you in the 72% number?', 'Moderately. It comes from six internal walkthroughs, so I treat it as directional, and I say so up front.'),
      ('Why not just delete the wizard’s steps?', 'I tried it first. A tester called it “a cockpit.” The stages were right; hiding the document was the mistake.'),
      ('What would you do with more time or budget?', 'Test with external law firms and instrument real production metrics instead of relying on six sessions.')],
),

# ------------------------------------------------------------------ CASENOTES
dict(
 slug='casenotes', name='CaseNotes', tags=['Legal tech', 'AI', '0 → 1'], read=8,
 cover='assets/img/cover/casenotes.webp',
 title='A notetaker that files each client call to its case, and lets the lawyer go off the record.',
 lede='CaseNotes records and summarizes legal meetings, files the notes to the right matter, and lets a lawyer **go off the record with one keystroke**.',
 meta=[('Role', 'Founding product designer, 0 to 1'), ('Users', 'Partners, associates, paralegals'), ('Domain', 'Legal-tech meeting intelligence'), ('Status', 'Pre-launch beta')],
 stats=[('12 + 7', 'Research', 'Live client meetings observed, then follow-up interviews, across four firms'), ('88%', 'Prototype trust', 'Of legal testers would trust it on privileged calls'), ('45 min', 'Time saved', 'Per matter, weekly, on note re-entry and billing prep')],
 tldr=[('The problem', 'Lawyers paused AI notetakers whenever talk turned to strategy, because consumer tools don’t protect privilege. The notes had gaps, and paralegals re-typed them into three tools.'),
       ('What I did', 'As founding designer, I set two rules every screen follows: the lawyer controls the record, and every note belongs to a matter. Then I designed the meeting flow, four role views and mobile.'),
       ('Where it stands', 'Pre-launch beta. The numbers come from prototype testing with legal teams, not production usage. Desktop screens are under NDA; I walk through them on a call.')],
 sections=[
  ('The problem', 'A recorded client meeting can end up in discovery.', [
    ('lead', 'Imagine you’re an associate on a call with a client. The client starts talking about settlement numbers. You reach over and pause the AI notetaker, because courts have said consumer AI tools don’t preserve attorney-client privilege and the recording could end up in discovery.'),
    ('p', 'Now there’s a gap in the notes, and you rebuild it from memory. After the call, a paralegal re-types the same notes into three different tools. And nothing connects this call to the deposition prep in October.'),
  ]),
  ('What CaseNotes does', 'Three things a law firm needs from a notetaker.', [
    ('p', 'Generic notetakers treat every meeting the same. CaseNotes is built around three things a law firm needs.'),
    ('rows', [('Go off the record in one keystroke', 'The lawyer decides, in the moment, whether a record exists at all.'),
              ('File every note to its matter', 'Summaries attach to the case, carry privilege tags, and stay behind ethical walls.'),
              ('Remember the case, not the meeting', 'Decisions and deadlines connect across months of client and counsel sessions.')], None),
  ]),
  ('What I saw', 'I sat in on 12 client meetings before drawing a screen.', [
    ('p', 'I observed 12 live client meetings and case conferences across four small and midsize firms, then ran 7 follow-up interviews with partners, associates and paralegals.'),
    ('callout', 'The signal', 'In 9 of the 12 meetings, associates paused or stopped the recording when the talk turned to settlement or strategy.'),
    ('cards', [('Pauses had no rules', 'Each associate used a personal habit to decide when to stop recording, so the firm’s records were inconsistent.'),
               ('Paralegals paid the price', 'They spent hours re-typing the same notes into practice management, document drives and billing logs.'),
               ('Meetings differ', 'Lawyers treat an internal huddle and a privileged client session differently. Their tools didn’t.')]),
    ('fig', 'casenotes-research-approach.webp', 'A lean research plan: interviews, a 12-tool competitive audit, workflow mapping and AI trust research.'),
  ]),
  ('My role', 'I designed CaseNotes from zero.', [
    ('table', ['Area', 'What I did'], [
      ['Research', 'Shadowed 12 meetings, ran 7 interviews, and audited 12 AI notetakers including Fireflies, Otter and Fathom.'],
      ['Product thesis', 'Set the two principles every screen follows: the lawyer controls the record, and every output belongs to a matter.'],
      ['Meeting flow', 'Designed what happens before, during and after a call, including how the AI behaves.'],
      ['Roles', 'Defined four views so partners, associates, paralegals and clients each see only what they should.'],
      ['Mobile & integrations', 'Designed the mobile companion and how notes sync to Clio, NetDocuments and the rest of Omnis.']]),
  ]),
  ('One meeting', 'What happens before, during and after a call?', [
    ('p', 'Every meeting moves through three moments, and each answers a different question for the lawyer.'),
    ('rows', [('Before · Is this call privileged?', 'CaseNotes checks the calendar and the matter. Litigation calls start as privileged and restricted; firm admin meetings start open.'),
              ('During · Is it recording right now?', 'The interface stays quiet: no bot avatar, no scrolling transcript. A small indicator shows when it’s recording, and one shortcut pauses it.'),
              ('After · Where did it go?', 'The summary files to the case: decisions, owners, deadlines and privilege tags per segment. The raw transcript sits in a secondary drawer.')], None),
    ('fig', 'casenotes-architecture-capture-routing.webp', 'The capture gate: audio is held briefly, checked for privilege, then routed by role.'),
  ]),
  ('Privilege', 'How do I go off the record?', [
    ('lead', 'One keystroke, **⌘+P** on desktop or one tap on mobile, pauses capture mid-sentence and marks that segment privileged.'),
    ('p', 'The screen switches to a high-contrast state so everyone can see nothing is being recorded. If opposing counsel walks in, one tap is enough.'),
    ('figs', [('casenotes-mobile-courtroom-live.webp', 'In a hearing: the pause is one thumb-sized button.'), ('casenotes-mobile-digest.webp', 'After the call: decisions, tasks and billing entries.'), ('casenotes-mobile-dashboard.webp', 'The day at a glance, between court and the office.')]),
  ]),
  ('AI you can check', 'Can I trust what the AI wrote?', [
    ('p', 'CaseNotes only summarizes what someone said. If a term wasn’t discussed, it says so instead of guessing. Every point links to the exact moment in the audio, so a lawyer can verify it in seconds. Client data never trains the AI models.'),
  ]),
  ('Roles & integrations', 'Who sees what, and where do the notes go?', [
    ('table', ['Role', 'What they see from the same meeting'], [
      ['Partner', 'Decisions, risk, billable time and staffing.'], ['Associate', 'Research tasks, drafting deadlines and cited sources.'],
      ['Paralegal', 'Filing dates, document requests and docket items.'], ['Client', 'A plain-language digest. Privileged notes are removed before display.']]),
    ('p', 'Summaries, deadlines and time entries push to Clio, PracticePanther or MyCase. Memos go to NetDocuments or iManage with the firm’s existing permissions. Inside Omnis, notes feed the CRM, MedChron timelines and LitDraft documents.'),
    ('fig', 'casenotes-ecosystem-integrations.webp', 'CaseNotes connects to practice management, document storage, calendars and the rest of Omnis.'),
  ]),
  ('Design decisions', 'Four calls that shaped CaseNotes.', [
    ('rows', [('Why does the lawyer control recording?', 'Associates were already pausing recorders by habit. One visible keystroke turned a private workaround into a firm-wide rule.'),
              ('Why file notes to a matter?', 'Lawyers organize their work by case. Filing each summary to its matter links March’s settlement talk to October’s deposition prep.'),
              ('Why hide the raw transcript?', 'The transcript is evidence; the summary is what the lawyer needs. Leading with the summary keeps less discoverable text in front of people.'),
              ('Why only summarize what was said?', 'In litigation, an invented fact can lead to court sanctions. Linking each point to the audio lets a lawyer check it before relying on it.')], None),
  ]),
  ('Results', 'What prototype testing showed.', [
    ('stats', [('94%', 'Task completion', 'Finding a matter’s privilege status'), ('88%', 'Would trust it', 'On privileged client calls'), ('86', 'Usability (SUS)', 'Across partner and associate testers')]),
    ('honest', 'Scope note.', 'These come from prototype validation with legal teams before launch, not from production usage.'),
  ]),
  ('Looking back', 'What CaseNotes taught me.', [
    ('rows', [('Compliance is a design input', 'Most AI products add compliance after the design is done. In law it has to shape the first screen.'),
              ('Defaults carry legal weight', 'Whether a call starts privileged or open is a product choice with legal weight. A wrong default creates a liability.'),
              ('Design the system, then the screens', 'The matter-linked structure did more for lawyers than any single screen, because it made every other feature possible.')], None),
  ]),
 ],
 faq=[('Why can’t I see the desktop screens?', 'They’re under NDA. I walk through them live on a call, and the mobile screens and diagrams here show the same system.'),
      ('Are the numbers from real usage?', 'No. They come from prototype testing with legal teams before launch, and I label them that way.')],
),

# ------------------------------------------------------------------ AI UX AUDIT
dict(
 slug='audit-engine', name='AI UX Audit Engine', tags=['AI tooling', 'Design QA'], read=10,
 cover='assets/img/cover/audit-engine.webp',
 title='Design QA took me a day per release. So I built an engine that takes minutes.',
 lede='A tool that opens a web app the way a person would, clicks through its menus and pop-ups, and lists each design problem it finds with **the exact code fix**. It costs about $0.30 a screen.',
 meta=[('Role', 'Solo product designer & builder'), ('Duration', 'Jun – Jul 2026 · Omnis AI'), ('Owned', 'Problem, design, architecture, ~27k lines of TypeScript'), ('Skills', 'Design QA, accessibility, AI pipelines, full-stack TS')],
 stats=[('$0.30', 'Per screen', 'In about 3 minutes, vs 2–3 hours per product by hand'), ('90%+', 'Proof', 'Of findings tied to a real element on the page'), ('229', 'Rules', 'Fixed checks before any AI judgement')],
 tldr=[('The problem', 'As the only designer across five products, I checked every release by hand. Design bugs hid behind dropdowns, errors and empty states nobody had time to open.'),
       ('What I did', 'Designed and built an engine that signs in, clicks through every state and checks it against 229 rules. A finding that can’t point to a real element is thrown out.'),
       ('Where it stands', 'A working prototype: about $0.30 and 3 minutes a screen, 90%+ of findings tied to an element, 187 tests. Parked after a restructuring; not run at scale.')],
 sections=[
  ('Overview', 'I built a tool to do the QA nobody had time for.', [
    ('p', 'I was the only designer across five legal-tech products at Omnis AI. Before each release I checked every screen by hand, and it took hours. So I built a tool that does the checking, and I keep the final say.'),
    ('rows', [('Give it a link', 'And a test login for the staging app.'), ('It clicks through', 'Screens, menus, dialogs and pop-ups, the way a person would.'),
              ('It checks each state', 'Against 229 fixed rules, then an AI pass for layout.'), ('You get a report', 'Every problem tied to an element, with a fix ready to paste.')], None),
  ]),
  ('The problem', 'Most design bugs show up only after a click.', [
    ('p', 'A screen can pass review when it first loads. The problems show up after someone opens a dropdown, submits a form with an error, or lands on an empty page. Nobody had time to click through all of those states before each release, so those bugs reached real users.'),
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
    ('p', 'A typical manual check meant taking screenshots, drawing red boxes in Figma, listing the design tokens and writing tickets. When engineers fixed something, I checked everything again. Design QA became the thing holding releases back.'),
    ('fig', 'audit-02.webp', 'Before: my manual review in Figma, one note per problem.'),
  ]),
  ('Design process', 'Version one invented a button. Version two checks the real page.', [
    ('p', 'Each version tested one question: can a tool find design problems engineers trust enough to fix?'),
    ('iters', [('bad', 'V1 · Rejected', 'Reading screenshots with AI', 'A vision model listed problems from screenshots. On a dashboard I knew well it reported low contrast on “the secondary button beside the search field.” That button didn’t exist.', None),
               ('good', 'Final', 'Checking the real page, with proof', 'The tool works inside a live browser, runs 229 fixed rules first and uses AI only for layout. Any problem that can’t point to a real element is thrown out.', None)]),
    ('figs', [('audit-v1-vision-report.webp', 'V1 flagged a button that isn’t there.'), ('audit-08.webp', 'Final: each flagged element maps to a numbered finding with its selector and fix.')]),
    ('callout', 'Insight', 'If one finding is made up, you double-check all of them. So the tool drops any finding it can’t tie to an element.'),
  ]),
  ('Outcome', 'What changed between the manual way and the tool.', [
    ('stats', [('$0.30', 'Cost and time', 'Per screen, in about 3 minutes'), ('89', 'One run', 'Problems across 22 states of CaseNotes in ~11 min, ~$1.20'), ('90%+', 'Proof', 'Of findings tied to a real element')]),
    ('table', ['Before · by hand', 'After · the tool'], [
      ['Hours of designer time per product', 'About 3 minutes per screen'], ['Some states checked, when there was time', 'All reachable controls on the audited screens'],
      ['A Figma screenshot with a red box', 'The exact element and a copy-paste fix'], ['Check everything again after a fix', 'One command re-checks and shows what changed']]),
    ('fig', 'audit-05.webp', 'The tool’s report, with the screen annotated and each problem tied to its element.'),
    ('honest', 'Scope note.', 'I measured these on my own test runs against Omnis staging apps. Nobody outside the team has checked them, and I haven’t run them on live traffic.'),
  ]),
  ('Design decisions', 'Proof first, clicks before judging, fixes ready to paste.', [
    ('rows', [('Proof before opinion', 'Fixed rules handle what can be measured: contrast, accessibility attributes and design tokens. AI handles judgement calls, only when it can point to the element.'),
              ('Click before judging', 'The tool opens each dialog, dropdown, drawer and tab before it reviews a screen.'),
              ('Every problem comes with its fix', 'Each card shows severity, the rule, a plain title, the principle behind it, a copy-paste CSS fix and a confidence score.'),
              ('Each role sees its own list', 'One run, six readers: designer, frontend, QA, content, engineering manager and leadership.')], None),
    ('figs', [('audit-04.webp', 'Going past the first screen to check dialogs, drawers and open dropdowns.'), ('audit-pr-handoff.webp', 'What the engineer receives: the rule, the element, measured colours and a fix.')]),
    ('fig', 'audit-fleet-dashboard.webp', 'One run across four products: findings per product, open blockers with an owner, fixes per week and a release gate.'),
  ]),
  ('Under the hood', 'Two codebases, one TypeScript stack.', [
    ('table', ['Layer', 'Technology'], [
      ['Runtime', 'Node + TypeScript, Model Context Protocol (MCP) SDK'], ['Capture', 'Playwright: sessions, full-page screenshots, DOM inventory, state crawler'],
      ['Accessibility', '@axe-core/playwright, run live per page'], ['AI vision', 'OpenAI-compatible SDK with Gemini Flash and OpenRouter fallbacks'],
      ['Service', 'Next.js 16, React 19, Tailwind 4, Prisma 7 + Postgres, BullMQ + Redis, Docker']]),
    ('fig', 'audit-terminal-run.webp', 'One command logs in, opens each state, drops findings it can’t tie to an element, and saves HTML and Markdown reports.'),
  ]),
  ('Looking back', 'What building it taught me.', [
    ('rows', [('Trust comes before speed', 'A tool that reports 50 problems with 15 made up costs more time than checking by hand.'),
              ('Real checks need clicks', 'Looking only at first loads misses overflowing dropdowns, error messages and empty pages.'),
              ('Engineers fix what they can paste', 'A selector and a code fix get merged. A vague comment gets skipped.')], None),
    ('panels', [('mid', 'Next', 'If I pick it back up', ['Remember a baseline per product so runs flag only new problems.', 'Run on every staging deploy through GitHub Actions.', 'Re-check after a fix is merged.', 'Send verified notes back into Figma.'])]),
  ]),
 ],
 faq=[('Are you a designer or an engineer?', 'Product design is my foundation: research, UX architecture, interaction design and design systems. I also write production TypeScript to ship working prototypes and tooling end to end.'),
      ('How do you prevent hallucinations?', 'Deterministic checks cover objective rules like contrast maths and ARIA. AI findings are rejected unless they map to a real DOM node.'),
      ('How is this different from axe-core or Lighthouse?', 'Those check one static URL. This engine signs in, crawls interactive states, pairs axe-core with layout checks and exports ready-to-paste fixes.'),
      ('Can it run in CI?', 'Not yet. Running on every staging deploy and flagging blockers on pull requests is the next step.')],
),

# ------------------------------------------------------------------ CASEPRO
dict(
 slug='casepro', name='CasePro Matter Redesign', tags=['Legal SaaS', 'AI-assisted'], read=11,
 cover='assets/img/cover/casepro.webp',
 title='CasePro: rebuilding matter creation around what a client says, not what a form demands.',
 lede='Intake and matter creation used to be one overloaded form. Now they are two connected systems, one **AI-assisted** and one manual.',
 meta=[('Role', 'Product Designer, system redesign'), ('Domain', 'Legal practice management · CRM'), ('Users', 'Intake specialists, paralegals, attorneys, admins'), ('Status', 'Design → engineering handoff')],
 stats=[('1 → 2', 'Data model', 'One merged object became intake and matter, linked'), ('2 paths', 'Creation', 'Create with AI Agent, or Create Manually'), ('6 steps', 'Shared structure', 'Both paths, one review gate')],
 tldr=[('The problem', 'Intake and matter creation were one overloaded form, so a paralegal had to know the whole matter before a client had finished explaining it.'),
       ('What I did', 'Split them into two linked modules and gave matter creation two paths, AI agent or manual, sharing one six-step structure and one review gate. I brought three options to stakeholders instead of one.'),
       ('Where it stands', 'Handed off to engineering with a full spec. It hasn’t shipped, so there is no production data yet, and this case study says so.')],
 sections=[
  ('Overview', 'CasePro runs a case from the first call to close.', [
    ('p', 'CasePro is the practice-management layer firms use to run a case from the first client call to close: matters, parties, incident facts, documents, deadlines and staffing.'),
    ('callout', 'The opening insight', 'I watched intake specialists do the same thing three times in one morning: transcribe a client call into a text box, open a new matter, then retype half of it into six more tabs. The form did the job of two tools and did neither well.'),
  ]),
  ('The problem', 'Each new matter started by guessing what the client already told someone.', [
    ('rows', [('Intake was a text box', 'The only place client information lived was one freeform field: “Notes or links to intake form.” Nothing structured, nothing reusable.'),
              ('One form, every practice area', 'The same fields for an auto accident, a slip-and-fall or a commercial dispute. Firms couldn’t tailor questions to their region or practice.'),
              ('Nothing carried forward', 'Answers from intake never flowed into the matter. Paralegals re-typed names, dates and incident details by hand.')], None),
    ('figs', [('before-01-matter-form-freeform-intake.webp', 'Before: the entire intake is one textarea in step 1 of 6.'), ('before-03-mega-form-scroll.webp', 'Before: eight sections stacked as if they were one decision.')]),
  ]),
  ('Research & diagnosis', 'The form sat on the wrong data model.', [
    ('p', 'I wanted three independent signals to agree before proposing anything.'),
    ('cards', [('Shadowing', 'Two weeks of live matter creation with intake specialists and paralegals, timing every pause and backtrack.'),
               ('The CRM’s own data', 'In a sample of recent matters, the intake questionnaire field was empty or just a name on most of them.'),
               ('Reframed interviews', 'With the ops lead and two attorneys: “walk me through the last matter you opened,” not “what’s wrong with the form.”')]),
    ('callout', 'The reframe', 'Intake is what a client tells you, once, in their own words. A matter is the legal record your firm builds from it, and firms need to build it two ways, depending on how much is already captured.'),
  ]),
  ('Options on the table', 'I brought three options and rejected the two fastest.', [
    ('iters', [('bad', 'Option A · Rejected', 'Polish the existing form', 'Cleaner steps and validation, intake still a field inside matter. A better-looking version of the same bug.', None),
               ('bad', 'Option B · Rejected', 'One button, fully automatic', 'Always generate the matter from intake. Stakeholders liked it first, but many matters start with almost no intake, and a bad guess would land in a legal record unchecked.', None),
               ('good', 'Option C · Chosen', 'Separate intake, let the user choose', 'Intake becomes its own customizable entity. Matter creation forks: AI-assisted where intake supports it, manual where it doesn’t.', None)]),
  ]),
  ('Design thesis', 'Two decisions that reshaped the system.', [
    ('rows', [('Intake and matter are separate, linked entities', 'Firms can define their own intake questions per state, county or practice, without touching the matter schema. A voice agent can join a client call and fill structured intake fields.'),
              ('Matter creation needs two paths, not one assumption', 'Let the person creating the matter say how much is already known, and route them accordingly.')], None),
    ('fig', 'after-01-choose-path.webp', 'After: the first screen asks one question, how much do we already know? Neither path is presented as the “smart” default.'),
  ]),
  ('Path A · Create with AI', 'The AI path shows where each value came from.', [
    ('rows', [('Understand intake', 'Scores how usable the linked intake is: 17 fields ready, 2 to review, 4 missing.'),
              ('Prepare draft', 'Narrates each extraction step in the background, visible and cancellable.'),
              ('Review & edit', 'Every field labels its source: From Intake, AI Matched or AI Suggested.'),
              ('Ask the assistant', 'Fills gaps where the reviewer is already working.'),
              ('Review before create', 'The same review gate as the manual path. Nothing skips it.')], None),
    ('figs', [('after-02-intake-readiness.webp', 'Readiness, scored per intake category.'), ('after-04-matter-prefilled-provenance.webp', 'Field-level provenance instead of a blanket confidence score.')]),
    ('figs', [('after-05-ai-chat-assistant.webp', 'The assistant suggests next steps: fill gaps, summarize, find similar matters.'), ('after-06-review-before-create.webp', 'Step 6 of 6: review and confirm before anything is created.')]),
    ('callout', 'The rule behind it', 'Nothing in a matter should look identical whether a human confirmed it or the model guessed it.'),
  ]),
  ('Path B · Create manually', 'The manual path uses the same six steps, without the AI draft.', [
    ('flow', ['Matter Overview', 'Parties Involved', 'Incident Details', 'Legal & Insurance', 'Team Assignment', 'Images & Outcome']),
    ('figs', [('after-08-manual-incident-autofill.webp', 'Typing an incident address fills city, state and zip.'), ('after-09-manual-team-roundrobin.webp', 'Staffing suggestions from the firm’s round-robin logic instead of empty dropdowns.')]),
  ]),
  ('Results & impact', 'Back to the paralegal retyping the same story into six tabs.', [
    ('cards', [('Intake specialists', 'The notes they capture on the call are the record the matter is built from, shaped to their firm’s questions.'),
               ('Paralegals', 'They confirm an AI draft field by field, or fill one guided form. They type each fact once.'),
               ('Attorneys & admins', 'Every matter arrives as the same reviewable record, and firms reshape intake without an engineering ticket.')]),
    ('honest', 'What’s designed vs. what’s measured.', 'These outcomes come from design review and the engineering handoff spec, not production adoption. I’d rather say that than invent a metric.'),
  ]),
  ('What I learned', 'Three lessons from CasePro.', [
    ('rows', [('Check the data model before the screen', 'The form was correct for the data model it sat on. The redesign only worked once the model changed.'),
              ('Confidence needs a visible source', 'Provenance tags and readiness scores make trust checkable, not assumed.'),
              ('A fallback path erodes over time', 'Manual creation stays usable only if it’s built and maintained as a first-class path.')], None),
    ('lead', 'Splitting intake from matter added screens. It also let firms shape intake to their own practice.'),
  ]),
 ],
 faq=[('Why not ship the one-click AI version stakeholders liked?', 'The CRM data showed many matters start with incomplete intake. As the only path, it would have broken on the common case and written guesses into legal records.'),
      ('Has this shipped?', 'No. It’s at engineering handoff, so there’s no production data yet.')],
),

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

# ------------------------------------------------------------------ LITBOX
dict(
 slug='litbox', name='LitBox', tags=['Legal SaaS', 'Secure storage'], read=12,
 cover='assets/img/cover/litbox.webp',
 title='When every legal product needs the same files, why store them in different places?',
 lede='I designed LitBox, a matter-aware file platform that gives the Omnis AI suite **one owned storage layer** instead of a third-party drive detour per product.',
 meta=[('Role', 'Solo product designer, end to end'), ('Domain', 'Legal tech SaaS · secure storage'), ('Timeline', 'Jan – Jun 2026 · Omnis AI'), ('Status', 'Internal beta / dogfooding')],
 stats=[('5 products', 'Ecosystem', 'LitBox running inside MedChron, AutoDoc, LitDraft and OmnisProof in staging'), ('25+', 'Edge states', 'Empty, error and permission states specified first'), ('1', 'Storage layer', 'One first-party layer instead of a drive per product')],
 tldr=[('The problem', 'Every Omnis AI product depended on Dropbox, Box or Google Drive, so the same document was re-uploaded into each tool with no shared record of who could see it.'),
       ('What I did', 'As the only designer, I led LitBox end to end: the case for owning storage, the IA and permission model, the UI system with 25+ edge states, and the integrations other products plug into.'),
       ('Where it stands', 'Internal beta. LitBox’s picker and search already run inside MedChron, AutoDoc and OmnisProof in staging. No usage metrics yet, and none invented.')],
 sections=[
  ('What we’re building', 'A unified legal file layer inside the ecosystem.', [
    ('rows', [('Third-party drive detours', 'A file had to live in Dropbox, Box or Drive before any Omnis product could touch it, with repeated re-authorizations and no matter context.', 'A matter-organized file workspace every product in the firm can reach.'),
              ('Sharing without chain of custody', 'Requesting confidential records through drive links exposed litigation data with no expiry, PIN or audit log.', 'Matter-governed File Requests with PINs, expiry and an audit trail.'),
              ('Disconnected product silos', 'Attorneys downloaded files and re-uploaded them into each tool, creating duplicates and version chaos.', 'A shared file layer embedded into every product through pickers and APIs.')], ('Problem', 'Building')),
    ('fig', 'dashboard.webp', 'The LitBox dashboard: storage, file and folder counts, and recent activity at a glance.'),
  ]),
  ('Why storage first', 'Why storage had to ship before the rest of the roadmap.', [
    ('p', 'CasePro attaches evidence, OmnisProof signs documents, MedChron builds chronologies from records, NotaryNow notarizes. If each solved “where do files live” alone, the platform would have as many storage models as products. Shipping LitBox first meant everything after could assume one owned file layer.'),
    ('panels', [('bad', 'Before', 'One file, three detours', ['Upload to a third-party drive', 'Re-authorize it in each product', 'Download and re-upload per product', '3 copies, no audit trail']),
                ('good', 'After', 'Uploaded once, reachable everywhere', ['Upload once to the matter folder', 'AutoDoc reads it directly', 'E-sign in place in OmnisProof', 'Every action logged'])]),
  ]),
  ('Research', 'A law firm’s storage has to protect privilege.', [
    ('cards', [('Legal research', 'ABA Model Rule 1.6(c), five verified law-firm breaches, and what legal vendors say “secure” must include.'),
               ('Competitive teardown', 'Dropbox, Box and Google Drive, module by module, scored for feature parity.'),
               ('Stakeholder interviews', 'Product leads for AutoDoc, OmnisProof, CasePro and MedChron. Not lawyers, and I call that gap out.')]),
    ('fig', 'competitor-dropbox.webp', 'Reference: Dropbox has files, folders and search, but no concept of a matter, a case team or a retention rule.'),
  ]),
  ('Options considered', 'I weighed three places to put the file layer.', [
    ('iters', [('bad', 'A · Rejected', 'Each product keeps its own storage', 'A nicer shared picker over separate backends. Fast, but it re-skins the fragmentation.', None),
               ('bad', 'B · Rejected', 'Fold storage into CasePro', 'The “obvious” answer, but it ties every product’s file access to CasePro’s releases and permissions.', None),
               ('good', 'C · Chosen', 'A standalone layer, embeddable everywhere', 'LitBox owns each file once and exposes search and a picker any product can call, on its own timeline.', None)]),
  ]),
  ('The workspace', 'I designed the empty, error and permission states first.', [
    ('p', 'Most of the work isn’t the happy path. It’s an empty grid, a folder you don’t have permission for, and a delete that can’t be undone after a set window. More than two dozen of those states were designed up front.'),
    ('fig', 'my-files-workspace.webp', 'My Files: a matter-organized workspace with familiar Drive-like patterns.'),
    ('figs', [('folder-access-restricted.webp', 'Access restricted, with a clear way to ask for it.'), ('delete-file-modal.webp', 'Delete says exactly what happens and for how long it can be undone.')]),
  ]),
  ('Five features', 'The surfaces that carry most of the daily weight.', [
    ('figs', [('create-request-advanced.webp', 'File Requests: routed to a folder, with deadline, PIN and late-upload rule.'), ('audit-timeline-populated.webp', 'The audit timeline: every upload, share, permission change and deletion.')]),
    ('fig', 'design-system-board.webp', 'The LitBox design system board: buttons, storage widget, filters and activity components.'),
  ]),
  ('LitBox everywhere', 'Pick a file from LitBox once, use it in any product.', [
    ('p', 'Instead of uploading the same document into every product, a product calls into LitBox directly through a search bar or picker. The internal Figma section was literally named “avoid context switching.”'),
    ('figs', [('embedded-medchron-picker.webp', 'LitBox’s picker running inside MedChron, in staging.'), ('embedded-autodoc-search-content.webp', 'Content search inside AutoDoc: page, snippet and source.')]),
    ('fig', 'esign-integration.webp', 'E-signature launched straight from a document’s detail view.'),
  ]),
  ('AI assistant · concept', 'One assistant on top of a search index it doesn’t have to rebuild.', [
    ('honest', 'Concept only.', 'Content search is designed and working in the prototype. The conversational assistant is a direction worth exploring, explicitly not something LitBox has built.'),
    ('fig', 'ai-assistant-panel.webp', 'Concept: an assistant that searches, compares documents and finds related files, within existing permissions.'),
  ]),
  ('Where this stands', 'What I can show today.', [
    ('tldr', [('mid', 'Measured', 'None yet. LitBox is in internal beta with no usage baseline, and I won’t invent adoption numbers.'),
              ('good', 'Observed', 'AutoDoc and OmnisProof integrations work end to end; search is live inside MedChron and AutoDoc in staging.'),
              ('bad', 'Expected', 'Less re-uploading, a defensible audit trail and fewer uncontrolled public links. Hypotheses to validate.')]),
    ('rows', [('Shared infrastructure is a different job', 'LitBox’s users include AutoDoc and OmnisProof. A broken metadata assumption breaks someone else’s product.'),
              ('Parity was the starting line', 'Matching Dropbox and Box was groundwork; the difference came from the matter model and the ecosystem.')], None),
  ]),
 ],
 faq=[('Why not just use Google Drive or Dropbox?', 'They’re secure and mature, but they organize around folders, not legal matters, and Omnis AI can’t audit them.'),
      ('Did you talk to lawyers?', 'Not directly for LitBox. Research combined legal rules, breach cases, a competitor teardown and product-lead interviews, and I flag that gap.')],
),
]

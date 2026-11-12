"""Regenerates the six HTML pages from the data lists below. Run: python3 scripts/build.py"""
import html, os, re
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
EMAIL = 'rahamanmuzeeb1108@gmail.com'
CDN = 'https://cdn-images-1.medium.com/max/400/'

ARTICLES = [  # (year, mm/dd, title, url, thumb, topic, claps, read min, views or None)
 # Titles, claps and read time from medium.com/@Muzeebdesign; views from medium.com/me/stats (lifetime), both 2026-11-01.
 # When views is set it replaces the claps badge; None falls back to claps, then read time.
 (2026,'10/24',"How to show AI skills in a design portfolio without faking it",'https://medium.com/@Muzeebdesign/how-to-show-ai-skills-in-a-design-portfolio-without-faking-it-f863b02a95d0','https://miro.medium.com/v2/resize:fill:208:136/1*JZGFjuslXuKkrSGvR6_QDw.png','AI in design',0,8,None),
 (2026,'10/16',"A notetaker lawyers can trust",'https://medium.com/design-bootcamp/a-notetaker-lawyers-can-trust-8b4b56bed58a','https://miro.medium.com/v2/resize:fill:208:136/1*8dgXbrYcMr9KYBcrNloOQw.jpeg','Case studies',0,19,10),
 (2026,'09/30',"100+ screens in 4 days",'https://medium.com/design-bootcamp/i-designed-100-screens-in-4-days-heres-what-speed-without-research-really-costs-f80333be1bbc','https://miro.medium.com/v2/resize:fill:208:136/1*eOvUUxxtSH1M6f81s-wd1Q.jpeg','User research',0,7,28),
 (2025,'07/20',"Test with five users",'https://medium.com/design-bootcamp/the-1-reason-most-digital-products-fail-hint-its-usability-157f8f70ef72','https://miro.medium.com/v2/resize:fill:208:136/1*W3ZAT4EUcaE4FQmTofmgmg.png','Usability',19,3,41),
 (2025,'07/14',"Designing for Real People: Why Human Experience (HX) Matters More Than Just UX",'https://medium.com/design-bootcamp/designing-for-real-people-why-human-experience-hx-matters-more-than-just-ux-bda7dfb24ec6','https://cdn-images-1.medium.com/max/400/1*vjNXDUbz1gxGVueVNGi6RA.png','Human experience',26,4,29),
 (2025,'05/22',"Engaging or addictive?",'https://medium.com/design-bootcamp/the-secret-to-designing-products-people-love-without-making-them-addictive-655ad97f4efa','https://miro.medium.com/v2/da:true/resize:fill:208:136/0*dYWM2MqO7z-ePCwM','Psychology',17,4,93),
 (2025,'04/21',"A poll assistant for live chat",'https://medium.com/design-bootcamp/how-ai-polls-could-save-youtube-and-twitch-streamers-from-chat-chaos-ce1c5997e054','https://miro.medium.com/v2/da:true/resize:fill:208:136/0*nNWI6cdpHbaLG2L_','AI concepts',1,3,25),
 (2025,'04/16',"UI vs UX for new designers",'https://medium.com/design-bootcamp/from-pretty-pixels-to-user-wins-your-ui-ux-guide-to-designing-with-impact-7b16b7071790','https://cdn-images-1.medium.com/max/400/1*lu52ukmZ0KptXp_X2PuTRg.jpeg','UI/UX',41,5,41),
 (2024,'06/05',"The full UX case study",'https://medium.com/design-bootcamp/unlock-your-talent-the-case-study-formula-for-ui-ux-design-success-part-2-da1ba2453dbd','https://cdn-images-1.medium.com/max/400/0*IaRl_ixUhkLVUDLb.jpg','Portfolio',10,10,188),
 (2024,'05/27',"Unlock Your Talent: The Case Study Formula for UI/UX Design Success, Part 1",'https://medium.com/design-bootcamp/unlock-your-talent-the-case-study-formula-for-ui-ux-design-success-part-1-8df5010c02af','https://cdn-images-1.medium.com/max/400/1*X6H8l_wWpILV7_HA5HnGRg.png','Portfolio',9,5,234),
 (2024,'05/06',"Design Like a Pro: Mastering Metrics, Testing, and Human Touch",'https://medium.com/design-bootcamp/design-like-a-pro-mastering-metrics-testing-and-human-touch-4585a9e71704','https://cdn-images-1.medium.com/max/400/0*0gSESdZm7330BNta.png','Metrics & testing',8,4,45),
 (2024,'04/04',"Mastering Interaction Design and Prototyping: Your Essential Guide to Product Management",'https://medium.com/@Muzeebdesign/mastering-interaction-design-and-prototyping-your-essential-guide-to-product-management-ac7b64b00e4c','https://cdn-images-1.medium.com/max/400/0*P24BI59qPVWTittD.gif','Prototyping',0,3,192),
 (2024,'04/03',"UX for PMs: The Secret to Building Products Users Love",'https://medium.com/@Muzeebdesign/ux-for-pms-the-secret-to-building-products-users-love-30996ff37c02','https://cdn-images-1.medium.com/max/400/0*4A3PcLvmMtRtpnbJ.png','Product',0,6,22),
 (2024,'03/03',"Making Customers Happy: Your Guide to the Kano Framework in Product Management",'https://medium.com/@Muzeebdesign/making-customers-happy-your-guide-to-the-kano-framework-in-product-management-b8d84e39101e','https://miro.medium.com/v2/resize:fill:208:136/0*53_N-BpNd7kOgay6.png','Product strategy',8,7,158),
 (2024,'02/21',"Choosing What’s Best: The Simple Guide to Feature Prioritization for Product Managers",'https://medium.com/@Muzeebdesign/choosing-whats-best-the-simple-guide-to-feature-prioritization-for-product-managers-12333490cd13','https://miro.medium.com/v2/resize:fill:208:136/0*RedwdM305vlFqjmx.png','Prioritization',0,7,355),
 (2024,'02/12',"Mastering Competitor Research: A Strategic Guide for Product Managers",'https://medium.com/@Muzeebdesign/mastering-competitor-research-a-strategic-guide-for-product-managers-f91622727434','https://miro.medium.com/v2/da:true/resize:fill:208:136/0*YD5ezBkV3jxRS1hj','Competitor research',0,5,203),
 (2023,'06/22',"User Observation in UX Research",'https://medium.com/@Muzeebdesign/user-observation-in-ux-research-c15357142f9b','https://miro.medium.com/v2/resize:fill:208:136/1*LgIVRE8N76wGkUrn6DcaxA.png','User research',36,5,1400),
 (2023,'03/27',"E-commerce “Search” button",'https://medium.com/@Muzeebdesign/e-commerce-search-button-4bee4bf3ba6a','https://miro.medium.com/v2/resize:fill:208:136/0*m9IEv0nzc3Kb_vO8.png','E-commerce',2,19,143),
]

PROJECTS = [  # (name, domain, desc, cover, url); same order as CASES in case_studies.py
 ('GoFully','chrome web store','A screenshot extension rebuilt around privacy: new brand, token system, 70+ screens and a site that says nothing leaves your device.','gofully','projects/gofully.html'),
 ('Jobly','chrome extension · web','Fresh jobs with real posting dates, plus apply assist, resume tailoring and cover letters. Founded, designed and built solo.','jobly','projects/jobly.html'),
 ('Assistantly','ai design qa','Clicks through every state of a web app and reports each design problem with its exact code fix, for about $0.30 a screen.','assistantly','projects/assistantly.html'),
 ('Careway Landing Page','healthcare · competitor audit','I audited a competitor’s oncology software page, found 13 problems, and designed a landing page that answers each one.','careway','projects/careway.html'),
 ('Petsy','e-commerce · 3d','A pet clothing store with a 3D fitting room, so a dog or cat tries the coat on before you buy.','petsy','projects/petsy.html'),
 ('Avatarly','figma plugin','Fills every avatar in a mockup from 12 collections, straight from the Figma menu, without breaking the layout.','avatarly','projects/avatarly.html'),
 ('Blobby','figma plugin','A blob generator where every blob stays editable: re-select it weeks later and keep tweaking.','blobby','projects/blobby.html'),
]


# (brand svg in assets/brands, name, what I use it for, tile colour, logo colour) — logos from Simple Icons (CC0)
TOOLS = [
 ('figma','Figma','design','#F24E1E','#fff'),
 ('claude','Claude Code','build + skills','#D97757','#fff'),
 ('jira','Jira','delivery','#0052CC','#fff'),
 ('slack','Slack','QA reports','#4A154B','#fff'),
 ('github','GitHub','side projects','#181717','#fff'),
 ('react','React','production UI','#20232A','#61DAFB'),
 ('tailwindcss','Tailwind CSS','styling','#0B1120','#38BDF8'),
 ('html5','HTML & CSS','prototypes in code','#E34F26','#fff'),
 ('googlechrome','Chrome','extensions','#1A73E8','#fff'),
 ('vercel','Vercel','shipping sites','#000000','#fff'),
 ('railway','Railway','hosting web apps','#13111C','#fff'),
 ('medium','Medium','writing','#000000','#fff'),
]
def tool(b, name, use, bg, fg):
    logo = open(os.path.join(OUT, 'assets', 'brands', b + '.svg')).read().strip().replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
    return f'<div class="tool"><span class="mk" style="background:{bg};color:{fg}">{logo}</span><b>{E(name)}</b><small>{E(use)}</small></div>'

# (file id, title, note, category); order = curated best first
WORKS = [
 ('21','Sales Dashboard','Metrics, graphs and sales at a glance','product'),
 ('01','Eve Wellness','Employee mental wellness app and flows','mobile'),
 ('46','E-sign Components','Signature field and signing components','product'),
 ('03','Pharmflow','Medical e-commerce app','mobile'),
 ('11','Affil.ai','Affiliate marketing dashboard','product'),
 ('47','Mental Health Landing','Wellness landing page','web'),
 ('8','We Forest','YC website redesign','web'),
 ('18','Math AI Tutor','Onboarding for an AI math tutor','mobile'),
 ('22','Analytics Dashboard','Data-heavy dashboard with clean panels','product'),
 ('7','Oodle','Dating app screens and matching','mobile'),
 ('04','Eve Landing Page','Landing page for the Eve platform','web'),
 ('41','Screenshot Redesign','Screenshot tool interface','product'),
 ('13','Rivet','YC devtools website redesign','web'),
 ('02','Eve Wellness App','Wellness tracking screens','mobile'),
 ('48','E-commerce Landing','Business landing page','web'),
 ('20','Pricing Modal','SaaS plan selection dialog','product'),
 ('12','Relaw','YC legal-tech website redesign','web'),
 ('23','Donation App','Light and dark theme exploration','mobile'),
 ('38','Component Library','Figma-ready UI components','product'),
 ('9','Mail Tester','YC website redesign','web'),
 ('19','Rosify','Dating app onboarding','mobile'),
 ('37','Chat UI','Message history and composer','product'),
 ('10','Healthtech Platform','YC healthtech website concept','web'),
 ('24','Math AI Workspace','Main screens of the AI math helper','mobile'),
 ('40','Upload Flow','File upload states','product'),
 ('44','Shopify Home Page','Store home page design','web'),
 ('36','Oodle Discovery','Match discovery and profiles','mobile'),
 ('35','LetMeGrab Login','E-commerce login and brand tokens','product'),
 ('49','How It Works · Eve AI','Explainer section','web'),
 ('06','Wellness Tracking','Employee wellness section','web'),
 ('15','RemoveBG','Background removal app','mobile'),
 ('43','Screenshot Redesign II','Alternate screenshot tool layout','product'),
 ('16','Eve Footer','Responsive footer','web'),
 ('17','Bundled','App screen and component layout','mobile'),
 ('32','Splash Screen','App intro screen','mobile'),
 ('33','Onboarding Flow','Step-by-step onboarding','mobile'),
 ('39','Landing Page','Marketing landing page','web'),
 ('05','Q Group','Logo and corporate identity','brand'),
 ('6','Pharmflow Brand','Guidelines, colour and assets','brand'),
 ('14','Click','Logo and identity concepts','brand'),
 ('27','Roomlocker','Corporate identity and logo','brand'),
 ('25','LinkedIn Cover','Feature banner design','social'),
 ('26','Instagram Templates','Post templates and styling','social'),
 ('29','Instagram Post','Brand messaging layout','social'),
 ('34','Social Post','Creative post template','social'),
 ('28','Thumbnail','Video and blog thumbnail','social'),
 ('30','Thumbnail Concept','Video preview layout','social'),
 ('31','Thumbnail Mockup','Alternate thumbnail options','social'),
]
CATS = [('all','All'),('product','Product UI'),('mobile','Mobile'),('web','Web'),('brand','Branding'),('social','Social')]

# Iconsax "Bulk" duotone icons (github.com/lusaxweb/iconsax), stored in assets/icons and inlined at build time.
# The 40%-opacity layer carries class="duo" so CSS can tint it.
ICON_DIR = os.path.join(OUT, 'assets', 'icons')
def svg(k, cls=''):
    s = open(os.path.join(ICON_DIR, k + '.svg')).read().strip()
    attrs = ' class="ico' + (' ' + cls if cls else '') + '" aria-hidden="true" focusable="false"'
    return s.replace('<svg ', '<svg' + attrs + ' ', 1)

NAV = [('index.html','home','Home'),('writing.html','writing','Writing'),('projects.html','projects','Projects'),('best-design.html','design','Best Design'),('skills.html','skills','AI Skills'),('journey.html','journey','Journey')]

SHORTCUT = {'home': 'H', 'writing': 'W', 'projects': 'P', 'design': 'D', 'skills': 'S', 'journey': 'J'}

def tip(label, keys):
    return f'<span class="tip" aria-hidden="true"><span class="tl">{E(label)}</span>' + ''.join(f'<kbd>{k}</kbd>' for k in keys) + '</span>'

def dock(cur):
    items = []
    for href, key, label in NAV:
        ac = ' aria-current="page"' if key == cur else ''
        t = tip(label, ['G', SHORTCUT[key]])
        attrs = f'href="{href}" aria-label="{label}" aria-keyshortcuts="G {SHORTCUT[key]}" data-key="{SHORTCUT[key].lower()}"{ac}'
        if key == 'home':
            items.append(f'<a {attrs} class="me"><canvas aria-hidden="true"></canvas>{t}</a><span class="sep"></span>')
        else:
            items.append(f'<a {attrs}>{svg(key)}{t}</a>')
    items.append('<span class="sep"></span>')
    items.append(f'<button class="snd" type="button" aria-pressed="true" aria-keyshortcuts="M">{svg("sound-on", "on")}{svg("sound-off", "off")}{tip("Sound", ["M"])}</button>')
    items.append(f'<button class="thm" type="button" aria-keyshortcuts="T">{svg("sun", "sun")}{svg("moon", "moon")}{tip("Theme", ["T"])}</button>')
    return '<nav class="dock" aria-label="Site">' + ''.join(items) + '</nav>'

FOOT = f'''<footer class="foot"><span>© 2026 Muzeeb Urrahaman</span><button class="copy" type="button" data-copy="{EMAIL}" data-done="Copied">{svg("copy", "i-copy")}{svg("tick", "i-tick")}<span class="lbl" aria-live="polite">Copy email</span></button><a href="https://www.linkedin.com/in/muzeeburrahaman" rel="noopener">LinkedIn ↗</a></footer>'''

# Home build animation: hide the page before first paint so finished content never flashes.
# Skipped with ?nobuild, under reduced motion, and after one full build per browser session (?build forces it).
PREBUILD = """<script>try{var q=location.search,d=document.documentElement;if(!/nobuild/.test(q)&&!matchMedia('(prefers-reduced-motion: reduce)').matches&&(/[?&]build/.test(q)||!sessionStorage.getItem('built'))){d.classList.add('pre-build');setTimeout(function(){if(!d.classList.contains('building'))d.classList.remove('pre-build')},5000)}}catch(e){}</script>"""
BUILD_JS = '\n<script src="assets/js/build-anim.js"></script>'

import hashlib
ASSET_V = hashlib.md5(b''.join(open(os.path.join(OUT, f), 'rb').read() for f in ('assets/css/site.css', 'assets/js/site.js', 'assets/js/portrait-dots.js'))).hexdigest()[:8]

def page(fname, key, title, desc, body, base=''):
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta name="theme-color" content="#f7f7f5" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f0f0e" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@200;400;500;600&family=Geist+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/css/site.css?v={ASSET_V}">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>{PREBUILD if key == 'home' else ''}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="page">
<main id="main" class="col">
{body}
{FOOT}
</main>
</div>
{dock(key)}
<script src="assets/js/portrait-dots.js?v={ASSET_V}"></script>
<script src="assets/js/site.js?v={ASSET_V}"></script>{BUILD_JS if key == 'home' else ''}
</body>
</html>
'''
    if base:  # pages in a subfolder: point local links and assets one level up
        doc = re.sub(r'(href|src|data-full)="(?!https?:|#|mailto:|data:|/)', lambda m: m.group(0) + base, doc)
    path = os.path.join(OUT, fname); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(doc)

def prow(name, where, desc, img, url):
    ext = url.startswith('http')
    pop = f' data-dialog="{url[1:]}" aria-haspopup="dialog"' if url.startswith('#') else ''
    return (f'<a class="prow" href="{E(url)}"{" rel=noopener" if ext else ""}{pop}>'
            f'<span class="icon"><img src="{img}" alt="" loading="lazy" decoding="async" width="44" height="44"></span>'
            f'<span><b>{E(name)}</b><span class="arr" aria-hidden="true">{"↗" if ext else ("+" if pop else "→")}</span><small>{E(where)}</small></span>'
            f'<p>{E(desc)}</p></a>')

TOPIC_TONE = {  # tag -> badge tint, shared by writing topics, case study tags and skills
 'Legal tech': 'slate', 'Legal SaaS': 'slate', 'AI': 'amber', 'AI tooling': 'amber', 'AI-assisted': 'amber',
 '0 → 1': 'sage', 'Design QA': 'sage', 'Chrome extension': 'rose', 'Brand + product': 'sand', 'Secure storage': 'plum',
 'User research': 'slate', 'Usability': 'slate', 'Metrics & testing': 'slate',
 'Human experience': 'plum', 'Psychology': 'plum',
 'AI concepts': 'amber', 'AI in design': 'amber', 'UI/UX': 'sage', 'Prototyping': 'sage',
 'Portfolio': 'sand', 'Case studies': 'sand', 'Product': 'rose',
 'Product strategy': 'rose', 'Prioritization': 'sand', 'Competitor research': 'slate', 'E-commerce': 'sage'}

def tag(text, tone=None):
    return f'<span class="badge topic {tone or TOPIC_TONE.get(text, "slate")}">{E(text)}</span>'

def stat_badge(claps, read, views):
    if views:
        short = f'{views / 1000:.1f}K'.replace('.0K', 'K') if views >= 1000 else str(views)
        return f'<span class="badge stat" title="{views:,} views on Medium">{svg("eye")}<span>{short}</span><span class="visually-hidden"> views</span></span>'
    if claps: return f'<span class="badge stat" title="{claps} claps on Medium">{svg("flash")}<span>{claps}</span><span class="visually-hidden"> claps</span></span>'
    return f'<span class="badge stat" title="{read} minute read">{svg("clock")}<span>{read} min</span><span class="visually-hidden"> read</span></span>'

def post(a, full_date=False):
    y, d, t, u, th, topic, claps, read, views = a
    date = f'{str(y)[2:]}/{d}' if full_date else d
    return (f'<a class="post" href="{E(u)}" rel="noopener"><span class="th"><img src="{E(th)}" alt="" loading="lazy" decoding="async" width="52" height="34"></span>'
            f'<span class="t">{E(t)}</span><span class="lead" aria-hidden="true"></span>'
            f'<span class="badges">{tag(topic)}{stat_badge(claps, read, views)}</span>'
            f'<span class="d">{date}</span></a>')

def work(w, i):
    fid, t, note, cat = w
    return (f'<button class="work" type="button" data-cat="{cat}" data-full="assets/img/work/{fid}.webp">'
            f'<span class="im"><img src="assets/img/work/{fid}-thumb.webp" alt="{E(t)}: {E(note)}" loading="{"eager" if i < 4 else "lazy"}" decoding="async" width="600" height="450"></span>'
            f'<b>{E(t)}</b><small>{E(note)}</small></button>')

# ---------------- HOME ----------------
home = f'''
<section class="hero" aria-label="Intro">
  <div>
    <h1>Muzeeb Urrahaman <span class="dot" role="img" title="Open to work" aria-label="Open to work"></span></h1>
    <p>I’m Muzeeb, a <span class="chip">product designer</span> and design engineer. I design the system, then ship it in code.</p>
    <p>For <strong>4.8+ years</strong> I’ve taken AI, legal and SaaS products from <span class="chip">0 → 1</span>, most recently 7 legal-tech products at Omnis AI.</p>
    <p>I was the only designer on most of my teams, so I’m used to making calls without a clear answer. I ask questions until the problem is clear, then move fast.</p>
    <p class="find">Find me on <a href="https://www.linkedin.com/in/muzeeburrahaman" rel="noopener">LinkedIn</a>, <a href="https://github.com/MUZEEBURRAHAMAN" rel="noopener">GitHub</a>, <a href="https://dribbble.com/Muzeeburrahaman" rel="noopener">Dribbble</a> and <a href="#" data-copy="{EMAIL}">{EMAIL}</a></p>
  </div>
  <div class="portrait" role="img" aria-label="Dot portrait of Muzeeb in a black cap. Move the pointer over it to scatter the dots."><canvas></canvas><span class="hint" aria-hidden="true"><span class="h-ptr">poke me</span><span class="h-tch">tap me</span></span></div>
</section>

<nav class="tiles" aria-label="Sections">
  <a class="tile" href="writing.html"><span class="ic">{svg('writing')}</span><b>Writing</b><small>{len(ARTICLES)} posts</small></a>
  <a class="tile" href="best-design.html"><span class="ic">{svg('design')}</span><b>Best Design</b><small>{len(WORKS)} works</small></a>
  <a class="tile" href="projects.html"><span class="ic">{svg('projects')}</span><b>Projects</b><small>{len(PROJECTS)} case studies</small></a>
</nav>

<section class="sec" aria-labelledby="h-proj">
  <div class="eyebrow" id="h-proj"><span class="n">01</span> Projects <a class="more" href="projects.html">View all {len(PROJECTS)} →</a></div>
  <div class="plist">{''.join(prow(n, w, d, f'assets/img/cover/{c}.webp', u) for n, w, d, c, u in PROJECTS[:2])}</div>
</section>

<section class="sec" aria-labelledby="h-exp">
  <div class="eyebrow" id="h-exp"><span class="n">02</span> Experience</div>
  <div class="rows">
    <div class="row"><div class="t"><b>Omnis AI</b><small>Product Designer / Design Engineer</small></div><span class="d">2024–2026</span></div>
    <div class="row"><div class="t"><b>LetMeGrab</b><small>UI/UX Designer & Researcher</small></div><span class="d">2023–2024</span></div>
    <div class="row"><div class="t"><b>Photoshooto</b><small>UI/UX Designer</small></div><span class="d">2022–2023</span></div>
    <div class="row"><div class="t"><b>EngineerHUB · Kartexa</b><small>Jr. UI/UX Designer · Design Intern</small></div><span class="d">2022</span></div>
  </div>
</section>

<section class="sec" aria-labelledby="h-wr">
  <div class="eyebrow" id="h-wr"><span class="n">03</span> Writing <a class="more" href="writing.html">View all {len(ARTICLES)} →</a></div>
  <div class="posts">{''.join(post(a, True) for a in ARTICLES[:5])}</div>
</section>

<section class="sec" aria-labelledby="h-bd">
  <div class="eyebrow" id="h-bd"><span class="n">04</span> Best Design <a class="more" href="best-design.html">View all {len(WORKS)} →</a></div>
  <div class="grid2">
    <a class="work" href="best-design.html"><span class="im"><img src="assets/img/work/01-thumb.webp" alt="Eve Wellness mobile app screens" loading="lazy" decoding="async" width="600" height="450"></span><b>Eve Wellness</b><small>Employee mental wellness app</small></a>
    <a class="work" href="best-design.html"><span class="im"><img src="assets/img/work/21-thumb.webp" alt="Sales dashboard design" loading="lazy" decoding="async" width="600" height="450"></span><b>Sales Dashboard</b><small>Metrics, graphs and sales</small></a>
  </div>
</section>

<section class="sec tools" aria-labelledby="h-tools">
  <div class="eyebrow" id="h-tools"><span class="n">05</span> Tools I live in <span class="nav"><button class="prev" type="button" aria-label="Previous tools" aria-controls="tool-track">{svg("prev")}</button><button class="next" type="button" aria-label="Next tools" aria-controls="tool-track">{svg("next")}</button></span></div>
  <div class="track" id="tool-track" tabindex="0" role="region" aria-label="Tools, scroll sideways">{''.join(tool(*t) for t in TOOLS)}</div>
</section>
'''
page('index.html','home','Muzeeb Urrahaman · Product Designer & Design Engineer','Product designer and design engineer with 4.8+ years shipping AI, legal and SaaS products from 0 to 1.',home)

# ---------------- WRITING ----------------
years = {}
for a in ARTICLES: years.setdefault(a[0], []).append(a)
wr = '<header class="pagehead"><div class="eyebrow"><span class="slash">//</span> Writing<h1 class="visually-hidden">Writing</h1> <a class="more" href="https://medium.com/@Muzeebdesign" rel="noopener">Medium ↗</a></div><p class="lede">Notes on usability, research and building products people use. All published on Medium.</p></header>'
for y in sorted(years, reverse=True):
    wr += f'<section class="year" aria-labelledby="y{y}"><span class="big" aria-hidden="true" data-y="{str(y)[2:]}"></span><h2 id="y{y}" class="badge stat year-badge">{y}</h2><div class="posts">{"".join(post(a) for a in years[y])}</div></section>'
page('writing.html','writing','Writing · Muzeeb Urrahaman','Articles by Muzeeb Urrahaman on usability, research and product design, published on Medium.',wr)

# ---------------- PROJECTS ----------------
pr = f'''<header class="pagehead"><div class="eyebrow"><span class="slash">//</span> Projects<h1 class="visually-hidden">Projects</h1></div><p class="lede">Four products I designed end to end: two browser tools, an AI design-QA engine and a healthcare landing page. Each one opens the full case study.</p></header>
<div class="plist">{''.join(prow(n, w, d, f'assets/img/cover/{c}.webp', u) for n, w, d, c, u in PROJECTS)}</div>'''
page('projects.html','projects','Projects · Muzeeb Urrahaman','Four product design case studies: GoFully, Jobly, Assistantly and the Careway landing page.',pr)

# ---------------- BEST DESIGN ----------------
counts = {k: sum(1 for w in WORKS if w[3] == k) for k, _ in CATS}; counts['all'] = len(WORKS)
chips = ''.join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{l}<span>{counts[k]}</span></button>' for k, l in CATS)
bd = f'''<header class="pagehead"><div class="eyebrow"><span class="slash">//</span> Best Design<h1 class="visually-hidden">Best Design</h1></div><p class="lede">{len(WORKS)} visual works: product UI, dashboards, mobile apps, landing pages and branding. Click any piece to see it full size.</p>
<div class="chips" role="group" aria-label="Filter by type">{chips}</div></header>
<div class="grid2 works">{''.join(work(w, i) for i, w in enumerate(WORKS))}</div>'''
page('best-design.html','design','Best Design · Muzeeb Urrahaman','A visual archive of product UI, dashboards, mobile apps, landing pages and branding by Muzeeb Urrahaman.',bd)

# ---------------- JOURNEY ----------------
jr = f'''<header class="pagehead"><div class="eyebrow"><span class="slash">//</span> Journey<h1 class="visually-hidden">Journey</h1> <a class="more dl" href="assets/files/Muzeeb-Urrahaman-Resume.pdf">{svg("download")}Download PDF</a></div>
<p class="lede">Product Designer & Design Engineer. AI product design, SaaS and design systems. Based in Uttar Pradesh, India, open to remote and relocation.</p></header>
<div class="stats"><div><b>4.8+</b><small>Years designing</small></div><div><b>7</b><small>AI products shipped</small></div><div><b>40%</b><small>Fewer UI inconsistencies</small></div></div>
<section class="sec" aria-labelledby="h-jx"><div class="eyebrow" id="h-jx"><span class="n">01</span> Experience</div>
<div class="rows">
 <div class="row"><div class="t"><b>Omnis AI LLC</b><small>Product Designer / Design Engineer · Texas, remote</small><ul>
  <li>Led end-to-end design across 7 AI legal-tech products, from research to prototypes, with founders and engineering.</li>
  <li>Built the Omnis Design System: one component library and token set. UI inconsistencies dropped 40% and feature design went from days to hours.</li>
  <li>Cut legal case-management workflows from 8 steps to 3 and raised internal efficiency 25%.</li>
  <li>Built AI design-QA automation that replaced 4+ hours of manual review per sprint.</li></ul></div><span class="d">12/24–07/26</span></div>
 <div class="row"><div class="t"><b>LetMeGrab</b><small>UI/UX Designer & Researcher · Surat, on-site</small><ul>
  <li>Owned UX across seller, customer and admin platforms, from onboarding to checkout.</li>
  <li>Redesigned seller onboarding and checkout: conversion up 18%, drop-off down 22%.</li>
  <li>Set up reusable component libraries across 3 platform verticals.</li></ul></div><span class="d">01/23–12/24</span></div>
 <div class="row"><div class="t"><b>Photoshooto · EngineerHUB · Kartexa</b><small>UI/UX Designer · Jr. UI/UX Designer · Design Intern</small><ul>
  <li>Web and mobile experiences across SaaS, e-commerce and consumer products.</li></ul></div><span class="d">2022–2023</span></div>
</div></section>
<section class="sec" aria-labelledby="h-js"><div class="eyebrow" id="h-js"><span class="n">02</span> Skills</div>
<div class="tags">{tag('UX strategy','slate')}{tag('Interaction design','sage')}{tag('Design systems','sage')}{tag('Prototyping','sage')}{tag('User research','slate')}{tag('Front-end (HTML, CSS, React)','plum')}{tag('AI-assisted workflows','amber')}{tag('0 → 1 products','sand')}</div></section>
<section class="sec" aria-labelledby="h-jq"><div class="eyebrow" id="h-jq"><span class="n">03</span> Kind words</div>
<div class="quotes">
 <blockquote class="quote"><p>“Muzeeb’s creative vision is top-notch. He keeps teams aligned and infuses craft into every product detail.”</p><footer><img src="assets/img/people/danielle-caldwell.webp" alt="" width="32" height="32" loading="lazy"><span>Danielle Caldwell<small>Product Design Lead, PatientPoint</small></span></footer></blockquote>
 <blockquote class="quote"><p>“Our speed is intense and every design challenge is met with relentless craft.”</p><footer><img src="assets/img/people/nicoletta-pizzocheri.webp" alt="" width="32" height="32" loading="lazy"><span>Nicoletta Pizzocheri<small>Lead Product Designer, Femme Palette</small></span></footer></blockquote>
</div></section>'''
page('journey.html','journey','Journey · Muzeeb Urrahaman','Experience, skills and résumé of Muzeeb Urrahaman, product designer and design engineer.',jr)

# ---------------- CASE STUDIES ----------------
from case_studies import CASES

def md(t):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', E(t))

def img_size(path):
    """Width and height of a WebP, read from its header."""
    b = open(os.path.join(OUT, path), 'rb').read(40)
    if b[12:16] == b'VP8X': return 1 + int.from_bytes(b[24:27], 'little'), 1 + int.from_bytes(b[27:30], 'little')
    if b[12:16] == b'VP8 ': return int.from_bytes(b[26:28], 'little') & 0x3fff, int.from_bytes(b[28:30], 'little') & 0x3fff
    v = int.from_bytes(b[21:25], 'little'); return (v & 0x3fff) + 1, ((v >> 14) & 0x3fff) + 1

def img_kind(w, h):
    r = h / w
    if 1.9 <= r <= 2.4: return 'phone'   # mobile screens: shown in a phone-sized frame
    if r > 1.6: return 'long'            # full-page captures: cropped preview, full size on click
    if r > 1.1: return 'tall'            # portrait panels: narrower so they don't dominate
    return 'wide'

def cs_img(slug, f, cap, eager=False):
    src = f'assets/img/cs/{slug}/{f}'; w, h = img_size(src); kind = img_kind(w, h)
    more = '<span class="more-hint" aria-hidden="true">View full page</span>' if kind == 'long' else ''
    return (f'<figure class="cs-fig {kind}"><button type="button" class="zoom" data-full="{src}" aria-label="Open image full size">'
            f'<img src="{src}" alt="{E(cap)}" width="{w}" height="{h}" loading="{"eager" if eager else "lazy"}" decoding="async">{more}</button>'
            f'<figcaption>{md(cap)}</figcaption></figure>')

def pill(kind, text): return f'<span class="cs-pill {kind}">{E(text)}</span>'

def block(slug, b):
    k = b[0]
    if k == 'p': return f'<p class="cs-p">{md(b[1])}</p>'
    if k == 'lead': return f'<p class="cs-lead">{md(b[1])}</p>'
    if k == 'list': return '<ul class="cs-list">' + ''.join(f'<li>{md(i)}</li>' for i in b[1]) + '</ul>'
    if k == 'flow': return '<div class="cs-flow">' + ''.join(f'<span>{md(i)}</span>' for i in b[1]) + '</div>'
    if k == 'quote': return f'<p class="cs-quote">{md(b[1])}</p>'
    if k == 'callout': return f'<p class="cs-callout"><small>{E(b[1])}</small>{md(b[2])}</p>'
    if k == 'honest': return f'<p class="cs-honest"><strong>{E(b[1])}</strong> {md(b[2])}</p>'
    if k == 'rows':
        labels = b[2]; out = []
        for n, it in enumerate(b[1], 1):
            body = f'<h3>{md(it[0])}</h3>'
            if len(it) == 3 and labels:
                body += f'<p class="cs-p"><small>{labels[0]}</small>{md(it[1])}</p><p><small>{labels[1]}</small>{md(it[2])}</p>'
            else:
                body += f'<p class="cs-p">{md(it[1])}</p>'
            out.append(f'<div class="cs-row"><span>{n:02d}</span><div>{body}</div></div>')
        return '<div class="cs-rows">' + ''.join(out) + '</div>'
    if k == 'panels':
        return f'<div class="cs-panels n{len(b[1])}">' + ''.join(
            f'<div class="cs-panel"><h3>{pill(pk, pt)} {E(t)}</h3><ul>' + ''.join(f'<li>{md(i)}</li>' for i in items) + '</ul></div>'
            for pk, pt, t, items in b[1]) + '</div>'
    if k == 'cards':
        return '<div class="cs-cards">' + ''.join(f'<div><b>{E(t)}</b><small>{md(x)}</small></div>' for t, x in b[1]) + '</div>'
    if k == 'stats':
        return '<div class="stats cs-stats">' + ''.join(f'<div><b>{E(big)}</b><em>{E(l)}</em><small>{md(sub)}</small></div>' for big, l, sub in b[1]) + '</div>'
    if k == 'table':
        head = ''.join(f'<th scope="col">{E(h)}</th>' for h in b[1])
        rows = ''.join('<tr>' + ''.join(f'<td>{md(c)}</td>' for c in r) + '</tr>' for r in b[2])
        return f'<div class="cs-tbl" tabindex="0" role="region" aria-label="Table: {E(" vs ".join(b[1]))}"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    if k == 'tldr':
        return '<div class="cs-tldr">' + ''.join(f'<div><small>{pill(pk, l)}</small><p>{md(t)}</p></div>' for pk, l, t in b[1]) + '</div>'
    if k == 'iters':
        out = []
        for pk, pt, t, x, q in b[1]:
            out.append(f'<div class="cs-iter{" win" if pk == "good" else ""}"><header>{pill(pk, pt)}<h3>{E(t)}</h3></header><p class="cs-p">{md(x)}</p>'
                       + (f'<q>{E(q)}</q>' if q else '') + '</div>')
        return '<div class="cs-iters">' + ''.join(out) + '</div>'
    if k == 'fig': return cs_img(slug, b[1], b[2])
    if k == 'figs':
        kinds = {img_kind(*img_size(f'assets/img/cs/{slug}/{f}')) for f, _ in b[1]}
        # matching shapes sit side by side; mixed shapes (wide next to a long capture) stack full width
        cls = ' phones' if kinds == {'phone'} else (' stack' if len(kinds) > 1 else '')
        return f'<div class="cs-figs n{len(b[1])}{cls}">' + ''.join(cs_img(slug, f, c) for f, c in b[1]) + '</div>'
    if k == 'cmp':
        _, bf, af, bl, al = b
        aw, ah = img_size(f'assets/img/cs/{slug}/{af}')
        return (f'<figure class="cs-cmp"><div class="frame"><img src="assets/img/cs/{slug}/{af}" alt="{E(al)}" width="{aw}" height="{ah}" loading="lazy" decoding="async">'
                f'<div class="before"><img src="assets/img/cs/{slug}/{bf}" alt="{E(bl)}" loading="lazy" decoding="async"></div>'
                f'<span class="tag l">{E(bl)}</span><span class="tag r">{E(al)}</span><span class="handle" aria-hidden="true"></span></div>'
                f'<input type="range" min="0" max="100" value="50" aria-label="Drag to compare {E(bl)} and {E(al)}"></figure>')
    if k == 'details':
        return f'<details class="cs-details"><summary>{E(b[1])}</summary><ul>' + ''.join(f'<li>{md(i)}</li>' for i in b[2]) + '</ul></details>'
    if k == 'links':
        return '<div class="cs-links">' + ''.join(
            f'<a class="btn" href="{E(u)}"' + (' rel="noopener" target="_blank"' if u.startswith('http') else '')
            + f'>{E(l)} {"↗" if u.startswith("http") or u.endswith((".html", ".md")) else "↓"}</a>' for l, u in b[1]) + '</div>'
    if k == 'feature':
        # one feature: a label, a short title, one or two lines, then the UI large
        _, label, t, text, files = b
        files = files if isinstance(files, list) else [files]
        imgs = ''.join(cs_img(slug, f, f'{t}: {label}') if isinstance(f, str) else cs_img(slug, f[0], f[1]) for f in files)
        return (f'<div class="cs-feature"><div class="cs-feature-txt"><small>{E(label)}</small><h3>{md(t)}</h3><p class="cs-p">{md(text)}</p></div>'
                f'<div class="cs-feature-img n{len(files)}">{imgs}</div></div>')
    if k == 'chips':
        return '<div class="cs-chips">' + ''.join(f'<span>{E(x)}</span>' for x in b[1]) + '</div>'
    if k == 'pipeline':
        # same markup as the user-flow skill: label lozenge, outcome title, stages, optional loop
        _, kind, label, t, stages, ret = (list(b) + [None])[:6]
        st = '<div class="flow-connector" aria-hidden="true"></div>'.join(f'<div class="flow-stage">{md(x)}</div>' for x in stages)
        r = f'<div class="flow-return"><span class="flow-return-label">{E(ret)}</span></div>' if ret else ''
        return (f'<section class="flow-diagram flow-diagram--{kind}" aria-label="{E(label)}"><div class="flow-label"><span class="lozenge">{E(label)}</span>'
                f'<span class="flow-title">{md(t)}</span></div><div class="flow-pipeline">{st}</div>{r}</section>')
    if k == 'gallery':
        _, items = b[:2]; cols = b[2] if len(b) > 2 else 3
        return f'<div class="cs-gallery c{cols}">' + ''.join(cs_img(slug, f, c) for f, c in items) + '</div>'
    if k == 'browser':
        # a full-page capture inside a browser frame that scrolls in place
        _, f, url, cap = b; src = f'assets/img/cs/{slug}/{f}'; w, h = img_size(src)
        return (f'<figure class="cs-browser"><div class="bar"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="url">{E(url)}</span>'
                f'<span class="hint" aria-hidden="true">Scroll inside ↓</span></div>'
                f'<div class="view" tabindex="0" role="region" aria-label="Scrollable full-page preview: {E(url)}">'
                f'<img src="{src}" alt="{E(cap)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
                f'<figcaption>{md(cap)}</figcaption></figure>')
    if k == 'findings':
        out = []
        for n, sev, t, ev, fix in b[1]:
            mark = f'<span class="cs-mark">{n}</span>' if isinstance(n, int) else '<span class="cs-mark none">–</span>'
            out.append(f'<div class="cs-find">{mark}<div><h3>{pill({"Blocker": "bad", "Major": "mid"}.get(sev, "good"), sev)} {md(t)}</h3>'
                       f'<p class="cs-p"><small>What I found</small>{md(ev)}</p><p class="cs-p"><small>Careway</small>{md(fix)}</p></div></div>')
        return '<div class="cs-finds">' + ''.join(out) + '</div>'
    raise ValueError('unknown block ' + k)

def case_page(i, c):
    slug = c['slug']
    secs = list(c['sections']) + ([('Questions I expect', None, None)] if c.get('faq') else [])
    toc = ''.join(f'<a href="#s{n}"><span>{n:02d}</span>{E(t)}</a>' for n, (t, _, _) in enumerate(secs, 1))
    tldr_html = ('<section class="sec" aria-label="Summary"><div class="eyebrow">TL;DR</div><div class="cs-tldr">'
                 + ''.join(f'<div><small>{E(k)}</small><p>{md(v)}</p></div>' for k, v in c['tldr']) + '</div></section>') if c.get('tldr') else ''
    body = [f'''<header class="cs-head">
  <nav class="crumb" aria-label="Breadcrumb"><a href="projects.html">← Projects</a><span aria-hidden="true">/</span><span aria-current="page">{E(c["name"])}</span></nav>
  <div class="eyebrow"><span class="slash">//</span> Case study {"".join(tag(t) for t in c["tags"])}<span class="more">{c["read"]} min read</span></div>
  <h1 class="cs-title">{E(c["title"])}</h1>
  <p class="cs-lead">{md(c["lede"])}</p>
</header>
<dl class="cs-meta">{"".join(f'<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>' for k, v in c["meta"])}</dl>
<figure class="cs-fig cs-hero"><button type="button" class="zoom" data-full="{c["cover"]}" aria-label="Open cover image full size"><img src="{c["cover"]}" alt="{E(c["name"])} cover" width="{img_size(c["cover"])[0]}" height="{img_size(c["cover"])[1]}" decoding="async" fetchpriority="high"></button></figure>
{block(slug, ('stats', c['stats'])) if c.get('stats') else ''}
{tldr_html}
{block(slug, ('links', c['links'])) if c.get('links') else ''}
{'' if c.get('compact') else f'<nav class="sec" aria-label="Contents"><div class="eyebrow">Contents</div><div class="cs-toc">{toc}</div></nav>'}''']
    for n, (eb, h, blocks) in enumerate(c['sections'], 1):
        body.append(f'<section class="sec cs-sec" id="s{n}" aria-labelledby="h{n}"><div class="eyebrow"><span class="n">{n:02d}</span> {E(eb)}</div>'
                    f'<h2 class="cs-h" id="h{n}">{E(h)}</h2>' + ''.join(block(slug, b) for b in blocks) + '</section>')
    if c.get('faq'):
        n = len(secs)
        body.append(f'<section class="sec cs-sec" id="s{n}" aria-labelledby="h{n}"><div class="eyebrow"><span class="n">{n:02d}</span> Questions I expect</div>'
                    f'<h2 class="cs-h visually-hidden" id="h{n}">Questions I expect</h2><div class="cs-faq">'
                    + ''.join(f'<details{" open" if j == 0 else ""}><summary>{E(q)}</summary><p>{md(a)}</p></details>' for j, (q, a) in enumerate(c['faq'])) + '</div></section>')
    nxt = [PROJECTS[(i + k) % len(PROJECTS)] for k in (1, 2)]
    body.append('<section class="sec"><div class="eyebrow">Next case study <a class="more" href="projects.html">All projects →</a></div><div class="plist">'
                + ''.join(prow(nm, w, d, f'assets/img/cover/{cv}.webp', u) for nm, w, d, cv, u in nxt) + '</div></section>')
    body.append('<div class="cs-progress" aria-hidden="true"><b></b></div>')
    page(f'projects/{slug}.html', 'projects', f'{c["name"]} · Case Study · Muzeeb Urrahaman', re.sub(r'\*\*', '', c['lede'])[:155], '\n'.join(body), base='../')

for i, c in enumerate(CASES):
    case_page(i, c)

# ---------------- AI SKILLS ----------------
# Skill sources live in ../claude-skills (published at github.com/MUZEEBURRAHAMAN/claude-skills).
# The build copies each SKILL.md and a zipped bundle into assets/skills/<slug>/ so the site serves them too.
import zipfile, shutil, html as _html
SKILL_SRC = os.path.join(os.path.dirname(OUT), 'claude-skills')
SKILL_REPO = 'https://github.com/MUZEEBURRAHAMAN/claude-skills'
SKILL_RAW = 'https://raw.githubusercontent.com/MUZEEBURRAHAMAN/claude-skills/main'
from skills_meta import SKILLS
import json as _json
_WS = os.path.join(os.path.dirname(OUT), 'claude-skills-workspace', 'iteration-1')
_CASE = {}
for _sk in SKILLS:
    _ev = os.path.join(SKILL_SRC, _sk['slug'], 'evals')
    if os.path.isdir(_ev):
        for _c in sorted(os.listdir(_ev)):
            def _score(cfg, c=_c):
                g = os.path.join(_WS, c, cfg, 'grading.json')
                if not os.path.exists(g): return None
                x = _json.load(open(g))['summary']; return x['passed'], x['total']
            w, wo = _score('with_skill'), _score('without_skill')
            if w and wo and not _sk.get('tested'):
                _sk['tested'] = dict(**{'with': f'{w[0]}/{w[1]}', 'without': f'{wo[0]}/{wo[1]}'}, checks=str(w[1]),
                    note=f'One realistic task, run twice: once with the skill and once with plain Claude. A grader checked both against {w[1]} written checks. Test case: `{_c}`.')

def bundle_skill(slug):
    """Copy SKILL.md and zip the whole skill folder (without tests) into assets/skills/<slug>/."""
    src, dst = os.path.join(SKILL_SRC, slug), os.path.join(OUT, 'assets', 'skills', slug)
    os.makedirs(dst, exist_ok=True)
    shutil.copy(os.path.join(src, 'SKILL.md'), os.path.join(dst, 'SKILL.md'))
    with zipfile.ZipFile(os.path.join(dst, f'{slug}.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(src):
            dirs[:] = [d for d in dirs if d != 'evals']
            for f in files:
                if f == '.DS_Store': continue
                full = os.path.join(root, f)
                z.write(full, os.path.join(slug, os.path.relpath(full, src)))
    return open(os.path.join(src, 'SKILL.md')).read()

def skill_row(k):
    return (f'<div class="sk-row"><span class="sk-ic">{svg(k["icon"])}</span>'
            f'<a class="sk-main" href="skills/{k["slug"]}.html"><b>{E(k["name"])}</b><small>{E(k["tagline"])}</small></a>'
            f'<span class="sk-meta">{tag(k["category"], k["tone"])}<span class="badge stat">{E(k["version"])}</span></span>'
            f'<span class="sk-act"><a class="btn sm" href="skills/{k["slug"]}.html">View</a>'
            f'<a class="btn sm" href="assets/skills/{k["slug"]}/{k["slug"]}.zip" download>{svg("download")}Download</a></span></div>')

sk = f'''<header class="pagehead"><div class="eyebrow"><span class="slash">//</span> AI Skills <a class="more" href="{SKILL_REPO}" rel="noopener">GitHub ↗</a><h1 class="visually-hidden">AI Skills</h1></div>
<p class="lede">Claude skills I built from the reviews and checks I repeat. Each one is tested against a baseline, free to download, and installs in one command.</p></header>
<div class="sk-list">{''.join(skill_row(k) for k in SKILLS)}</div>
<section class="sec" aria-labelledby="h-how"><div class="eyebrow" id="h-how"><span class="n">?</span> How to install</div>
<div class="cs-rows"><div class="cs-row"><span>01</span><div><h3>Claude Code</h3><p class="cs-p">Open a skill and copy its install command. It drops the skill into <code>~/.claude/skills/</code>.</p></div></div>
<div class="cs-row"><span>02</span><div><h3>Claude.ai</h3><p class="cs-p">Download the .zip and upload it under Settings → Capabilities → Skills.</p></div></div>
<div class="cs-row"><span>03</span><div><h3>Use it</h3><p class="cs-p">Ask in plain words. Each skill page lists phrases that switch it on.</p></div></div></div></section>'''
page('skills.html','skills','AI Skills · Muzeeb Urrahaman','Free, tested Claude skills by Muzeeb Urrahaman: honest design review, UX audit, portfolio review, antislop for copy and UI, fact checking, user flows and brand kits.', sk)

def flow_html(f):
    def st(x):
        if isinstance(x, tuple):
            return f'<div class="flow-stage-wrap"><div class="flow-stage">{E(x[0])}</div><div class="flow-branch">{E(x[1])}</div></div>'
        return f'<div class="flow-stage">{E(x)}</div>'
    stages = '<div class="flow-connector" aria-hidden="true"></div>'.join(st(x) for x in f['stages'])
    ret = f'<div class="flow-return"><span class="flow-return-label">{E(f["ret"])}</span></div>' if f.get('ret') else ''
    return (f'<section class="flow-diagram flow-diagram--{f["kind"]}" aria-label="{E(f["label"])}"><div class="flow-label"><span class="lozenge">{E(f["label"])}</span>'
            f'<span class="flow-title">{E(f["title"])}</span></div><div class="flow-pipeline">{stages}</div>{ret}</section>')

def demo_html(k):
    d = k.get('demo')
    if not d: return ''
    if d['type'] == 'flows':
        body = ''.join(flow_html(f) for f in d['flows'])
    elif d['type'] == 'highlight':
        body = (f'<div class="sk-demo-tabs" role="group" aria-label="Demo view"><button type="button" class="chip-btn" aria-pressed="false" data-hl>Highlight what it catches</button></div>'
                f'<div class="sk-demo-text">{d["html"]}</div>')
    else:
        body = f'<pre class="sk-demo-pre">{E(d["text"])}</pre>'
    cap = f'<p class="sk-demo-cap">{md(d["caption"])}</p>' if d.get('caption') else ''
    return f'<section class="sec" aria-labelledby="h-demo"><div class="eyebrow" id="h-demo"><span class="n">✦</span> {E(d["title"])}</div>{body}{cap}</section>'

def skill_page(i, k):
    slug = k['slug']; text = bundle_skill(slug)
    install = f'mkdir -p ~/.claude/skills && curl -fsSL {SKILL_REPO}/raw/main/dist/{slug}.zip -o /tmp/{slug}.zip && unzip -oq /tmp/{slug}.zip -d ~/.claude/skills/'
    meta = [('Level', k['level']), ('Saves', k['saves']), ('Version', k['version']), ('Updated', k['updated']), ('Available in', 'Claude Code · Claude.ai')]
    tested = k.get('tested')
    test_html = ''
    if tested:
        test_html = (f'<section class="sec" aria-labelledby="h-test"><div class="eyebrow" id="h-test"><span class="n">✓</span> Tested</div>'
                     f'<div class="stats"><div><b>{E(tested["with"])}</b><small>Checks passed with the skill</small></div><div><b>{E(tested["without"])}</b><small>Same task without it</small></div><div><b>{E(tested["checks"])}</b><small>Checks in the test</small></div></div>'
                     f'<p class="cs-p">{md(tested["note"])}</p></section>')
    others = [SKILLS[(i + n) % len(SKILLS)] for n in (1, 2)]
    body = f'''<header class="cs-head">
<nav class="crumb" aria-label="Breadcrumb"><a href="skills.html">← AI Skills</a><span aria-hidden="true">/</span><span aria-current="page">{E(k["name"])}</span></nav>
<div class="eyebrow"><span class="slash">//</span> Claude skill {tag(k["category"], k["tone"])}</div>
<h1 class="cs-title">{E(k["name"])}</h1><p class="cs-lead">{md(k["description"])}</p>
<div class="sk-links"><a class="btn" href="assets/skills/{slug}/{slug}.zip" download>{svg("download")}Download .zip</a><a class="btn" href="#skill-md">View SKILL.md</a><a class="btn" href="{SKILL_REPO}/tree/main/{slug}" rel="noopener" target="_blank">GitHub ↗</a></div>
</header>
<dl class="cs-meta sk-dl">{"".join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a, b in meta)}</dl>
<section class="sec" aria-labelledby="h-who"><div class="eyebrow" id="h-who"><span class="n">01</span> Who it is for</div><p class="cs-lead">{E(k["who"])}</p></section>
<section class="sec" aria-labelledby="h-use"><div class="eyebrow" id="h-use"><span class="n">02</span> Use cases</div><ul class="cs-list">{"".join(f"<li>{md(u)}</li>" for u in k["uses"])}</ul></section>
<section class="sec" aria-labelledby="h-say"><div class="eyebrow" id="h-say"><span class="n">03</span> Say this to activate it</div>
<div class="sk-says">{"".join(f'<button type="button" class="sk-say" data-copy="{E(t)}" data-done="Copied">“{E(t)}”</button>' for t in k["triggers"])}</div></section>
{demo_html(k)}
<section class="sec" aria-labelledby="h-inst"><div class="eyebrow" id="h-inst"><span class="n">04</span> Install</div>
<div class="sk-code"><pre><code>{E(install)}</code></pre><button type="button" class="btn sm" data-copy="{E(install)}" data-done="Copied">{svg("copy")}<span class="lbl">Copy</span></button></div>
<p class="cs-p">The command downloads the skill and unpacks it into <code>~/.claude/skills/</code>. No terminal? Download the .zip and upload it in Claude.ai under Settings → Capabilities → Skills.</p></section>
{test_html}
<section class="sec" id="skill-md" aria-labelledby="h-md"><div class="eyebrow" id="h-md"><span class="n">05</span> SKILL.md
<span class="more sk-md-act"><button type="button" class="btn sm" data-copy-from="md-{slug}" data-done="Copied">{svg("copy")}<span class="lbl">Copy</span></button><a class="btn sm" href="assets/skills/{slug}/SKILL.md" download="SKILL.md">{svg("download")}Download</a></span></div>
<pre class="sk-md" id="md-{slug}" tabindex="0">{E(text)}</pre></section>
<section class="sec"><div class="eyebrow">More skills <a class="more" href="skills.html">All skills →</a></div><div class="sk-list">{"".join(skill_row(o) for o in others)}</div></section>'''
    page(f'skills/{slug}.html', 'skills', f'{k["name"]} · Claude Skill · Muzeeb Urrahaman', k['tagline'], body, base='../')


for i, k in enumerate(SKILLS):
    skill_page(i, k)

print('built', sorted(f for f in os.listdir(OUT) if f.endswith('.html')), sorted(os.listdir(os.path.join(OUT, 'projects'))))

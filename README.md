# Muzeeb Urrahaman · Portfolio

Static site: plain HTML, one stylesheet, one script. No framework, no build dependencies beyond Python 3.

## Pages

| File | Page |
|---|---|
| `index.html` | Home |
| `writing.html` | Writing (Medium articles) |
| `projects.html` | Projects list |
| `projects/<slug>.html` | 4 case studies: GoFully, Jobly, Assistantly, Careway |
| `best-design.html` | Best Design gallery |
| `skills.html` | AI Skills (Claude skills, coming soon) |
| `journey.html` | Journey (résumé) |

## Editing content

All pages are generated. Edit the data, then rebuild:

```bash
python3 scripts/build.py
```

- `scripts/build.py`: articles, projects, AI skills, Best Design works, tools, and every page layout.
- `scripts/case_studies.py`: case study text and images (block guide at the top of the file).

Articles take `(year, date, title, url, thumb, topic, claps, read minutes, views)`. Views come from medium.com/me/stats; when set, they replace the claps badge.

## Assets

- `assets/css/site.css`, `assets/js/site.js`, `assets/js/portrait-dots.js` (the dot portrait grid)
- `assets/icons/`: Iconsax Bulk icons (duotone), inlined at build time
- `assets/brands/`: tool logos from Simple Icons (CC0)
- `assets/img/`: covers, case study images, Best Design works

## Preview and deploy

```bash
python3 -m http.server 5179 --directory site
```

Deploy the `site/` folder as-is to any static host (Vercel, Netlify, GitHub Pages).

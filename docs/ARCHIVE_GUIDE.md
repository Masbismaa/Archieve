# Archive 4D-42-50: build notes

How the profile is put together, how to run and change it, and what still needs your input.

## 1. Creative direction

A working archive, not a showcase. The visitor opens a read-only file on a developer and finds records: techniques with evidence, missions with status, a training log, and the security rules that are applied in practice.

- **Tone.** Short sentences, specific nouns, a little dry humour ("Nobody here is pretending it has been ten"). No claims that the history cannot back up.
- **World.** Shinobi vocabulary only where it maps to something real: *techniques* are tools with evidence, *missions* are projects, *sealing arts* are security controls, *chakra flow* is live GitHub activity. There are no characters, clans or franchise references.
- **Japanese type.** One kanji per chapter, used as a seal, and each one states its meaning (記 record, 術 technique, 任 mission, 修 practice, 封 seal, 流 flow, 問 to ask, 信 message). There is no other decorative Japanese.

## 2. Information architecture

| Order | Chapter | Question it answers | README | Website |
|---|---|---|---|---|
| 00 | Gate | Who is this, what are they doing now | header SVG | typed access log, ledger |
| 01 | Dossier | How does this person work | terminal block and two paragraphs | prose and record sheet |
| 02 | Techniques | What can they actually use, and how do we know | tier table, inspect details | tier legend, inspector panel |
| 03 | Missions | What did they build | M-01 card, M-01 file, archive table | expandable files, request-flow diagram |
| 04 | Training log | How did they get here | path SVG and table | path that fills as you read |
| 05 | Sealing arts | How do they treat security | status table | status table |
| 06 | Chakra flow | Are they active | live cards from the workflow | the same cards |
| 07 | Terminal | Can I ask it things | static console block | working command line |
| 08 | Signal | How do I reach them | contact table | contact with copy button |
| -- | Sealed | Reward for exploring | `∴` details, raw-file comment | `ls -a`, `cat .scroll`, `seal` |

## 3. Visual system

| Token | Value | Use |
|---|---|---|
| ink-0 | `#0b0c0f` | page ground |
| ink-1 | `#121419` | panels |
| ink-2 | `#151b27` | selected rows (dark navy) |
| parchment | `#d9cfb8` | headings, seals text |
| paper | `#ece7dc` | body text |
| crimson | `#8e1b24` | seals, primary actions |
| red | `#c24b43` | IDs, selected marker |
| ember | `#d0703a` | only for live or current things (status, current stage) |
| ok | `#9fb49a` | "implemented" |

- **Type.** Shippori Mincho B1 for display, JetBrains Mono for records and metadata, IBM Plex Sans for reading.
- **Texture.** One faint 48 px terminal grid and a vignette. No particles.
- **Motion.** Each animation has a job:
  - access log typing and name decode, once;
  - seal stamp when a chapter enters;
  - inspector scan when you pick a technique;
  - mission file unroll;
  - training path fill;
  - ember pulse on live status;
  - flowing dashes on the request path.

  All of it is switched off by `prefers-reduced-motion`.

## 4 and 5. Files

```text
README.md                      profile README (GitHub renders this)
index.html                     headquarters website (GitHub Pages)
css/tokens.css                 colour, type, spacing tokens
css/base.css                   reset, body, focus, reduced motion
css/layout.css                 top bar, index rail, reading column
css/components.css             chapters, techniques, missions, path, table, terminal
js/main.js                     boot order
js/data/archive.js             ALL content and statuses (edit this)
js/ui/dom.js                   small helpers
js/ui/chapters.js              seals, quotes, index progress, mobile menu
js/ui/gate.js                  opening log and name decode
js/ui/techniques.js            technique list and inspector
js/ui/missions.js              mission files and the ALR diagram
js/ui/records.js               dossier, training path, seals table, activity cards, contact
js/ui/terminal.js              command line
js/ui/secrets.js               hidden discoveries
assets/readme/*.svg            README images (generated)
tools/readme_svgs.py           regenerates the README SVGs
.github/workflows/profile-images.yml   daily activity cards
.github/scripts/stats_card.py  writes stats.svg, langs.svg, chakra.svg to the output branch
docs/ARCHIVE_GUIDE.md          this file
```

No framework, no build step, no runtime dependency except Google Fonts. The JavaScript is split into eight modules, each about 30 to 120 lines.

## 6. What the README can and cannot do on GitHub

GitHub strips scripts, styles and event handlers from README files. What is used here and works:

- `<details>` and `<summary>` for progressive disclosure: the M-01 file, the mission archive, technique inspection, and the sealed note.
- Heading anchors for the top navigation. `## Training log` becomes `#training-log`.
- SVG through `<img>` with CSS animation inside the SVG: typing, stamp, path draw, flow dashes. Fonts inside those SVGs fall back to system fonts, because GitHub does not load web fonts for images.
- Tables, code blocks, blockquotes, an HTML comment visible only in the raw file.

What cannot work in a README, and the alternative used here:

| Wanted | Why not | Alternative |
|---|---|---|
| Typing a command | no scripts or inputs | static `console` block in the README, real terminal on the website |
| Clicking a technique to inspect it | no state | `<details>` table in the README, inspector on the website |
| Live counters written by hand | numbers would go stale or be invented | workflow regenerates cards from the GitHub API every day |

## 7. Setup (local)

1. Put this folder anywhere, then run a static server in it, for example `python -m http.server 8000`.
2. Open `http://localhost:8000`. Opening `index.html` directly as a file does not work, because browsers block ES modules on `file://`.
3. After changing the README numbers, run `python tools/readme_svgs.py`.
4. To test the activity cards without the network, run `MOCK=1 python .github/scripts/stats_card.py dist` in bash. In PowerShell: `$env:MOCK=1; python .github/scripts/stats_card.py dist`.

## 8. Deploy on GitHub

1. Repository **Masbismaa/Masbismaa**. It must be public, and the name must match the username so GitHub shows the README on the profile.
2. Delete the old theme files: the old `css/`, `js/`, `assets/` folders, the old `index.html`, and `tools/`. Keep the `.github` folder; it gets overwritten.
3. **Add file → Upload files**. Drag in everything from this folder, then **Commit changes**. If the `.github` folder does not upload (hidden folder), create both files with **Create new file** using the same paths.
4. **Settings → Actions → General → Workflow permissions → Read and write permissions → Save.**
5. **Actions → Generate profile images → Run workflow.** This creates the `output` branch with `stats.svg`, `langs.svg` and `chakra.svg`.
6. **Settings → Pages → Deploy from a branch → main / (root) → Save.** The site appears at `https://masbismaa.github.io/Masbismaa/` within a minute or two.

## 9. Customising

- **Change a status** (for example, workspaces are done): in `js/data/archive.js`, change `'progress'` to `'implemented'` for that feature. Then update the same row in `README.md` and the `ALR` counts at the top of `tools/readme_svgs.py`, and run the script.
- **Add a technique:** add an object to `TECHNIQUES`. The tier must match the evidence:
  - `honed`: daily use on an active project;
  - `drilled`: a real project;
  - `studied`: no mission yet;
  - `training`: studying now.
- **Add a mission:** add an object to `MISSIONS` with the next ID. An `objective` and a `system` are enough for a short record. Add `features`, `lessons` or `progression` to make it expandable. Also add a row to the "OPEN MISSION ARCHIVE" table in the README.
- **Quotes:** `QUOTES` in `archive.js`, one per chapter. Keep them short and keep them yours.
- **Repository links:** set `repo` on a mission to a URL string once a repository is public.

## 10. Where the content came from

From earlier conversations and your answers:

- **About you:** name, role at Spindo, 3 to 5 years, S1 Informatika, BNSP and HTML (Microsoft) certificates, open to remote, the four learning topics, hobbies, contacts.
- **Projects:** the MTOA ALR requirements, roles and data rules, naming conventions, branching, milestone commits, Pytest positive and negative scenarios, and the Tabler UI with local assets. Also the Django, Laravel and Flutter projects and the thesis.
- **Your answers in this session:**
  - Login and OTP, RBAC with Public/Private, CSRF, sessions, validation, audit log, Alembic and Pytest are implemented.
  - The Flask and PostgreSQL project was your own CRUD practice app.

**Needs your confirmation** (marked "in progress" until you say otherwise):

- dynamic form per category;
- search, filter and Excel export;
- workspaces with invites;
- link status check.

**Needs your input:**

- links for any public repositories (all show as internal or unpublished now);
- dates for the training stages (left out on purpose rather than guessed);
- whether rate limiting is finished in ALR (marked implemented, based on your earlier answer that OTP and rate limiting are part of how you build).

**Invented on purpose:** the terminology, the archive ID (MBP in hex), the quotes and the secret notes. These are fiction and style, not claims.

## 11. Testing checklist

- [ ] No console errors on load (DevTools console)
- [ ] Widths 360, 390, 768, 1024, 1366: no horizontal scroll
- [ ] Index rail highlights the current chapter; menu opens and closes on mobile, Esc closes it
- [ ] Every technique button opens the inspector; the mission link inside it opens that file
- [ ] Every mission toggle opens and closes; `/#M-01` opens M-01 directly
- [ ] Terminal: `help`, `whoami`, `mission --current`, `archive --list`, `archive --open M-00`, `skills --inspect sqlalchemy`, `training`, `seals`, `git log`, `contact`, `clear`, arrow-up history
- [ ] Secrets: three clicks on ARCHIVE 4D-42-50, the `∴` button, `ls -a`, `cat .scroll`, `seal` opens Field notes
- [ ] Keyboard only: Tab reaches the skip link first, then every control, with a visible ember outline
- [ ] With reduced motion on in the OS: no typing, no decode, everything readable at once
- [ ] Activity cards load after the first workflow run; before that, the fallback sentence shows

## 12. Performance checklist

- [ ] HTML, CSS and JS together stay around 70 KB raw, about 20 KB gzipped (GitHub Pages serves gzip)
- [ ] No images on the site except the three activity SVGs, lazy-loaded
- [ ] No libraries; animations are CSS or one short `requestAnimationFrame` loop that ends
- [ ] Fonts load with `display=swap`, and every stack has a system fallback
- [ ] README SVGs stay under 10 KB each

## 13. GitHub compatibility checklist

- [ ] README renders with no raw HTML visible (check on github.com and in the GitHub mobile app)
- [ ] Top navigation links jump to the right headings
- [ ] Every `<details>` has a blank line after `</summary>` so Markdown inside renders
- [ ] All README images have alt text
- [ ] Images from `raw.githubusercontent.com/.../output/` load after the workflow runs
- [ ] No emoji anywhere (search the repository)

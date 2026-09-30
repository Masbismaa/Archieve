<!--
  You opened the raw file. Good instinct.
  Rule zero of this archive: nothing here claims more than the commit history can prove.
  The headquarters terminal has a file that `ls` does not show. Try `ls -a`.
-->

<div align="center">

<img src="./assets/readme/gate.svg" width="100%" alt="Archive 4D-42-50 opening: Mochammad Bisma Prasetya, IT Developer at Spindo. Status active, open to remote work. Current mission M-01 MTOA Access Link Register." />

<sub>

[`DOSSIER`](#dossier) &nbsp;·&nbsp;
[`TECHNIQUES`](#techniques) &nbsp;·&nbsp;
[`MISSIONS`](#missions) &nbsp;·&nbsp;
[`TRAINING`](#training-log) &nbsp;·&nbsp;
[`SEALS`](#sealing-arts) &nbsp;·&nbsp;
[`CHAKRA FLOW`](#chakra-flow) &nbsp;·&nbsp;
[`SIGNAL`](#signal)

</sub>

</div>

<br />

## Dossier

```console
$ whoami
Mochammad Bisma Prasetya
IT Developer at Spindo · 3-5 years of writing code · S1 Informatika

$ mission --current
M-01   MTOA Access Link Register                  ACTIVE
       access links in one place; private means private, even for the admin
       features: 9 implemented · 4 in progress · 1 planned

$ skills --inspect flask
Flask  [####]  honed
built    MTOA ALR, split into routes / services / models / schemas / security / utils
learned  routes stay thin; rules live in services, where tests can reach them
```

I build the internal tools other teams use at Spindo: an asset inventory, a reporting dashboard, and now an access link register that has to keep secrets from its own administrators.

I learn by building the thing. Flask and PostgreSQL started as a practice CRUD app. The same stack now runs ALR, with migrations, tests, and an audit log nobody can edit. Before that: Laravel sites, Flutter apps, and a thesis about stock-keeping for small grocery stores.

> *Nothing in this archive claims more than the commit history can prove.*

<a href="https://masbismaa.github.io/Masbismaa/"><img src="./assets/readme/hq.svg" width="100%" alt="Enter the headquarters: the full archive with a working terminal at masbismaa.github.io/Masbismaa" /></a>

<br />

## Techniques

Tiers are earned by evidence. **Honed**: in daily use on an active project. **Drilled**: used to build at least one real project. **Studied**: learned and practised, no mission on record. **In training**: studying now.

| Tier | Techniques |
|:--|:--|
| `■■■■` **Honed** | Python · Flask · PostgreSQL · SQLAlchemy · Alembic · Pytest · Git |
| `■■■□` **Drilled** | Django · Laravel · PHP · MySQL · Firestore · Flutter · Dart · HTML/CSS/JS · OWASP ZAP · PowerShell |
| `■■□□` **Studied** | CodeIgniter · MongoDB · Tailwind CSS · GitLab CI · C++ · C# |
| `■□□□` **In training** | Docker and cloud · Penetration testing · API design and microservices · LLM integration |

<details>
<summary><b>INSPECT TECHNIQUES</b> &nbsp;<sub>what each one was actually used for</sub></summary>
<br />

| Technique | Built with it | What it taught |
|:--|:--|:--|
| **Python** | ALR backend, the training-ground app, Django tools at work | Written conventions keep a growing codebase readable: `snake_case` modules, `PascalCase` models, booleans starting with `is_` / `has_` / `can_` |
| **Flask** | MTOA ALR, modular backend | Routes stay thin. Validation and access rules live in services |
| **PostgreSQL** | ALR database, training-ground app | Rules that matter go into the schema as constraints, not only into form checks |
| **SQLAlchemy** | All ALR models | Foreign keys named `entity_id` make queries read like the requirement |
| **Alembic** | ALR schema migrations | A migration is part of the change and gets reviewed like code |
| **Pytest** | ALR test suite | A negative test is where an access bug shows up first |
| **Git** | `main`, `develop`, `feature/*`; one commit per milestone; Conventional Commits | History is documentation |
| **Django** | IT asset inventory, reporting dashboard | Batteries included is fast. Knowing what the batteries do pays off later |
| **Laravel / PHP / MySQL** | Online store, information system | How much a framework decides for you |
| **Flutter / Dart** | POS cashier, catalog with ordering, field reporting, thesis app | State that has to survive a bad signal |
| **Firestore** | Thesis: real-time stock data | Modelling around documents and live sync instead of joins |
| **OWASP ZAP** | Baseline scans on apps I build | Reproduce the finding, fix the cause |
| **HTML / CSS / JS** | ALR interface on the Tabler UI kit, assets served locally | Keep markup, style and behaviour in separate files |

</details>

> *Read the stack trace before you blame the framework.*

<br />

## Missions

<img src="./assets/readme/mission-m01.svg" width="100%" alt="Mission M-01, MTOA Access Link Register, active. Request flow from browser through routes, services and models to PostgreSQL inside a security layer, with an audit log. Feature status: 9 implemented, 4 in progress, 1 planned." />

<details>
<summary><b>OPEN FILE M-01</b> &nbsp;<sub>MTOA Access Link Register</sub></summary>
<br />

**Objective.** ICT access links, with their notes and credentials, were scattered across different places. Put them in one web app, with strict rules about who can see what.

| | |
|:--|:--|
| **System** | Flask · SQLAlchemy · Alembic · PostgreSQL · Pytest · Tabler UI (served locally) |
| **Architecture** | `routes` handle requests · `services` hold rules and validation · `models` map tables · `schemas` shape input and output · `security` holds auth, OTP and RBAC · `utils` holds shared helpers |
| **Database** | Master categories (Web, Application, Network, General), users, access entries, attachments, audit log. Tables `snake_case` plural, models `PascalCase` singular, keys `id` and `entity_id` |
| **Testing** | Every rule tested from both sides. An admin must not read a private entry; a user must not edit someone else's public entry |
| **Repository** | Private, company GitLab |

| Feature | Status |
|:--|:--|
| Login: corporate email and password, then a one-time code | `implemented` |
| Roles: Admin and User Entry | `implemented` |
| Public and Private entries (Private is hidden even from Admin) | `implemented` |
| CSRF protection and session security | `implemented` |
| URL validation (http/https), duplicate detection for URL, address and port | `implemented` |
| Upload checks: allowed file types, 10 MB per file, 5 files per entry | `implemented` |
| Rate limiting on login and OTP | `implemented` |
| Immutable audit log: who, when, what, IP, old and new values | `implemented` |
| Schema migrations and database constraints | `implemented` |
| Dynamic form per category, extra fields for General | `in progress` |
| Search, category filter, export to Excel | `in progress` |
| Workspaces with member invites | `in progress` |
| Link status check | `in progress` |
| OTP delivery by internal email (printed to the server log during development) | `planned` |

**Lessons.** "Private" had to mean private for the admin too; that one rule shaped the whole permission model. Tagging every task with its requirement ID kept scope honest. One commit per milestone keeps the history readable for review.

</details>

<details>
<summary><b>OPEN MISSION ARCHIVE</b> &nbsp;<sub>7 more files</sub></summary>
<br />

| ID | Mission | System | State |
|:--|:--|:--|:--|
| M-00 | **Flask and PostgreSQL training ground.** A CRUD app built from an empty folder: routes and forms, relationships, migrations, first tests, reading tracebacks to the last line | Flask · SQLAlchemy · PostgreSQL · Pytest | closed |
| M-02 | **IT Asset Inventory.** Laptops and printers to software licenses | Django | closed |
| M-03 | **Reporting Dashboard.** Operational data as summaries and charts for management | Django | closed |
| M-04 | **Online Store.** Product catalog and order management | Laravel · MySQL | closed |
| M-05 | **Information System.** Institutional data for places like schools or clinics | Laravel · MySQL | closed |
| M-06 | **Mobile field kit.** POS cashier, catalog with ordering, field activity reporting | Flutter | closed |
| M-07 | **Thesis: grocery store inventory.** Stock records synced in real time | Flutter · Firestore | closed |

</details>

> *Private means private. Even from the admin.*

<br />

## Training log

<img src="./assets/readme/training.svg" width="100%" alt="Training log: I Groundwork, II Training ground, III Field work, IV Deeper systems, V Sealing discipline, VI Current." />

| Stage | What happened there |
|:--|:--|
| **I · Groundwork** | S1 Informatika · HTML certification (Microsoft) · PHP and Laravel with MySQL · Flutter apps, then a thesis on Flutter and Firestore · BNSP certification |
| **II · Training ground** | Flask CRUD from an empty folder · PostgreSQL and SQLAlchemy relationships · migrations · first tests · debugging by reading the whole traceback |
| **III · Field work** | Django tools for internal use · requirement IDs attached to every task |
| **IV · Deeper systems** | Two-step authentication · authorization by role and ownership · Alembic · positive and negative tests for every rule |
| **V · Sealing discipline** | Validation at the boundary · RBAC · CSRF and sessions · upload checks · immutable audit log · OWASP ZAP |
| **VI · Current** | MTOA ALR hardening and tests · Docker and cloud · penetration testing · API design · LLM integration |

> *Break it on your own machine first.*

<br />

## Sealing arts

Security here is a written list of what I do when I build, with a status next to each item.

| Seal | What it covers | Where | Status |
|:--|:--|:--|:--|
| Authentication | Email and password, then a one-time code | M-01 | `implemented` |
| Authorization | Admin and User Entry roles, ownership, Public and Private | M-01 | `implemented` |
| CSRF and sessions | State-changing forms, session handling after login and OTP | M-01 | `implemented` |
| Input validation | URL scheme, duplicate URL, address and port | M-01 | `implemented` |
| Upload checks | Allowed types, size and count limits | M-01 | `implemented` |
| Rate limiting | Login and OTP attempts | M-01 | `implemented` |
| Audit logging | Immutable; who, when, what, IP, old and new values | M-01 | `implemented` |
| Database constraints | Integrity enforced by PostgreSQL, not only by forms | M-01 | `implemented` |
| Injection and XSS | Parameterised queries through the ORM, escaped output | habit | `implemented` |
| Security testing | Negative tests for access rules, ZAP baseline scans | habit | `implemented` |
| OTP by email | Real delivery instead of the development log | M-01 | `planned` |
| Penetration testing | Learning to attack what I build | training | `in progress` |

> *Validate at the border. Trust nothing that crossed it.*

<br />

## Chakra flow

Live activity, regenerated daily by [a workflow in this repository](./.github/workflows/profile-images.yml). The numbers are GitHub's. Contributions are the energy map; the full calendar is on the [profile page](https://github.com/Masbismaa).

<img src="https://raw.githubusercontent.com/Masbismaa/Masbismaa/output/chakra.svg" width="100%" alt="Energy map: contribution calendar for the last twelve months" />

<img src="https://raw.githubusercontent.com/Masbismaa/Masbismaa/output/stats.svg" width="49%" alt="Reserves: contributions, commits, pull requests, issues, repositories, stars" /> <img src="https://raw.githubusercontent.com/Masbismaa/Masbismaa/output/langs.svg" width="49%" alt="Techniques by volume: most used languages in public code" />

> *Commit when the milestone is done, not when the day is.*

<br />

## Signal

| | |
|:--|:--|
| Email | `moch.bismap@gmail.com` |
| GitHub | [github.com/Masbismaa](https://github.com/Masbismaa) |
| Instagram | [@bisma.prasetya_](https://www.instagram.com/bisma.prasetya_) |
| Open to | Remote work |

<details>
<summary><sub>∴</sub></summary>
<br />

```text
archive keeper, note 0

rule zero   nothing here claims more than the commit history can prove
rule one    a feature is not done until its negative test fails the right way
rule two    the admin does not get to read private entries. not even me

the headquarters terminal keeps one more file. it does not show up in ls.
```

</details>

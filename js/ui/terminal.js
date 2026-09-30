// A small command line over the same data the page shows. No network, no eval.
import { $, esc } from './dom.js';
import { PERSON, TECHNIQUES, TIERS, MISSIONS, SEALS, TRAINING, STATUS, ARCHIVE_SECRET } from '../data/archive.js';
import { inspect } from './techniques.js';
import { openMission } from './missions.js';
import { unseal } from './secrets.js';

const pad = (s, n) => String(s).padEnd(n);

const COMMANDS = {
  help: () => [
    'whoami               who keeps this archive',
    'mission --current    the active mission',
    'archive --list       every mission on record',
    'archive --open <id>  open a mission file, e.g. archive --open M-01',
    'skills --list        techniques by tier',
    'skills --inspect <n> inspect a technique, e.g. skills --inspect flask',
    'training             the training log',
    'seals                security practice and its status',
    'git log              how commits are written here',
    'contact              how to reach me',
    'clear                clear the screen',
    '<dim>Some files are not listed.</dim>',
  ],
  whoami: () => [`${PERSON.name}`, `${PERSON.role}. ${PERSON.experience}. ${PERSON.education}.`, `<dim>${PERSON.line}</dim>`],
  'whoami --real': () => ['Bisma. Anime, games, music.', 'Reads error messages all the way to the last line.'],
  'mission --current': () => {
    const m = MISSIONS.find(x => x.state === 'Active');
    const done = m.features.filter(f => f[1] === 'implemented').length;
    return [`${m.id}  ${m.name}`, `<dim>${m.objective}</dim>`, `features implemented: <hot>${done}/${m.features.length}</hot>`, `open the file: archive --open ${m.id}`];
  },
  'archive --list': () => MISSIONS.map(m => `${pad(m.id, 6)}${pad(m.state.toUpperCase(), 9)}${m.name}`),
  'skills --list': () => Object.keys(TIERS).flatMap(k => [`<hot>${TIERS[k].label.toUpperCase()}</hot>`, '  ' + TECHNIQUES.filter(t => t.tier === k).map(t => t.name).join(', ')]),
  training: () => TRAINING.map(s => `${pad(s.stage, 5)}${pad(s.title, 20)}${s.current ? '<hot>current</hot>' : ''}`),
  seals: () => SEALS.map(([n, , w, s]) => `${pad(n, 24)}${pad(w, 10)}${STATUS[s]}`),
  'git log': () => ['<dim>sample of the house style: type, no scope, description in Indonesian</dim>', 'feat: tambah validasi duplikasi url', 'fix: perbaiki pengecekan role user entry', 'test: tambah skenario negative login otp', 'docs: update panduan instalasi'],
  contact: () => [`email      ${PERSON.email}`, `github     ${PERSON.github}`, `instagram  ${PERSON.instagram}`],
  ls: () => ['dossier  techniques  missions  training  seals  flow'],
  'ls -a': () => ['.  ..  .scroll  dossier  techniques  missions  training  seals  flow'],
  'cat .scroll': () => ARCHIVE_SECRET.map(l => `<dim>${l}</dim>`),
  seal: () => { unseal(); return ['', '      +-------+', '      |  秘  |   sealed chapter opened', '      +-------+   scroll down, below the terminal', '']; },
  sudo: () => ['<err>sudo: visitor is not in the sudoers file.</err>', '<dim>This incident will be reported to the audit log.</dim>'],
  'rm -rf /': () => ['<err>refused.</err>', '<dim>Logged with your IP. Not really. ALR would, though.</dim>'],
  exit: () => ['<dim>There is no exit. Only Esc, and scrolling.</dim>'],
};

export function initTerminal() {
  const out = $('termOut'), input = $('termInput'), history = [];
  let hi = 0;
  const print = lines => {
    out.insertAdjacentHTML('beforeend', lines.map(l => `<div>${format(l)}</div>`).join(''));
    out.scrollTop = out.scrollHeight;
  };
  print(['archive shell. type <hot>help</hot>.']);

  $('termForm').addEventListener('submit', e => {
    e.preventDefault();
    const raw = input.value.trim();
    input.value = '';
    if (!raw) return;
    history.push(raw); hi = history.length;
    out.insertAdjacentHTML('beforeend', `<div class="cmd">${esc(raw)}</div>`);
    if (raw === 'clear') { out.innerHTML = ''; return; }
    print(run(raw));
  });
  input.addEventListener('keydown', e => {
    if (e.key === 'ArrowUp' && hi > 0) { input.value = history[--hi]; e.preventDefault(); }
    if (e.key === 'ArrowDown') { hi = Math.min(history.length, hi + 1); input.value = history[hi] || ''; e.preventDefault(); }
  });
}

function run(raw) {
  const cmd = raw.replace(/\s+/g, ' ').toLowerCase();
  if (COMMANDS[cmd]) return COMMANDS[cmd]();
  if (cmd.startsWith('sudo ')) return COMMANDS.sudo();
  let m = cmd.match(/^skills --inspect (.+)$/);
  if (m) {
    const t = inspect(TECHNIQUES.find(x => x.name.toLowerCase().startsWith(m[1]) || x.id === m[1])?.id || m[1]);
    return t ? [`${t.name}  <hot>${TIERS[t.tier].label}</hot>`, `built:   ${esc(t.built)}`, `mission: ${t.mission || 'none'}`, `learned: ${esc(t.learned)}`, '<dim>also shown in the Techniques inspector above.</dim>']
      : [`<err>no technique called "${esc(m[1])}".</err> try skills --list`];
  }
  m = cmd.match(/^archive --open (m-\d+)$/);
  if (m) return openMission(m[1].toUpperCase()) ? [`opening ${m[1].toUpperCase()}.`] : [`<err>no mission ${esc(m[1])}.</err> try archive --list`];
  return [`<err>${esc(raw)}: command not found.</err> try help`];
}

// tiny markup so lines can carry colour without HTML in the command table
const format = l => l.replace(/<(dim|hot|err)>(.*?)<\/\1>/g, (_, c, t) => `<span class="${c}">${t}</span>`);

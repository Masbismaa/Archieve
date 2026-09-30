// The opening: a short access log types out while the dossier is already on screen.
// Nothing waits for it; it is decoration with a purpose (you are opening someone's archive).
import { $, reduceMotion } from './dom.js';
import { PERSON } from '../data/archive.js';

const LOG = [
  ['$ ', `archive open --id ${PERSON.archiveId}`],
  ['  visitor ....... ', '<b>unregistered</b>'],
  ['  access ........ ', '<b>read-only</b>'],
  ['  archive ....... ', '<i>open</i>'],
];

export function initGate() {
  $('gateLine').textContent = `${PERSON.role}. ${PERSON.line}`;
  $('ledger').innerHTML = [
    ['Status', PERSON.status, 'live'],
    ['Current mission', `<a href="#missions">${PERSON.mission}</a>`],
    ['In training', PERSON.training],
  ].map(([k, v, cls]) => `<dt>${k}</dt><dd${cls ? ` class="${cls}"` : ''}>${v}</dd>`).join('');

  const log = $('gateLog');
  if (reduceMotion) { log.innerHTML = LOG.map(l => l.join('')).join('\n'); return; }
  typeLog(log);
  decode($('gateName'));
}

async function typeLog(el) {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  let html = '';
  for (const [i, [lead, value]] of LOG.entries()) {
    if (i === 0) {
      for (let k = 0; k <= value.length; k++) { el.innerHTML = html + lead + value.slice(0, k) + '<span class="caret">_</span>'; await sleep(26); }
      html += lead + value + '\n';
      await sleep(180);
    } else {
      html += lead + value + '\n';
      el.innerHTML = html;
      await sleep(140);
    }
  }
}

// The name resolves from scrambled glyphs, left to right, once.
function decode(el) {
  const text = el.dataset.text, glyphs = '#%&*+=?/\\<>[]{}01';
  const t0 = performance.now(), dur = 900;
  el.setAttribute('aria-label', text);
  const frame = t => {
    const p = Math.min(1, (t - t0) / dur), fixed = Math.floor(p * text.length);
    el.textContent = [...text].map((c, i) => i < fixed || c === ' ' ? c : glyphs[(i * 7 + Math.floor(t / 50)) % glyphs.length]).join('');
    if (p < 1) requestAnimationFrame(frame); else el.textContent = text;
  };
  requestAnimationFrame(frame);
}

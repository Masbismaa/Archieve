// Small discoveries for visitors who poke around. Each one points to the next.
import { $ } from './dom.js';
import { QUOTES } from '../data/archive.js';

export function initSecrets() {
  // three clicks on the archive id in the top bar leave a hint
  let clicks = 0, timer;
  $('archiveId').addEventListener('click', () => {
    clicks++; clearTimeout(timer); timer = setTimeout(() => { clicks = 0; }, 1200);
    if (clicks >= 3) { $('idHint').textContent = 'index key accepted. the terminal knows ls -a'; clicks = 0; }
  });
  // the mark in the colophon
  $('glyph').addEventListener('click', e => {
    e.currentTarget.insertAdjacentHTML('afterend', '<span>therefore: the terminal has a file that <kbd>ls</kbd> does not show.</span>');
    e.currentTarget.disabled = true;
  });
}

export function unseal() {
  const s = $('sealed');
  if (!s.hidden) return;
  $('notes').innerHTML = Object.values(QUOTES).map(q => `<li>${q}</li>`).join('') +
    '<li>A migration you cannot roll back is a promise you cannot keep.</li><li>The bug you hide today is the incident you explain later.</li>';
  s.hidden = false;
}

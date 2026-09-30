// Boot order: content first (so the page is complete without motion), then the moving parts.
import { initChapters, initIndex } from './ui/chapters.js';
import { initGate } from './ui/gate.js';
import { initRecords } from './ui/records.js';
import { initTechniques } from './ui/techniques.js';
import { initMissions, openMission } from './ui/missions.js';
import { initTerminal } from './ui/terminal.js';
import { initSecrets } from './ui/secrets.js';

initChapters();
initRecords();
initTechniques();
initMissions();
initTerminal();
initSecrets();
initGate();
initIndex();

// deep links like /#M-01 open that mission file, on load and when the hash changes
const openFromHash = () => { if (/^#M-\d+$/.test(location.hash)) openMission(location.hash.slice(1)); };
openFromHash();
addEventListener('hashchange', openFromHash);

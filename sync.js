// Keeps the website copy of the game identical to the desktop copy (game/index.html is the single source).
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
fs.mkdirSync(path.join(root, 'site', 'play'), { recursive: true });
fs.copyFileSync(path.join(root, 'game', 'index.html'), path.join(root, 'site', 'play', 'index.html'));
console.log('synced game/index.html -> site/play/index.html');

const { app, BrowserWindow, Menu, shell } = require('electron');
const path = require('path');

if (!app.requestSingleInstanceLock()) { app.quit(); } else {
  let win;
  const create = () => {
    Menu.setApplicationMenu(null);
    win = new BrowserWindow({
      width: 1100, height: 720, minWidth: 640, minHeight: 420, show: false,
      backgroundColor: '#140c07', title: 'DEATHSTEP', autoHideMenuBar: true,
      icon: path.join(__dirname, 'build', 'icon.png'),
      webPreferences: { contextIsolation: true, nodeIntegration: false, sandbox: true, autoplayPolicy: 'no-user-gesture-required' }
    });
    win.loadFile(path.join(__dirname, 'game', 'index.html'));
    win.once('ready-to-show', () => win.show());
    win.webContents.on('page-title-updated', e => e.preventDefault());
    win.webContents.setWindowOpenHandler(({ url }) => { shell.openExternal(url); return { action: 'deny' }; });
    win.webContents.on('will-navigate', e => e.preventDefault());
    // F11 or Alt+Enter toggles fullscreen, Esc leaves it
    win.webContents.on('before-input-event', (e, i) => {
      if (i.type !== 'keyDown') return;
      if (i.key === 'F11' || (i.alt && i.key === 'Enter')) { win.setFullScreen(!win.isFullScreen()); e.preventDefault(); }
      else if (i.key === 'Escape' && win.isFullScreen()) { win.setFullScreen(false); }
    });
  };
  app.whenReady().then(create);
  app.on('second-instance', () => { if (win) { if (win.isMinimized()) win.restore(); win.focus(); } });
  app.on('window-all-closed', () => app.quit());
}

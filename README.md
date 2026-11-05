# DEATHSTEP distribution

Two ways to play: **online** (website, nothing to install) and **Windows installer** (offline, from GitHub Releases).

```
game/index.html   the game (single source of truth)
site/             website (Play Online + Download buttons); site/play/ is a synced copy of the game
main.js           Electron wrapper (offline desktop app, F11 / Alt+Enter fullscreen)
build/icon.*      app icon (.ico for the installer, .png for window and website)
.github/workflows/release.yml   builds DEATHSTEP-Setup.exe on Windows and publishes a GitHub Release
```

## 1. Put it on GitHub
Create a **public** repo named `deathstep` under your account (https://github.com/Pocket34), then:
```
git init && git add . && git commit -m "DEATHSTEP 1.0.0"
git branch -M main
git remote add origin https://github.com/Pocket34/deathstep.git
git push -u origin main
```
If you name the repo something else, change `REPO` at the bottom of `site/index.html`.

## 2. Publish a Windows release (versioned)
```
git tag v1.0.0
git push origin v1.0.0
```
GitHub Actions builds on a Windows runner, sets the app version from the tag, creates `DEATHSTEP-Setup.exe` and `SHA256SUMS.txt`, and publishes the release.
The file name never changes, so `https://github.com/Pocket34/deathstep/releases/latest/download/DEATHSTEP-Setup.exe` always points at the newest installer.
The website also reads the latest release from the GitHub API and shows its real version, size, date and notes.
To test the build without releasing: Actions tab > "Build and release Windows installer" > Run workflow (downloads the .exe as an artifact).

## 3. Deploy the website on Vercel
Vercel > Add New > Project > import the repo. Set **Root Directory** to `site`, Framework Preset **Other**, leave Build Command empty. Deploy.
(GitHub Pages also works: Settings > Pages > deploy from `/site` via a workflow, or move the contents of `site/` to the repo root.)

## 4. Update the game later
1. Edit `game/index.html`.
2. `npm run sync` (copies it to `site/play/index.html`), commit, push (Vercel redeploys the web version).
3. `git tag v1.0.1 && git push origin v1.0.1` (new Windows installer, website shows the new version automatically).

## Local commands (Windows or any OS with Node 22+)
```
npm install
npm start        # run the desktop app
npm run dist     # build dist/DEATHSTEP-Setup.exe (run on Windows)
```

## Known limits
- The installer is **not code-signed**, so Windows SmartScreen shows "Windows protected your PC" (More info > Run anyway). Signing needs a paid certificate.
- Progress is saved in the browser or app storage on that device, and is not shared between the web and desktop versions.

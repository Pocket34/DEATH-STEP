"""Builds site/downloads/DEATHSTEP.zip (+ version.json) from game/index.html. Run: python scripts/make_zip.py"""
import zipfile, hashlib, json, datetime, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
version = json.loads((root / 'package.json').read_text())['version']
bat = r'''@echo off
title DEATHSTEP
set "GAME=%~dp0index.html"
set "URL=file:///%GAME:\=/%"
set "E1=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
set "E2=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
set "C1=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
set "C2=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if exist "%E1%" start "" "%E1%" --app="%URL%" --start-fullscreen & if exist "%E1%" exit /b
if exist "%E2%" start "" "%E2%" --app="%URL%" --start-fullscreen & if exist "%E2%" exit /b
if exist "%C1%" start "" "%C1%" --app="%URL%" --start-fullscreen & if exist "%C1%" exit /b
if exist "%C2%" start "" "%C2%" --app="%URL%" --start-fullscreen & if exist "%C2%" exit /b
start "" "%GAME%"
'''.replace('\n', '\r\n')
txt = f'''DEATHSTEP v{version}
====================
HOW TO PLAY (no install needed, works offline)
1. Right-click the ZIP and choose "Extract All..." (do not run the game from inside the ZIP).
2. Open the extracted DEATHSTEP folder and double-click "PLAY DEATHSTEP.bat".
   If Windows says "Windows protected your PC": More info > Run anyway.
   Or just double-click index.html - it opens in any browser.
3. Press Play. Pick a door on the map with the arrow keys and press Space.

CONTROLS
Arrow keys or A / D = move     Space or W or Up = jump
M = map     Q / E = change chapter     Fullscreen button (or F11 in the browser)

Progress is saved in your browser on this computer.
'''.replace('\n', '\r\n')
out = root / 'site' / 'downloads'; out.mkdir(parents=True, exist_ok=True)
z = out / 'DEATHSTEP.zip'
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as f:
    f.write(root / 'game' / 'index.html', 'DEATHSTEP/index.html')
    f.writestr('DEATHSTEP/PLAY DEATHSTEP.bat', bat)
    f.writestr('DEATHSTEP/HOW TO PLAY.txt', txt)
    f.write(root / 'build' / 'icon.png', 'DEATHSTEP/icon.png')
info = {'version': version, 'date': datetime.date.today().isoformat(), 'size': z.stat().st_size,
        'sha256': hashlib.sha256(z.read_bytes()).hexdigest(), 'file': 'DEATHSTEP.zip'}
(out / 'version.json').write_text(json.dumps(info, indent=2))
print(info)

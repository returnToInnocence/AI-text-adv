# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\Code\\projects\\Experience\\AI-game-test\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\Code\\projects\\Experience\\AI-game-test\\config', 'config/'), ('D:\\Code\\projects\\Experience\\AI-game-test\\logs', 'logs/'), ('D:\\Code\\projects\\Experience\\AI-game-test\\saves', 'saves/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'PyQt6', 'tkinter', 'numpy', 'pandas', 'scipy', 'matplotlib'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\Code\\projects\\Experience\\AI-game-test\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)

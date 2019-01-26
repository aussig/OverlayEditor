# -*- mode: python -*-

block_cipher = None

data_files = [('Resources/OverlayEditor.html', '.'),
    ('Resources/OverlayEditor.png', '.'),
    ('Resources/Sea01.png', '.'),
    ('Resources/add.png', '.'),
    ('Resources/addnode.png', '.'),
    ('Resources/airport0_000.png', '.'),
    ('Resources/autogen.png', '.'),
    ('Resources/autogens.png', '.'),
    ('Resources/background.png', '.'),
    ('Resources/bad.png', '.'),
    ('Resources/bezier.png', '.'),
    ('Resources/blank.png', '.'),
    ('Resources/color.fs', '.'),
    ('Resources/color.vs', '.'),
    ('Resources/copy.png', '.'),
    ('Resources/cut.png', '.'),
    ('Resources/delete.png', '.'),
    ('Resources/exc.png', '.'),
    ('Resources/fac.png', '.'),
    ('Resources/facs.png', '.'),
    ('Resources/fallback.png', '.'),
    ('Resources/for.png', '.'),
    ('Resources/fors.png', '.'),
    ('Resources/goto.png', '.'),
    ('Resources/help.png', '.'),
    ('Resources/import-region.png', '.'),
    ('Resources/import.png', '.'),
    ('Resources/inspector.png', '.'),
    ('Resources/instanced.vs', '.'),
    ('Resources/lin.png', '.'),
    ('Resources/lins.png', '.'),
    ('Resources/net.png', '.'),
    ('Resources/new.png', '.'),
    ('Resources/node.png', '.'),
    ('Resources/obj.png', '.'),
    ('Resources/objs.png', '.'),
    ('Resources/open.png', '.'),
    ('Resources/ortho.png', '.'),
    ('Resources/orthos.png', '.'),
    ('Resources/padlock.png', '.'),
    ('Resources/paste.png', '.'),
    ('Resources/point.fs', '.'),
    ('Resources/pol.png', '.'),
    ('Resources/pols.png', '.'),
    ('Resources/prefs.png', '.'),
    ('Resources/region.png', '.'),
    ('Resources/reload.png', '.'),
    ('Resources/save.png', '.'),
    ('Resources/screenshot.jpg', '.'),
    ('Resources/str.png', '.'),
    ('Resources/strs.png', '.'),
    ('Resources/surfaces.png', '.'),
    ('Resources/undo.png', '.'),
    ('Resources/unlit.fs', '.'),
    ('Resources/vanilla.vs', '.'),
    ('Resources/windsock.obj', '.'),
    ('Resources/windsock.png', '.'),
    ('MacOS/agp.icns', '.'),
    ('MacOS/fac.icns', '.'),
    ('MacOS/for.icns', '.'),
    ('MacOS/lin.icns', '.'),
    ('MacOS/obj.icns', '.'),
    ('MacOS/pol.icns', '.'),
    ('MacOS/str.icns', '.'),
    ('MacOS/OverlayEditor.png', '.'),
    ('MacOS/delete.png', '.'),
    ('MacOS/help.png', '.'),
    ('MacOS/import-region.png', '.'),
    ('MacOS/import.png', '.'),
    ('MacOS/inspector.png', '.'),
    ('MacOS/new.png', '.'),
    ('MacOS/open.png', '.'),
    ('MacOS/padlock.png', '.'),
    ('MacOS/prefs.png', '.'),
    ('MacOS/reload.png', '.'),
    ('MacOS/save.png', '.'),
    ('MacOS/undo.png', '.')]

binary_files = [('MacOS/DSFTool', 'DSFTool')]

a = Analysis(['OverlayEditor.py'],
    pathex=['/Users/austin/Development/OverlayEditor'],
    binaries=binary_files,
    datas=data_files,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
    cipher=block_cipher)

exe = EXE(pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='OverlayEditor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False )

coll = COLLECT(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='OverlayEditor')

app = BUNDLE(coll,
    name='OverlayEditor.app',
    icon='MacOS/OverlayEditor.icns',
    bundle_identifier='com.aussi.overlayeditor',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'CFBundleShortVersionString': '2.70-b6-aussi'
    })

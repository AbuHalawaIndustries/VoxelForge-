# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['voxel_forge.py'],       # اسم ملف التطبيق الرئيسي
    pathex=['.'],
    binaries=[],
    datas=[
        ('assets/logo/VoxelForge.png', 'assets/logo'),  # اللوغو
        ('assets', 'assets'),                           # كل ملفات المشروع داخل assets
    ],
    hiddenimports=['OpenGL', 'pyqtgraph.opengl'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=False,
    name='VoxelForge',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # False لو التطبيق GUI
    icon='assets/logo/VoxelForge.png'  # مسار اللوغو
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='voxel_forge'
)
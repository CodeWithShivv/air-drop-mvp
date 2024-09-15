# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_submodules, copy_metadata
from PyInstaller.building.build_main import Analysis, PYZ, EXE, BUNDLE

# Set the project path relative to the current working directory
# This assumes the .spec file is in the root of the project directory
project_path = os.getcwd()

# Collect hidden imports and metadata for the zeroconf package
hiddenimports = collect_submodules('zeroconf')
datas = copy_metadata('zeroconf')

a = Analysis(
    ['airdrop.py'],
    pathex=[project_path],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[os.path.join(project_path, 'hooks')],  # Ensure this directory contains your custom hooks
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='airdrop',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name='airdrop.app',
    icon=None,
    bundle_identifier=None,
)

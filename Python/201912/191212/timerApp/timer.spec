# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\pcuser\\timer.py'],
             pathex=['C:\\Users\\pcuser'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('noodle.png', '.\\noodle.png', 'DATA')]
a.datas += [('udon.png', '.\\udon.png', 'DATA')]
a.datas += [('start.png', '.\\start.png', 'DATA')]
a.datas += [('reset.png', '.\\reset.png', 'DATA')]
a.datas += [('stop.png', '.\\stop.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          [],
          name='timer',
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
               upx_exclude=[],
               name='timer')

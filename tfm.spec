# -*- mode: python -*-

block_cipher = None


a = Analysis(['tfm.py'],
             pathex=['C:\\Users\\jfayr\\flight-following'],
             binaries=[],
             datas=[('sounds/*.wav', 'sounds')],
             hiddenimports=['babel.numbers'],
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
          name='tfm',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , uac_admin=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='tfm')
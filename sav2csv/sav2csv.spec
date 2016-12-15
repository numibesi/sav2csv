# -*- mode: python -*-

block_cipher = None


a = Analysis(['sav2csv.py'],
             pathex=['C:/Users/vonwalha/src/sav2csv/sav2csv'],
             binaries=[('C:/Users/vonwalha/src/sav2csv/venv/Lib/site-packages/savReaderWriter/spssio/win32/',
                        './savReaderWriter/spssio/win32/')],
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='sav2csv',
          debug=False,
          strip=False,
          upx=True,
          console=True )

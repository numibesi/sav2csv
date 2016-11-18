# -*- mode: python -*-

block_cipher = None


a = Analysis(['sav2csv.py'],
             pathex=['/home/vonwalha/spss/sav2csv'],
             binaries=[('/home/vonwalha/spss/src/savreaderwriter/savReaderWriter/spssio/lin64/*',
                        './savReaderWriter/spssio/lin64/')],
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

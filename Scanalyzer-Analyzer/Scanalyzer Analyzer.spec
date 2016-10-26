# -*- mode: python -*-

block_cipher = None


a = Analysis(['Scanalyzer Analyzer.py'],
             pathex=['C:\\Users\\GPH\\Desktop\\Scanalyzer\\Scripts'],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[])

a.datas += [('jquery-2.2.2.min.js', 'jquery-2.2.2.min.js', 'Data')]
a.datas += [('JavaScript.js', 'JavaScript.js', 'Data')]
a.datas += [('flats.js', 'plate layouts/flats.js', 'Data')]
a.datas += [('6 Well.html', 'plate layouts/6 Well.html', 'Data')]
a.datas += [('6 Well StyleSheet.css', 'plate layouts/6 Well StyleSheet.css', 'Data')]
a.datas += [('12 Well.html', 'plate layouts/12 Well.html', 'Data')]
a.datas += [('12 Well StyleSheet.css', 'plate layouts/12 Well StyleSheet.css', 'Data')]
a.datas += [('24 well.html', 'plate layouts/24 Well.html', 'Data')]
a.datas += [('24 Well StyleSheet.css', 'plate layouts/24 Well StyleSheet.css', 'Data')]
a.datas += [('48 Well.html', 'plate layouts/48 Well.html', 'Data')]
a.datas += [('48 Well StyleSheet.css', 'plate layouts/48 Well StyleSheet.css', 'Data')]
a.datas += [('96 Well.html', 'plate layouts/96 Well.html', 'Data')]
a.datas += [('96 Well StyleSheet.css', 'plate layouts/96 Well StyleSheet.css', 'Data')]
a.datas += [('32 Well Flat.html', 'plate layouts/32 Well Flat.html', 'Data')]
a.datas += [('32 Well StyleSheet.css', 'plate layouts/32 Well StyleSheet.css', 'Data')]
a.datas += [('72 Well Flat.html', 'plate layouts/72 Well Flat.html', 'Data')]
a.datas += [('72 Well StyleSheet.css', 'plate layouts/72 Well StyleSheet.css', 'Data')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Scanalyzer Analyzer',
          debug=False,
          strip=False,
          upx=True,
          console=False )

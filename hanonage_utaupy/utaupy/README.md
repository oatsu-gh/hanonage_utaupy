# utaupy

[utaupy](https://github.com/oatsu-gh/utaupy) v1.4.0 です。

## 主な仕様

- utaupy.ust.Ust では全エントリを utaupy.ust.Note として取得する

- utaupy.utauplugin.Plugin では 各エントリを utaupy.ust.Note として取得し、次のように登録する
  - [#VERSION] を self.version
  - [#SETTING] を self.setting
  - [#PREV]  を self.prev
  - [#NEXT]  を self.next
  - それ以外のノートは self.notes のリストに登録
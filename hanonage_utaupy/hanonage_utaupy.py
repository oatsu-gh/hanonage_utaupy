#!python3
# coding: utf-8
# Copyright (c) oatsu
"""
utaupyをつかった半音上げプラグイン
hanonage_utaupy: https://github.com/oatsu-gh/hanonage_utaupy
utaupy: https://github.com/oatsu-gh/utaupy
"""
import sys

import utaupy as up


def notenum_plus1(plugin):
    """
    全てのノートを半音上げる
    """
    # Pluginオブジェクトのうちノート部分を取得
    notes = plugin.notes
    # 半音上げ
    for note in notes:
        note.notenum += 1


def main():
    """
    パスの取得とファイル入出力
    """
    # UTAUから出力されるプラグインスクリプトのパスを取得
    path = sys.argv[1]
    # up.utauplugin.Plugin オブジェクトとしてプラグインスクリプトを読み取る
    plugin = up.utauplugin.load(path)
    # 半音上げを実行
    notenum_plus1(plugin)
    # プラグインスクリプトを上書き
    plugin.write(path)


if __name__ == '__main__':
    print('_____ξ・ヮ・) < hanonage_utaupy v1.0.0 ________')
    main()

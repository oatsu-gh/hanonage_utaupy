#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) oatsu
"""
utaupyをつかった半音上げプラグイン
hanonage_utaupy: https://github.com/oatsu-gh/hanonage_utaupy
utaupy: https://github.com/oatsu-gh/utaupy
"""
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


if __name__ == '__main__':
    print('_____ξ・ヮ・) < hanonage_utaupy v1.3.1 ________')
    # run() に渡すのを notenum_plus1() としないように注意
    up.utauplugin.run(notenum_plus1)

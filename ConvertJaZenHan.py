#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin


def reverseDictionary(d):
    u"""辞書の{ハッシュ: キー}を入れ替える
    """
    return dict((value, key) for key, value in d.items())


def convertToHanKana(region):
    ret_region = u''

    for char_current in region:
        if char_current in dict_multiKana:
            ret_region += dict_multiKana[char_current]
        else:
            ret_region += char_current

    return ret_region


def convertToZenKana(region):
    ret_region = u''
    char_prev = u''

    for char_current in region:
        if not char_prev:
            char_prev = char_current
            continue

        if char_current == str_dakuten or char_current == str_handakuten:
            ret_region += dict_singleKana['%s%s' % (char_prev, char_current)]
            char_prev = u''
            continue

        if char_prev in dict_singleKana:
            ret_region += dict_singleKana[char_prev]
        else:
            ret_region += char_prev

        char_prev = char_current

    if char_prev == '\n' or char_prev == '\r' or char_prev == '\r\n':
        ret_region += char_prev
    else:
        ret_region += dict_singleKana[char_prev]

    return ret_region


dict_multiKana = {
    u'ア': u'ｱ', u'イ': u'ｲ', u'ウ': u'ｳ', u'エ': u'ｴ', u'オ': u'ｵ',
    u'カ': u'ｶ', u'キ': u'ｷ', u'ク': u'ｸ', u'ケ': u'ｹ', u'コ': u'ｺ',
    u'サ': u'ｻ', u'シ': u'ｼ', u'ス': u'ｽ', u'セ': u'ｾ', u'ソ': u'ｿ',
    u'タ': u'ﾀ', u'チ': u'ﾁ', u'ツ': u'ﾂ', u'テ': u'ﾃ', u'ト': u'ﾄ',
    u'ナ': u'ﾅ', u'ニ': u'ﾆ', u'ヌ': u'ﾇ', u'ネ': u'ﾈ', u'ノ': u'ﾉ',
    u'ハ': u'ﾊ', u'ヒ': u'ﾋ', u'フ': u'ﾌ', u'ヘ': u'ﾍ', u'ホ': u'ﾎ',
    u'マ': u'ﾏ', u'ミ': u'ﾐ', u'ム': u'ﾑ', u'メ': u'ﾒ', u'モ': u'ﾓ',
    u'ヤ': u'ﾔ', u'ユ': u'ﾕ', u'ヨ': u'ﾖ',
    u'ラ': u'ﾗ', u'リ': u'ﾘ', u'ル': u'ﾙ', u'レ': u'ﾚ', u'ロ': u'ﾛ',
    u'ワ': u'ﾜ', u'ヲ': u'ｦ', u'ン': u'ﾝ', u'ヴ': u'ｳﾞ',
    u'ァ': u'ｧ', u'ィ': u'ｨ', u'ゥ': u'ｩ', u'ェ': u'ｪ', u'ォ': u'ｫ',
    u'ッ': u'ｯ', u'ャ': u'ｬ', u'ュ': u'ｭ', u'ョ': u'ｮ',
    u'ガ': u'ｶﾞ', u'ギ': u'ｷﾞ', u'グ': u'ｸﾞ', u'ゲ': u'ｹﾞ', u'ゴ': u'ｺﾞ',
    u'ザ': u'ｻﾞ', u'ジ': u'ｼﾞ', u'ズ': u'ｽﾞ', u'ゼ': u'ｾﾞ', u'ゾ': u'ｿﾞ',
    u'ダ': u'ﾀﾞ', u'ヂ': u'ﾁﾞ', u'ヅ': u'ﾂﾞ', u'デ': u'ﾃﾞ', u'ド': u'ﾄﾞ',
    u'バ': u'ﾊﾞ', u'ビ': u'ﾋﾞ', u'ブ': u'ﾌﾞ', u'ベ': u'ﾍﾞ', u'ボ': u'ﾎﾞ',
    u'パ': u'ﾊﾟ', u'ピ': u'ﾋﾟ', u'プ': u'ﾌﾟ', u'ペ': u'ﾍﾟ', u'ポ': u'ﾎﾟ',
    u'０': u'0', u'１': u'1', u'２': u'2', u'３': u'3', u'４': u'4',
    u'５': u'5', u'６': u'6', u'７': u'7', u'８': u'8', u'９': u'9',
    u'Ａ': u'A', u'Ｂ': u'B', u'Ｃ': u'C', u'Ｄ': u'D',
    u'Ｅ': u'E', u'Ｆ': u'F', u'Ｇ': u'G', u'Ｈ': u'H',
    u'Ｉ': u'I', u'Ｊ': u'J', u'Ｋ': u'K', u'Ｌ': u'L',
    u'Ｍ': u'M', u'Ｎ': u'N', u'Ｏ': u'O', u'Ｐ': u'P',
    u'Ｑ': u'Q', u'Ｒ': u'R', u'Ｓ': u'S', u'Ｔ': u'T',
    u'Ｕ': u'U', u'Ｖ': u'V', u'Ｗ': u'W', u'Ｘ': u'X',
    u'Ｙ': u'Y', u'Ｚ': u'Z',
    u'ａ': u'a', u'ｂ': u'b', u'ｃ': u'c', u'ｄ': u'd',
    u'ｅ': u'e', u'ｆ': u'f', u'ｇ': u'g', u'ｈ': u'h',
    u'ｉ': u'i', u'ｊ': u'j', u'ｋ': u'k', u'ｌ': u'l',
    u'ｍ': u'm', u'ｎ': u'n', u'ｏ': u'o', u'ｐ': u'p',
    u'ｑ': u'q', u'ｒ': u'r', u'ｓ': u's', u'ｔ': u't',
    u'ｕ': u'u', u'ｖ': u'v', u'ｗ': u'w', u'ｘ': u'x',
    u'ｙ': u'y', u'ｚ': u'z',
    u'！': u'!', u'？': u'?', u'．': u'.', u'／': u'/', u'：': u':',
    u'；': u';', u'＋': u'+', u'ー': u'ｰ', u'、': u'､', u'。': u'｡',
    u'「': u'｢', u'」': u'｣', u'（': u'(', u'）': u')', u'＃': u'#',
    u'・': u'･', u'　': u' '
}

str_dakuten = u'ﾞ'
str_handakuten = u'ﾟ'
dict_singleKana = reverseDictionary(dict_multiKana)


class ConvertToZenKanaAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # select all Region
        region_all = sublime.Region(0, self.view.size())
        region_all_str = self.view.substr(region_all)
        region_all_converted = convertToZenKana(region_all_str)

        self.view.replace(edit, region_all, region_all_converted)


class ConvertToZenKanaSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # select current Region
        for region_current in self.view.sel():
            region_current_str = self.view.substr(region_current)
            region_current_converted = convertToZenKana(region_current_str)

            self.view.replace(edit, region_current, region_current_converted)


class ConvertToHanKanaAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # select all Region
        region_all = sublime.Region(0, self.view.size())
        region_all_str = self.view.substr(region_all)
        region_all_converted = convertToHanKana(region_all_str)

        self.view.replace(edit, region_all, region_all_converted)


class ConvertToHanKanaSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # select current Region
        for region_current in self.view.sel():
            region_current_str = self.view.substr(region_current)
            region_current_converted = convertToHanKana(region_current_str)

            self.view.replace(edit, region_current, region_current_converted)

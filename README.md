ConvertJaZenHan
==============

_A Sublime Text plugin for converting the Japanese characters between singlebyte and doublebyte._

__日本語での解説は[こちらのページ](http://orememo-v2.tumblr.com/post/95237450958/convet-zenhan)をご覧ください。__

## Intstallation

1. Find "Package Control: Add Repository" in Command Pallete.
2. Input "https://github.com/Satoh-D/ConvertJaZenHan".
3. Find "Package Control: Install Package" in Command Pallete.
4. Select "ConvertJaZenHan".

## Usage

You will find command look like __ConvertJaZenHan: Convert to...__ in the Command Pallete.  
ConvertJaZenHan will convert the Japanese charcters in a selection or multiple selections or current file.

- __Convert to Zenkaku in File__: converting the singelebyte characters into multibyte characters in the current file.
- __Convert to Zenkaku in Selection__: converting the singelebyte characters into multibyte characters in the current selections.
- __Convert to Hankaku in File__: converting the multibyte characters into singlebyte characters in the current file.
- __Convert to Hankaku in Selection__: converting the multibyte characters into singlebyte characters in the current selecitons.

## Example

this characters:

```html
アイウエオ  
ガギグゲゴ  
パピプペポ  
０１２３４５６７８９  
ＡＢＣＤＥ  
ａｂｃｄｅ  
。、！？．／：；「」（）＃・　

ｱｲｳｴｵ  
ｶﾞｷﾞｸﾞｹﾞｺﾞ  
ﾊﾟﾋﾟﾌﾟﾍﾟﾎﾟ  
0123456789  
ABCDE  
abcde  
｡､!?./:;｢｣()#･ 
```

into this:

```html
ｱｲｳｴｵ  
ｶﾞｷﾞｸﾞｹﾞｺﾞ  
ﾊﾟﾋﾟﾌﾟﾍﾟﾎﾟ  
0123456789  
ABCDE  
abcde  
｡､!?./:;｢｣()#･   

アイウエオ  
ガギグゲゴ  
パピプペポ  
０１２３４５６７８９  
ＡＢＣＤＥ  
ａｂｃｄｅ  
。、！？．／：；「」（）＃・　
```

## Characters Supported

- Katakana
- Number(1234567890)
- Punctuation marks(、。！？／：；＋ー「」（）＃・)
- Space(" ")

## License

MIT.

## Copyrights

2014, [Sato Daiki](http://orememo-v2.tumblr.com) ([@Satoh_D](http://twitter.com/Satoh_D)).

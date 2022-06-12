
# 松山市文化財データAPP
![スクリーンショット 2022-06-11 201621](https://user-images.githubusercontent.com/84378453/173185716-515c104f-79f3-4e86-b17a-755c36a9fe70.png)

## Overview
愛媛県松山市のオープンデータをもとに絞り込み、検索できる文化財リストを作製。
また、foliumで文化財の場所をプロットしたleafletの地図を作製。
それをまとめdjangoでwebアプリの形にしました。

## Requirement
### base
- Windows10
- Python3.9
- Django4.0.5
### map
- folium
- leaflet.js
### etc
- feedparser
- numpy
- pandas


## Description
### datal ist
- objects.filterを使用し絞り込み検索を可能にした
- ※defaultではobjects.all
- ※キーワード検索では__icontains使用のため完全一致ではなく部分一致検索になる





https://user-images.githubusercontent.com/84378453/173225493-2380213b-0bf7-4e9e-8568-1fdbed76db8a.mp4



### map
- 地図のzoom度合いにより表示されるマーカーを集約し、視認性を向上。


![スクリーンショット 2022-06-11 202641](https://user-images.githubusercontent.com/84378453/173185930-44d00391-f32a-40bf-b476-38638ac12e20.png)

- マーカーを押すとpopupが表示され住所や名称、文化財分類と種類などを表示する。
- プラグインにより現在地表示、タイル変更、文化財の検索を可能にした。(google map APIと違いleaflet.js使用のためdefaultでついている機能ではなく導入に少々苦労した)


https://user-images.githubusercontent.com/84378453/173185778-2adfabf8-c2d2-409f-9702-5919e08acdbb.mp4


### etc
- feedparserを使用して文化財についてのニュースなども表示。


![スクリーンショット 2022-06-11 195127](https://user-images.githubusercontent.com/84378453/173185699-aebfaa72-1303-482b-80a5-91de6f5ae4fb.png)


## Reference
- leaflet基本
https://ktgis.net/service/leafletlearn/advanced.html#step12
- Markerのiconのマーク
https://chayarokurokuro.hatenablog.com/entry/2020/09/02/212350
https://github.com/domoritz/leaflet-locatecontrol
- leaflet現在地表示
https://kita-note.com/leaflet-plugin-locatecontrol
https://kita-note.com/leaflet-plugin-icon-pulse
- データ不足分の緯度経度情報会得
https://elsammit-beginnerblg.hatenablog.com/entry/2021/07/14/225200
- 地図タイル変更
https://2ndart.hatenablog.com/entry/2021/04/28/164803
https://2ndart.hatenablog.com/entry/2021/04/29/111336

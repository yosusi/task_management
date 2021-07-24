# Critical path analysis tool

## Overview
csvファイルを読み込むことでクリティカルパスを分析して、ガントチャートのひな形をcsv形式で出力するツール

## How to use
### Test
1. ダウンロードかcloneした後、main.exeを起動する
2. 'enter LOAD csv path'には test/test.csvの絶対パスを指定（Browseより指定）
3. 'enter SAVE csv path'には 保存先を指定（Browseより指定可能）
4. ANALYSISボタンを押すと解析開始。ボタン下の表示が'analysis is done'に変わったら解析完了

### 解析するためのcsv作り
- 基本的にはtest.csvを参照

```
ID,task_name,time,Predecessor
1,A,2,
2,B,3,1
3,C,4,1
4,D,5,2
5,E,3,3.4
```
- 1行目のタイトルは変更不可。エクセルファイル作成時も入れてください。
- ID：タスクID 1から始まる番号で振る
- Task_name: タスク名 任意の名前でOK。英語を推奨
- time: タスクの所要時間 整数入力を推奨
- Predecessor: 前提となるタスクをIDで指定(例えば1を指定するとタスクID1を完了するまで取り掛かれない)
- Predecessorに複数タスクを指定する場合はドット(.)で区切ってください。,だと動作しません(改善予定)
- エクセルで上記の表を作成したのち、区切り文字を,にしてcsv形式にエクスポートしてください。

### 出力されたcsvの内容
```
id,task_name,time,ES,EF,is_cp,1,2,3,4,5,6,7,8,9,10,11,12,13
1,A,2,1,2,x,1,1,0,0,0,0,0,0,0,0,0,0,0
2,B,3,3,5,x,0,0,1,1,1,0,0,0,0,0,0,0,0
3,C,4,3,6,,0,0,1,1,1,1,0,0,0,0,0,0,0
4,D,5,6,10,x,0,0,0,0,0,1,1,1,1,1,0,0,0
5,E,3,11,13,x,0,0,0,0,0,0,0,0,0,0,1,1,1
```
- id: タスクID
- task_name: タスク名
- time: 所要時間
- ES: Early start 最早開始時間
- EF: Early finish 最早終了時間
- is_cp: クリティカルパスか否か。xと書かれているものがクリティカルパスに該当

## 参考URL

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[yosusi](https://github.com/yosusi)
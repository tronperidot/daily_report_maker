#!/usr/bin/env python
# coding:utf-8
import subprocess
from Tkinter import Tk
from cls.my_print import MyPrint
from cls.my_string import MyString
import cls.formater

# 見出しのタイトル
TITLES = [
  '１．本日の作業内容\n',
  '２．明日の作業予定\n',
  '３．所感、困りごと\n'
]

# 案件名
PROJECTS = {'1': '案件1\n', '2':'案件2\n', '3':'案件3\n'}

# クリップボードへコピー
def setpb_data(data):
    # mac
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(data)
    # windows
    #r = Tk()
    #r.clipboard_append(test)

# 作業実績の作成
def detail(is_to_day):
  printer = MyPrint()
  contents = MyString()
  if is_to_day:
    contents.put(TITLES[0])
  else:
    contents.put(TITLES[1])

  while True:
    printer.log(str(PROJECTS).decode('string-escape'))
    project_idx = raw_input('プロジェクトを撰択して下さい。（範囲外で処理を抜けます。）:')
    project = PROJECTS.get(project_idx)
    if not project:
      break
    printer.log(project_idx)
    printer.log(project)
    contents.put(project)
    while True:
      msg = raw_input('作業内容を書いて下さい。（範囲外で処理を抜けます。）:')
      if not msg:
        break
      contents.put(msg)
      # HACK 汚い
      msg = ( cls.formater.progress_format() if is_to_day else cls.formater.taget_frmat() )
      contents.put(msg)
  return str(contents)

# 所感の作成
def comment():
  contents = MyString()
  contents.put(TITLES[2])
  printer.log('所感の入力をして下さい（未記入で抜けます。）')
  while True:
    msg = raw_input()
    if not msg:
      break
    contents.put_line(msg)
  return str(contents)

# ここからメイン処理
printer = MyPrint()
printer.log('python app')
ms = MyString()

printer.headline_log('本日の作業内容入力モード')
ms.put(detail(True))
printer.headline_log('明日の作業予定入力モード')
ms.put(detail(False))
printer.headline_log('所感入力モード')
ms.put(comment())
text = str(ms)
printer.log(text)

# to clip borad
setpb_data(text)

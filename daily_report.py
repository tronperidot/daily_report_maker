#!/usr/bin/env python
# coding:utf-8
import subprocess
from Tkinter import Tk

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

# consoleへの出力
def log(msg):
  print msg
  return msg

# 一行線を出力
def line():
  log('---------------------')

# 見出しの出力
def headline_log(msg):
  log('')
  line()
  log(msg)
  line()

# percentの算出
def percent(num):
  return '---' if (not num) else num

# 目標と達成率
def progress_format():
  goal = raw_input('目標率:')
  achi = raw_input('達成率:')
  return "（目標：{}% 達成率:{}%）\n".format(percent(goal), percent(achi))

# 明日の目標
def taget_frmat():
  goal = raw_input('目標率:')
  return "（目標：{}%）\n".format(percent(goal))

# 作業実績の作成
def detail(is_to_day):
  if is_to_day:
    contents = TITLES[0]
  else:
    contents = TITLES[1]

  while True:
    log(str(PROJECTS).decode('string-escape'))
    project_idx = raw_input('プロジェクトを撰択して下さい。（範囲外で処理を抜けます。）:')
    project = PROJECTS.get(project_idx)
    if not project:
      break
    log(project_idx)
    log(project)
    contents = contents + project
    while True:
      msg = raw_input('作業内容を書いて下さい。（範囲外で処理を抜けます。）:')
      if not msg:
        break
      msg = msg + ( progress_format() if is_to_day else taget_frmat() )
      contents = contents + msg
  return contents

# 所感の作成
def comment():
  contents = TITLES[2]
  log('所感の入力をして下さい（未記入で抜けます。）')
  while True:
    msg = raw_input()
    if not msg:
      break
    contents = contents + msg + '\n'
  return contents

# ここからメイン処理
log('python app')

headline_log('本日の作業内容入力モード')
text = detail(True)
headline_log('明日の作業予定入力モード')
text = text + detail(False)
headline_log('所感入力モード')
text = text + comment()
log(text)

# to clip borad
setpb_data(text)

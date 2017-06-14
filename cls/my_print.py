#!/usr/bin/env python
# coding:utf-8

# print 機能を独自用ラップしたクラス
class MyPrint:
  # consoleへ出力
  def log(self, msg):
    print msg
    return msg

  # 一行線を出力
  def line(self):
    self.log('---------------------')

  # 見出しの出力
  def headline_log(self, msg):
    self.log('')
    self.line()
    self.log(msg)
    self.line()

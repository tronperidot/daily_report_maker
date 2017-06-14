#!/usr/bin/env python
# coding:utf-8

# wrapしたstringクラス
class MyString:

  def __init__(self):
    self.data = ""

  def __str__(self):
    return self.data

  # 追加
  def put(self, msg):
    self.data = self.data + msg

  def put_line(self, msg):
    self.put(msg + '\n')

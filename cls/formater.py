#!/usr/bin/env python
# coding:utf-8

# formatの集まり
# HACK: formaterと名付けながらraw_inputしているのはどうか

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

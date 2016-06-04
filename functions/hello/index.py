from __future__ import print_function
import arrow

def handle(event, context):
  msg = "Hello World!"
  time = str(arrow.now())
  tmsg = msg+" The time now is: "+time
  return tmsg

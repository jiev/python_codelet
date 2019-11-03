import os
import time
import re

def task_kill(task_name = ""):
     if task_name == "":
          return

     command = 'taskkill /F /IM '+task_name
     os.system (command)


if __name__ == "__main__":
     process_name = 'SogouExplorer.exe'
     rule_str = r'^'+process_name
     rule = re.compile(rule_str)

     while 1:
          process_strings = os.popen('tasklist').readlines()

          for line in process_strings:
               process = rule.findall(line)
               if len(process) > 0:
                    task_kill(process_name)

          time.sleep(6000)
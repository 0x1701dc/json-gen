#!/usr/bin/env python3

import sys

def main():
 # TODO(sjv): This needs to be refactored - this is dirt but gets the job done
 # NOTE(sjv): { "paramName": (IsThisRequired, NextArgSetToThis) } 
 success, options = parse_args({"--in": (True, True), "--out": (False, True), "--print": (False, False)})
 if not success: 
   print(print_command_line_options())
 else: 
   print(options)

def print_command_line_options():
  # TODO(sjv): Build this up from the args dict we are using above
  return f"{sys.argv[0]}: --options go --here file"

def parse_args(arguments):
  success = True
  index = 1 
  arguments_out = {}
  while index < len(sys.argv):
    arg = sys.argv[index]
    if arg in arguments:
      _, req_second_arg  = arguments[arg]
      val = None
      if req_second_arg:
        if (index + 1) < len(sys.argv):
          sec_arg = sys.argv[index + 1]
          if sec_arg.startswith("--"):
            print(f"{sec_arg} is invalid for {arg}")
            success = False
          else:
            val = sec_arg
            index = index + 1
        else:
          print(f"{arg} requires an argument")
          success = False
      else:
        val = True
      
      arguments_out[arg] = val
      del(arguments[arg])
    elif arg in arguments_out:
      print(f"{arg} is set more than once")
      success = False
    else:
      print(f"{arg} is an unknown options")
      success = False

    index = index + 1
  
  for req_key in (k for k, v in arguments.items() if v[0]):
    print(f"{req_key} is a required argument")
    success = False

  return success, arguments_out 

if __name__ == '__main__':
  main()

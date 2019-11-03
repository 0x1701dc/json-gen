#!/usr/bin/env python3

import sys

def main():
 success, options = parse_args({"--in": True, "--out": False})
 if not success: 
   print(print_command_line_options())
 else: 
   print(options)

def print_command_line_options():
  return f"{sys.argv[0]}: --options go --here file"

def parse_args(arguments):
  success = True
  index = 1 
  arguments_out = {}
  while index < len(sys.argv):
    arg = sys.argv[index]
    if arg in arguments:
      arguments_out[arg] = "This is set"
      del(arguments[arg])
    elif arg in arguments_out:
      print(f"{arg} is set more than once")
      success = False
    else:
      print(f"{arg} is an unknown options")
      success = False

    index = index + 1
  
  for req_key in (k for k, v in arguments.items() if v):
    print(f"{req_key} is a required argument")
    success = False

  return success, arguments_out 

if __name__ == '__main__':
  main()

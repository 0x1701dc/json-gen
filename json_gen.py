#!/usr/bin/env python3
import sys
import parse_arguments as pa

def main():
 # TODO(sjv): This needs to be refactored - this is dirty but gets the job done
 # NOTE(sjv): { "paramName": (IsThisRequired, NextArgSetToThis) } 
 valid_args = {"--in": (True, True), "--out": (False, True), "--print": (False, False)}
 success, options = pa.parse_arguments(valid_args)
 
 if not success: 
   print(options)
   print(print_command_line_options())
 else: 
   print(options)

def print_command_line_options():
  # TODO(sjv): Build this up from the args dict we are using above
  return f"{sys.argv[0]}: --options go --here file"

if __name__ == '__main__':
  main()

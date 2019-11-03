import sys

def parse_arguments(arguments):
  success = True
  index = 1 
  arguments_out = {}
  positional_args = []
  while index < len(sys.argv):
    arg = sys.argv[index]
    if not arg.startswith("--"):
      positional_args.append(arg)
    elif arg in arguments:
      if len(positional_args) > 0:
        for parg in positional_args:
          print(f"Positional arg {parg} found in the middle of the command.")
        success = False
        positional_args = []

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
            index += 1 
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

    index += 1 
  
  for req_key in (k for k, v in arguments.items() if v[0]):
    print(f"{req_key} is a required argument")
    success = False
    
  arguments_out["positional_args"] = positional_args

  return success, arguments_out 

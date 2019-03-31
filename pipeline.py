# 4. Pipeline
def pipeline(*funcs):
  def helper(arg):
    result = None
    for func in funcs:
      if result is None:
        result = func(arg)
      else:
        result = func(result)
    return result
  return helper

fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))

#should print 5.0
#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):

  if not (url.startswith('http://') or url.startswith('https://')):
    return False

  #begins with a most one ?
  qc=url.count('?')
  if qc>1:
    return False

  #at most one #
  hc=url.count("#")
  if hc>1:
    return False

  #no spaces
  if ' ' in url:
    return False
  # # must be before ?
  if url.find("?") !=-1:
    if url.find("#")>url.find("?"):
      return False

      
  #host before '/'
  sc=url.count("/")
  if sc<3:
    return False
  scheme, after = url.split('://')
  hostport, afterslash = after.split("/", 1)
  if hostport=="":
    return False 

#At most two :, check hostname isnt empty and port is digits 
  cc=url.count(":")
  if cc>2:
    return False
  if cc==2:
    if ":" not in hostport:
      return False
      
  return True


def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")

testurl()
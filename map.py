from pprint import pprint
import re
import tomllib

def is_color(s):
    c = re.findall("#\w{6}", s)
    if len(c) == 1:
        return c[0]
    return False

def get_color_key(s):
    k = re.findall('^.*#', s)
    if len(k) == 1:
        return k[0]

def populate(i,l):
     c = is_color(l)
     if c:
         try:
             d[c].append(l.strip())
         except:
             d[c] = [l.strip()]


if __name__ == "__main__":
    
    d = {}
    with open("example/example.conf", "r") as f:
        for i,l in enumerate(f.readlines()):
            populate(i,l)
    
    nl = []
    with open("example/example.toml", "r") as f2:
        for i,l in enumerate(f2.readlines()):
            c =  is_color(l)
            if c:
                k = get_color_key(d[c][0])
                if k: 
                    l = l[0:-10] + '"' + "{{  " + k[0:-2] + "  }}" + '"' + "\n"
            nl.append(l)
    
    with open("map.toml", "w") as f3:
        f3.writelines(l for l in nl)
    
    pprint(d)
    pprint(nl)

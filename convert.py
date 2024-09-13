import os
import re
import pathlib
from map import is_color

def populate(l):
    c = is_color(l)
    if c:
        i = l.index(c)
        k = l[0:i-1]
        return k.strip(), c.strip()
    return "",""
        

def convert_theme(f, o='', dr=''):
    try:
        with open(f, "r") as f1:
            d = {}
            p = pathlib.Path(f)
            if o == '':
                o = p.stem + ".toml"
            for i, l in enumerate(f1.readlines()):
                k,v = populate(l)
                d[k] = v
    
            with open("map.toml") as m:
                nl = [f"#0x From the {p.stem} color palette\n\n\n"]
                for l in m.readlines():
                    r = re.findall('{{ .* }}',l)
                    if len(r) == 1:
                        r = r[0]
                        k = r[4:-4]
                        i = l.index(r) 
                        l = l[0:i]+ d[k] + l[i + len(r)]
                    nl.append(l+"\n")
                if not dr =="":
                    o = dr + "/" + o
                with open(o, "w") as f2:
                    f2.writelines(l for l in nl)
        print(f"successfully parsed{f}")
    except Exception as e:
        print(f"failed to parse {f}")
        print(repr(e))
                    
                            
d = os.fsencode("kitty-themes")
for file in os.listdir(d):
    convert_theme("kitty-themes/" + os.fsdecode(file), dr="alacritty-themes")

convert_theme("example/example.conf")

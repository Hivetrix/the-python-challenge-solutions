


def load(path):
    with open(path) as f:
        lines = f.readlines()
        lines = [line for line in lines if not line.startswith('#') and line != '\n' > 0]
        lines = map(lambda line: [int(x.strip()) for x in line.split()], lines) 
        n, m = lines[0] 
        h = lines[1:n+1]
        v = lines[n+2:]
        return h, v


h,v = load("warmup.txt")
print((h,v))

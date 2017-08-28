import sys
from graphviz import Digraph

f = Digraph('afd', filename='afd.afd', format='png')
f.attr(rankdir='LR', size='8,5')

sigma = sys.stdin.readline().strip().split(',')
Q     = sys.stdin.readline().strip().split(',')
s0    = sys.stdin.readline().strip()
F     = sys.stdin.readline().strip().split(',')

f.attr('node', shape='doublecircle')
for i in F:
    f.node(i)

delta = {}

for i in range( int( sys.stdin.readline().strip() ) ):
    (qinput, el, qoutput) = sys.stdin.readline().strip().split(',')
    if qinput not in delta:
        delta[qinput] = {}
    (delta[qinput])[el] = qoutput

f.attr('node', shape='circle')
for i in delta:
    for j in delta[i]:
        f.edge(i, delta[i][j], label=j)
        print i, " - ", delta[i][j], j

f.view()

for i in range( int( sys.stdin.readline().strip() ) ):
    s = s0
    string = sys.stdin.readline().strip()
    if len( string ) == 0 and s in F:
        print "Cadena vacia aceptada en el estado q0"
    else:
        for c in string:
            try:
                s = ( delta[s] )[c]
            except KeyError:
                print "Cadena %(string)s no valida porque uno de sus elementos no esta en el alfabeto" % { 'string': string }
                break
        else:
            if s in F:
                print "Cadena %(string)s aceptada en el estado %(s)s" % { 'string': string, 's': s }
            else:
                print "Cadena %(string)s no aceptada en estado %(s)s" % { 'string': string, 's': s }
print ""
print "=== I N F O R M A C I O N ==="
print ""
print "sigma = ", sigma
print "Q     = ", Q
print "s0    = ", s0
print "F     = ", F
print "delta = ", delta

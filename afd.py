import sys

sigma = sys.stdin.readline().strip().split(',')
Q     = sys.stdin.readline().strip().split(',')
s0    = sys.stdin.readline().strip()
F     = sys.stdin.readline().strip().split(',')

delta = {}

for i in range( int( sys.stdin.readline().strip() ) ):
    (qinput, el, qoutput) = sys.stdin.readline().strip().split(',')
    if qinput not in delta:
        delta[qinput] = {}
    (delta[qinput])[el] = qoutput

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

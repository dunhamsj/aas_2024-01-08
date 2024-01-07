#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use( 'publication.sty' )

fig, ax = plt.subplots()

def y(x):
    return 1.0 + 0.1 * np.sin( 2.0 * np.pi * x )

x = np.linspace( 0.0, 1.0, 100 )

xL = 0.6
xH = 0.8

ax.plot( x, y(x), 'k-' )
ax.set_xlabel( r'$x$' )
ax.set_ylabel( r'$u$' )

for x in [ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ]:
    ax.axvline( x )

xticks = ax.get_xticks()
xticklabels = ax.get_xticklabels()

#xts   = [ xL ]
#xlabs = [ r'$x_{\mathrm{L}}$' ]
#for i in range( len( xticks ) ):
#    xts.append( xticks[i] )
#    xlabs.append( xticklabels[i] )
#xts.append( xH )
#xlabs.append( r'$x_{\mathrm{H}}$' )
#ax.set_xticks( xts, xlabs )

ax.text( 0.6, 1.03, r'$\Delta x=x_{\mathrm{H}}-x_{\mathrm{L}}$', \
         fontsize = 9 )
ax.set_xlim( -0.1, 1.1 )

#plt.show()
plt.savefig( 'fig.sine.png', dpi = 300 )

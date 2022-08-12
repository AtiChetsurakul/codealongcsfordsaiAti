def fd_vortex(eq):
    a,b,c = eq.replace(' ','').split('x')
    return round((int(b)*-1)/(int(a)*2))

from decimal import localcontext, Decimal, ROUND_HALF_UP
with localcontext() as ctx:
...     ctx.rounding = ROUND_HALF_UP

...         

print(fd_vortex('9x +81x -27'))
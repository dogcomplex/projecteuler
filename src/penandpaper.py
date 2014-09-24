'''
Created on May 16, 2013

@author: W
'''

C = .11
A = 41




maxreg = 0
MR = ()
maxdouble = 0
MD = ()
maxconc = 0
MC = ()
vmaxreg = 0
VMR = ()
vmaxdouble = 0
VMD = ()
vmaxconc = 0
VMC = ()

n = 20
mp = 46

for aa in range(0,n):
    for cc in range(0,n-aa):
        for con in range(0,n-aa-cc):
            for dd in range(0,n-aa-cc-con):
                a = A +aa
                MP = mp
                crit = C
                
                reg = (crit*2 + (1-crit))*a
                doub = 2*(crit*2 + (1-crit))*a*(.6+.05*dd)
                conc = (crit*2 + (1-crit))*a*(1.10+.05*con)
                
                if reg > maxreg:
                    maxreg = reg
                    MR = (maxreg,aa,cc,con,dd, reg, doub, conc)
                if doub*(1+2*dd)*1.0/MP > maxdouble:
                    maxdouble = doub*(1+2*dd)*1.0/MP
                    MD = (maxdouble,aa,cc,con,dd, reg, doub, conc,(1+2*dd),(1+2*dd)*1.0/MP)
                if conc*(3+2*dd)*1.0/MP > maxconc:
                    maxconc = conc*(3+2*dd)*1.0/MP
                    MC = (maxconc,aa,cc,con,dd, reg, doub, conc,(3+2*dd),(3+2*dd)*1.0/MP)
                
                
                MP = mp-(2+cc)
                crit = C + cc*.06
                vreg = (crit*2 + (1-crit))*a
                vdoub = 2*(crit*2 + (1-crit))*a*(.6+.05*dd)
                vconc = (crit*2 + (1-crit))*a*(1.10+.05*con)
                
                if vreg > vmaxreg:
                    vmaxreg = vreg
                    VMR = (vmaxreg,aa,cc,con,dd, vreg, vdoub, vconc)
                if vdoub*(1+2*dd)*1.0/MP > vmaxdouble:
                    vmaxdouble = vdoub*(1+2*dd)*1.0/MP
                    VMD = (vmaxdouble,aa,cc,con,dd, vreg, vdoub, vconc,(1+2*dd),(1+2*dd)*1.0/MP)
                if vconc*(3+2*dd)*1.0/MP > vmaxconc:
                    vmaxconc = vconc*(3+2*dd)*1.0/MP
                    VMC = (vmaxconc,aa,cc,con,dd, vreg, vdoub, vconc,(3+2*dd),(3+2*dd)*1.0/MP)
                    
                print aa,cc,con,dd, doub, conc
print
print MR
print MD
print MC
print VMR
print VMD
print VMC

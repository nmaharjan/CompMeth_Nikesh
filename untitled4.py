from numpy import pi,sqrt,arange
from pylab import plot,show,ylabel

# Constants
m0 = 9.10938291E-31 # Free electron rest mass
h = 6.62606957E-34 # Plank constant
hbar = h/(2*pi) # Reduced Plank constant
ee = 1.60217657E-19 # Electron charge

#Parameters GaAs/AlGaAs
L = 14.5E-9 # GaAs QW width
N = 1000
h = L/N
Eg_well = 1.518 # Bandgap eV
Eg_barrier = 2.5753
dEc = 0.4729# conduction band discontinuity
exciton_binding = 8.5E-3# Exciton binding energy (eV)

select = int(input("Type 1 for Electron, 2 for light-Hole or 3 for heavy-Hole energies:  "))

if select == 1:
    # Electron
    V0_ee = (Eg_barrier-Eg_well)*dEc*ee # Barrier height
    m_ee = 0.067*m0 # Effective electron mass

    def d2p(E,phi):
        return -E*phi/hbar**2*2*m_ee
    answer = []

    for E in arange(0,V0_ee,V0_ee/1000):
        k = sqrt(2*m_ee*E)/hbar
        a = sqrt(2*m_ee*(V0_ee-E))/hbar
        p = []
        dp = []
        p0 = 1
        dp0 = a
        for i in range(N):
            p.append(p0)
            dp.append(dp0)
            dp0 += d2p(E,p0)*h
            p0 += dp0*h
        if abs(1 + a*p[-1]/dp[-1]) < 1e-1:
            answer.append(E)

    plot(answer,'bo')
    ylabel("Energy in Joules")
    show()

if select == 2:
    # Light hole
    V0_lh = (Eg_barrier-Eg_well)*(1-dEc)*ee # Barrier height
    m_lh = 0.087*m0 # Effective hole mass

    def d2p(E,phi):
        return -E*phi/hbar**2*2*m_lh
    answer = []

    for E in arange(0,V0_lh,V0_lh/1000):
        k = sqrt(2*m_lh*E)/hbar
        a = sqrt(2*m_lh*(V0_lh-E))/hbar
        p = []
        dp = []
        p0 = 1
        dp0 = a
        for i in range(N):
            p.append(p0)
            dp.append(dp0)
            dp0 += d2p(E,p0)*h
            p0 += dp0*h
        if abs(1 + a*p[-1]/dp[-1]) < 2e-1:
            answer.append(E)

    plot(answer,'bo')
    ylabel("Energy in Joules")
    show()

if select == 3:
    # Heavy hole
    V0_hh = (Eg_barrier-Eg_well)*(1-dEc)*ee # Barrier height
    m_hh = 0.62*m0 # Effective hole mass

    def d2p(E,phi):
        return -E*phi/hbar**2*2*m_hh
    answer = []

    for E in arange(0,V0_hh,V0_hh/1000):
        k = sqrt(2*m_hh*E)/hbar
        a = sqrt(2*m_hh*(V0_hh-E))/hbar
        p = []
        dp = []
        p0 = 1
        dp0 = a
        for i in range(N):
            p.append(p0)
            dp.append(dp0)
            dp0 += d2p(E,p0)*h
            p0 += dp0*h
        if abs(1 + a*p[-1]/dp[-1]) < 5:
            answer.append(E)

    plot(answer,'bo')
    ylabel("Energy in Joules")
    show()

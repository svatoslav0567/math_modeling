from lec3_mod import earth_mass  as em
from lec3_mod import sigma_staff_bolc  as sigma
from lec3_mod import gravity_constant  as G

g = 500 * G / 10**2
print(g)

x = em * g * sigma
print(x)

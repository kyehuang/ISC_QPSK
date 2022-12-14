# 2022/10/2 Chen-Fu Huang edited
# kye1234321@gmail.com

import binascii
from itertools import count
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import random

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def Convert_8bits_to_list(string_ASCII):
    i = 1
    list = []
    a = ""
    for ch in string_ASCII:
        if i<1:
            a += str(ch)
            i+=1
        else:
            i=1
            a += str(ch)
            list.append(a)            
            a = ""
    return list


# string MCDX{Start at 4pm}
string = "MCDX{5TocT_ot_4gM}"

# Convert String to ASCII
string_ASCII = text_to_bits(string)

# Convert 8bits to list

list = Convert_8bits_to_list(string_ASCII)

for t in list:
    print(t,end="")


t = np.linspace(0,1,100)  # Time
tb = 1
fc = 1    # carrier frequency

c1 = sqrt(2/tb)*np.cos(2*np.pi*fc*t)  # carrier frequency cosine wave
c2 = sqrt(2/tb)*np.sin(2*np.pi*fc*t)  # carrier frequency sine wave

m = []

for item in list:
    if(item=='0'):
        m.append(0)
    else:
        m.append(1)

t1 = 0
t2 = tb
## modulation

odd_sig = np.zeros((m.__len__(),100))
even_sig = np.zeros((m.__len__(),100))
fig, ax4 = plt.subplots()
for i in range(0,m.__len__(),2):
    t = np.linspace(t1,t2,100)
    if (m[i]>0.5):
        m[i] = 1
        m_s = np.ones((1,len(t)))
    else:
        m[i] = 0
        m_s = (-1)*np.ones((1,len(t)))

    odd_sig[i,:] = c1*m_s

    if (m[i+1]>0.5):
        m[i+1] = 1
        m_s = np.ones((1,len(t)))
    else:
        m[i+1] = 0
        m_s = (-1)*np.ones((1,len(t)))

    even_sig[i,:] = c2*m_s

    qpsk = odd_sig + even_sig   # modulated wave = oddbits + evenbits

    ax4.plot(t,qpsk[i,:])
    t1 = t1 + (tb+0.01)
    t2 = t2 + (tb+0.01)

ax4.grid()
plt.title('Modulated Wave')
plt.show()
# Python Implementation
from typing import List
import coba as convert_pdf


def rolling_hash(s: str, window_size: int, base: int = 26, mod: int = 10**9 + 7) -> List[int]:
    """
    Calculates the rolling hash values of all substrings of length window_size in string s.
    Uses the polynomial rolling hash algorithm with base and mod as constants.

    :param s: the input string
    :param window_size: the size of the rolling window
    :param base: the base for the polynomial hash function
    :param mod: the modulus for the polynomial hash function
    :return: a list of hash values of all substrings of length window_size in s
    """
    n = len(s)
    power = [1] * (n + 1)
    hash_values = [0] * (n - window_size + 1)

    # Precompute the powers of the
    # base modulo the mod
    for i in range(1, n + 1):
        power[i] = (power[i - 1] * base) % mod

    # Compute the hash value of
    # the first window
    current_hash = 0
    for i in range(window_size):
        current_hash = (current_hash * base + ord(s[i])) % mod

    hash_values[0] = current_hash

    # Compute the hash values of the
    # rest of the substrings
    for i in range(1, n - window_size + 1):

        # Remove the contribution of the
        # first character in the window
        current_hash = (
            current_hash - power[window_size - 1] * ord(s[i - 1])) % mod

        # Shift the window by one character
        # and add the new character
        # to the hash
        current_hash = (current_hash * base + ord(s[i + window_size - 1])) % mod

        hash_values[i] = current_hash

    return hash_values


# Driver code
def mainx(s, sx):

    # Input string
    # s = "bagus ga"
    # s.replace


    # Window size
    window_size = 3

    # Calculate rolling hash values
    hash_values = rolling_hash(s, window_size)

    # Print the hash values
    # print(hash_values)

    # Input string
    # sx = "bagus bro"

    # Window size
    # window_size = 3

    # Calculate rolling hash values
    hash_valuess = rolling_hash(sx, window_size)

    # Print the hash values
    # print(hash_valuess)
    return (hash_values, hash_valuess)



def semua(data1, data2):
    
    # data1 = "okeh kah sudah"
    data1 =data1.replace(' ', '')
    # data2 = "masa sih kah sudah"
    data2 =data2.replace(' ', '')
    
    # print(data2)
    oke1 , oke2 =mainx(data1, data2)
    
    panjang_awal1 = len(oke1)
    panjang_awal2 = len(oke2)
    
    panjang_data1 = len(oke1) - 1
    panjang_data2 = len(oke2) - 1
    
    ketemu = 0
    
    index1= 0
    index2= 0
    while index1 <= panjang_data1:
        index2 = 0
        while index2 <= panjang_data2:
            if oke1[index1] == oke2[index2]:
                oke1.remove(oke1[index1])
                oke2.remove(oke2[index2])
                index1 -=1
                panjang_data1-=1
                panjang_data2-=1
                ketemu +=1
                break
            else:
                # index1+=1
                index2+=1
        index1+=1
    
    # print(f'ketemu {ketemu} hash yang sama dari {panjang_awal2}')
    
    # print(f'dengan kemiripan sebesar {ketemu/panjang_awal2*100}')
    return ketemu, panjang_awal2
    
def kesamaan(pdf1, pdf2):
    # for i in range()
    ketemu =0
    # with as f:
    # f= open(r'C:\Users\ADMIN\Desktop\serverNode\Delfan Rynaldo Laden - 1915016069 - preprocessing.txt', 'r', encoding='utf-8')
    # fs = open(r'C:\Users\ADMIN\Desktop\serverNode\Proposal_Skripsi_abdullah - preprocessing.txt', 'r', encoding='utf-8')
    f = open(convert_pdf.preprocessing(pdf1), 'r', encoding='utf8')
    fs = open(convert_pdf.preprocessing(pdf2), 'r', encoding='utf8')


    oweh = f.read()
    print(oweh)
    oweh = oweh.split('\n')
    for ilo in oweh:
        if len(ilo) < 4:
            oweh.remove(ilo)
    # print(oweh)

    owehs = fs.read()
    print(owehs)
    owehs = owehs.split('\n')
    for ilo in owehs:
        if len(ilo) < 4:
            owehs.remove(ilo)
            
    total_hash = 0
    print(oweh)
    print(owehs)
    if(len(oweh) < 1) or (len(owehs) <1 ):
        return 0
    for i in owehs:
        tertinggi = 0
        for il in oweh:
            # print(il)
            okeh, panjang = semua(il, i)
            # tertinggi = okeh
            if okeh >= panjang:
                print(okeh, panjang)
                # ketemu+=okeh
                tertinggi = okeh
                # total_hash += panjang
                break
            elif okeh > tertinggi :
                tertinggi = okeh
        if(tertinggi/panjang) >= 0.50:
            ketemu= ketemu+tertinggi
        total_hash+=panjang
        print(f"sudah ketemu plagiat sebanyak {ketemu} hash dari {total_hash} total hash")

    
    if total_hash >0:
        print(f'kemiripannya adalah {ketemu/total_hash*100}%')
        return ketemu/total_hash*100
    else:
        return 0
    


# dokumen_asli = 'C:/Users/ADMIN/Desktop/serverNode/Delfan Rynaldo Laden - 1915016069.pdf'
# dokumen_pembanding = 'C:/Users/ADMIN/Desktop/serverNode/Proposal_Skripsi_abdullah.pdf'
# kesamaan(dokumen_asli, dokumen_pembanding)
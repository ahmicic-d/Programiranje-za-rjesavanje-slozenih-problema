def pronadi_znamenku(q, upiti):
    trenutna_pozicija = 0
    trenutni_broj = 1
    
    rezultati = []
    
    for i in range(q):
        k = upiti[i]
        while trenutna_pozicija + len(str(trenutni_broj)) < k:
            trenutna_pozicija += len(str(trenutni_broj))
            trenutni_broj += 1
        
        znamenka_na_k = str(trenutni_broj)[k - trenutna_pozicija - 1]
        rezultati.append(znamenka_na_k)
    
    return rezultati

# Primjer korištenja
q = 4
upiti = [3, 7, 12, 19]
rezultati = pronadi_znamenku(q, upiti)
for znamenka in rezultati:
    print(znamenka)

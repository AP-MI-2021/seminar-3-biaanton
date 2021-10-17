import math
def menu():
    print('1.Citire date')
    print('2.Afisarea tuturor numerelor intregi din lista')
    print('3.Afisarea celui mai mare numar divizibil cu un numar citit de la tastatura')
    print('4.Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.')
    print('5.Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă')
    print('x.Iesire din program')


#5. Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt
#puse ca string-uri cu caracterele în ordine inversă. Exemplu: [10.0, 100.0, 12.45, 50.0, 101.2] --> ['0.01', 100.0, '54.21', '0.05', 101.2]
def este_prim(numar):
    '''
    Determina daca un numar este prim
    :param numar: numarul pe care il verificam dac este prim
    :return: valoarea 1 daca numarul este prim si 0 in caz contrar
    '''
    if numar<2: return 0
    for div in range(2,numar//2):
        if numar%div==0: return 0
    return 1

def caractere_in_ordine_inversa(numar):
    '''
    Punem caracterele in ordine inversa
    :param numar: numarul ai carui caractere le inversam
    :return: Caracterele in ordine inversa
    '''
    numar_str=str(numar)
    return numar_str[::-1]


def float_ordine_inversa(lst):
    '''
    Determina lista obtinuta din lista initiala in care floaturile cu partea intreaga a radicalului numar prim sunt puse ca stringuri cu caracterele in ordine inversa
    :param lst: lista din care luam numerele
    :return: lista obtinuta din lista initiala in care floaturile cu partea intreaga a radicalului numar prim sunt puse ca stringuri cu caracterele in ordine inversa
    '''
    result=[]
    for num in lst:
        sqrt_num= math.sqrt(num)
        sqrt_int= math.trunc(sqrt_num)
        if este_prim(sqrt_int):
            result.append(caractere_in_ordine_inversa(num))
        else: result.append(num)
    return result

#4.Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.
def palindrom(numar):
    '''
    Verifica daca un numar este palindrom
    :param numar: numarul pe care il verificam
    :return: valoarea 1 daca numarul este palindrom, respectiv 0 in caz contrar
    '''
    copie=numar
    oglindit=0
    while copie>0:
        oglindit=oglindit*10+copie%10
        copie=copie//10
    if oglindit==numar:
        return 1
    return 0

def parte_fractionara(numar):
    '''
    Extrage partea fractionara a unui numar
    :param numar: numarul a carui partea fractionara o extragem
    :return: partea fractionara a numarului
    '''
    return str(numar).split('.')[1]

def toate_cu_parte_fractionara_palindrom(lst):
    '''
    Determina toate float-urile a caror parte fractionara este palindrom
    :param lst: lista din care verificam numerele
    :return: numerele care au parte fractionara palindrom
    '''
    result=[]
    for num in lst:
        fract_str=parte_fractionara(num)
        if palindrom(int(fract_str)):
            result.append(num)
    return result


#3. Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură
def div_mai_mare(lst,k):
    '''
    Determina cel mai mare numar divizibil cu un numar citit de la tastatura
    :param lst: lista din care verificam numerele
    :param k: numarul citit de la tastatura
    :return: numarul divizibil cu k
    '''
    maxx=None
    for num in lst:
        if num%k==0:
            if maxx is None:
                maxx=num
            if maxx<num:
                maxx=num
    return maxx


def test_div_mai_mare():
    assert div_mai_mare([2,3,4,5,6,7,8,9],2)==8
    assert div_mai_mare([3,6,2,4],3)==6


#2. Afișarea tuturor numerelor întregi din listă (de exemplu, 3 și 2.0 se consideră întregi).
def determinare_intregi(lst):
    '''
    Determina numerele intregi din lista
    :param lst: Lista din care se extrag numerele
    :return: lista cu numerele intregi
    '''
    result=[]
    for num in lst:
        if num==int(num):
            result.append(int(num))
    return result

def test_determinare_intregi():
    assert determinare_intregi([1,2.5,6,3,2.0,100.2])==[1,6,3,2.0]
    assert determinare_intregi([10.255,10.3,14,2.6])==[14]


#1. Citirea unei liste de float-uri. Citirile repetate suprascriu listele precedente.
def citire_lista():
    lst = []
    lst_str = input('Dati numerele separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
         lst.append(float(num_str))
    return lst

def main():
    lst = []
    while True:
        menu()
        opt = input('Optiunea: ')
        if opt == '1':
            lst = citire_lista()
        elif opt=='2':
            print(f'Numerele intregi din lista sunt: {determinare_intregi(lst)}')
        elif opt=='3':
            numar=int(input('Dati numarul k: '))
            print(f'Cel mai mare numar divizibil cu {numar} este {div_mai_mare(lst,numar)}')
        elif opt=='4':
            print(f'Float-urlie ale caror parte fractionara e palindrom sunt: {toate_cu_parte_fractionara_palindrom(lst)}')
        elif opt=='5':
            print(f'lista obtinuta din lista initiala in care floaturile cu partea intreaga a radicalului numar prim sunt puse ca stringuri cu caracterele in ordine inversa este: {float_ordine_inversa(lst)}')
        elif opt == 'x':
            break
        else:
            print('Optiune invalida.')


if __name__ == '__main__':
        main()
        test_determinare_intregi()
        test_div_mai_mare()
from random import*
import random
#on pose le problème et ses paramètres
gens = A = B = C = D = E = F = G = H = I = J = K = L = (randint(1,100))
intrus = (randint(1,100))

#on s'assure que l'intrus n'ait pas le meme poids que les gens
while intrus == gens:
  intrus = (randint(1,100))

suspects = [A, B, C, D, E, F, G, H, I, J, K, L]
innocents = [] 

#définition de fonctions
def bouger_i(x):
  global innocents
  global suspects
  innocents.append(x)
  suspects.remove(x)

poids_intrus = 0
position_intrus = 0
def mystèrieux(y):
  global poids_intrus
  poids_intrus = (randint(1,100))  
  while poids_intrus == gens:
    poids_intrus = (randint(1,100))
def sep():
  print("... ")
  
  
    
#on choisis la position de l'intrus
position_intrus = (randint(0,11))
print(position_intrus+1)
if position_intrus == 0:
  mystèrieux(0)
  A = poids_intrus  
  suspects[0] = A

elif position_intrus == 1:
  mystèrieux(1)
  B = poids_intrus
  suspects[1] = B
  

elif position_intrus == 2:
  mystèrieux(2)
  C = poids_intrus
  suspects[2] = C
    
elif position_intrus == 3:
  mystèrieux(3)
  D = poids_intrus
  suspects[3] = D
    
elif position_intrus == 4:
  mystèrieux(4)
  E = poids_intrus
  suspects[4] = E
    
elif position_intrus == 5:
  mystèrieux(5)
  F = poids_intrus
  suspects[5] = F
  
elif position_intrus == 6:
  mystèrieux(6)
  G = poids_intrus
  suspects[6] = G
    
elif position_intrus == 7:
  mystèrieux(7)
  H = poids_intrus
  suspects[7] = H
    
elif position_intrus == 8:
  mystèrieux(8)
  I = poids_intrus
  suspects[8] = I

elif position_intrus == 9:
  mystèrieux(9)
  J = poids_intrus
  suspects[9] = J
  
elif position_intrus == 10:
  mystèrieux(10)
  K = poids_intrus
  suspects[10] = K
    
elif position_intrus == 11:
  mystèrieux(11)
  L = poids_intrus
  suspects[11] = L
    
    
#on fait des groupes
pesée1a = A + B + C + D
pesée1b = E + F + G + H 

print(suspects)
print(poids_intrus)
sep

#on compare ces groupes
print("1ère pesée: On pèse ABCD contre EFGH.")
if pesée1a == pesée1b:
  bouger_i(A)
  bouger_i(B)
  bouger_i(C)
  bouger_i(D)
  bouger_i(E)
  bouger_i(F)
  bouger_i(G)
  bouger_i(H)
  print("Les gens sont équilibrés. A, B, C, D, E, F, G et H sont donc innocents.")
  print("Les suspects après la première étape sont :",suspects)
  print("Les innocents après la première étape sont :",innocents)
  pesée2a = I + J
  pesée2b = A + B 
  sep
  print("On pèse IJ contre AB.")
  if pesée2a == pesée2b:
    bouger_i(I)
    bouger_i(J)
    print("Les gens sont équilibrés. I et J sont donc innocents.")
    print("Les suspects après la deuxième étape sont :",suspects)
    print("Les innocents après la deuxième étape sont :",innocents)
    print("On pèse K contre A")
    if K == A:
      bouger_i(K)
      print("Les gens sont équilibrés. K est donc innocent.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc L.")
    else:
      bouger_i(L)
      print("Les gens ne sont pas équilibrés. L est donc innocent.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocets après la troisième étape sont :",innocents)
      print("L'intru est donc K.")
  else:
    bouger_i(K)
    bouger_i(L)
    print("Les gens ne sont pas équilibrés. K et L sont donc innocents")
    print("Les suspects après la deuxième étape sont :",suspects)
    print("Les innocents après la deuxième étape sont :",innocents)
    print("On pèse I contre A.")
    if I == A:
      bouger_i(I)
      print("Les gens sont équilibrés. I est donc innocent.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc J.")
    else:
      bouger_i(J)
      print("Les gens ne sont pas équilibrés. J est donc innocent.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc I.")
  
else:
  bouger_i(I)
  bouger_i(J)
  bouger_i(K)
  bouger_i(L)
  print("Les gens ne sont pas equilibrés.I, J, K et L sont donc innocents.")
  print("Les suspects après la première étape sont :",suspects)
  print("Les innocents après la première étape sont :",innocents)
  pesée2a = A + F + G + H 
  pesée2b = E + J + K + L
  sep
  print("On fait une pérmutation. On pèse AFGH contre EJKL.")
  if pesée2a > pesée2b:
    bouger_i(F)
    bouger_i(G)
    bouger_i(H)
    print("AFGH sont les gens les plus poidsées. F, G et H sont donc innocents.")
    print("Les suspects après la deuxième étape sont :",suspects)
    print("Les innocents après la deuxième étape sont :",innocents)
    sep
    print("On pèse A contre B.")
    if A == B:
      bouger_i(A)
      print("Les gens sont équilibrés. A et est donc innocents.")
      print("Les suspects après la deuxième étape sont :",suspects)
      print("Les innocents après la deuxième étape sont :",innocents)
      print("L'intru est donc E.")
    else:
      bouger_i(E)
      print("Les gens ne sont pas équilibrés. E est donc innocent.")
      print("Les suspects après la deuxième étape sont :",suspects)
      print("Les innocents après la deuxième étape sont :",innocents)
      print("L'intru est donc A.")
  elif pesée2a < pesée2b:
    bouger_i(A)
    bouger_i(E)
    print("E, J, K et L sont les plus poidsées. A et E sont donc innocents.")
    print("Les suspects après la deuxième étape sont :",suspects)
    print("Les innocents après la deuxième étape sont :",innocents)
    print("On sait donc aussi que l'intru pèse moins que le reste.")
    sep
    print("On pèse F contre G.")
    if F == G:
      bouger_i(F)
      bouger_i(G)
      print("Les gens sont équilibrés. F et G sont donc innocents.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc H.")
    elif F < G:
      bouger_i(G)
      bouger_i(H)
      print("G est plus poidsé que F. G et H sont donc innocents.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc F.")
    elif F > G:
      bouger_i(f)
      bouger_i(H)
      print("F est plus poidsé que G. F et H sont donc innocents.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc G.")
  elif pesée2a == pesée2b:
    bouger_i(A)
    bouger_i(F)
    bouger_i(G)
    bouger_i(H)
    bouger_i(E)
    bouger_i(J)
    bouger_i(K)
    bouger_i(L)
    print("Les gens sont équilibrés. A, F, G, H, E, J, K et L sont donc innocents.")
    print("Les suspects après la deuxième étape sont :",suspects)
    print("Les innocents après la deuxième étape sont :",innocents)
    print("On sait donc aussi que l'intru pèse plus que les reste")
    sep
    print("On pèse B contre C.")
    if B == C:
      bouger_i(B)
      bouger_i(C)
      print("Les gens sont équilibrés. B et C sont donc innocents.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc D.")
    elif B < C:
      bouger_i(B)
      bouger_i(D)
      print("C est plus poidsé que B. B et D sont donc innocents.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc C.")
    elif B > C:
      bouger_i(C)
      bouger_i(D)
      print("B est plus poidsé que C. B et D sont donc innocents.")
      print("Les suspects après la troisième étape sont :",suspects)
      print("Les innocents après la troisième étape sont :",innocents)
      print("L'intru est donc B.")
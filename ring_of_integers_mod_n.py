from math import gcd

def order (x, mod):
  #Iteratively find the (multiplicative) order of an element of the ring of integers modulo mod.
  #This function is only be called when x is coprime to mod, as otherwise necessarily x is not invertible and thus cannot have a multiplicative order.
  inc = 1
  y = x
  while y != 1:
    y = x**inc % mod
    inc = inc + 1
  if inc == 1:
    return inc
  else:
      return inc -1

def order2 (x,mod):
  #Used in order to apply a map.
  def F(x):
    return order(x,mod)
  return F

def coprimes(mod):
  #Find all elements coprime to a given natural number and also less than that number.
  list = []
  for i in range(1, mod):
    if gcd(i, mod) == 1:
      list.append(i)
  return list

def idempotents (mod):
  #Assuming mod >= 2, find all idempotents in the ring of integers modulo mod.
  #Recall that in any ring the additive and multiplicative identities are trivially idempotent.
  list = [0, 1]
  for i in range(2,mod):
    if i**2 % mod == i:
      list.append(i)
  return list

def self_inverses (mod):
  #Assuming mod >= 2, find all self-inverses modulo mod, if any exist.
  #The multiplicative identity element is always self-inverse.
  list = [1]
  for i in range(2,mod):
    if i**2 % mod == 1:
      list.append(i)
  return list

def residues (res, mod):
  #Assuming mod >= 2, find all quadratic residues of res modulo mod, if any exist.
  list = []
  for i in range(1, mod):
    if i**2 % mod == res:
      list.append(i)
  return list

inp = input("Choose from a number of functions relating to the ring of integers modulo n. Notice here that in all cases n is taken to be an integer greater than 1. \n Type one of the following handles to access the corresponding function: \n  \n ord: Find the multiplicative orders of non-zero-divisors in the ring of integers modulo n \n res: Find all quadratic residues (if any) of a given integer modulo n. \n idem: Find all idempotents in the ring of integers modulo n. \n selfinv: Find all (multiplicatively) self-inverse elements in the ring of integers modulo n. \n")

if inp == "ord":
  n1 = input("Enter any integer greater than 1:")
  try:
    n = int(n1)
    if n < 2:
      print("Given integer must be greater than 1.")
    else:
      x = coprimes(n)
      print("Multiplicative orders of non-zero-divisors of the integers modulo " + str(n))
      for i,j in zip(x, list(map(order2(x, n), x))):
        print("Ord([" + str(i) + "])" + ": " + str(j))
  
  except ValueError:
    print("User has not entered a valid integer.")
elif inp == "res":
  m1 = input("Enter an integer: ")
  n1 = input("Enter a modulus greater than 1: ")
  try:
    n = int(n1)
    m = int(m1) % n
    if n < 2:
      print("Modulus must be greater than 1.")
    else:
      print("The integer " + m1 + " modulo " + n1 + " is the equivalence class [" + str(m) + "].")
      lst = residues(m, n)
      if len(lst) == 0:
        print("The equivalence class [" + str(m) + "] is not a quadratic residue modulo " + n1 + ".")
      else:
        print("The residues of " + str(m) + " modulo " + n1 + " are given by the following list:")
        print(*lst, sep = ", ")
  except ValueError:
    print("User has not entered valid inputs.")
elif inp == "idem":
  n1 = input("Enter a modulus greater than 1:")
  try:
    n = int(n1)
    if n < 2:
      print("Modulus must be greater than 1.")
    else:
      print("The idempotents in the ring of integers modulo " + n1 + " are given by: ")
      print(*idempotents(n), sep = ", ")
  except ValueError:
    print("User has not entered valid inputs.")
elif inp == "selfinv":
  n1 = input("Enter a modulus greater than 1:")
  try:
    n = int(n1)
    if n < 2:
      print("Modulus must be greater than 1.")
    else:
      print("The self-inverses in the ring of integers modulo " + n1 + " are given by: ")
      print(*self_inverses(n), sep = ", ")
  except ValueError:
    print("User has not entered valid inputs.")
else:
  print("Keyword does not match aforementioned handles.")



pow :: Integer -> Integer -> Integer
pow _ 0 = 1
pow 0 _ = 0
pow x n
       | even n = sqrHalf
       | otherwise = x * sqrHalf
       where
          halfn = n `div` 2
          sqrHalf = sqr (pow x halfn)
          sqr k = k*k

order1 :: Integer -> Integer -> Integer -> Integer
--Used in the definition of 'order: Integer -> Integer -> Integer' to find the (multiplicative) order of an element x of the ring of integers modulo n.
--This function is only be called when x is coprime to n, as otherwise necessarily x is not invertible and thus cannot possess a multiplicative order.
order1 x n m
          | (pow x m) `mod` n == 1 = m
          | otherwise = order1 x n (m+1)

order :: Integer -> Integer -> Integer
order x n = order1 x n 1

coprimes :: Integer -> [Integer]
--Notice that n will never be coprime to n so we may omit this from the list. The integer n will be assumed to be greater than or equal to 2 as this is the only case where the ring of integers modulo n makes sense and is finite.
coprimes n = [x | x <- [1..n-1], gcd x n == 1]

idempotents :: Integer -> [Integer]
--We append 0,1 to the list because 0,1 are trivially idempotent in any ring with multiplicative identity.
idempotents n = 0:1:[x | x <- [2..n-1], x*x `mod` n == x]

self_inverses :: Integer -> [Integer]
--Find all self-inverse elements in the ring of integers modulo n. Notice that the multiplicative identity is always trivially self-inverse, as is the equivalence class -1 modulo n for n > 2. Moreover the zero element (equivalence class n modulo n) is never invertible and hence has no self-inverse.
self_inverses 2 = [1]
self_inverses n = 1:[x | x <- [2..n-2], x*x `mod` n == 1]++[n-1]

residues :: Integer -> Integer -> [Integer]
--Find all x such that x**2 modulo n equates to q modulo n for 0 <= q < n.
residues q n = [x | x <- [0..n-1], x*x `mod` n == q `mod` n]


main = do
  print (residues 6 5)


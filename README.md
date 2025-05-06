# Password_Gen_Locker
A Password Generator and Locker

I am definitely not trying to recreate the wheel. There are definitely better options to create and store passwords. This is just to illustrate a few concepts.

The two driving factors to password security are:
1. Length
2. Complexity

The longer the password the more time it will take to guess.
The number of options scales with each additional character. The math formula is 26^X. Where X is the number of characters in the password.
| Num_characters | Formula | Options |
|---------------|---------|---------|
| 1             | 26^1    | 26      |
| 2             | 26^2    | 676      |
| 3             | 26^3    | 17,576     |
| 5             | 26^5    | 11,881,376      |
| 10             | 26^10    | 141,167,095,653,376      |
| 14            | 26^14    | 64,509,974,703,297,150,976      |


The more complex a password the harder it is to guess.
Simply adding in the possibility of uppercase letters makes it much harder to guess.
| Num_characters | Formula | Options |
|---------------|---------|---------|
| 1             | 52^1    | 52      |
| 2             | 26^2    | 2,704      |
| 3             | 26^3    | 140,608    |
| 5             | 26^5    | 550,731,776      |
| 10             | 26^10    | 303,305,489,096,114,176      |
| 14            | 26^14    | 2,982,856,619,293,778,479,415,296      |

# Password Generator and Manager
A Password Generator and Manager

I am definitely not trying to recreate the wheel. There are definitely better options to create and store passwords. This is just to illustrate a few concepts.
The passgen.py file will allow a user to create a password. It then asks if they want to store the password in a locker.

The passlocker file uses the password created and asks for a username. The password is then hashed and stored in a dictionary.
The contents of the dictionary are deleted once the program stops runnings
!!!!DO NOT RELY UPON THIS FOR AN ACTUAL PASSWORD MANAGER!!!!!

This is just a concept.

The three driving factors to password security are:
1. Length
2. Complexity
3. Unique

First, Length
The longer the password the more time it will take to guess.
The number of options scales with each additional character. If we limit our password to only lower case letters in the english alphabet then the math formula is 26^X. 
Where X is the number of characters in the password.
The table below shows how many options are available with only lower case letters for a given number of characters in a password.
| Num_characters | Formula | Options |
|---------------|---------|---------|
| 1             | 26^1    | 26      |
| 2             | 26^2    | 676      |
| 3             | 26^3    | 17,576     |
| 5             | 26^5    | 11,881,376      |
| 10             | 26^10    | 141,167,095,653,376      |
| 14            | 26^14    | 64,509,974,703,297,150,976      |


Second, Complexity
The more complex a password the harder it is to guess.
Simply adding in the possibility of uppercase letters makes it much harder to guess.
Adding in numbers, and special characters will also make it harder.
Looking at these two tables, a 14 character password with upper and lower case letters adds 5 more digits worth of options.
| Num_characters | Formula | Options |
|---------------|---------|---------|
| 1             | 52^1    | 52      |
| 2             | 26^2    | 2,704      |
| 3             | 26^3    | 140,608    |
| 5             | 26^5    | 550,731,776      |
| 10             | 26^10    | 303,305,489,096,114,176      |
| 14            | 26^14    | 2,982,856,619,293,778,479,415,296      |

Third, Unique
This means you should:
1. Never reuse passwords! That is what a password manager is for.
2. Never use easy passwords like: password, password1234, companyname9876

Cybercriminals have lists of common passwords that make their job at cracking your password easier.
If you must create a password and can't store it in a password manager, think of it as a passphrase.
For example:
"Mj#wIpcsw27!" That is an acronym for "My jersey number when I played college soccer was 27" It was not my number because I did not play soccer in college :P
"C@tzEetbrwnM!ce" Cats eat brown mice.

A passphrase can be remembered easier than a string of random characters, and is just as effective. Just avoid using plain words.
There are things called Leetspeek convertes that will help transform your text.

Here is an option.
https://simpletools4u.com/leetspeak-converter/

*Password Manager*
Passwords should never be stored in plain text. Plain text means the password is not encrypted, or jumbled up. If a hacker got access to the password database that was not encrypted then they could immediately login.

Without going into detail passwords should be stored as hashs. Hashs are irreversible mathematical functions. Which means you can go from A -> B but not B -> A. You can hash a password, but you cannot unhash it.
Like password lists, or dictionaries, criminals also have hash dictionaries, which function the same way. They have a password, and its hashed version. If they get access to a password database that contains hashed passwords they can perform a simple look up to find a matching hasing.
To protect against this, and is not shown in this code is to add "salt" to your password. This is just extra random characters to make the hash even harder to crack.

Key takeaways:
1. Make your password long
2. Add complexity
3. Never reuse passwords
4. Use passphrases if necessary
5. Hash and salt your password.



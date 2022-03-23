# Password_Checker
A secure way for you to check if the passwords you use in real life have ever been hacked.

Securely checks if your password has ever been compromised.

With a basic online password checker, you could potentially give your password to a hacker. When you use this code to check if your password has been compromised, you eliminate any possibility that a hacker could get it.

Passwords are retrieved from a text file that you can delete later. It then uses SHA1 to hash your password/s, but it breaks them into two parts since that could also be used to determine what your password is. Pwnedpasswords.com api returns a list of possible passwords based on the first piece of information (5 characters). With the second piece (the rest of the characters), it locates the password/s matching the list. Finally, we'll mention the number of times your password has been compromised and if it has been found in a hack.

Don't forget to run "pip install requests" if you are running this on your own machine.

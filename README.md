# jazz2crack
Tools for removing and bruteforcing passwords in .j2l files for the game Jazz Jackrabbit 2

## Removing passwords:
Start the script removePW.py with the file you want to remove the password from as argument.
> python removePW.py mapFile.j2l

Basically the script overrides the 3 bytes where the hashed password is saved with 0x0. When opening the Map in JCS you can now enter an empty password.

## Cracking passwords:
Start the script crackPW.py with the file and the desired charset as follows:
> python crackPW.py mapFile.j2l CHARSET

Where CHARSET is a combination auf the charsets you want to use:
- u: Uppercase chars
- l: Lowercase chars
- n: Numbers
So if you want to bruteforce using numbers and lowercase chars use the command
> python crackPW.py mapFile.j2l ln

The method to save the passwords in the mapfile is basically a crc32 checksum where only the lower 3 bytes are used. Because of that, there is a huge chance for finding a collision which works, instead of the original password. Beause of that using only the uppercase charset will nearly always find a password with length 8.

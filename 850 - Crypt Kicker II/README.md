# 850 - Crypt Kicker II

A common but insecure method of encrypting text is to permute the letters of the alphabet. That is,
in the text, each letter of the alphabet is consistently replaced by some other letter. So as to ensure
that the encryption is reversible, no two letters are replaced by the same letter.
A common method of cryptanalysis is the known plaintext attack. In a known plaintext attack, the
cryptanalist manages to have a known phrase or sentence encrypted by the enemy, and by observing
the encrypted text then deduces the method of encoding.
Your task is to decrypt several encrypted lines of text, assuming that each line uses the same set of
replacements, and that one of the lines of input is the encrypted form of the plaintext

**the quick brown fox jumps over the lazy dog**


## Input

**The input begins with a single positive integer on a line by itself indicating the number
of the cases following, each of them as described below. This line is followed by a blank
line, and there is also a blank line between two consecutive inputs.**

The input consists of several lines of input. Each line is encrypted as described above. The encrypted
lines contain only lower case letters and spaces and do not exceed 80 characters in length. There are
at most 100 input lines.


## Output

**For each test case, the output must follow the description below. The outputs of two
consecutive cases will be separated by a blank line.**

Decrypt each line and print it to standard output. If there is more than one possible decryption
(several lines can be decoded to the key sentence), use the first line found for decoding.
If decryption is impossible, output a single line:
No solution.


## Sample Input

```bash
1

vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq
xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj
frtjrpgguvj otvxmdxd prm iev prmvx xnmq
```

## Sample Output

```bash
now is the time for all good men to come to the aid of the party
the quick brown fox jumps over the lazy dog
programming contests are fun arent they
```

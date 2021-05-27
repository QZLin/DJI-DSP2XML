from binascii import a2b_base64
from Cryptodome.Cipher import AES

key = b'TRoP4GWuc30k6WUp'
iv = b'bP3crVEO6wABzOc0'

aes = AES.new(key, AES.MODE_CBC, iv)
decrypt_aes = AES.new(key, AES.MODE_CBC, iv)

code_base64 = "aXb5+G/vlWMXsoo7FLIu6EGleERqc+y1eMMV3UEtCF6TMSyrmWjESTHCXErHEIKnZ3nbLvFq3/3g/d" \
              "/jFUVLBzBM5ujRqLfR3VSLPtmdx4YlJCmeOHhtv4JoEmY0yn9FlvM20LlgPtyHY7Z5l7MIAJHuZfo1KEFORl4e4" \
              "/4CT5IfuYkL1GJPxqaSiqveqmkSaFk/J87rpNcUycow5njBh5V7yNr0wwy7Vof775qHp7Eo5hWTbPnXAdf7lDrx/7ZLGpTZoo" \
              "+JKR6ulBIuNLlES/SZ960GLIPTZWSli2+FSqusLBfpVi8lwhXd2nRmgUhvgeEvLDLmep0JGw" \
              "+yFTadL4uMrcruspP5zfwdDQ35DQ0vg15/4a6oU7bUEmP+F579eDs08oOhE57gKLwV+/Xc+l3FkRELtq4E4MDgJzdZ" \
              "/e7QgdbzONkVGvnlfFBg04eSXGGq8KyqtH2+wQ8Z1InUdRSPhok294jCJ1hDYSE" \
              "+NCXPBVa0JnFq9UPnKJiV9eshT9kywgidAfenn8OtKwLIgIaFOv" \
              "+ZVEVTGOTzKA0JLIclvXrI86iKRYmBWiIdWASgiAk2F3guI7lUWus4gLRvMfbKkk6JPXPy7ORu5PkZLAFkZuhtv" \
              "/5U9tLBzeeYD39YwAxTDcjj9cbdJt8vPkEtT365/bba7VbQdeEfXUzOUJntlrCVa2ldveVl9/1do+zkY9H8kTyNl/FeJLtm" \
              "+QhN5IuTP4ZE8NttyDiuIPneAZJvSNNxIdUhzshlODJVyFSCBXxG+XbcuBBPVTj10h5qdxPRPliQ2/7mg" \
              "+sqXTlInK5QZIRsY7T0YBdBIdYb0Z/MZ6sHp4vwmj5frKJg2RCCgI2qPyQojgxYvkXOC10Y8Ebq6A6+vVr77aET48/dRfuIwhQ" \
              "/KBsYYQYtl9noEw2Bw6jQTECF5WqWWma3rKy7+eX/MJtFGf6kbTV9ZiPAkNj+Hsx0x+9aOc0Ar5mcICbsAZTWwbfU" \
              "+6Hc53dPN0x4K8918EmuRntFAHiPR8uymTBzu6Jc2Gki5GdPH1oxXkZzE" \
              "+f9OZMJqPatXWQki44e91R6kH0aNfxXfUcFYP2W3axhbKOmbPW0teFYelXmG4D5COWREJ+bZFKDvbcb6bxg0nrP2a" \
              "+yPHQ837hcy618hL+1ZENB71A8H9QBo/X6bJolwHjQxo9LIqyhCJ" \
              "/eGuHDNbb5ZRUndHGTKVh7av4iSgxeLNNEUbWjSNHK0UxZ3KckqwhFEW1CiEkRHzwEBl7EuNMWDYBrBuaCp/nE59hX23Ys" \
              "/PIDVL437hJpuQL0JMT/tP1XRqOG1RV7lOnAcIgiHJD9IoQuiwssTFY+jkmmbpIdpru8H08qyhGqDgaHYoR/jp+uXuW+NDlg3XSSB" \
              "/57QSNj6WpWX064Nmr0AQH4zWaVmrGVZ3Wka0hQ2i73Oc7HO6JZu7rehCZYIuiW4BZh7wwpO913fSc" \
              "+LVDoz20JpiCBhC22lWwVzHWTu5V+T0DRtt8pnSZUwClTiHzcWYLkkEq/pw/aFEzyQyFK45KAso0H "
print(bytes.decode(decrypt_aes.decrypt(a2b_base64(
    code_base64))))

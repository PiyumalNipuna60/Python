x = "piyumal"

# ----- print normal---
print("x : " + x);  # piyumal

# ----- first latter capital ----
print("x.capitalize() : " + x.capitalize());  # Piyumal

# ----- all latter capital ----
print("x.upper() : " + x.upper())  # PIYUMAL

# ----- all latter simple ----
print("x.lower() : " + x.lower())  # piyumal

# ----- first latter print ----
print("x[0] : " + x[0])  # p

# ----- 2-... latter print ----
print("x[2:] : " + x[2:])  # yumal

# ----- ...-4 latter print ----
print("x[ :4] : " + x[:4])  # piyu

# ----- 2,3,4,5 latter print ----
print("x[2:6] : " + x[2:6])  # yuma

# ----- replace latter print ----
print("x.replace('l','K') : " + x.replace('l', 'K'))  # piyumaK

# ----- split (ven karanna)) ----
print(x.split('u'))  # ['piy', 'mal']

# ----- join (join karanna)) ----
z=x.split('a');
y = 'nipuna '.join(z)
print(y)  # piyumnipuna l

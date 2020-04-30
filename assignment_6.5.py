text = "X-DSPAM-Confidence:    0.8475";
a = text.find(":")
b = len(text)
x = text[a+1 : b]
x.strip()
print(float(x))
import re

texto = "Contacto: fernan@gmail.com, pietrantuono@gmail.com"
mails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print(mails)

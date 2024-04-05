import re
def Extract_money_value(text):
    money_value = re.search(r'R\$\s*([\d\.,]+)', text)
    if money_value:
        return money_value.group(1).replace('.', '').replace(',', '.')
    return None

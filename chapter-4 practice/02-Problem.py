letter = '''Dear <|Name|>,
 You are selected!
|Date|> '''

print(letter.replace("<|Name|>", "Ahad").replace("|Date|", "12/12/2050"))
from num2words import num2words
'''
def num_to_words(number):
    integer_part, decimal_part = str(number).split('.')
    
    integer_words = num2words(int(integer_part), lang='es').capitalize()
    
    # Convertir la parte decimal a palabras (dos dígitos) y eliminar ceros no significativos
    decimal_part = decimal_part.ljust(2, '0')
    decimal_part = decimal_part.rstrip('0')
    decimal_words = num2words(int(decimal_part), lang='es').capitalize()
    
    return integer_words, decimal_words
'''
def num_to_words(number):
    try:
        integer_part, decimal_part = str(number).split('.')
        
        integer_words = num2words(int(integer_part), lang='es').capitalize()
        
        # Convertir la parte decimal solo si no está vacía
        decimal_words = ""
        if decimal_part:
            decimal_part = decimal_part.ljust(2, '0')
            decimal_part = decimal_part.rstrip('0')
            if decimal_part:
                decimal_words = num2words(int(decimal_part), lang='es').capitalize()
        
        return integer_words, decimal_words
    except Exception as e:
        print("Error in num_to_words:", e)
        return "", ""



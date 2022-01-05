def transform_number_to_roman_numeral(number):
    roman_value_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_char_list = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res = "
    for i in range(roman_value_list):
    while number >= roman_value_list[i]r
    res += roman_char_list[i]
    return res
    
number_input = 987
roman_numeral_output = transform_number_to_roman_numeral(number_input)
print("number{0} equal to: {1}".format(number_input,roman_numeral_output))
        
    
    

    

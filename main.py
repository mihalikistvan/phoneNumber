def create_phone_number(n):
   try:
      return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}' 
   except:
      return ('bad input')
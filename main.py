import hashlib
while(True):
  user_id = int(input("\nWhat is your 3 digit UID?\n"))
  temp_pass = input("Whis is your 4 digit password?\n")
  is_validated = False
    # check if user is entered a password
  entered_password=False
    # if user entered a password
    #is_validated = False
  if len(temp_pass) > 3:
      entered_password = True
      temp_pass = int(temp_pass)
    
  
  def main():
    is_validated = False
    real_pass = ''
    real_salt = ''
    show_source = ''
    my_bool = 0
    check_hash= 0
    with open("UID.txt") as user_file:
      i = 0
      for x in user_file: 
         i = i + 1
         k = 0
         show_source=''
        # k = x
         if int(x) == user_id: # If user matches a user
          with open("Password.txt") as fp: # Open password db
            for y in fp:
                if temp_pass == int(y):   # If password matches that user
                  if my_bool < 1:
                   my_bool = my_bool + 1
                   real_pass = temp_pass
                  with open("Salt.txt",encoding='utf8') as salt: # open salts db
                   j = 1
                   for el in salt: 
                     if (j == i):
                       temp_salt = str(el.strip())
                       if my_bool < 2:
                         my_bool = my_bool + 1
                       hash = y.strip('\n')+temp_salt # password+salt =>
                       m = hashlib.md5()
                       m.update(hash.encode('utf-8')) # = GENERATE hash code
                       hash_code = m.hexdigest() 
                     
                       
                       with open("Hash.txt",encoding='utf8') as f: # open hashes db
                        for z in f:
                          password = y
                          source_hash = z.strip()
                          if source_hash == hash_code:  # check hash against db hash
                            if check_hash < 1:
                             show_source = source_hash
                             print(show_source)
                             check_hash= 1
                            if my_bool < 3:
                             is_validated = True
                             show_source = source_hash
                             real_salt = temp_salt 
                             
                             my_bool = my_bool + 1
                             
                            break
                     else :# End salt loop
                       j = j + 1    
      # End outter for-loop                 
      return (real_pass, real_salt, show_source, is_validated)
  #End Main
  def p_cracker():
    found_pass =''
    found_salt =''
    
    i = 0 
    with open("UID.txt") as user_file:
     for x in user_file:
       if int(x) == user_id:
         break
         continue
       else :
          i = i + 1
     j = 0
     with open("Password.txt") as fp:
      for x in fp:
       if j == i:
         found_pass = x
         break
         continue
       else:
         j = j + 1
      k = 0
      with open("Salt.txt") as f:
        for x in f:
         if k == i:
          found_salt = x
          break
         else:
           k = k + 1
    return(found_pass, found_salt)
  
    
  if entered_password == True:
    arr = main()
    real_pass = arr[0]
    real_salt = arr[1]
    show_source = arr[2]
    print(show_source)
    print('The input password and salt MATCHES the hash value in the database\n')
    answer = input("Another login? (y/n) \n")
    if answer != 'y':
      break
   
  else:
    print('The input password and salt does not match the hash value in the database...\n')
    answer = input("Crack it? ( y/n ) \n")
    if(answer=='y'):
      arr = p_cracker()
      print("Password: "+arr[0] +'\nSalt: '+arr[1]) 
    else:
      break
    
  


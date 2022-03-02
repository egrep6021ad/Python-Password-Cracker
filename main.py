import hashlib

while(True):   

  # Main password cracker  
  def main(is_validated):
    with open("UID.txt") as user_file: # For all lines in UID.txt
      i = 0
      for x in user_file: 
         if is_validated == True:
           break
         i = i + 1
         if int(x) == user_id:         # If user input matches UID entry
          with open("Password.txt") as fp: # For all lines in UID.txt
            for y in fp:
              if temp_pass == int(y):   # If password matches password entry
                with open("Salt.txt",encoding='utf8') as salt: #
                 j = 1
                 for el in salt:                    # For all lines in Salt.txt
                   if (j == i):                     # If the current line is in the sme row as the UID's row
                     temp_salt = str(el.strip())
                     hash = y.strip('\n')+temp_salt # password+salt => hash function
                     m = hashlib.md5()
                     m.update(hash.encode('utf-8')) #  GENERATE hash code
                     hash_code = m.hexdigest() 
                     with open("Hash.txt",encoding='utf8') as f: # For all lines in Hash.txt
                      for z in f:
                        if is_validated == True:                 # Optimize
                         break
                        source_hash = z.strip()
                        if source_hash == hash_code:             # Compare current lines hash with generated hash
                          print(f'\n Source  hash : {source_hash}')   # Print source hash_code
                          print(f'Generated hash: {hash_code}')     # Print generated hash_code
                          is_validated = True                    # Mark user as validated
                          break
                   else : # Otherwise, go to next salt entry
                     j = j + 1   
      # End outter for-loop                 
      return is_validated
  #End Main
  def p_cracker(found_pass, found_salt, i):
    with open("UID.txt") as user_file: # For all lines in UID.txt
     for x in user_file:              
       if int(x) == user_id:           # If current line matches user input
         break                         # Break such that i = the line number
         #continue                      
       else :
          i = i + 1
     j = 0                             # Set new line counter
     with open("Password.txt") as fp:  # For all lines in Password.txt
      for x in fp:          
       if j == i:                      # When the line numbers are the same
         found_pass = x                # The password has been found
         break
         #continue
       else:
         j = j + 1
      k = 0                            # Set new line counter
      with open("Salt.txt") as f:      # For all lines in Salt.txt
        for x in f:
         if k == i:                    # When the line number is the same as the UID line row
          found_salt = x               # The salt has been found
          break  
         else:
           k = k + 1
    return(found_pass, found_salt)     # Return the users password and salt 


    

  # Get user input
  user_id = int(input("\nWhat is your 3 digit UID?\n"))
  temp_pass = input("Whis is your 4 digit password?\n")

  # If the user entered a password make it an integer
  if len(temp_pass) > 3:
      temp_pass = int(temp_pass)
  # Check validation
  is_validated = main(False)
  # If the user is validated:
  if is_validated:
    print('\nThe input password and salt MATCHES the hash value in the database')
    answer = input("\nAnother login? (y/n) \n")
    is_validated = False
    if answer != 'y':
      break
  else:
    # If the user is NOT validated, give them a choice:
    print('The input password and salt does not match the hash value in the database...\n')
    answer = input("Crack it? ( y/n ) \n")
    # If user chose to crack password:
    if(answer=='y'):
      arr = p_cracker('','',0)
      print("Password: "+arr[0] +'\nSalt: '+arr[1]) 
    # Else allow them to attempt again
    else:
      continue
    
  


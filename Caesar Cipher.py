def caesar_cipher():
    
    def play_again():
                    ans=input("\nWould you like to encrypt or decrypt another set of text?(y/exit)").strip().lower()
                    
                    if ans=='y':
                        return caesar_cipher()
                    elif ans=='exit':
                        print("Thank you for checking out Caesar Cipher!!!")
                        return

                    else:
                        print("Invalid answer")
                        return play_again()
                    
    try:
        print("-----------Welcome to Caesar Cipher-----------")
        pt=input("\nWould you like to encrypt your text, or decrypt your text?(e/d/exit)").strip().lower()


        if pt == 'exit':
            return

        if pt not in ('e', 'd'):
            print("\nInvalid input!!!")
            return caesar_cipher()

        
        key=int(input("please specify key(1-25)"))


        if not (1 <= key <= 25):
            print("\nInvalid Input!!!\nReason:\nValue Out of Bounds")
            return caesar_cipher()

        direction=input("Please enter the direction of encryption.\n(left/right)").strip().lower()

        if direction not in ("left", 'right'):
            print("\nInvalid input!!!")
            print("please choose between left or right.")

            return caesar_cipher()
            
        def encryption():
            r_t=''
            u_t=str(input("Please provide the text to be encrypted:(only alphabets) "))
            if direction=='left':
                
                for i in u_t:
                    if i.isalpha():
                        d_t_n=ord(i)-key
                        
                        if i.isupper() and d_t_n<65:
                            key2=65-d_t_n
                            key2=90-key2
                            key2+=1
                            d_t=chr(key2)

                        elif i.islower() and d_t_n<97:
                            key2=97-d_t_n
                            key2=122-key2
                            key2+=1
                            d_t=chr(key2)
                        else:
                            d_t=chr(d_t_n)

                        
                        r_t+=d_t
                    elif i.isspace():
                        r_t+=' '
                print(r_t, "is your encrypted text.")
                play_again()
                return

        
            elif direction=='right':
                for i in u_t:
                    if i.isalpha():
                        d_t_n=ord(i)+key
                        
                        if i.isupper() and d_t_n>90:
                            key2=d_t_n-90
                            key2=65+key2
                            key2=key2-1
                            d_t=chr(key2)

                        elif i.islower() and d_t_n>122:
                            key2=d_t_n-122
                            key2=97+key2
                            key2=key2-1
                            d_t=chr(key2)
                        else:
                            d_t=chr(d_t_n)

                        
                        r_t+=d_t
                    elif i.isspace():
                        r_t+=' '
                print(r_t, "is your encrypted text.")
                play_again()
                return
            return

        def decryption():
            r_t=''
            u_t=str(input("Please provide the text to be decrypted:(only alphabets) "))
            if direction=='left':

                
                for i in u_t:
                    if i.isalpha():
                        d_t_n=ord(i)-key
                        
                        if i.isupper() and d_t_n<65:
                            key2=65-d_t_n
                            key2=90-key2
                            key2+=1
                            d_t=chr(key2)

                        elif i.islower() and d_t_n<97:
                            key2=97-d_t_n
                            key2=122-key2
                            key2+=1
                            d_t=chr(key2)
                        else:
                            d_t=chr(d_t_n)

                        
                        r_t+=d_t
                    elif i.isspace():
                        r_t+=' '


                print(r_t, "is your decrypted text.")
                play_again()
                return

            
            elif direction=='right':
                for i in u_t:
                    if i.isalpha():
                        d_t_n=ord(i)+key
                        
                        if i.isupper() and d_t_n>90:
                            key2=d_t_n-90
                            key2=65+key2
                            key2=key2-1
                            d_t=chr(key2)

                        elif i.islower() and d_t_n>122:
                            key2=d_t_n-122
                            key2=97+key2
                            key2=key2-1
                            d_t=chr(key2)
                        else:
                            d_t=chr(d_t_n)

                        
                        r_t+=d_t
                    elif i.isspace():
                        r_t+=' '
                print(r_t, "is your decrypted text.")
                play_again()
                
            return


        if pt=='e':
            encryption()

        elif pt=='d':
            decryption()
    except ValueError:
        print("\nInvalid input!!!")
        print(ValueError)
        caesar_cipher()



caesar_cipher()

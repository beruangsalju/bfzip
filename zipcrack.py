#!/bin/env/python
#sh0rtCut
#OmestGanz


'''imports'''
import zipfile


count = 1

with open('(WORDLISTLO TXT','rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('(TARGETZIPLO.ZIP','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''******************************\n[+] memek terpecahkan! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] memeknya sulit di jebol! - %s' % (number,password.decode('utf8')))
            count += 1
            pass



import os
import json
from time import sleep

data = open("Arseniy_Zaikin_py/Python_04/data.json", "r")
sp = json.loads(data.read())
data.close()
    

def add(sp, sex = 'Male', height = 178, weight = 70):
    login = str(input('Enter login - '))
    log = list.copy(sp)
    for i in range(len(log)):
        for k, v in log[i].items():
            while login == k:
                print('Fail')
                login = str(input('Enter login - '))
    sex = str(input('Enter sex(Male/Female) - '))
    while sex != ('Male' or 'Female'):
        print('Fail') 
        sex = str(input('Enter sex(Male/Female) - '))
    else: 
        None
    height = input('Enter height - ')
    while type(height) != int:
        try:
            height = int(height)
        except:
            print('Fail')
            height = input('Enter height - ')
    height = int(height)
    weight = input('Enter weight - ')
    while type(weight) != int:
        try:
            weight = int(weight)
        except:
            print('Fail')
            weight = input('Enter weight - ')
    weight = int(weight)
    sp.append({login: [sex, height, weight]})

def log_sp(sp, log = []):
    log = list.copy(sp)
    print('Users:')
    for i in range(len(log)):
        for k, v in log[i].items():
            print(' ', k)
    return log

def info(inf_req):
    log = list.copy(sp)
    for i in range(len(log)):
        for k, v in log[i].items():
            if k == inf_req:
                os.system('cls') 
                print(k, ':', '\nSex - ', v[0], '\nHeight - ', v[1], '\nWeight - ', v[2])
                BMI = round((v[2]/(v[1]**2))*10000, 2)
                print('BMI - ', BMI)
                if BMI > 60 or BMI < 10:
                    print('Impossible value')
                else:
                    BMI = round(BMI)
                    skale = '10' + '='*48 + '60'
                    print(skale[:BMI-10], '|', skale[BMI-10:], sep='=')
                break
            else:
                if i + 1 == len(log):
                    os.system('cls')
                    print('Fail')
        if k == inf_req:
            break
            
    
def change(n_req):
    log = list.copy(sp)
    for i in range(len(log)):
        for k, v in log[i].items():  
            if k == n_req:  
                slot_chg = input('Change(sex, height, weight)? - ')
                if slot_chg == 'sex':
                    info_chg = input('Enter new sex(Male/Female) - ')
                    while info_chg != 'Male' and info_chg != 'Female':
                        print('Fail')
                        info_chg = input('Enter new sex(Male/Female) - ')   
                    else: 
                        v[0] = info_chg
                    print('Changed')
                elif slot_chg == 'height':
                    info_chg = input('Enter new height - ')
                    while type(info_chg) != int:
                        try:
                            info_chg = int(info_chg)
                        except:
                            print('Fail')
                            info_chg = input('Enter height - ')
                    v[1] = int(info_chg)
                    print('Changed')
                elif slot_chg == 'weight':
                    info_chg = input('Enter new weight - ')
                    while type(info_chg) != int:
                        try:
                            info_chg = int(info_chg)
                        except:
                            print('Fail')
                            info_chg = input('Enter weight - ')
                    v[2] = int(info_chg)
                    print('Changed')
                else:
                    print('Fail')
            else:
                if i + 1 == len(log):
                    os.system('cls')
                    print('Fail')
        if k == n_req:
            break

def delete(sp, del_item):
    log = list.copy(sp)
    for i in range(len(log)):
        for k, v in list(log[i].items()):
            if k == del_item:
                sp.pop(i)
                print('User', del_item, 'deleted')
            else:
                if i + 1 == len(log):
                    print('Fail')
        if k == del_item:
            break



while True:
    os.system('cls')
    m_comand = input('List/Info/Change/Delete/Add/Exit\n')
    if m_comand == 'list':
        os.system('cls')
        log_sp(sp)

        input("Press Enter to continue...")
    elif m_comand == 'info':
        os.system('cls')
        log_sp(sp)
        inf_req = input('Choose user: ')
        info(inf_req)
        input("Press Enter to continue...")
    elif m_comand == 'change':
        os.system('cls')
        log_sp(sp)
        n_req = str(input('Choose user: '))
        os.system('cls')
        print('Choose user: ', n_req)
        change(n_req)
        data = open("Arseniy_Zaikin_py/Python_04/data.json", "w")
        data.write(json.dumps(sp))
        data.close()
        input("Press Enter to continue...")
    elif m_comand == 'delete':
        chk = 0
        os.system('cls')
        log_sp(sp)
        del_item = str(input('Choose user to delete: '))
        os.system('cls')
        delete(sp, del_item)
        data = open("Arseniy_Zaikin_py/Python_04/data.json", "w")
        data.write(json.dumps(sp))
        data.close()
        input("Press Enter to continue...")
    elif m_comand == 'add':
        os.system('cls')
        add(sp)
        os.system('cls')
        print('User added')
        data = open("Arseniy_Zaikin_py/Python_04/data.json", "w")
        data.write(json.dumps(sp))
        data.close()
        input("Press Enter to continue...")
    elif m_comand == 'exit':
        exit(0)
    elif m_comand == '':
        None
    else:
        print('Fail')
        sleep(0.1)
from admin import *

members = {
    1:{'kilat':0, 'sscepat':0, 'cepat':0, 'biasa':0}, # non member
    2:{'kilat':0, 'sscepat':0, 'cepat':0.05, 'biasa':0.1}, # bronze
    3:{'kilat':0, 'sscepat':0.05, 'cepat':0.1, 'biasa':0.15}, # silver
    4:{'kilat':0.05, 'sscepat':0.1, 'cepat':0.15, 'biasa':0.20}, # gold
    5:{'kilat':0.1, 'sscepat':0.2, 'cepat':0.5, 'biasa':0.7} # platinum
}          

def get_discount(x):
    if x == 0:
        x = 1

    elif x > 12:
        x = 5

    elif x <= 3:
        x = 2

    elif x <= 6:
        x = 3

    elif x <= 12:
        x = 4

    else:
        x = 1

    kilat = members[x]['kilat']
    sscepat = members[x]['sscepat']
    cepat = members[x]['cepat']
    biasa = members[x]['biasa']
    return kilat, sscepat, cepat, biasa


def generate_discount_price(name, method, prices):
    m_name, m_date = look_member(name)
            
    # convert membership year and month to month only so it can be subtracted to look membership type
    membership_date = int(m_date[0:4]) * 12 + int(m_date[5:7])
    converted_date = int(date[0:4]) * 12 + int(date[5:7])
    membership_counter = converted_date - membership_date

    kilat, sscepat, cepat, biasa = get_discount(membership_counter)

    match method:
        case 1:
            method = kilat

        case 2:
            method = sscepat

        case 3:
            method = cepat
            
        case 4:
            method = biasa

    a = prices * method
    # print(a)
    return a

# generate_discount_price("John", 1, 15000)

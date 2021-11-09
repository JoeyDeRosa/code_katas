'''My code for the SeaSick Snorkelling code kata.'''


def sea_sick(sea):
    '''Determin if the change from rough to calm water is over 20%.'''
    el_nino = 0
    for i in range(len(sea) - 1):
        if sea[i] != sea[i + 1]:
            el_nino += 1
    if el_nino / len(sea) > 0.2:
        return 'Throw Up'
    else:
        return 'No Problem'

import time

def epoch_to_data(vdata):
    vdata = str(vdata)[0:10]
    vdata = int(vdata)
    date_returned = time.strftime('%d-%m-%Y', time.localtime(vdata))
    date_returned = str(date_returned)

    return date_returned

# import this method and provide three parameter 
def bgnumber(nmb,min,say):
    rtn =''
    if nmb % min == 0:
        if nmb / min == 1:
            rtn = 'one' + " " + say
        else:
            reminder = nmb / min    # reminder 999/100 = 9
            rtn =  numb2word(reminder)+ " " + say 
    else:
        remnd = nmb % min     #9999/1000 = 999
        div10 = nmb - remnd    #9999 - 999 = 9000
        newdigit =   numb2word(remnd) 
        new10digit =  numb2word(div10) + 's'
        rtn = new10digit + ' ' + newdigit 
    return rtn






def numb2word(nmb):
    rtnable =''
    nmbr = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'tweenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    if nmb <=20:
        rtnable = nmbr[nmb]
    elif nmb > 20 and nmb<100: 
        if nmb % 10 == 0 : 
            rtnable = nmbr[nmb]
        else:
            remnd = nmb%10
            div10 = nmb-remnd
            newdigit = numb2word(remnd)
            new10digit = numb2word(div10)
            rtnable = new10digit + " " + newdigit
    min = 100 
    max = min*10
    say = 'Hundred'
    if nmb >= min and nmb <max:
        rtnable = bgnumber(nmb,min,say)
    # end of hundreds
                
    min = min *10           # 1000
    max = min * 100         #1000*100 = 100000
    say = 'thousand'
    if nmb>= min and nmb < min*100:
        rtnable = bgnumber(nmb,min,say)
    # end of thousands 

    min = min*100
    max = min * 100 
    say = 'lakh'
    if nmb >= min and nmb < min*100:
        rtnable = bgnumber(nmb,min,say)
    
    # end of lakh
    min = min*100
    max = min * 100 
    say = 'Crore'
    if nmb >= min and nmb<min*100:
        rtnable = bgnumber(nmb,min,say)

    #end of crore
    min = min*100
    max = min * 100 
    say = 'Arab'
    if nmb >= min and nmb<min*100:
        rtnable = bgnumber(nmb,min,say)
    # end of arab

    min = min*100
    max = min * 100 
    say = 'Kharab'
    if nmb >= min and nmb<min*100:
        rtnable = bgnumber(nmb,min,say)
    # end of kharab

    min = min*100
    max = min * 100 
    say = 'neel'
    if nmb >= min and nmb<min*100:
        rtnable = bgnumber(nmb,min,say)
    # end of neel

    min = min*100
    max = min * 100 
    say = 'padam'
    if nmb >= min and nmb<min*100:
        rtnable = bgnumber(nmb,min,say)
    # end of the padam

    min = min*100
    max = min * 100 
    say = 'Sankha'
    if nmb >= min and nmb<min*100:
        rtnable = bgnumber(nmb,min,say)
    # end of sankha

    say = 'mha sankh'
    min = min * 100
    max = min * 100
    if nmb >=min and nmb<min*100:
        rtnable = bgnumber(nmb,min,say)

    return(rtnable.capitalize())


   
# use numb2word(5) this function return in word 
#a = int(input('enter the number: ' ))
#print(numb2word(a))
    

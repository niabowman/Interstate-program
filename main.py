interstate_input_ns_odd = (5,15,25,35,45,55,65,75,85,95)
interstate_input_ew = (10,20,30,40,50,60,70,80,90)
invalid = (100,200,300,400,500,600,700,800,900)


inter_num = int(input())
aux = 0


if inter_num >= 101 and inter_num <= 199:
        aux = inter_num - 100
elif inter_num >= 201 and inter_num < 299:
        aux = inter_num - 200
elif inter_num >= 301 and inter_num < 399:
        aux = inter_num - 300
elif inter_num >= 401 and inter_num < 499:
        aux = inter_num - 400

elif inter_num >= 501 and inter_num < 599:
        aux = inter_num - 500
elif inter_num >= 601 and inter_num < 699:
        aux = inter_num - 600
elif inter_num >= 701 and inter_num < 799:
        aux = inter_num - 700
elif inter_num >= 801 and inter_num < 899: 
        aux = inter_num - 800
elif inter_num >= 901 and inter_num <= 999: 
        aux = inter_num - 900


if inter_num in invalid:
    print(f'{inter_num} is not a valid interstate highway number.')
elif inter_num in interstate_input_ns_odd:
    print(f'I-{inter_num} is primary, going north/south.')
elif inter_num in interstate_input_ew:
    print(f'I-{inter_num} is primary, going east/west.')
elif inter_num >= 100 and inter_num <=999:
    if inter_num % 2 == 0:
        print(f'I-{inter_num} is auxiliary, serving I-{aux}, going east/west.')
    elif inter_num % 2 > 0: 
        print(f'I-{inter_num} is auxiliary, serving I-{aux}, going north/south.')
else: 
    print(f'{inter_num} is not a valid interstate highway number.')
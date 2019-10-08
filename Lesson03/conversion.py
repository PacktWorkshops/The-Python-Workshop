def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

def convert_and_sum_list(usd_list, rate=0.75):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, rate=rate)
    return total

def convert_and_sum_list_kwargs(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, **kwargs)
    return total

print(convert_and_sum_list_kwargs([1, 3], rate=0.8))

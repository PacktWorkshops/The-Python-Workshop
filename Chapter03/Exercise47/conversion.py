def convert_and_sum_list_kwargs(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, **kwargs)
    return total

print(convert_and_sum_list_kwargs([1, 3], rate=0.8))

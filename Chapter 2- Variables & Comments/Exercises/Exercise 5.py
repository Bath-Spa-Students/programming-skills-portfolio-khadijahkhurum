
usb_stick_price = 10
total_budget = 35

num_usb_sticks = total_budget // usb_stick_price


remaining_pounds = total_budget % usb_stick_price


print("With £35, she can buy", num_usb_sticks, "USB sticks.")
print("She will have £", remaining_pounds, "left.")

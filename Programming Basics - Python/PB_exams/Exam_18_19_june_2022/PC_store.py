price_for_cpu_in_dollars = float(input())
price_for_video_in_dollars = float(input())
price_for_RAM_in_dollars = float(input())
number_of_rams = int(input())
percentage_discount = float(input())
price_cpu_bgn = price_for_cpu_in_dollars * 1.57 - ((price_for_cpu_in_dollars * 1.57) * percentage_discount)
price_video_bgn = price_for_video_in_dollars * 1.57 - ((price_for_video_in_dollars * 1.57) * percentage_discount)
price_ram_bgn = (price_for_RAM_in_dollars * 1.57) * number_of_rams
total_price = price_cpu_bgn + price_video_bgn + price_ram_bgn
print(f"Money needed - {total_price:.2f} leva.")

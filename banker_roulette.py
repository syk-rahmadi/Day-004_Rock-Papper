import random

names_list = list(map(str, input("Key in your name separated by space: ").split()))
number_of_names = len(names_list)
random_names = random.randint(0, number_of_names - 1)
today_boss = names_list[random_names]
print(f"Today {today_boss} will pay our neal. Yepeeee")
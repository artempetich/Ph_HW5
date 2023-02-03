def main():
    candies = 150
    enabel_bot = int(input("Включить игру с ботом (1), с другим игроком (0): "))
    print(f'На столе {candies} конфет')
    while candies > 0:
        pl_1 = int(input("Первый игрок вводит число от 1 до 28: "))
        candies -= pl_1
        print(f'Осталось {candies} конфет')
        if candies == 0:
            print("Первый игрок выигрывает")
            break
        if enabel_bot:
            pl_2 = bot_choice(candies)
        else:
            pl_2 = int(input("Второй игрок вводит число от 1 до 28: "))
        candies -= pl_2
        if enabel_bot:
            print(f'Второй игрок взял {pl_2} конфет')
        print(f'Осталось {candies} конфет')
        if candies == 0:
            print("Второй игрок выигрывает")
            break

def bot_choice(candies):
    if candies <= 28: return candies
    if not candies % 28: return 27
    if candies % 28: return candies % 28
    else: return 1

if __name__ == '__main__':
    main()
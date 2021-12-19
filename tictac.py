blocks  = {1: ' ' ,2: ' ' ,3: ' '
           ,4: ' ' ,5: ' ' ,6: ' '
           ,7: ' ' ,8: ' ' ,9: ' ' }

blocks_key = []

for key in blocks:
    blocks_key.append(key)

def printblock(block):
    print(block[1] + '|' + block[2] + '|' + block[3])
    print('-+-+-+')
    print(block[4] + '|' + block[5] + '|' + block[6])
    print('-+-+-+')
    print(block[7] + '|' + block[8] + '|' + block[9])

def game():

    turn = 'x'
    count = 0
    n = 0
    a = 0


    for i in range(100):
        printblock(blocks)
        try:
            print("It's your turn," + turn + ".Move to which place?")
            move = int(input())
        except ValueError:
            print("wrong Input!")
            continue

        if move < 1 or move > 9:
            print("wrong input, please re-enter\n")
            count = count + 1
            continue

        if   blocks[move] == ' ':
             blocks[move] = turn
             count += 1
        else:
            print("that place is already filled. \nMove to which place?")
            count += 1
            continue

        if count >=5:
            if blocks[7] == blocks[8] == blocks[9]!= ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
            elif blocks[4] == blocks[5] == blocks[6]!= ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
            elif blocks[1] == blocks[2] == blocks[3]!= ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
            elif blocks[1] == blocks[4] == blocks[7] != ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
            elif blocks[2] == blocks[5] == blocks[8] != ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
            elif blocks[3] == blocks[6] == blocks[9]!= ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
            elif blocks[7] == blocks[5] == blocks[3]!= ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
            elif blocks[1] == blocks[5] == blocks[9]!= ' ':
                printblock(blocks)
                print("\nGame is over\n")
                print(" **** " + turn + " won. ****")
                n += 1
                break
        if count >= 9:
            for x in range(1, 10):
                if blocks[x] != ' ':
                    a += 1
                if a == 9:
                    print("Game is over")
                    print("It is a Tie")
                    n +=1
                    break
            if a ==9:
                break




        if turn =='x':
            turn = 'O'
        else:
            turn = 'x'

    if n == 1:
        restart = input('do you want to play again?(y/n)')
        if restart == 'y' or restart == 'Y':
            for key in blocks_key:
                blocks[key] = ' '
        game()

if __name__ == "__main__":
    game()

def init():
    filename = 'inputs/input4.txt'
    with open(filename) as f: all = f.read()

    numbers = [int(x) for x in all.split('\n')[0].split(',')]
    cards = [x.split('\n') for x in all.split('\n\n')[1:]]
    for card_number in range(0,len(cards)):
        for line_number in range(0,len(cards[card_number])):
            cards[card_number][line_number]=[int(x) for x in cards[card_number][line_number].split()]
    return numbers, cards

def mark_number_in_all_cards(number, cards):
    for card_number in range(0,len(cards)):
        for line_number in range(0,len(cards[card_number])):
            cards[card_number][line_number] = [-1 if x == number else x for x in cards[card_number][line_number]]

def vertical_line_found(card):
    for line in card:
        if all(x == -1 for x in line):
            return True
    return False

def horizontal_line_found(card):
    for col_number in range(0,len(card[0])):
        found = True
        for line in card:
            if line[col_number] != -1: found = False
        if found: 
            return True
    return False

def check_line_in_list_of_cards(all_cards, cards_to_check):
    cards_with_lines_found = []
    for card_number in range(0,len(all_cards)):
        if card_number in cards_to_check and (vertical_line_found(all_cards[card_number]) or horizontal_line_found(all_cards[card_number])):
            cards_with_lines_found.append(card_number)
    return cards_with_lines_found

def get_sum_of_remaining(card):
    total = 0
    for line in card:
        for number in line:
            if number >= 0: 
                total += number
    return total

def part1():
    numbers, cards = init()
    for number in numbers:
        mark_number_in_all_cards(number, cards)
        winning_cards_numbers = check_line_in_list_of_cards(cards, [x for x in range(0,len(cards))])
        if len(winning_cards_numbers) > 0:
            sum_of_remaining = get_sum_of_remaining(cards[winning_cards_numbers[0]])
            print("Solution part 1: " + str(number * sum_of_remaining))
            break

def part2():
    numbers, cards = init()
    incomplete_cards_numbers = [x for x in range(0,len(cards))]

    for number in numbers:
        mark_number_in_all_cards(number, cards)
        winning_cards_numbers = check_line_in_list_of_cards(cards, incomplete_cards_numbers)

        for card_number in winning_cards_numbers: 
            incomplete_cards_numbers.remove(card_number)
        
        if len(incomplete_cards_numbers) == 1:
            unlucky_card_number = incomplete_cards_numbers[0]
        elif len(incomplete_cards_numbers) == 0:
            sum_of_remaining = get_sum_of_remaining(cards[unlucky_card_number])
            print("Solution part 2: " + str(number * sum_of_remaining))
            break

if __name__ == '__main__':
    part1()    
    part2()



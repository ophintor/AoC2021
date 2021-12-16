def init():
    filename = 'inputs/input16.txt'
    with open(filename) as f:         
        hex = f.read()
    
    return bin(int(hex, 16))[2:].zfill(4)
    

def process_literal(packet, tracking_info):
    literal_value_bin = ""
    while True:
        literal_value_bin += packet[tracking_info["index"]+1:tracking_info["index"]+5]
        if packet[tracking_info["index"]] == "0":
            tracking_info["index"] += 5
            break
        tracking_info["index"] += 5
    tracking_info["expression"].append(int(literal_value_bin, 2))


def is_literal_value(packet, tracking_info):
    return (packet[tracking_info["index"]:tracking_info["index"]+3] == "100")


def get_operator(packet, tracking_info):
    if packet[tracking_info["index"]:tracking_info["index"]+3] == "000":
        tracking_info["expression"].append("+")
    elif packet[tracking_info["index"]:tracking_info["index"]+3] == "001":
        tracking_info["expression"].append("*")
    elif packet[tracking_info["index"]:tracking_info["index"]+3] == "010":
        tracking_info["expression"].append("min")
    elif packet[tracking_info["index"]:tracking_info["index"]+3] == "011":
        tracking_info["expression"].append("max")
    elif packet[tracking_info["index"]:tracking_info["index"]+3] == "101":
        tracking_info["expression"].append(">")
    elif packet[tracking_info["index"]:tracking_info["index"]+3] == "110":
        tracking_info["expression"].append("<")
    elif packet[tracking_info["index"]:tracking_info["index"]+3] == "111":
        tracking_info["expression"].append("=")


def process_packet(binary_string, tracking_info):
    version = int(binary_string[tracking_info["index"]:tracking_info["index"]+3], 2)
    tracking_info["version"] += version
    tracking_info["index"] += 3

    if is_literal_value(binary_string, tracking_info):
        tracking_info["index"] += 3
        process_literal(binary_string, tracking_info)
    else:
        tracking_info["expression"].append("(")
        get_operator(binary_string, tracking_info)
        tracking_info["index"] += 3
        length_type_id = binary_string[tracking_info["index"]]
        tracking_info["index"] += 1
        if length_type_id == "0":
            total_packet_length = int(binary_string[tracking_info["index"]:tracking_info["index"]+15], 2)
            tracking_info["index"] += 15
            index_target = tracking_info["index"] + total_packet_length
            while tracking_info["index"] < index_target:
                process_packet(binary_string, tracking_info)
        elif length_type_id == "1":
            number_of_packets = int(binary_string[tracking_info["index"]:tracking_info["index"]+11], 2)
            tracking_info["index"] += 11
            for _ in range(number_of_packets):
                process_packet(binary_string, tracking_info)
        tracking_info["expression"].append(")")


def collect_operands(expression, i):
    operands = []
    while i < len(expression) and isinstance(expression[i], int):
        operands.append(expression[i])
        i += 1
    return operands


def is_innermost_bracket(expression, index):
    innermost_bracket = False
    while expression[index] not in ('(', ')'):
        index += 1
    if expression[index] == ')':
        innermost_bracket = True
    return innermost_bracket


def process_expression(expression, index):
    operands = []

    if len(expression) > 1:
        while not (expression[index] == '(' and is_innermost_bracket(expression, index + 1)):
            index += 1
        
        index += 1
        operands = collect_operands(expression, index+1)
        
        if expression[index] == '+':
            expression[index + len(operands) + 1] = sum(operands)
        elif expression[index] == '*':
            product = 1
            for f in operands: product *= f
            expression[index + len(operands) + 1] = product
        elif expression[index] == 'min':
            expression[index + len(operands) + 1] = min(operands)
        elif expression[index] == 'max':
            expression[index + len(operands) + 1] = max(operands)
        elif expression[index] == '>':
            if operands[0] > operands[1]:
                expression[index + len(operands) + 1] = 1
            else:
                expression[index + len(operands) + 1] = 0
        elif expression[index] == '<':
            if operands[0] < operands[1]:
                expression[index + len(operands) + 1] = 1
            else:
                expression[index + len(operands) + 1] = 0
        elif expression[index] == '=':
            if operands[0] == operands[1]:
                expression[index + len(operands) + 1] = 1
            else:
                expression[index + len(operands) + 1] = 0

        index -= 1
        for _ in range(len(operands) + 2):
            del(expression[index])
        
        process_expression(expression, 0)


def part1():
    binary_string = init()
    tracking_info = {"version": 0, "index": 0, "expression": []}
    process_packet(binary_string, tracking_info)
    return tracking_info["version"]


def part2():
    binary_string = init()
    tracking_info = {"version": 0, "index": 0, "expression": []}
    process_packet(binary_string, tracking_info)
    process_expression(tracking_info["expression"], 0)
    return tracking_info["expression"][0]


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    

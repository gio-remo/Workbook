# problems : <class 'list'>

def arithmetic_arranger(problems, results=False):

    # Check of 'problems' list lenght
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        items = problem.rsplit(" ")

        # Check of opeators and operands correctness
        if items[1] != "+" and items[1] != "-": # only + or -
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        elif not items[0].isdigit() or not items[2].isdigit(): # only digits
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
        elif len(items[0]) > 4 or len(items[2]) > 4: # length
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

        first_op = items[0]
        second_op = items[2]
        operator = items[1]
        result = 0

        if operator == "+":
            result = int(first_op) + int(second_op)
        else:
            result = int(first_op) - int(second_op)

        result = str(result)
        print(result)

        temp1 = ""
        temp2 = ""
        temp3 = ""
        temp4 = ""

        if len(first_op) < len(second_op):
            l = len(second_op) - len(first_op)

            i = 0
            while i < l:
                temp1 += " "
                i += 1

            temp1 += "  " + first_op
            temp2 += operator + " " + second_op
            
            i = -2
            while i < len(second_op):
                temp3 += "-"
                i += 1
        else:
            temp1 = "  " + first_op

            l = len(first_op) - len(second_op)

            temp2 = operator + " "

            i = 0
            while i < l:
                temp2 += " "
                i += 1

            temp2 += second_op
            
            i = -2
            while i < len(first_op):
                temp3 += "-"
                i += 1
        
        if line1 == "":
            line1 = temp1
        else:
            line1 += "    " + temp1

        if line2 == "":
            line2 = temp2
        else:
            line2 += "    " + temp2

        if line3 == "":
            line3 = temp3
        else:
            line3 += "    " + temp3

        if results is True:
            l = len(temp3) - len(result)

            i = 0
            while i < l:
                temp4 += " "
                i += 1
            
            if line4 == "":
                line4 = temp4 + result
            else:
                line4 += "    " + temp4 + result
    
    if results is False:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3
        print(arranged_problems)
    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        print(arranged_problems)

    return arranged_problems
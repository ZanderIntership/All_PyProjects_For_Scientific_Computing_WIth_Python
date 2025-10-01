def arithmetic_arranger(problems, solve=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts

   
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

   
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."


        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

      
        width = max(len(num1), len(num2)) + 2

     
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes.append("-" * width)

        if solve:
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(width))

  
    arranged = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)
    if solve:
        arranged += "\n" + "    ".join(results)

    return arranged

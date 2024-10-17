import random
from tabnanny import check

# funcions, excercises

print("\n--- 1 ---")
def my_sum(a, b):
    print(f"suma: {a+b}")
my_sum(5,2)

print("\n--- 2 ---")
def PISq():
    return 9.8596
result = PISq()
print(f"pi squared: {result}")

print("\n--- 3 ---")
def mult(a,b):
    return a * b
result = mult(5, 10)
print(f"multiplication result: {result}")

print("\n--- 4 ---")
def print_members(my_list):
    for member in my_list:
        print(member)
print_members([1, 2, 3, "labas", False])

print("\n --- 5 ---")
def generate_rand_num(low, high):
    rand_num = random.randint(low, high)
    return rand_num
rand_num = generate_rand_num(10,20)
print(f"Random number: {rand_num}")

print("\n--- 6 ---")
def generate_random_numbers(low, high, length):
    result = [random.randint(low,high) for i in range(length)]
    return result
random_numbers = generate_random_numbers(1, 100, 10)
print(f"List of random numbers: {random_numbers}")

print("\n--- 7 ---")
def sum_random_numbers(randon_numbers):
    return sum(random_numbers)
result = sum_random_numbers(random_numbers)
print(f"Sum of random numbers: {result}")

print("\n--- 8 ---")
def avg_random_numbers(random_numbers):
    return sum(random_numbers)/len(random_numbers)
result = avg_random_numbers(random_numbers)
print(f"Avg of random numbers: {result}")

print("\n--- 9 ---")
def generate_rectangle(x_len, y_len):
    for y in range(y_len):
        print("*" * x_len)
generate_rectangle(20, 3)

print("\n--- 10 ---")
def count_symbols(sentence):
    spaces = sentence.count(" ")
    symbols = len(sentence) - spaces
    print(f"Sakinyje yra {spaces} tarpai")
    print(f"Sakinyje yra {symbols} raides (simboliai)")
sentence = "Siandien labai grazi diena"
count_symbols(sentence)

print("\n--- 11 ---")
def reverse_sentence(sentence):
    new_sentence = sentence[::-1]
    return new_sentence
result = reverse_sentence(sentence)
print(f"Apverstas sakinys: {result}")

# Uzduotys is funkciju medziagos:

print("\n--- 1 ---")
def about_me():
    print("Vardas: Tomas")
    print("Kodel pasirinktas programavimas? Patinka kurti dalykus")
about_me()
about_me()
about_me()

print("\n--- 2 ---")
def get_poem():
    print("Eilerascio pirma eile")
    print("Stai eina jau antra")
    print("Pabandom kurpti viena dar")
    print("Ir stai dabar gana")
    print("Psio!\n")

get_poem()
get_poem()
get_poem()
get_poem()
get_poem()

print("\n--- 3 ---")
def gen_text1():
    print("Generated text 1")
def gen_text2():
    print("Generated text 2")
def gen_text3():
    print("Generated text 3")
gen_text1()
gen_text2()
gen_text3()

print("\n--- 4 ---")
def gen_text1():
    print("Generated text 1")
def gen_text2():
    print("Generated text 2")
def call_functions():
    gen_text1()
    gen_text2()
call_functions()

print("\n--- 5 ---")
def gen_rand_and_sum():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f"{num1}+{num2}={num1+num2}")
gen_rand_and_sum()
gen_rand_and_sum()
gen_rand_and_sum()

print("\n--- 6 ---")
def policeman():
    name = "Jonas"
    surname = "Petraitis"
    age = 42
    wage = 1500
    workload = 0.8
    specialty = "Patrulis"

    print(f"{specialty} {name} {surname} (amz. {age} m.) dirba {workload} etato uz {wage} EUR alga")
policeman()

print("\n--- 7 ---")
def gen_rand_nums():
    nums = [random.randint(1,100) for i in range(10)]
    for num in nums:
        print(num,"\n")
gen_rand_nums()
gen_rand_nums()
gen_rand_nums()
gen_rand_nums()
gen_rand_nums()

print("\n--- 8 ---")
def gen_rand_num():
    print(random.randint(1,100))
for i in range(10):
    gen_rand_num()

print("\n--- 9 ---")
def say_hi(name):
    print(f"Labas, {name}!")
def say_bye(name):
    print(f"Viso gero, {name}!")
name = "Tomas"
say_hi(name)
say_bye(name)

print("\n--- 10 ---")
def compare_numbers(x, y):
    print(f"\nSkaiciai: {x} ir {y}")
    if x>y:
        print("Pirmas skaicius didesnis")
    elif x<y:
        print("Antras skaicius didesnis")
    else:
        print("Abu skaiciai lygus")
compare_numbers(2, 3)
compare_numbers(3,3)
compare_numbers(5,3)

print("\n--- 11 ---")
def describe_car(make, model, year, displacement):
    print(f"{make} {model}. Production year: {year}. Engine displacement: {displacement} L")
describe_car("Ford", "Mustang", 1968, 5.0)
describe_car("Porsche", "911 Turbo", 2024, 3.6)

print("\n--- 12 ---")
def get_sum(x, y):
    print(f"{x}+{y}={x+y}")
def get_subtraction(x, y):
    print(f"{x}-{y}={x-y}")
def get_muliplication(x, y):
    print(f"{x}*{y}={x*y}")
def get_division(x, y):
    print(f"{x}/{y}={round(x / y,1)}\n")
def implement_functions():
    x = random.randint(1,100)
    y = random.randint(1,100)
    get_sum(x,y)
    get_subtraction(x,y)
    get_muliplication(x,y)
    get_division(x,y)
implement_functions()
implement_functions()
implement_functions()

print("\n--- 13 ---")
def print_words(word_list):
    for word in word_list:
        print(f"{word} - {len(word)} raides")

word_list = ["mano", "atsitiktiniu", "zodziu", "masyvas"]
print_words(word_list)

print("\n--- 14 ---")
def get_derivatives(num_list):
    for num in num_list:
        print(f"Skaicius: {num}; kvadratas: {num**2}; kvadratas/2: {(num**2)/2}")

get_derivatives([1,2,3,4,5,8,6,1,5])
get_derivatives([54,215,3,51,5,5,24,4])

print("\n--- 15 ---")
def describe_student(name, surname, grades):
    print(f"Studentas {name} {surname}")
    print(f"Studento pazymiai: {grades}")
    print(f"Studento pazymiu vidurkis: {round(sum(grades)/len(grades),1)}\n")
describe_student("Tomas", "Ramanauskas", [10, 9, 8, 7, 9, 10])
describe_student("Jonas", "Petraitis", [9,6,7,8,6,9,10])

print("\n--- 16 ---")
def get_max(num_list):
    print(f"Didziausias skaicius is masyvp: {max(num_list)}")
def generate_random_numbers(num_list, length):
    for i in range(length):
        num_list.append(random.randint(1,100))
    return(num_list)

num_list1 = []
num_list2 = []
num_list3 = []
generate_random_numbers(num_list1, 10)
generate_random_numbers(num_list2, 5)
generate_random_numbers(num_list3, 3)

print(f"{num_list1}\n{num_list2}\n{num_list3}")

get_max(num_list1)
get_max(num_list2)
get_max(num_list3)


print("\n--- 17 ---")
def print_sentence(sentence):
    print(sentence)
print_sentence("Siandien puiki diena.")
print_sentence("Ir labai grazus oras.")

print("\n--- 18 ---")
def gen_random():
    return random.randint(1,100)
rand1 = gen_random()
rand2 = gen_random()
print(f"Sugeneruoti atsitiktiniai skaiciai: {rand1} ir {rand2}")


print("\n--- 19 ---")
def get_student_grade(name, grade):
    return f"Studentas: {name}. Vidurkis: {grade}"

student1 = get_student_grade("Tomas", 8.7)
student2 = get_student_grade("Jonas", 9)

print(student1)
print(student2)

print("\n--- 20 ---")
def get_lowest_divisor(num):
    for i in range(2,num+1):
        if num%i==0:
            print(f"Skaiciaus {num} maziausias daliklis: {i}")
            return i

for i in range(10,30):
    get_lowest_divisor(i)

print("\n--- 21 ---")
def check_if_primary(num):
    primary = False
    for i in range(2,num):
        if num%i==0:
            primary = False
            break
        primary = True
    if num == 2:
        primary = True
    return primary

for i in range(2,15):
    primary = check_if_primary(i)
    print(f"Skaicius {i} yra {"pirminis" if primary else "ne pirminis"}")

print("\n--- 22 ---")
def sum_2_nums(a, b):
    print(f"{a}+{b}={a+b}")
def sum_3_nums(a, b, c):
    print(f"{a}+{b}+{c}={a+b+c}")
def multiply_3_nums(a, b, c):
    print(f"{a}*{b}*{c}={a * b * c}")

def implement_functions():
    a = random.randint(1,100)
    b= random.randint(1,100)
    c = random.randint(1,100)
    sum_2_nums(a,b)
    sum_3_nums(a,b,c)
    multiply_3_nums(a,b,c)
implement_functions()

print("\n--- 23 ---")
def get_sum(num_list):
    return sum(num_list)
list1 = [1, 2,3,45,2]
list2 = [20,10,7,2]
sum1 = get_sum(list1)
sum2 = get_sum(list2)
print(f"Pirmo masyvo nariu suma: {sum1}")
print(f"Antro masyvo nariu suma: {sum2}")
if sum1>sum2:
    print("pirmoji suma didesne")
elif sum2>sum1:
    print("antroji suma didesne")
else:
    print("abi sumos lygios")

print("\n--- 24 ---")
def find_longest_word(word_list):
    word_list.sort(key= lambda x: len(x))
    return word_list[-1]
print(f"Zodziu sarasas: {word_list}")
longest_word = find_longest_word(word_list)
print(f"Ilgiausias zodis: {longest_word} ({len(longest_word)} raides)")

print("\n--- 25 ---")
def check_if_all_good_grades(grades):
    result = any(grade<5 for grade in grades)
    return result
grades1 = [7, 8, 9, 10, 9, 8, 10]
grades2 = [1,2,3,5,9,10,9,8]
all_good1 = check_if_all_good_grades(grades1)
all_good2 = check_if_all_good_grades(grades2)
print("1 studento pazymiai teigiami" if all_good1 else "1 studentas turi neigiamu pazymiu" )
print("2 studento pazymiai teigiami" if all_good2 else "2 studentas turi neigiamu pazymiu" )

print("\n--- 26 ---")
def sum_two_numbers(a, b=5):
    print(f"{a}+{b}={a+b}")
sum_two_numbers(10,10)
sum_two_numbers(10)


















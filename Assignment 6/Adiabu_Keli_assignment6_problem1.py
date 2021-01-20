# Sieve of Eratosthenes

n = int(input("Enter a positive number greater than or equal to 10: "))

while n < 10:
    n = int(input("Enter a positive number greater than or equal to 10: "))


def prime(num):
    prime_list = []
    num += 1
    new_list = ['P' for i in range(0, num + 1)]
    new_list[0] = 'N'
    new_list[1] = 'N'
    starts = 2
    while starts < num:
        while not new_list[starts] == 'P':  # doesn't even look at the Ns
            starts += 1
        prime_list.append(starts)  # add initial primes to list
        x = 2
        while (starts * x) < num:
            new_list[starts * x] = 'N'  # make multiples not prime
            x += 1
        starts += 1
    print("All prime numbers from 0 to", n)
    count = 0
    for i in prime_list:
        print(str(i), end=" "),
        count += 1
        if count % 10 == 0:
            print("")


prime(n)
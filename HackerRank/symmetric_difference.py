if __name__ == '__main__':

    english_count = int(input())
    if not (english_count > 0 & english_count < 1000):
        print("Total number of students in college not in range !!!")

    english = list(map(int, input().split()))
    english = english[0:english_count]
    english_set = set(english)

    french_count = int(input())
    if not (french_count > 0 & french_count < 1000):
        print("Total number of students in college not in range !!!")

    french = list(map(int, input().split()))
    french = french[0:french_count]
    french_set = set(french)

    print(len(english_set.symmetric_difference(french_set)))

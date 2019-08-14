#input: two strings
#output: boolean whether one string is a rotation of the other

#Run instructions:
#python3 string_rotation.py str1 str2

#Example: python3 string_rotation.py waterbottle erbottlewat => true
import sys

def string_rotation(str1: str, str2: str):
    if str1 is None or str2 is None or len(str1) != len(str2):
        return False

    double_str2 = str(str2 + str2)

    print(str1 in double_str2) # print output for testing
    return str1 in double_str2


if __name__ == "__main__":
    string_rotation(sys.argv[1], sys.argv[2])


# O(N) time, O(1) space
def validatingSubsequence(array, sequence):
    sequencePointer = 0

    for i in array:
        if sequencePointer < len(sequence):
            if i == sequence[sequencePointer]:
                sequencePointer += 1
            else:
                continue
    return sequencePointer == len(sequence)

# x = [5, 1, 22, 25, 6, -1, 8, 10]
# y = [5, 1, 22, 23, 6, -1, 8, 10]


# print(validatingSubsequence(x,y))

def validSubsequence(array, sequence):
    arrIdx = 0

    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1

        arrIdx += 1



    return seqIdx == len(sequence) - 1

# x = [5, 1, 22, 25, 6, -1, 8, 10]
# y = [5, 1, 22, 23, 6, -1, 8, 10]


# print(validSubsequence(x,y))
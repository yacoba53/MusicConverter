CHORD_CONSTANT_R = {'A': 0, 'B+': 1, 'B': 2, 'C': 3, 'C+': 4, 'D': 5, 'D+': 6, 'E': 7, 'F': 8, 'F+': 9, 'G': 10, 'G+': 11}
WRAP = len(CHORD_CONSTANT_R)
CHORD_CONSTANT = ['A', 'B+', 'B', 'C', 'C+', 'D', 'D+', 'E', 'F', 'F+', 'G', 'G+']
STANDARD_TUNE = ['E', 'A', 'D', 'G', 'B', 'E']
CENTER_OCTAVE = 2

C_MAJ = [[-1, 3, 2, 0, 1, 0], 'C']
D_MAJ = [[-1, -1, 0, 2, 3, 2], 'D']
G_MAJ = [[3, 2, 0, 0, 0, 3], 'G']
E_Min = [[0, 2, 2, 0, 0, 0], 'E-']


ALL_CHORDS = [C_MAJ,D_MAJ,G_MAJ,E_Min]

def findChordFromName(name):
    for chord in ALL_CHORDS:
        if chord[1] == name:
            return chord
    return None

def incrementChord(chord, increment, oct=0):
    startVal = CHORD_CONSTANT_R[chord]
    newVal = 0
    octIncrement = int(increment / WRAP) + oct + CENTER_OCTAVE
    chIncrement = increment % WRAP
    if (chIncrement + startVal) > WRAP:
        octIncrement += 1
    newVal = (chIncrement + startVal) % WRAP
    return [CHORD_CONSTANT[newVal], octIncrement]


def getRollForChordTune(chord, tune=STANDARD_TUNE):
    newRoll = []
    oct = 0
    for i in range(6):
        if i > 0 and oct <3:
            oct = 1
        if i > 3:
            oct = 2
        if chord[i] != -1:
            newRoll.append(incrementChord(tune[i], chord[i], oct))
        else:
            newRoll.append([tune[i], None])
    return newRoll


def printChord(chord):
    out = ""
    for x in chord:
        if x[1] == None:
            out += "X "
        else:
            out += x[0] + str(x[1]) + " "
    print(out)


def printChordList(chordList):
    for x in chordList:
        printChord(getRollForChordTune(x[0]))

def printChordNames(chordList):
    out = ""
    for x in chordList:
        out+= x[1]
    print(out)


def insertStringAtIndex(s, newS, index):
    s[:index] + newS + s[index:]

def processChordCSV(csv):
    chordNames = csv.split(",")
    chords = []
    for name in chordNames:
        chords.append(findChordFromName(name))
    return chords
def main():
    print("please input csv chords:::")
    x = input()
    chords=processChordCSV(x)
    printChordNames(chords)
    printChordList(chords)


if __name__ == "__main__":
    main()


#C,D,G,E-
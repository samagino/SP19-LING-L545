"""
orderthing.py - finds average object-verb word order of languages given conllu file
"""

import sys

def thing():
    OV = 0
    VO = 0

    line = sys.stdin.readline()

    while line:
        # comments begin with #, also wanna skip newlines
        if(line[0] == '#' or line == '\n'):
            line = sys.stdin.readline()
            continue

        line = line.split('\t')
        

        if (line[7] == 'obj'):
            if (int(line[6]) > int(line[0])):
                OV += 1
            else :
                VO += 1

        line = sys.stdin.readline()

    total = OV + VO
    OVRate = float(OV) / float(total)
    VORate = float(VO) / float(total)

    sys.stdout.write('Object Before Verb: ' + str(OVRate) + '\nVerb Before Object: ' + str(VORate) + '\n')


thing()

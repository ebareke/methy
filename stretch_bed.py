# modified version (for readability) of the original stretch_bed.py script coded by Dr. Simon Papillon while in Majewski Lab

import sys

def process_file(input_file, output_file, name):
    with open(input_file, 'r') as file_object, open(output_file, 'w') as output:
        output.write("#track color=255,000,000 midColor=255,255,255 altColor=000,000,255 viewLimits=0:100 midRange=50:50 graphType=heatmap\n")
        output.write("Chromosome\tStart\tEnd\tFeature\t{}\n".format(name))
        file_object.readline()
        prev_line = file_object.readline().rstrip('\n').split('\t')
        i = 1

        for line in file_object:
            cur_line = line.rstrip('\n').split('\t')
            
            if prev_line[0] == cur_line[0]:
                midpoint = str((int(prev_line[2]) + int(cur_line[1])) / 2)
                prev_line[2] = midpoint
                cur_line[1] = midpoint
            
            value = prev_line[3]
            prev_line[3] = str(i)
            prev_line.append(value)
            i += 1
            output.write('\t'.join(prev_line))
            output.write('\n')
            prev_line = cur_line

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_file name")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    name = sys.argv[3]
    process_file(input_file, output_file, name)

from Bio import SeqIO


handle = open('input.fasta','r')
fasta_sequences = SeqIO.parse(handle,'fasta')
sequence_IDs = []
sequences = []
for record in fasta_sequences:
    sequence_IDs.append(record.id)
    sequences.append(str(record.seq))
handle.close()


sorted_sequences = sorted(sequences, key=len)
shortest_sequence = sorted_sequences[0]
other_sequences = sorted_sequences[1:]
motif = ''


for i in range(len(shortest_sequence)):
    for j in range(i,len(shortest_sequence)):
        possible_motif = shortest_sequence[i:j+1]
        found  = False
        for seq in other_sequences:
            if possible_motif in seq:
                found = True
            else:
                found = False
                break
        if found and len(possible_motif) > len(motif):
            motif = possible_motif

print(motif)
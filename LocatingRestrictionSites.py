from Bio import SeqIO

record = SeqIO.read('input.fasta','fasta')
forward_seq = str(record.seq)
reverse_seq = str(record.seq.complement())


for i in range(0, len(forward_seq)):
    for j in range(i, len(forward_seq)):
        motif = forward_seq[i:j+1]
        rev_motif = reverse_seq[i:j+1]
        if len(motif) >= 4 and len(motif) <= 12:
            if motif == rev_motif[::-1]:
                print(i+1, len(motif))
				
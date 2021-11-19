from os import walk
import os

f = []
for (dirpath, dirnames, filenames) in walk('./seqs/'):
    f.extend(filenames)
    break

print('files: ',len(f))


for file in f:
	print(file)
	epi = file
	print(1)
	cmd = 'minimap2 -a ref.fasta seqs/'+file+' > output.sam' 

	os.system(cmd)
	
	print(2)
	
	cmd2 = ' samtools view -bS output.sam  | samtools sort > output.bam'
	os.system(cmd2)
	
	print(3)	
	cmd3 = 'bcftools mpileup -Ou -f ref.fasta  output.bam | bcftools call -Ou -mv | bcftools filter -s LowQual -e "%QUAL<20" > variants/'+epi+'.vcf' 
	os.system(cmd3)




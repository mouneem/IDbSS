from os import walk
import os

f = []
for (dirpath, dirnames, filenames) in walk('./seqs/'):
    f.extend(filenames)
    break

print('files: ',len(f))

c = 0
vcf = open('vcfs.csv', 'a+')

annotation = open('Annotation.csv', 'r')
annotationLines = annotation.readlines()

for file in f:
	print(file)
	epi = file.split('/')[-1]
	cmd = 'minimap2 -a ref/ref.fasta seqs/'+epi+' > variants/'+epi+'.sam' 
	cmd2 = ' samtools view -bS variants/'+epi+'.sam > variants/'+epi+'.bam'
	cmd3 = 'bcftools mpileup -f ref/ref.fasta variants/'+epi+'.bam > variants/'+epi+'.vcf' 
	os.system(cmd)
	os.system(cmd2)
	os.system(cmd3)
	os.system('rm -f variants/'+epi+'.sam')
	os.system('rm -f variants/'+epi+'.bam')
	os.system('rm -f seqs/'+epi)

	c+=1
	print((100*c)/138838,':' , c)
	vcffile.close()

	


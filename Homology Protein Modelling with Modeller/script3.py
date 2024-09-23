from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='6nzu', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6nzu', atom_files='6nzu.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-6nzu.ali', alignment_format='PIR')
aln.write(file='qseq1-6nzu.pap', alignment_format='PAP')
#Reading from a PDB file

import sys

path = '/home_b/gargi/project_1/test_on_PTS/smog/new_str_2/cont/adjust_pdb/'                    
pdbtraj = open('/home_b/gargi/project_1/test_on_PTS/smog/new_str_2/cont/pts.pdb','r')
trajlines = pdbtraj.readlines()
newfile = open('pts_new4.pdb', 'w')
for line in trajlines:
    if line.startswith(("ATOM" or "HETATM")):
        atomtype = line[0:6]
        at_num = line[6:11]
        at_name = line[11:16]
        res_name = line[16:20]
        res_num = line[22:26]
        cord_x = line[30:38]
        cord_y = line[38:46]
        cord_z = line[46:54]
        occu = line[54:60]
        temp_fact = line[60:66]
        element = line[66:78]
        
        s = [atomtype, at_num, at_name, res_name," A", res_num, cord_x, cord_y, cord_z, occu, temp_fact, element, "\n"]
        newfile.writelines(s)
newfile.close()
pdbtraj.close()

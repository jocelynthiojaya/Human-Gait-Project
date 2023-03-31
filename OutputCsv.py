import csv

def outputCsv(filename, folder, nametag, frame_list):
    header = ['frame',
    'r_hip_ang','r_knee_ang','r_ankle_ang','r_elbow_ang','r_shoulder_ang', 
    'gender', 'age']
    with open(folder + "/" + nametag + "_csvoutput/" + filename + '.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(frame_list)
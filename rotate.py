from PIL import Image
import glob, sys

args = sys.argv
cmds = ['do','show','doandshow']
help_list = cmds.copy()
help_list.append('are the available commands for this application.')
help_msg = ' '.join(help_list)

if len(args) != 2 or args[1] not in cmds:
    print(help_msg)
else:
    cmd = args[1]

    if cmd == 'do' or cmd == 'doandshow':
        for infile in glob.glob("*.jpg"):
            im = Image.open(infile)
            im.rotate(-90, expand=1).save(infile)
    if cmd == 'show' or cmd == 'doandshow':
        for infile in glob.glob("*.jpg"):
            im = Image.open(infile)
            im.show()


parameters = {}

with open('test2.txt') as f:

        lines_loop = f.readlines()

        for l in lines_loop:
                
            if l.startswith("\Scan Size"):
                  
                  parameters['scan size'] = int(l.lstrip("\Scan Size: ").rstrip(' nm'))


print(parameters)



    
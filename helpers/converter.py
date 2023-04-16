import helpers.matplot_tools as mplt

def format_input(coords):
    list = []
    for coord in coords:
        list.append([coord.get('x'), coord.get('y')])
    return list
    

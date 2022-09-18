game_matrix =[['E', 'E', 'E'],
              ['E', 'E', 'E'],
              ['E', 'E', 'E']]


def render(matrix):
    render_matrix = matrix
    margin = 2 #размер клетки(размер отступа в клетке)
    border_char = '-'
    vert_border_char = '|'
    rendered_strings=[]
    def add_border():
        rendered_strings.append(border_char*(margin*2+2)*4+border_char)

    def render_string(matrix_string):
        result_string = ''
        for char in matrix_string:
            result_string+=vert_border_char # добавить границу слева
            result_string+=' '*margin + char+ ' '*margin
        rendered_strings.append(result_string+vert_border_char)
        add_border()

    render_string(['A','0','1','2'])
    for i in range(len(render_matrix)):
        string=render_matrix[i].copy()
        string.insert(0, str(i))
        render_string(string)
    for string in rendered_strings:
        print(string)

render(game_matrix)

def gena(): #генератор ходов дающий X и 0 по очереди
    while True:
        yield 'X'
        yield '0'
def Won(matrix): #проверяет завершена ли игра
    matrix=matrix.copy()
    def all_the_same(elements):
        return len(set(elements)) <= 1
    transmatrix = [[],
                   [],
                   []]
    for string in matrix:
        transmatrix[0].append(string[0])
        transmatrix[1].append(string[1])
        transmatrix[2].append(string[2])
        if all_the_same(string) and not ('E' in string):
            return True
    for string in transmatrix:
        if all_the_same(string) and not ('E' in string):
            return True
    diagonals = [[matrix[0][0],matrix[1][1],matrix[2][2]],[matrix[2][0],matrix[1][1],matrix[0][2]]]
    for string in diagonals:
        if all_the_same(string) and not ('E' in string):
            return True
    return False
for player in gena():
    while True:
        numbers = list(map(int, input('игрок '+player+ ", вводи координаты хода через пробел:").split(' ')))
        if len(numbers)<2:
            print("неверные координаты")
        elif numbers[0]>2 or numbers[1]>2:
            print('неверные координаты')
        elif game_matrix[numbers[0]][numbers[1]] in ['X','0']:
            print("клетка уже занята")
        else:
            game_matrix[numbers[0]][numbers[1]]=player
            break
    render(game_matrix)
    counter = 0
    for string in game_matrix:
        for char in string:
            if char in ['0','X']:
                counter+=1
    if Won(game_matrix):
        print('игрок', player, 'победил')
        break
    if counter ==9:
        print('всё поле занято, ничья')
        break
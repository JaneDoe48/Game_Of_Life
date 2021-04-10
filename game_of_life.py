import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random
import matplotlib.animation as animation


def print_grid(matrice):
    """List[List[int]] -> None
        dessine la matrice (0 ou 1) a l'aide de matplotlib rouge si 0 bleu si 1
    """
    cmap = colors.ListedColormap(['purple', 'black'])
    fig, ax = plt.subplots()
    ax.imshow(matrice, cmap=cmap)
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
    mat_len = len(matrice)
    ax.set_xticks(np.arange(-0.5, mat_len, 1))
    ax.set_yticks(np.arange(-0.5, mat_len, 1))
    plt.show()


def create_rand_matrice(taille):
    """int * int -> List[List[int]]
            renvoyer une matrice de 0 et de 1 crée (0,1 de façon aléatoire)
    """
    matrice = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(random.uniform(0, 1))
        matrice.append(ligne)
    return matrice


def create_empty_matrice(taille):
    """int -> List[List[int]]
                renvoyer une matrice de 0
    """
    matrice = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        matrice.append(ligne)
    return matrice


def copy_matrice(matrice):
    copy = []
    taille = len(matrice)
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(matrice[i][j])
        copy.append(ligne)
    return copy


def creat_block(matrice, position):
    """List[List[int]] * (int,int) -> List[List[int]]
                copier la première matrice et ajouter un block à la position désirée
    """
    copy = copy_matrice(matrice)
    i = position[0]
    j = position[1]
    copy[i][j] = 1
    copy[i][j - 1] = 1
    copy[i - 1][j] = 1
    copy[i - 1][j - 1] = 1
    return copy


def creat_Tub(matrice, position):
    """List[List[int]] * int -> List[List[int]]
                    copie la première matrice et ajouter un block à la position désirée
    """
    copy = copy_matrice(matrice)
    i = position[0]
    j = position[1]
    copy[i][j] = 1
    copy[i + 1][j - 1] = 1
    copy[i][j - 2] = 1
    copy[i - 1][j - 1] = 1
    return copy


def creat_bee_hive(matrice, position):
    """List[List[int]] * int -> List[List[int]]
                        copier la première matrice et ajouter un block à la position désirée
    """
    copy = copy_matrice(matrice)
    i = position[0]
    j = position[1]
    copy[i][j] = 1
    copy[i - 1][j - 1] = 1
    copy[i - 1][j - 2] = 1
    copy[i][j - 3] = 1
    copy[i + 1][j - 1] = 1
    copy[i + 1][j - 2] = 1
    return copy


def creat_loaf(matrice, position):
    """List[List[int]] * int -> List[List[int]]
                        copier la premère matrice et ajouter un block à la position désirée
    """
    copy = copy_matrice(matrice)
    i = position[0]
    j = position[1]
    copy[i][j] = 1
    copy[i + 1][j] = 1
    copy[i - 1][j - 1] = 1
    copy[i + 2][j - 1] = 1
    copy[i][j - 3] = 1
    copy[i - 1][j - 2] = 1
    copy[i + 1][j - 2] = 1
    return copy


def create_Blinker(matrice, position):
    copy = copy_matrice(matrice)
    i = position[0]
    j = position[1]
    copy[i][j] = 1
    copy[i + 1][j] = 1
    copy[i - 1][j] = 1
    return copy


def is_alive(matrice, position):
    """Rules:
         Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    cpt = 0
    i = position[0]
    j = position[1]
    Taille = len(matrice)
    if i + 1 < Taille and j + 1 < Taille:
        cpt += matrice[i + 1][j + 1]
    if i - 1 >= 0 and j - 1 >= 0:
        cpt += matrice[i - 1][j - 1]
    if i + 1 < Taille and j - 1 >= 0:
        cpt += matrice[i + 1][j - 1]
    if i - 1 >= 0:
        cpt += matrice[i - 1][j]
    if j - 1 >= 0:
        cpt += matrice[i][j - 1]
    if j + 1 < Taille:
        cpt += matrice[i][j + 1]
    if i + 1 < Taille:
        cpt += matrice[i + 1][j]
    if i - 1 >= 0 and j + 1 < Taille:
        cpt += matrice[i - 1][j + 1]
    cel = matrice[i][j]

    if cel == 1:
        if cpt == 2 or cpt == 3:
            return True
    else:
        if cpt == 3:
            return True
    return False


def game_of_life(grid, nmb_cycle):
    """
        List[List[int]] -> None
        Applique l'algorithme du jeu de la vie sur la matrice passée en paramètre
    """
    print_grid(grid)
    taille = len(grid)
    for n in range(nmb_cycle):
        copy = create_empty_matrice(taille)
        for i in range(taille):
            for j in range(taille):
                if is_alive(grid, (i, j)):
                    copy[i][j] = 1
                else:
                    copy[i][j] = 0

        grid = copy
        print_grid(grid)


matrice = create_empty_matrice(10)

matrice2 = create_Blinker(matrice, (5, 5))

game_of_life(matrice2, 2)

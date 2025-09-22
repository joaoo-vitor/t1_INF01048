import numpy as np
import pandas as pd

def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
    y_pred = b + w * x
    mse = np.mean((y - y_pred) ** 2)
    return mse


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
    y_pred = b + w * x
    delta_b = np.mean(2*(y_pred-y))
    delta_w = np.mean(2*x*(y_pred-y))
    return b-alpha*delta_b, w-alpha*delta_w


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    list_b = [b]
    list_w = [w]
    for _ in range(num_iterations):
        
        current_b, current_w= step_gradient(list_b[-1], list_w[-1], data, alpha)
        # Add current b and w to the list
        list_b.append(float(current_b))
        list_w.append(float(current_w))
    return list_b, list_w

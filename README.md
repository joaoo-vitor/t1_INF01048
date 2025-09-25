<h1 align="center">Trabalho 1 - Aprendizado Supervisionado - INF01048</h1>

# Alunos  
- Milton Pacheco - 590535  
- João Vitor de Souza - 581431


> **OBS:** Além do relatório do README, há um _storytelling_ sobre cada mudança feita dentro do arquivo `trabalho_redes_neurais.ipynb` nas quatro seções do `Training Networks`.


# Características dos datasets  
MNIST: 10 classes, 60.000 imagens de treino e 10.000 de teste, tamanho 28x28x1 em tons de cinza.  
Fashion-MNIST: 10 classes, 60.000 imagens de treino e 10.000 de teste, tamanho 28x28x1 em tons de cinza.  
CIFAR-10: 10 classes, 50.000 imagens de treino e 10.000 de teste, tamanho 32x32x3 em RGB.  
CIFAR-100: 100 classes, 50.000 imagens de treino e 10.000 de teste, tamanho 32x32x3 em RGB.  

Normalização dos dados  
Algumas técnicas de normalização foram implementadas para melhorar o treinamento das redes neurais. Os valores dos pixels foram convertidos do intervalo 0-255 para 0-1 através da divisão por 255.0, visando acelerar a convergência do treinamento e evitando problemas de gradiente, garantindo que todos os pixels tenham a mesma escala de valores.

Para os datasets MNIST e Fashion-MNIST, que são imagens em escala de cinza, foi adicionada uma dimensão de canal usando np.expand_dims(axis=-1), transformando as imagens de formato 28x28 para 28x28x1, essa alteração fez-se necessária devido a compatibilidade com as camadas convolucionais do TensorFlow/Keras.


# Resultados e reflexões 

## 1) Ordem de dificuldade dos datasets
<p align="center">
    <strong>
        MNIST &lt; Fashion-MNIST &lt; CIFAR-10 &lt; CIFAR-100
    </strong>
</p>

> **OBS:** O sinal '<' significa "é menos difícil de treinar uma CNN que"

- MNIST < FASHION_MNIST  
Isso se explica pois no MNIST temos apenas traços de dígitos, enquanto no MNIST_FASHION temos figuras mais complexas, que variam mais, de roupas.

- FASHION_MNIST < CIFAR10  
Aqui, temos imagens que representam fotos reais em ambos os casos. Porém, o CIFAR se mostrar mais difícil de abstrair a sua essência uma vez que as classe são de contextos mais variados que o MNIST_FASHION, que só possui imagens de roupas (único contexto). Além disso, as imagens do CIFAR são um pouco maiores.

- CIFAR10 < CIFAR100  
Para essa comparação, é fácil perceber que o segundo é mais difícil pois possui mais classes e portanto característica mais variadas à serem generalizadas pela rede.

## 2) Acurácia final e mudanças feitas
```python
results = {
    "mnist": {"time": 275.81, "acc": 98.52}, #10 epochs
    "fashion_mnist": {"time": 1404.66, "acc": 92.17}, #20 epochs
    "cifar10": {"time": 8481.60, "acc": 83.42}, #20 epochs
    "cifar100": {"time": 10881.05, "acc": 58.07}, #20 epochs
}
```

## Modelo para MNIST
Melhor acurácia obtida: aproximadamente 98.5%.  
Como esse é o mais simples dos datasets, redes rasas como a implementada já conseguem alta performance. Por isso, não quisemos seguir fazendo mudanças na rede, visto que ja atingimos uma taxa de acerto satisfatória.

## Fashion-MNIST  
Melhor acurácia obtida: aproximadamente 92%.  
Apesar de ter o mesmo tamanho de imagens que o MNIST, apresenta maior dificuldade porque roupas possuem similaridade visual entre classes. Mesmo assim, no primeiro modelo que construimos já tivemos uma boa performance, com acurácia alta. Porém, fizemos algumas pequenas mudanças análogas as mudanças que aplicamos em CIFAR. Tentamos aumentar o número de camadas convolucionais de 2 para 3, e tivemos um resultado que piorou levemente a acurácia. Porém, quando aumentamos as convoluções em cada bloco convolucional, a acuarácia sofreu uma melhora positiva pequena (1%), quando obtivemos nossa melhor acurácia.

## CIFAR-10  
Melhor acurácia obtida: aproximadamente 83%.  
Este caso é mais complexo que os anteriores, pois envolve imagens coloridas com mais fatores envolvidos, como fundo e texturas complexas. Logo, para obter melhores resultados, faz-se necessário utilizar redes mais profundas, aumentar o número de épocas de treino e aplicar técnicas robustas. 

## CIFAR-100  
Melhor acurácia obtida: aproximadamente 58%.  
É o mais difícil dos quatro datasets, pois possui toda a complexidade do CIFAR-10 com o adicional de 100 classes. Nos casos de teste a rede inciial utilizada foi fraca para esse nível de variação, além disso, o treino curto com apenas 10 épocas limitou ainda mais a performance. Dessa forma, é evidente que o aumento da profundide da rede aliado a técnicas mais avançadas elevaria o nível de acurária do modelo.

Para ambas os dois últimos datasets, testamos mudanças análogas para melhorar suas performances, com intensidade um pouco maior no segundo.
Das mudanças testadas:
- Aumentar o número de camadas convolucionais;
- Aumentar o número de convoluções em cada camada convolucionail (antes do pooling);
- Adicionar técnicas de normalização em batch;
- Fazer um dropout dos neurônios para reduzir overfitting.

# Conclusão Geral
A performance depende tanto das características do dataset quanto da capacidade da rede treinada. Logo, evidenciamos que datasets mais complexos exigem redes mais profundas, maior tempo de treino e técnicas avançadas de otimização. Dessa maneira, concluímos que este estudo mostrou claramente a progressão de dificuldade, desde o dataset MNIST, quase trivial, até CIFAR-100, extremamente complexo e desafiador.

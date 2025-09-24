Trabalho 1 - Aprendizado Supervisionado - INF01048

Alunos  
Milton Pacheco - 590535  
João Vitor de Souza - 

Características dos datasets  
MNIST: 10 classes, 60.000 imagens de treino e 10.000 de teste, tamanho 28x28x1 em tons de cinza.  
Fashion-MNIST: 10 classes, 60.000 imagens de treino e 10.000 de teste, tamanho 28x28x1 em tons de cinza.  
CIFAR-10: 10 classes, 50.000 imagens de treino e 10.000 de teste, tamanho 32x32x3 em RGB.  
CIFAR-100: 100 classes, 50.000 imagens de treino e 10.000 de teste, tamanho 32x32x3 em RGB.  

Normalização dos dados  
Algumas técnicas de normalização foram implementadas para melhorar o treinamento das redes neurais. Os valores dos pixels foram convertidos do intervalo 0-255 para 0-1 através da divisão por 255.0, visando acelerar a convergência do treinamento e evitando problemas de gradiente, garantindo que todos os pixels tenham a mesma escala de valores.

Para os datasets MNIST e Fashion-MNIST, que são imagens em escala de cinza, foi adicionada uma dimensão de canal usando np.expand_dims(axis=-1), transformando as imagens de formato 28x28 para 28x28x1, essa alteração fez-se necessária devido a compatibilidade com as camadas convolucionais do TensorFlow/Keras.


Resultados e reflexões  

MNIST  
Melhor acurácia obtida: aproximadamente 98.5%.
É o mais simples dos datasets, pois contém imagens pouco ruidosas e baixa variação intra-classe. Redes rasas como a implementada já conseguem alta performance.

Fashion-MNIST  
Melhor acurácia obtida: aproximadamente 91%.
Apesar de ter o mesmo tamanho de imagens que o MNIST, apresenta maior dificuldade porque roupas possuem similaridade visual entre classes. É mais complexo que o MNIST, mas redes simples mantém uma alta acurária.

CIFAR-10  
Melhor acurácia obtida: aproximadamente 69%.
Este caso é mais complexo que os anteriores, pois envolve imagens coloridas com mais fatores envolvidos, como fundo e texturas complexas. Logo, para obter melhores resultados, faz-se necessário utilizar redes mais profundas, aumentar o número de épocas de treino e aplicar técnicas robustas. Vale ressaltar durantes os testes foi possível perceber que o aumento do tamanho das camadas pode gerar overfitting caso não seja acompanhada de outras técnicas como o uso de batches.

CIFAR-100  
Melhor acurácia obtida: aproximadamente 37%.
É o mais difícil dos quatro datasets, pois possui toda a complexidade do CIFAR-10 com o adicional de 100 classes. Nos casos de teste a rede inciial utilizada foi fraca para esse nível de variação, além disso, o treino curto com apenas 10 épocas limitou ainda mais a performance. Dessa forma, é evidente que o aumento da profundide da rede aliado a técnicas mais avançadas elevaria o nível de acurária do modelo.


Conclusão  
A performance depende tanto das características do dataset quanto da capacidade da rede treinada. Logo, evidenciamos que datasets mais complexos exigem redes mais profundas, maior tempo de treino e técnicas avançadas de otimização. Dessa maneira, concluímos que este estudo mostrou claramente a progressão de dificuldade, desde o dataset MNIST, quase trivial, até CIFAR-100, extremamente complexo e desafiador.

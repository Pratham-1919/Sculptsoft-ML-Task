##  Transformer

### What is a transformer:-
Transformer is a deep learning based on multi-head attention that process sequential data in parallel, eliminating the need to recurence and convolutions which we used earlier in RNN's. This helps the model to capture the long range dependencies. 

The architecture consists of encoder and decoder in it. The encoder process the full input BIDIRECTIONALY using self-attention to create contextual representation. While decoder generates the output sequence autoregressively using masked self-attention. 

### Transformer Architecture

![Transformer Architecture](transformer_architecture.png)
 
### Encoder

The primary function of the encoder is to create a high-dimensional representation of the input sequence that the decoder can use to generate the output. Encoder consists of multiple layers and each layer is composed of two main sub-layers

#### Self-Attention Mechanism: This sub-layer allows the encoder to weigh the importance of different parts of the input sequence differently to capture dependencies regardless of their distance within the sequence.
#### Feed-Forward Neural Network: This sub-layer consists of two linear transformations with a ReLU activation in between. It processes the output of the self-attention mechanism to generate a refined representation.


### Decoder

Decoder in transformer also consists of multiple identical layers. Its primary function is to generate the output sequence based on the representations provided by the encoder and the previously generated tokens of the output.

Each decoder layer consists of three main sub-layers:

#### Masked Self-Attention Mechanism: Similar to the encoder's self-attention mechanism but its main purpose is to prevent attending to future tokens to maintain the autoregressive property (no cheating during generation).

#### Encoder-Decoder Attention Mechanism: This sub-layer allows the decoder to focus on relevant parts of the encoder's output representation. This allows the decoder to focus on relevant parts of the input, essential for tasks like translation.

#### Feed-Forward Neural Network: This sub-layer processes the combined output of the masked self-attention and encoder-decoder attention mechanisms.


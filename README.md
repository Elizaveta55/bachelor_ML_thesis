# Bachelor thesis

This repository contains bachelor qualification work and implementation. The basic idea is to use the patient's daily medical records to predict the success of the current heart disease treatment with LSTM model and word2vec for embeddings.

The most challanging parts were:
1. preparation of data due to garbage in medical certificates (spelling, abbreviations, professional standard abbreviations)
2. data analysis to remove explicit keywords (for example, the word "die" in the case of the diagnosis "patient dies during treatment")
3. choice of vectorization of the model.
4. Choice of neural network architecture.

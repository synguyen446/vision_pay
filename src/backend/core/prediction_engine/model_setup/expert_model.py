from tensorflow.keras import layers, models
import tensorflow as tf

class ExpertModel(tf.keras.Model):
  def __init__(self):
    super(ExpertModel, self).__init__()

    # Convulation layers to extract features and patterns
    self.conv1 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')
    self.conv2 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')
    self.conv3 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')

    # Flatten layer to 1D vector
    self.flatten = tf.keras.layers.Flatten()

    # Produce routing probabilities for each expert model
    self.dense = tf.keras.layers.Dense(64, activation='relu')

    # Output layer for probabilistic classification
    self.output_layer = tf.keras.layers.Dense(2, activation='softmax')

  def call(self, x):
    x = self.conv1(x)
    x = self.conv2(x)
    x = self.conv3(x)

    x = self.flatten(x)

    x = self.dense(x)

    return self.output_layer(x)
  
  def compile(self, **kwargs):
    # Set default optimizer, loss, and metric args
    if 'optimizer' not in kwargs:
        kwargs['optimizer'] = 'adam'
    if 'loss' not in kwargs:
        kwargs['loss'] = 'sparse_categorical_crossentropy'
    if 'metrics' not in kwargs:
        kwargs['metrics'] = ['accuracy']

    # Call the parent compile method with updated kwargs
    super(ExpertModel, self).compile(**kwargs)


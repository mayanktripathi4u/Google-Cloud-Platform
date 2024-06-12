
# MapTuple for key-value pairs. If your PCollection consists of (key, value) pairs, you can use MapTuple to unpack them into different function arguments.

import apache_beam as beam

def split_words(text):
  return text.split(',')

with beam.Pipeline() as pipeline:
  plants = (
      pipeline
      | 'Gardening plants' >> beam.Create([
          '🍓Strawberry,🥕Carrot,🍆Eggplant',
          '🍅Tomato,🥔Potato',
      ])
      | 'Split words' >> beam.FlatMap(split_words)
      | beam.Map(print)) 
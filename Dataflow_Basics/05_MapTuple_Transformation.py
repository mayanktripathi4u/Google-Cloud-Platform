
# MapTuple for key-value pairs. If your PCollection consists of (key, value) pairs, you can use MapTuple to unpack them into different function arguments.

import apache_beam as beam

def strip_header_and_newline(text):
  return text.strip('# \n')
# The strip() method removes any leading (starting) and trailing (ending) whitespaces from a given string.


# MapTuple for key-value pairs
with beam.Pipeline() as pipeline:
  plants = (
      pipeline
      | 'Gardening plants' >> beam.Create([
          ('🍓', 'Strawberry'),
          ('🥕', 'Carrot'),
          ('🍆', 'Eggplant'),
          ('🍅', 'Tomato'),
          ('🥔', 'Potato'),
      ])
      | 'Format' >> beam.MapTuple(lambda icon, plant: '{}{}'.format(icon, plant))
      | beam.Map(print))  
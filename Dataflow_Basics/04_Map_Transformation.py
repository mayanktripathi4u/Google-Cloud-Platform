
import apache_beam as beam

def strip_header_and_newline(text):
  return text.strip('# \n')
# The strip() method removes any leading (starting) and trailing (ending) whitespaces from a given string.

print("Option 1: Using UDF")
with beam.Pipeline() as pipeline:
  plants = (
      pipeline
      | 'Gardening plants' >> beam.Create([
          '# 🍓Strawberry\n',
          '# 🥕Carrot\n',
          '# 🍆Eggplant\n',
          '# 🍅Tomato\n',
          '# 🥔Potato\n',
      ])
      | 'Strip header' >> beam.Map(strip_header_and_newline)
      | beam.Map(print))
  
print("Option 2: Using Lambda")
with beam.Pipeline() as p:
  secondWay = (
    p
    | 'Gardening plants' >> beam.Create([
          '# 🍓Strawberry\n',
          '# 🥕Carrot\n',
          '# 🍆Eggplant\n',
          '# 🍅Tomato\n',
          '# 🥔Potato\n',
      ])
      | 'Strip header' >> beam.Map(lambda rec : rec.strip('# \n'))
      | beam.Map(print)
  )
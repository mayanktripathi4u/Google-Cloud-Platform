import apache_beam as beam

def is_grocerystore(store):
#   print(f"Record --> {store} ----------> and 8th element is {store[8]}")
  return store[8] == 'Medium'

#from external resources
p2 = beam.Pipeline()

grocery = (p2
           | "Read from Text" >> beam.io.ReadFromText("grocery.txt", skip_header_lines=1)
           | "split the record" >> beam.Map(lambda record: record.split(','))
           | 'Filter regular' >> beam.Filter(is_grocerystore)
           | 'Write to text'>> beam.io.WriteToText('regular_filter.txt')
           )  #| beam.Map(print))

p2.run()

# with beam.Pipeline() as p:
#     perenials = (
#         p
#         | 'Read from Text File' >> beam.io.ReadAllFromText("grocery.txt", skip_header_lines=1)
#         | "Split the Record" >> beam.Map(lambda rec: rec.split(','))
#         | 'Filter Grocery' >> beam.Filter(is_grocery)
#         | 'Write to Text' >> beam.io.WriteToText('filtered_data.txt')
#     )

 
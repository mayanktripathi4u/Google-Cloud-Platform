import apache_beam as beam

records = [("vignesh", [27, "engineer"]),
("neethu", [27, "developer"]),
("farooqui", [26, "data analyst"]),
("sai", [29, "web developer"]),
("tinkle", [28, "fullstack developer"]),
("neethu", 'Employed'),
("sai", 'Unemployed'),
("tinkle", 'Employed'),
("farooqui",'Employed'),
("vignesh", 'Unemployed')]

with beam.Pipeline() as pipeline:
  produce_counts = (
      pipeline
      | 'Create produce counts' >> beam.Create(records)
      | 'Group counts per produce' >> beam.GroupByKey()
      | 'GroupBy Output' >> beam.Map(print))
  
#   print("Pritning the same using beam : within 'with' block ")
#   produce_counts | 'Priting via beam Map within with block' >> beam.Map(print)
  
print(f"Printing produce_counts : {produce_counts}\n")

# Will not print any as this is outside of with.
print("Pritning the same using beam")
produce_counts | 'Priting via beam.Map' >> beam.Map(print)

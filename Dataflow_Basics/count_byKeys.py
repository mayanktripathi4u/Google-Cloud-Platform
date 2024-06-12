import apache_beam as beam

# Counting all elements in a PCollection
with beam.Pipeline() as pipeline:
    total_elements = (
        pipeline
        | 'Create plants' >> beam.Create([
            ('spring', '🍓'), 
            ('spring', '🥕'), 
            ('summer', '🥕'), 
            ('fall', '🥕'), 
            ('spring', '🍆'), 
            ('winter', '🍆'), 
            ('fall', '🍅'), 
            ('summer', '🍅'), 
            ('winter', '🍅'), 
            ('fall', '🌽')
        ]
        )
        | 'Create elements per key' >> beam.combiners.Count.PerKey()
        | "The total number of elements per key" >> beam.Map(print)
    )

if __name__ == "__main__":
    print("The total count is displayed above...")
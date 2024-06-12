import apache_beam as beam

# Counting all elements in a PCollection
with beam.Pipeline() as pipeline:
    total_elements = (
        pipeline
        | 'Create plants' >> beam.Create(
            ['🍓', '🥕', '🥕', '🥕', '🍆', '🍆', '🍅', '🍅', '🍅', '🌽']
        )
        | 'Create all elements' >> beam.combiners.Count.Globally()
        | "The total number of elements " >> beam.Map(print)
    )

if __name__ == "__main__":
    print("The total count is displayed above...")
import apache_beam as beam

with beam.Pipeline() as p:
    even_data = (
        p
        | "Create Even Records" >> beam.Create({2,4,6,8,10})
    )

    odd_data = (
        p
        | "Create Odd Records" >> beam.Create({1,3,5,7,9})
    )

    result = ((even_data, odd_data) | beam.Flatten()) | beam.Map(print)

    
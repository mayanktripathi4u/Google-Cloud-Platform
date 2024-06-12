import apache_beam as beam

def is_perennial(plant):
    print("is_perennial function called..........")
    return plant['duration'] == 'perennial'

with beam.Pipeline() as p:
    perenials = (
        p
        | 'Gardening Plants' >> beam.Create([
            {'icon': '🍓', 'name': 'Strawberry', 'duration': 'perennial'},
            {'icon': '🥕', 'name': 'Carrot', 'duration': 'biennial'},
            {'icon': '🍆', 'name': 'Eggplant', 'duration': 'perennial'},
            {'icon': '🍅', 'name': 'Tomato', 'duration': 'annual'},
            {'icon': '🥔', 'name': 'Potato', 'duration': 'perennial'},
        ])
        | 'Filter perennials' >> beam.Filter(is_perennial)
        | beam.Map(print)
    )

    # | "Printing the Result .... " >> beam.Map(print)
    # )
import apache_beam as beam
import re

# GroupBy
with beam.Pipeline() as pl:
    grouped = (
        pl
        | beam.Create(['Strawberry', 'Banana', 'StrawBerry', "Blueberry", "Blackberry", "Raspberry", 'Apple'])
        # | beam.GroupBy(lambda rec: rec[0])
        # | beam.GroupBy(lambda rec: rec[0:2])
        | beam.GroupBy(lambda rec: "Berry" if re.search('berry', rec) else rec[0] )
        | beam.Map(print)
    )

# Aggregation 
GROCERY_LIST = [
    beam.Row(recipe='pie', fruit='strawberry', quantity=3, unit_price=1.50),
    beam.Row(recipe='pie', fruit='raspberry', quantity=1, unit_price=2.50),
    beam.Row(recipe='pie', fruit='blackberry', quantity=2, unit_price=3.50),
    beam.Row(recipe='pie', fruit='Blueberry', quantity=4, unit_price=4.50),
    beam.Row(recipe='muffin', fruit='Blueberry', quantity=3, unit_price=3.50),
    beam.Row(recipe='muffin', fruit='banana', quantity=1, unit_price=1.50),
]

print(f"GROCERY_LIST ----------> {GROCERY_LIST} \n\n")

with beam.Pipeline() as pipeGrocery:
    grp = pipeGrocery | beam.Create(GROCERY_LIST) | beam.GroupBy('recipe') | beam.Map(print)

print("\n\n")

with beam.Pipeline() as p1:
    grouped = (
        p1
        | beam.Create(GROCERY_LIST)
        | beam.GroupBy('fruit').aggregate_field('quantity', sum, 'total_qty')
        | beam.Map(print)
    )
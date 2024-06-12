import apache_beam as beam

with beam.Pipeline() as pipe:
    lines = (
        pipe
        | beam.Create([
            "My first sentence.....",
            "Here is my second sentence to consider...",
            'Keep going with your sentences.',
            'Its a awesome, learning Apache Beam.',
        ])
    )

print("In Memory Beam ----> ")
print(lines)
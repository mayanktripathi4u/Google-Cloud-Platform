import apache_beam as beam

def run():
    # Step 1: Create the Pipeline
    print("Step 1: Pipeline Creation Started")
    with beam.Pipeline() as pipeline:
        input_string = "A Random Name"
        elements = (
            pipeline 
            | "Read the input" >> beam.Create(["Hello", "World!", input_string]) 
            | "Print th eelement" >> beam.Map(print)
        )

if __name__ == "__main__":
    run()
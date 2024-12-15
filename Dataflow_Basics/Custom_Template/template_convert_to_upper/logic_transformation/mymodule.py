import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.transforms.window import FixedWindows


class UpperCaseTransform(beam.DoFn):
    def process(self, element):
        # Transform each element to uppercase
        yield element.upper()

def run(argv=None):
    # Set up the pipeline options
    pipeline_options = PipelineOptions(argv)

    p = beam.Pipeline(options=pipeline_options)

    # Define the pipeline steps 
    (p
     | 'Create' >> beam.Create(['Hello', 'Mayank', 'Using', 'custom', 'template'])
     | 'Transform each element' >> beam.ParDo(UpperCaseTransform())
     | 'Write to Text' >> beam.io.WriteToText('gs://dataflow-handson-mayank/output/hello_world')
    )


    # Run the pipeline
    result = p.run()
    result.wait_until_finish()

if __name__ == '__main__':
    run()
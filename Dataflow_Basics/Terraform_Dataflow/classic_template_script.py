# This is a Basic script to read the file from given path and write the same content to another file and place it in output path.

import apache_beam as beam
from apache_beam.options.pipeline_options import _BeamArgumentParser, PipelineOptions

class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument('--input',  type=str, help="Input File Path")
        parser.add_value_provider_argument('--output', type=str, help="Output File Path")

def run(argv = None):
    # Setup Pipeline Option
    pipeline_options = PipelineOptions(argv)
    my_options = pipeline_options.view_as(MyOptions)

    # Create a Pipeline
    with beam.Pipeline(options=pipeline_options) as p:
        # Read from the Input File
        lines = p | "Read from Text File" >> beam.io.ReadFromText(my_options.input)

        # Write to thr output File
        lines | "Write to File" >> beam.io.WriteToText(my_options.output)

if __name__ == "__main__":
    run()
    



# Step 1: Write the Python Code which will be used as predefined template.
# Step 2: Run the below command to create the Google Cloud Dataflow Batch Job, and process it with the defined processing / transformation / pipeline provided.

# python classic_template_script.py --input=./data/my_input.txt --output=./output/dataflow_result.txt

# WIth this we are directly referencing the Python Script (could say Template).

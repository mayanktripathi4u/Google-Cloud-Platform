


# # import apache_beam as beam
# # from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
# # from apache_beam.transforms.window import FixedWindows

# # class UpperCaseTransform(beam.DoFn):
# #     def process(self, element):
# #         yield element.decode("utf-8").upper()

# # def run(input_subscription, output_path, template_location, pipeline_args):
# #     # Define pipeline options
# #     options = PipelineOptions(pipeline_args)
# #     options.view_as(StandardOptions).streaming = True  # Enable streaming mode

# #     # Create the pipeline
# #     with beam.Pipeline(options=options) as p:
# #         (
# #             p
# #             | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(subscription=input_subscription)
# #             | 'Window into Fixed Intervals' >> beam.WindowInto(FixedWindows(60))  # Use 60-second window
# #             | 'Convert to Uppercase' >> beam.ParDo(UpperCaseTransform())
# #             | 'Write to GCS' >> beam.io.WriteToText(output_path)
# #         )

# #     # Save the pipeline as a template if a template_location is provided
# #     if template_location:
# #         options.view_as(StandardOptions).save_main_session = True
# #         options.view_as(StandardOptions).template_location = template_location

# # if __name__ == '__main__':
# #     import argparse
# #     import sys

# #     parser = argparse.ArgumentParser(description='Dataflow pipeline for converting text to uppercase')
# #     parser.add_argument('--input_subscription', required=True, help='Pub/Sub subscription to read from')
# #     parser.add_argument('--output_path', required=True, help='Output path for GCS')
# #     parser.add_argument('--template_location', help='GCS path for saving the Dataflow template')
# #     known_args, pipeline_args = parser.parse_known_args()

# #     # Check if the required arguments are provided
# #     if not known_args.input_subscription or not known_args.output_path:
# #         print("Error: --input_subscription and --output_path are required arguments.")
# #         sys.exit(1)

# #     # Run the pipeline
# #     run(known_args.input_subscription, known_args.output_path, known_args.template_location, pipeline_args)


# import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions
# from apache_beam.options.pipeline_options import SetupOptions
# import argparse

# def run(argv=None):
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--input_subscription', required=False, help='Pub/Sub subscription to read from.')
#     parser.add_argument('--output_path', required=False, help='Output path to write results to.')
#     parser.add_argument('--template_location', required=False, help='GCS location to save the Dataflow template. / Path to save the Dataflow template.')

#     known_args, pipeline_args = parser.parse_known_args(argv)
#     print(f"Known Args : {known_args}")
#     print(f"Check if template exists : {known_args.template_location}")

#     if not known_args.output_path:
#         raise ValueError("The --output_path argument is required")
    
#     print(f"known_args.output_path : {known_args.output_path}")

#     # Create the pipeline options
#     pipeline_options = PipelineOptions(pipeline_args)
#     pipeline_options.view_as(SetupOptions).save_main_session = True

#     # Create the pipeline
#     with beam.Pipeline(options=pipeline_options) as p:
        
#         # Define your pipeline logic; Do not execute; just create a template
#         # Read from the input_subscription if provided (during job execution)
#         # input_data = (
#         #     p
#         #     | 'Read From PubSub' >> beam.io.ReadFromPubSub(subscription=known_args.input_subscription)
#         #     if known_args.input_subscription else
#         #     p | 'CreateEmpty' >> beam.Create([])
#         # )

#         # # Transform the input data to uppercase
#         # output_data = input_data | 'ToUpperCase' >> beam.Map(lambda x: x.decode('utf-8').upper().encode('utf-8'))

#         # # Write to the output path if provided (during job execution)
#         # if known_args.output_path:
#         #     output_data | 'WriteToGCS' >> beam.io.WriteToText(known_args.output_path)

#         # if known_args.template_location:
#         #     (
#         #      p
#         #      | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(subscription=known_args.input_subscription)
#         #      | 'Transform Data' >> beam.Map(lambda x: x.upper())
#         #      | 'Write to GCS' >> beam.io.WriteToText(known_args.output_path)
#         #     )
#         # else:
#         #     # Execute the pipeline
#         #     # Add logic for running the pipeline
#         #     pass

#         if known_args.input_subscription:
#             # Include the Pub/Sub step if input_subscription is provided
#             data = (p
#                     | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(subscription=known_args.input_subscription))
#         else:
#             # Create an empty PCollection if input_subscription is not provided
#             data = p | 'Create empty PCollection' >> beam.Create([])

#         # Common transformations (for template creation or job execution)
#         transformed_data = (data
#                             | 'Transform Data' >> beam.Map(lambda x: x.decode('utf-8').upper())
#                             | 'Write to GCS' >> beam.io.WriteToText(known_args.output_path)
#                         )


# if __name__ == '__main__':
#     run()

import apache_beam as beam

# Using ParDo
class SplitRow(beam.DoFn):
    def process(self, element):
        return [element.split(',')]
    
class ComputeWordLenFun(beam.DoFn):
    def process(self, element):
        return [len(element)]
    
with beam.Pipeline() as pl:
    input_data = (
        pl
        | "Read from Text" >> beam.io.ReadFromText("students.txt", skip_header_lines=1)
        | "Split the Recods" >> beam.ParDo(SplitRow())
    )

    fail_data = (
        input_data
        | "Filtering the Data for failed students" >> beam.Filter(lambda rec: rec[5] == 'FAIL')
    )

    word_length = (
        fail_data
        | "Word Length " >> beam.ParDo(ComputeWordLenFun())
    )

    write_toText1 = (
        word_length
        | "Write the Result to Text File" >> beam.io.WriteToText("result/word_length")
    )

    write_toText2 = (
        fail_data
        | "Write the Result to Text" >> beam.io.WriteToText("result/fail_data")
    )
    

# THe same is achieved using Map and Filter Transformation
with beam.Pipeline() as pipe:
    students = (
        pipe
        | "Read from Text" >> beam.io.ReadFromText("students.txt", skip_header_lines=1)
        | "Split the Recods" >> beam.Map(lambda rec: rec.split(','))
        | "Filtering the Data for failed students" >> beam.Filter(lambda rec: rec[5] == 'FAIL')
        | "Write the Result to Text" >> beam.io.WriteToText("result/failed_students") 
    )
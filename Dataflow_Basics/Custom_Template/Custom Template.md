# Create a Custom Classic Template using Python

The primary goal of the templates is to package the dataflow pipelines in the form of reusable components by only changing the required pipeline parameters. The template files are staged on GCS bucket and can be launched either from the console, gcloud command or from other services like Cloud Scheduler / Functions, etc.

Google already provides us with many examples of running the Dataflow jobs using python SDK and lots of examples can be found here https://github.com/GoogleCloudPlatform/DataflowTemplates

## Limitations
The limitations for creating Dataflow templates can be summarized in simpler terms as follows:

1. Custom Code Changes Not Allowed:
* Once you create a Dataflow template, you can't change or add new custom code to the pipeline at runtime. The template is essentially a "frozen" version of your code. If you need different code or new features, you have to create a new template.
2. Limited Support for Some Features:
* There are certain features in Apache Beam (the programming model used by Dataflow) that don't work with templates. For example:
  * **Unbounded Side Inputs**: You can't use unbounded (never-ending) data sources as side inputs, which are extra data sources used by your main pipeline.
  * **State and Timers**: You can't use features like stateful processing (where you store information about past events) or timers (to trigger actions at specific times).
3. Restrictions on Dynamic Values:
* Some values in the pipeline must be known ahead of time when creating the template. For example, if you need to set an output path, it has to be defined when you create the template, and you can't change it later at runtime.
4. Environment Variables and Packages Must Be Predefined:
* You can't add new environment variables or external Python packages once the template is created. Any required packages or environment settings need to be specified when you create the template.
5. No Access to Runtime Parameters in Certain Cases:
* There are some situations where you can't access certain runtime parameters (input values provided when the job is started) directly. This might limit flexibility in adjusting the job's behavior based on parameters provided at runtime.
6. Template Version Compatibility:
* Templates may not always be compatible with newer versions of Dataflow. If you update to a new version of Dataflow, you may need to recreate your template to ensure it works correctly.
7. Real-Time Processing Support:
* Classic templates do support real-time (streaming) data processing, such as reading from a Pub/Sub subscription. In fact, one common use case for Dataflow is processing streaming data from Pub/Sub.
* However, you cannot change the code or logic of the pipeline once the template is created. If you need to make changes to the way streaming data is processed, you would need to create a new template.
* Pub/Sub subscriptions can be used as inputs for a Dataflow job created from a classic template. This means you can still create a template that reads data from a Pub/Sub subscription and processes it in real-time.
* The limitation on "Unbounded Side Inputs" applies to using additional unbounded data sources as side inputs (auxiliary data sources), not to reading from the main input Pub/Sub subscription.
* **Dynamic Parameter Limitations**: While certain parameters like the Pub/Sub subscription can be specified at runtime using runtime parameters, some values need to be defined at template creation. This means you can still change the Pub/Sub subscription when launching a Dataflow job from the template, as long as it is specified as a runtime parameter.

These limitations mean that once a template is created, the options for modifying the pipeline are limited, and some advanced features may not be supported. For tasks requiring a lot of dynamic changes, non-template approaches might be more suitable.







Set up a directory structure and a Python script that serves as your module. Here’s how you can create the required structure step by step:

1. Create the Directory Structure
Create the following directory structure for your project:


3. Run the Command to Create a Dataflow Template
To create a Dataflow template using this module, run the command as shown below, replacing placeholders with your actual values:
```bash
python3 -m logic_transformation.mymodule \
  --runner DataflowRunner \
  --project gcphde-prim-dev-data \
  --staging_location gs://dataflow-handson-mayank/staging \
  --template_location gs://dataflow-handson-mayank/templates/uppercase \
  --region us-central1
```


# Install gcloud SDK on the macOS and start managing GCP through CLI
# Before Starting:
1. Create one google cloud Platform Project.
2. Cloud SDK requires Python. Supported versions are 3.5 to 3.7, and 2.7.9 or higher. To check the Python version installed on your system:
    
        python -V

3. Now install the gcloud using brew command as 
    
        brew install --cask google-cloud-sdk

# Configuring the SDK
1. Use the below-mentioned command to authorizing the SDK tools to access Google Cloud Platform using your user account credentials and setting up the default SDK configuration.
    
        gcloud init
2. Grant access to your google account associated with GCP.

        To continue, you must log in. Would you like to log in (Y/n)? Y
3. Now select the project from the available project which you want to get assigned to gcloud SDK.

        Pick cloud project to use:
        [1] [my-project-1]
        [2] [my-project-2]
        ...
        Please enter your numeric choice:
If you only have one project, `gcloud init` selects it for you.
4. Choose the zone of your project but if you have google compute engine API are enabled they automatically take the compute engine zone.

        Which compute zone would you like to use as project default?
        [1] [asia-east1-a]
        [2] [asia-east1-b]
        ...
        [14] Do not use default zone
        Please enter your numeric choice:

5. Now the `gcloud init` will confirm to that setup steps successfully:

        gcloud has now been configured!
        You can use [gcloud config] to change more gcloud settings.

        Your active configuration is: [default]

Now the gcloud SDK tools are successfully installed on your macOS and you can use to manage all the resources from CLI only you can check the info of current configuration by:

        gcloud info

Also make sure to provide credentials to [ADC](https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to)

## Create your credential file:
        gcloud auth application-default login

A sign-in screen appears. After you sign in, your credentials are stored in the local credential file used by ADC.

## Change the Project
        gcloud config set project my_project_123


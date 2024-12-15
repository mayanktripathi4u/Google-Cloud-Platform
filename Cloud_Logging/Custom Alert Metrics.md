- [Create a Custom Metrics (Log-based-metric) and Alerts](#create-a-custom-metrics-log-based-metric-and-alerts)
- [Alert with dynamic Threshold](#alert-with-dynamic-threshold)
  - [Key steps:](#key-steps)
  - [Important considerations:](#important-considerations)


# Create a Custom Metrics (Log-based-metric) and Alerts
[Refer](/Google-Cloud-Platform/Cloud_Logging/Example.md)

# Alert with dynamic Threshold
To set different thresholds for weekends and weekdays in Google Cloud custom metrics, you can leverage the "Monitoring Query Language (MQL)" within your alerting policy, using the timestamp.weekday() function to identify the day of the week and dynamically adjust the threshold based on the result. 
## Key steps:
1. Create your custom metric:
First, ensure your custom metric is set up correctly in Google Cloud Monitoring, capturing the relevant data you want to monitor. 
2. Create an alerting policy:
* Select the metric: Choose your custom metric as the metric to monitor. 
* Apply MQL condition:
  * Check for weekend: Use the timestamp.weekday() function to check if the timestamp falls on a weekend (Saturday or Sunday):
```bash
timestamp.weekday() >= 5 
```
  * Set weekend threshold: If the condition is true (weekend), set the threshold to 5:
```bash
if timestamp.weekday() >= 5 then 
    value > 5
else 
    value > 10 
```

**Explanation**:
* `timestamp.weekday()`:
  
    This function returns a number representing the day of the week (0 = Sunday, 6 = Saturday).
* `if` statement:
  
    The if statement allows you to apply different logic based on the weekday check. 
* Example MQL for the alerting policy:
```bash
if timestamp.weekday() >= 5 then 
    value > 5
else 
    value > 10 
```

## Important considerations:
* Time zone:

    Ensure your time zone settings are correct to accurately identify weekends.
* Alerting logic:

    Carefully consider the logic you want to apply for edge cases like holidays or specific time windows within the weekdays. 
# Power Platform Extension
![pp](https://i.imgur.com/aTbNb3F.png)  
I extended functionality of this project into the [Power Platform](https://powerplatform.microsoft.com/en-us/) for data reporting/visualization purposes. Please keep in mind that this is only an *extension* of project functionality and is *not* required to establish core functionality as described on this project's [main page](./../readme.md).

I wanted to record and store air quality measurements in the Power Platform and build an interactive dashboard to show me air quality trends over time.

I...

## *Installed* an **on-premises gateway** to allow cloud-based Power Platform resources to call to my local web server and collect air quality data
![gateway](https://i.imgur.com/09erpCQ.png)

## *Made* a **custom connector** to make HTTP calls to my web server and collect air quality data
![custom connector](https://i.imgur.com/uYe4LLs.png)

## *Created* a **Dataverse Table** with appropriate columns to store the air quality data in Dataverse
![table](https://i.imgur.com/NB3CchK.png)

## *Developed* a **Scheduled Power Automate Workflow** to collect and record air quality data every five minutes
![Power Automate workflow](https://i.imgur.com/Cd5noHV.png)

## *Configured* a **Model-Driven Power App** to allow me to review collected air quality data
![model-driven app](https://i.imgur.com/iZv3nzr.png)

## *Designed* a basic **Power BI Dashboard** to visualize my data and embedded it in my Model-Driven Power App as a **custom page**
![Power BI dashboard](https://i.imgur.com/bFQokzL.png)


## Resources
- Power Platform Solutions:
    - [Custom Connector Only Solution](https://github.com/TimHanewich/air-quality-box/releases/download/3/AirQualityMonitoringCustomConnector_1_0_0_1.zip) - This solution contains *only* the custom connector. It is vital that you install this solution **prior** to installing the full solution because the full solution has connection references that depend on this custom connector. If the custom connector is not present in the environment during installalation, installation of the base solution will fail due to missing dependencies.
    - [Full (remainder, without the custom connector) Power Platform Solution (.zip) file](https://github.com/TimHanewich/air-quality-box/releases/download/3/AirQualityMonitoring_1_0_0_3.zip).
- [Interactive Power BI **Air Quality Dashboard**](https://github.com/TimHanewich/air-quality-box/releases/download/1/air_quality_dashboard.pbix). You can embed this in the Model-Driven App that comes as part of the solution above.
# Withbond Carrier Integration

This document provides the technical documentation for this carrier integration.

Additional technical documentation can be found on this [Google Doc](https://docs.google.com/document/d/1yzQqW2oj7JBHL12wsprN1LAu19u9qyUFtLGHWSLWAXE/edit#).

## Supported Features

* Create shipments
* Retrieve a shipment
* Buy a shipment and receive a label
* Refund/void a shipment
* Retrieve a tracker

## Problems We Faced While Developing

1. Labels are returned as files and not links or data. This required us to save labels to disk as a temporary solution.
1. Labels must be purchased with an internal ID and not something the user would have on hand. This will require a retrieval of the ID or storing it on file.
1. You cannot pass a custom ID at time of creation since EasyPost needs to generate the shipment ID. This will require creating a shipment and then updating it afterwards (two API calls).
1. Tracking on Withbond doesn't provide tracking details, only the current status. This will require us to continually poll created shipments that have not yet been delivered for updates and store the statuses along the way in a DB.
   - Along these lines, Withbond does not even provide a tracking endpoint meaning you have to retrieve the tracker and interpret the status from those details.
1. There is a single rate and a single service levels - this required us to add custom logic to do rating in-house which luckily was simple enough with a single of each.

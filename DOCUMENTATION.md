# Withbond Carrier Integration

## Problems

1) Labels are returned as files and not links or data.
2) Labels must be purchased with an internal ID and not something the user would have on hand. This will require a retrieval of the ID or storing it on file
3) You cannot pass a custom ID at time of creation since EasyPost needs to generate the shipment ID. This will require creating a shipment and then updating it afterwards
4) Tracking on Withbond doesn't provide tracking details, only the current status. This will require us to continually poll created shipments that have not yet been delivered for updates and store the statuses along the way in a DB.
   - Along these lines, Withbond does not even provide a tracking endpoint meaning you have to retrieve the tracker and interpret the status from those details.

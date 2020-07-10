import json 
import withbond.tracker
from static_data import FLAT_RATE, SERVICE_LEVEL

def wb_to_ep_response(jsonData):
	wb_data = json.loads(jsonData)
	status = ""

	if(wb_data["status"] ==  "PENDING"):
		status = "pre_transit"

	if(wb_data["status"] ==  "READY_FOR_DELIVERY"):
		status = "in_transit"

	if(wb_data["status"] ==  "ON_THE_WAY"):
		status = "out_for_delivery"

	if(wb_data["status"] ==  "SERVICING"):
		status = "delivered"

	if(wb_data["status"] ==  "DONE"):
		status = "delivered"

	if(wb_data["status"] ==  "CANCELLED"):
		status = "cancelled"

	print(wb_data["packages"][0]["dimensions"]["height"])

	ep_response =	{
					    "created_at": wb_data["creationDate"],
					    "is_return": "false",
					    "messages": [],
					    "mode": "test",
					    "options": {
					        "currency": "USD",
					        "payment": {
					            "type": "SENDER"
					        },
					        "date_advance": 0
					    },
					    "reference": "null",
					    "status": status,
					    "tracking_code": wb_data["id"],
					    "updated_at": wb_data["creationDate"],
					    "batch_id": "null",
					    "batch_status": "null",
					    "batch_message": "null",
					    "customs_info": "null",
					    "from_address": {
					        "id": "null",
					        "object": "Address",
					        "created_at": "null",
					        "updated_at": "null",
					        "name": "null",
					        "company": "null",
					        "street1": "null",
					        "street2": "",
					        "city": "null",
					        "state": "null",
					        "zip": "null",
					        "country": "null",
					        "phone": "null",
					        "email": "null",
					        "mode": "null",
					        "carrier_facility": "null",
					        "residential": "null",
					        "federal_tax_id": "null",
					        "state_tax_id": "null",
					        "verifications": {}
					    },
					    "insurance": "null",
					    "order_id": "null",
					    "parcel": {
					        "id": "null",
					        "object": "Parcel",
					        "created_at": wb_data["creationDate"],
					        "updated_at": wb_data["creationDate"],
					        "length": wb_data["packages"][0]["dimensions"]["length"],
					        "width": wb_data["packages"][0]["dimensions"]["width"],
					        "height": wb_data["packages"][0]["dimensions"]["height"],
					        "predefined_package": "null",
					        "weight": wb_data["packages"][0]["dimensions"]["weight"],
					        "mode": "test"
					    },
					    "postage_label": {
					        "object": "PostageLabel",
					        "id": "null",
					        "created_at": wb_data["creationDate"],
					        "updated_at": wb_data["creationDate"],
					        "date_advance": 0,
					        "integrated_form": "none",
					        "label_date": wb_data["creationDate"],
					        "label_resolution": 300,
					        "label_size": "4x6",
					        "label_type": "default",
					        "label_file_type": "image/pdf",
					        "label_url": "null",
					        "label_pdf_url": "null",
					        "label_zpl_url": "null",
					        "label_epl2_url": "null",
					        "label_file": "null"
					    },
					    "rates": [
					        {
					            "id": "null",
					            "object": "Rate",
					            "created_at": wb_data["creationDate"],
					            "updated_at": wb_data["creationDate"],
					            "mode": "test",
					            "service": SERVICE_LEVEL,
					            "carrier": "WithBond",
					            "rate": FLAT_RATE,
					            "currency": "USD",
					            "retail_rate": FLAT_RATE,
					            "retail_currency": "USD",
					            "list_rate": FLAT_RATE,
					            "list_currency": "USD",
					            "delivery_days": "null",
					            "delivery_date": "null",
					            "delivery_date_guaranteed": "false",
					            "est_delivery_days": "null",
					            "shipment_id": wb_data["brandOrderId"],
					            "carrier_account_id": "null"
					        }
					    ],
					    "refund_status": "null",
					    "scan_form": "null",
					    "selected_rate": {
					            "id": "null",
					            "object": "Rate",
					            "created_at": wb_data["creationDate"],
					            "updated_at": wb_data["creationDate"],
					            "mode": "test",
					            "service": SERVICE_LEVEL,
					            "carrier": "WithBond",
					            "rate": FLAT_RATE,
					            "currency": "USD",
					            "retail_rate": FLAT_RATE,
					            "retail_currency": "USD",
					            "list_rate": FLAT_RATE,
					            "list_currency": "USD",
					            "delivery_days": "null",
					            "delivery_date": "null",
					            "delivery_date_guaranteed": "false",
					            "est_delivery_days": "null",
					            "shipment_id": wb_data["brandOrderId"],
					            "carrier_account_id": "null"
					    },
					    "tracker": {
					        "id": "null",
					        "object": "Tracker",
					        "mode": "test",
					        "tracking_code": wb_data["id"],
					        "status": status,
					        "status_detail": status,
					        "created_at": wb_data["creationDate"],
					        "updated_at": wb_data["creationDate"],
					        "signed_by": "null",
					        "weight": "null",
					        "est_delivery_date": "null",
					        "shipment_id": wb_data["brandOrderId"],
					        "carrier": "WithBond",
					        "tracking_details": [],
					        "fees": [],
					        "carrier_detail": "null",
					        "public_url": "null"
					    },
					    "to_address": {
					        "id": "null",
					        "object": "Address",
					        "created_at": wb_data["creationDate"],
					        "updated_at": wb_data["creationDate"],
					        "name": wb_data["receiver"]["name"],
					        "company": "",
					        "street1": wb_data["receiver"]["address"],
					        "street2": "",
					        "city": wb_data["receiver"]["city"],
					        "state": wb_data["receiver"]["state"],
					        "zip": wb_data["receiver"]["zipcode"],
					        "country": wb_data["receiver"]["country"],
					        "phone": wb_data["receiver"]["name"],
					        "email": wb_data["receiver"]["email"],
					        "mode": "test",
					        "carrier_facility": "null",
					        "residential": "null",
					        "federal_tax_id": "null",
					        "state_tax_id": "null",
					        "verifications": {}
					    },
					    "usps_zone": 1,
					    "return_address": {
					        "id": "null",
					        "object": "Address",
					        "created_at": "null",
					        "updated_at": "null",
					        "name": "null",
					        "company": "null",
					        "street1": "null",
					        "street2": "",
					        "city": "null",
					        "state": "null",
					        "zip": "null",
					        "country": "null",
					        "phone": "null",
					        "email": "null",
					        "mode": "null",
					        "carrier_facility": "null",
					        "residential": "null",
					        "federal_tax_id": "null",
					        "state_tax_id": "null",
					        "verifications": {}
					    },
					    "buyer_address": {
					        "id": "null",
					        "object": "Address",
					        "created_at": wb_data["creationDate"],
					        "updated_at": wb_data["creationDate"],
					        "name": wb_data["customer"]["name"],
					        "company": "",
					        "street1": wb_data["customer"]["address"],
					        "street2": "",
					        "city": wb_data["customer"]["city"],
					        "state": wb_data["customer"]["state"],
					        "zip": wb_data["customer"]["zipcode"],
					        "country": wb_data["customer"]["country"],
					        "phone": wb_data["customer"]["name"],
					        "email": wb_data["customer"]["email"],
					        "mode": "test",
					        "carrier_facility": "null",
					        "residential": "null",
					        "federal_tax_id": "null",
					        "state_tax_id": "null",
					        "verifications": {}
					    },
					    "forms": [],
					    "fees": [
					        {
					            "object": "Fee",
					            "type": "LabelFee",
					            "amount": "0.01000",
					            "charged": "true",
					            "refunded": "false"
					        }
					    ],
					    "id": wb_data["brandOrderId"],
					    "object": "Shipment"
					}
	return ep_response

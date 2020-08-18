
# NathanJames Toolbox

Collection of tools used by NathanJames

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

You can use pip to install the package.

```
pip install NathanJamesToolbox
```

## Usage

### AirtableToolbox Class
#### Overview
The class contains functions that help integrating with Airtable easier.

---

**Importing the module**

	>>> from NathanJamesToolbox import NathanJamesToolbox as nj

**AirtableToolbox Class Instance**

	_airtable = nj.airtableToolbox(<airtable base>, <airtable API Key>)
---
**Create a URL using the table name**
Create a formatted URL by supplying the table name

	>>> # _airtable.create_url(<Table Name>)
	>>> _airtable = nj.airtableToolbox('abcdefg', 'xyzApiKey')
	>>> url = _airtable.create_url('Master')
	>>> url
	'https://api.airtable.com/v0/Master'

**Create a dictionary of columns**
Loop through all the pages and create a dictionary based on the table columns.

	>>> _airtable = nj.airtableToolbox('abcdefg', 'xyzApiKey')
	>>> url = _airtable.create_url('Master?filterbyformula={SKU}=12345')
	
	>>> _dict_master = _airtable.create_dictionary(url, 'SKU', reverse=False)
	>>> _dict_master
	{'12345': ['recxyzId']}
	
	>>> _dict_master = _airtable.create_dictionary(url, 'SKU', reverse=False, 'Product Class', 'Item Status')
	>>> _dict_master
	{'12345': ['recxyzId', 'Regular', 'Live']}
**Create a list of JSON containing all data**
Loop through all the pages and create a list containing all data on all columns.

	>>> _airtable = nj.airtableToolbox('abcdefg', 'xyzApiKey')
	>>> url = _airtable.create_url('Master?filterbyformula={SKU}=12345')

	>>> _json_master = _airtable.get_json(url)
	>>> _json_master
	[{"id": "recxyzId","fields": {"SKU": "12345","Product Title": "Sample Title","PDS": ["recapABC"],"Product Class": "New","UPC": ["recABC"]}]
**Create a list of Airtable record IDs**
Loop through all the pages and create a dictionary containing the {record ID: column data}.
This is similar to create_dictionary but this limits the output to just 1 data point with the key being the record ID.
The function also does not allow you to pass in query parameters.

	>>> _airtable = nj.airtableToolbox('abcdefg', 'xyzApiKey')
	>>> _json_master = _airtable.get_ids('Master', 'SKU')
	{'recxyzId': '12345', 'recabcId': '54321', 'recasdId': '74125'}



## Authors

* **Paulo Fajardo** - *Initial work* - [github](https://github.com/pfajardo-nj/NathanJames-Automation-Script)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
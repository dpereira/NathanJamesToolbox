import requests

class Airtable:
    def __init__(self, base, apiKey):
        self.base = base
        self.apiKey = apiKey
        self.airtableURL = 'https://api.airtable.com/v0/{}'.format(base)
        self.airtableHeaders = {'content-type': 'application/json', 'Authorization': 'Bearer {}'.format(apiKey)}

    def create_dictionary(self, url, baseName, reverse=False, *args):
        _dict = {}
        _dict_reverse = {}
        atURL = url

        while True:
            print(atURL)
            r = requests.get(atURL, headers=self.airtableHeaders).json()
            if len(r) != 0:
                for rec in r['records']:
                    try:
                        _items = []
                        _name = str(rec['fields'][baseName]).strip()
                        for a in args:
                            try:
                                _items.append(str(rec['fields'][a]).strip())
                            except:
                                _items.append('N/A')

                        if reverse:
                            _items.insert(0, _name)
                            _dict_reverse[rec['id']] = _items
                        else:
                            _items.insert(0, rec['id'])
                            _dict[_name] = _items

                    except KeyError:
                        pass

                try:
                    offset = r['offset']
                    if '?' in url:
                        atURL = '{}&offset={}'.format(url, offset)
                    else:
                        atURL = '{}?offset={}'.format(url, offset)
                except KeyError:
                    break
                except Exception:
                    break
            else:
                if reverse:
                    _dict_reverse = {}
                else:
                    _dict = {}
                break
        if reverse:
            return _dict_reverse
        else:
            return _dict

    def clean_list_string(self, str):
        str = str.replace('[', '').replace("'", '').replace(']', '')
        return str

    def api_request(self, url, payload, method=None):
        r = requests.request(method, url, data=payload, headers=self.airtableHeaders)
        return r

    def push_data(self, url, payload, patch=True):
        try:
            if patch:
                r = requests.patch(url, payload, headers=self.airtableHeaders)
            else:
                r = requests.post(url, payload, headers=self.airtableHeaders)
            statCode = r.status_code
        except requests.exceptions.HTTPError as e:
            return e
        return statCode

    def table_duplicate_check(self, url, baseName):
        _list = []
        _dup_list = []
        atURL = url

        while True:
            print(atURL)
            r = requests.get(atURL, headers=self.airtableHeaders).json()
            if len(r) != 0:
                for rec in r['records']:
                    try:
                        _item = str(rec['fields'][baseName]).strip()
                        if _item not in _list:
                            _list.append(_item)
                        else:
                            _dup_list.append(_item)
                    except KeyError:
                        pass

                try:
                    offset = r['offset']
                    if '?' in url:
                        atURL = '{}&offset={}'.format(url, offset)
                    else:
                        atURL = '{}?offset={}'.format(url, offset)
                except KeyError:
                    break
                except Exception:
                    break
        if len(_dup_list) == 0:
            return 'No duplicates found on\n----table: {}\n----column: {}'.format(url, baseName)
        else:
            return 'The following duplicates found on\n----table: {}\n----column: {}'.format(url, _dup_list)

    def create_list(self, url, _column):
        airtableURL = url
        _list = []

        while True:
            print(airtableURL)
            r = requests.get(airtableURL, headers=self.airtableHeaders).json()
            if len(r) != 0:
                for rec in r['records']:
                    try:
                        _list.append(rec['fields'][_column])
                    except KeyError:
                        pass

                try:
                    offset = r['offset']
                    if '?' in url:
                        airtableURL = '{}&offset={}'.format(url, offset)
                    else:
                        airtableURL = '{}?offset={}'.format(url, offset)
                except KeyError:
                    break
                except Exception:
                    break
        return _list

    def get_json(self, url):
        airtableURL = url
        _list_json = []

        while True:
            print(airtableURL)
            r = requests.get(airtableURL, headers=self.airtableHeaders).json()
            for rec in r['records']:
                _list_json.append(rec)

            try:
                offset = r['offset']
                if '?' in url:
                    airtableURL = '{}&offset={}'.format(url, offset)
                else:
                    airtableURL = '{}?offset={}'.format(url, offset)
            except KeyError:
                break
            except Exception:
                break
        return _list_json

    def create_url(self, url_base):
        return '{}/{}'.format(self.airtableURL, url_base)

    def get_ids(self, table, column_name):
        if '?' in table:
            url = "{base_url}/{table}&sort[0][field]={column_name}&sort[0][direction]=desc&fields[]={column_name}". \
                format(base_url=self.airtableURL, table=table, column_name=column_name)
        else:
            url = "{base_url}/{table}?sort[0][field]={column_name}&sort[0][direction]=desc&fields[]={column_name}". \
                format(base_url=self.airtableURL, table=table, column_name=column_name)
        atURL = url
        _dict = {}

        while True:
            print(atURL)
            r = requests.get(atURL, headers=self.airtableHeaders).json()
            for row in r['records']:
                _id = row['id']
                poName = row['fields']['PO Name']
                _dict[_id] = poName

            try:
                offset = r['offset']
                if '?' in url:
                    atURL = '{}&offset={}'.format(url, offset)
                else:
                    atURL = '{}?offset={}'.format(url, offset)
            except KeyError:
                break
            except Exception:
                break

        _list_po = _dict
        _dict = {}
        for po in _list_po:
            _list = []
            key = _list_po.get(po)
            value = po
            if key in _dict:
                # get _dict _list, append value to _list
                _list_new = _dict.get(key)
                _list_new.append(value)
                _dict[key] = _list_new
                _list_new = []
            else:
                # add key to _dict and create new list
                _list_new = []
                _list_new.append(value)
                _dict[key] = _list_new
                _list_new = []
        return _dict

    def delete_ids(self, _table, _list_id):
        """
        Please note that the script can only handle a max of 10 IDs
        """
        _list_id = ['records[]={}'.format(_id) for _id in _list_id]
        if len(_list_id) > 10:
            raise Exception('Function NathanJamesToolbox.airtableToolbox.delete_ids can only handle a max of 10 IDs.')

        url = '{}/{}?{}'.format(self.airtableURL, _table, '&'.join(_list_id))
        r = requests.request('DELETE', url, headers=self.airtableHeaders)
        return r





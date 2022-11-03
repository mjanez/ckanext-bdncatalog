[![Tests](https://github.com/mjanez/ckanext-bdncatalog/workflows/Tests/badge.svg?branch=main)](https://github.com/mjanez/ckanext-bdncatalog/actions)

# ckanext-bdncatalog

**TODO:** Put a description of your extension here:  What does it do? What features does it have? Consider including some screenshots or embedding a video!


## Requirements

**TODO:** For example, you might want to mention here which versions of CKAN this
extension works with.

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | yes    |

>**Note**<br>
>Suggested values:
>* `yes`
>* `not tested` - I can't think of a reason why it wouldn't work
>* `not yet` - there is an intention to get it working
>* `no`


## Installation

**TODO:** Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-bdncatalog:

1. Activate your CKAN virtual environment.
2. Clone the source and install it on the virtualenv
	```bash
	git clone https://github.com/mjanez/ckanext-bdncatalog.git
	cd ckanext-bdncatalog
	pip install -e .
	pip install -r requirements.txt
	```
3. Add `bdncatalog` to the `ckan.plugins` setting in your CKAN
   config file.
	```ini
	ckan.plugins = stats text_view image_view recline_view scheming_datasets bdncatalog dcat structured_data
	```

4. Restart CKAN.


## Config settings
Update the `ckanext-scheming` custom schemas based on `ckanext-bdncatalog`.
```ini
# DCAT SCHEMING-BDNCATALOG
scheming.dataset_schemas = ckanext.bdncatalog:schema_collection.yaml
			   ckanext.bdncatalog:schema_direct_threats_type.yaml
			   ckanext.bdncatalog:schema_distribution_type.yaml
			   ckanext.bdncatalog:schema_habitats_type.yaml
			   ckanext.bdncatalog:schema_invasiveness_type.yaml
			   ckanext.bdncatalog:schema_legislation_type.yaml
			   ckanext.bdncatalog:schema_population_biology_type.yaml
			   ckanext.bdncatalog:schema_record_metadata_type.yaml
			   ckanext.bdncatalog:schema_reference_type.yaml
			   ckanext.bdncatalog:schema_taxon_record.yaml
			   ckanext.bdncatalog:schema_threat_status_type.yaml
			   ckanext.bdncatalog:schema_vernacular_name.yaml
			   ckanext.bdncatalog:schema_measurement_or_fact.yaml
			   ckanext.bdncatalog:schema_taxon.yaml
			   ckanext.bdncatalog:schema_location.yaml
			   ckanext.bdncatalog:schema_management_conservation_type.yaml
			   ckanext.bdncatalog:schema_dcat-ap_2.0.1.yaml


scheming.presets = ckanext.scheming:presets.json ckanext.bdncatalog:presets.json

ckanext.dcat.rdf.profiles = eidos_rdf_profile
```


## Developer installation

To install ckanext-bdncatalog for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/mjanez/ckanext-bdncatalog.git
    cd ckanext-bdncatalog
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-bdncatalog

If ckanext-bdncatalog should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags


## Load TTLs
Ad-hoc CKAN software to retrieve data from EIDOS TTL and ingest datasets into CKAN.

**Requeriments:**
The code compiles with Python 3. The required libraries can be found in `requirements.txt`.

### Configuration
The necessary steps to configure the environment and install the libraries are as follows. First create the `venv` directory where it will run (or replace `whoami` with the desired user name if you create for example one for `ckan`):
```bash
# Linux
cd /my/path
python3 -m venv .env    # sudo apt-get install python3-venv
. my/path/.env/bin/activate
python3 -m pip install  install -r requirements.txt

# Windows
cd /my/path
python -m venv .env
my/path/.env/Scripts/activate.bat  # CMD || env\Scripts\Activate.ps1  # Powershell
pip install  install -r requirements.txt
```

### Launch
1. Download https://datos.iepnb.es/datasets/eidos.ttl
	```bash
	curl -o eidos.ttl https://datos.iepnb.es/datasets/eidos.ttl
	```
2. Update `splitFilesEidosTTL.py` parameters:
	- `ckan_url`: CKAN site.
	- `path_orig`: Folder of EIDOS complete TTL.
	- `path_tmp`: Temp folder for TTLs

2. Execute splitFilesEidosTTL:
	```bash
	python3 splitFilesEidosTTL.py
	```
3. Create a `eidos-prueba` organization in CKAN.
4. Update `loadEidosTTL.py` parameters:
	- `ckan_url`: CKAN site.
	- `api_key`: http://{ckan_site_url}:5000/user/admin authorization key.
	- `path_tmp`: SplitFilesEidosTTL.py `path_tmp`
	
5. Load TTLs into CKAN
	```bash
	python3 loadEidosTTL.py
	```

### API
#### All datasets `org=eidos-prueba`
https://iepnb.es/catalogo-eidos/api/3/action/package_search?fq=organization:eidos-prueba

```json
{
   "author":null,
   "author_email":null,
   "creator_user_id":"c0447fed-9487-4f15-9735-33cdd96567f4",
   "id":"1aee5ddb-9a69-41f3-b37b-f6717478c78f",
   "isopen":false,
   "license_id":null,
   "license_title":null,
   "maintainer":null,
   "maintainer_email":null,
   "metadata_created":"2022-11-03T07:13:10.082966",
   "metadata_modified":"2022-11-03T07:13:10.082971",
   "name":"location_10kme316n182",
   "notes":null,
   "num_resources":0,
   "num_tags":0,
   "organization":{
      "id":"8658449a-1cf5-4fb1-88bb-88026b8574e3",
      "name":"eidos-prueba",
      "title":"eidos-prueba",
      "type":"organization",
      "description":"eidos-prueba",
      "image_url":"",
      "created":"2022-11-02T13:51:34.804045",
      "is_organization":true,
      "approval_status":"approved",
      "state":"active"
   },
   "owner_org":"8658449a-1cf5-4fb1-88bb-88026b8574e3",
   "private":false,
   "state":"active",
   "title":"10kmE316N182",
   "type":"location",
   "url":null,
   "version":null,
   "resources":[],
   "tags":[],
   "extras":[],
   "groups":[],
   "relationships_as_subject":[],
   "relationships_as_object":[]
}
```

### Sample:
**Darwin_Location100422.ttl**
```json
{
   "owner_org":"eidos-prueba",
   "type":"location",
   "Plinian_hasCell":[
      "https://datos.iepnb.es/recurso/sector-publico/cuadricula-espacial/celda/10kmE384N189"
   ],
   "Plinian_isLocationOf":[
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20075",
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20082",
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20092"
   ],
   "title":"10kmE384N189",
   "name":"location_10kme384n189",
   "uri":"https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/Location/10kmE384N189",
   "Darwin_locationID":[
      "10kmE384N189"
   ]
}
```
>**Note**<br>
> `Inserted location` - https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/Location/10kmE384N189


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
